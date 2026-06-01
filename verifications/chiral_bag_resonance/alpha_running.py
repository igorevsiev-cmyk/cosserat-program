#!/usr/bin/env python3
"""
alpha_running.py — direct radial running of the effective charge / α⁻¹(R)
for the canonical Cosserat-hopfion (paper NM-optimum at μ_c = 2π).

Three independent observables of "charge inside radius R" are computed:

  (B1) cumulative topological charge   Q_H(R) = (1/4π) ∫_{ρ<R} q_density dV
  (B2) Coulomb form factor             Φ(r)   = ⟨r²·(1−n_z)⟩_z|_{shell at r}
  (A)  polynomial inversion of mass    α⁻¹(R) = −1 + √(16·m(R) + 17)
       (cross-check; uses §3.2 unifying polynomial m/M₀ = x² + x/2 − 1)

ρ = √(r² + z²) is the spherical radius.

The "running α⁻¹(R)" is derived from each observable independently:
  via (B1): α⁻¹_topo(R)  = α⁻¹_bare · 1/|Q_H(R)|²
  via (B2): α⁻¹_coul(R)  = α⁻¹_bare · Φ(∞)/Φ(R)
  via (A):  polynomial inverse of cumulative mass

If all three agree (after suitable normalisation) -- strong cross-validation
of the unifying polynomial §3.2 in spatial decomposition.
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import torch

from stretched_grid import (
    create_stretched_grid,
    compute_E_u_screened,
    compute_Q_stretched,
    field_grad_r_stretched,
    field_grad_z_stretched,
)


# ----------------------------------------------------------------------
# Physical constants (CODATA 2018)
# ----------------------------------------------------------------------
EPS_0    = 8.854187817e-12
HBAR     = 1.054571817e-34
C_LIGHT  = 299792458.0
E_CHARGE = 1.602176634e-19
M0       = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV  = M0 * C_LIGHT**2 / E_CHARGE     # ≈ 429.51 eV
MU_C     = 2.0 * np.pi


class Cfg:
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    K1 = 2.0; K2 = 2.0; K3 = 14.56
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    cg_iter = 5000


# ----------------------------------------------------------------------
# Canonical Hopf ansatz (3 params) -- from paper NM-optimum
# ----------------------------------------------------------------------
def hopf_variational(rr, zz, R_r, R_z, w):
    r = rr / R_r
    z = zz / R_z
    Y = r * r + z * z - 1.0
    D = (2.0 * z)**2 + Y * Y
    w2 = w * w
    P = (D + 4.0 * r * r * w2).clamp(min=1e-30)
    n3 = (D - 4.0 * r * r * w2) / P
    n1 = 8.0 * r * z * w / P
    n2 = -4.0 * r * Y * w / P
    n = torch.stack([n1, n2, n3])
    return n / n.norm(dim=0, keepdim=True).clamp(min=1e-10)


# ----------------------------------------------------------------------
# Local densities (per-cell, NOT yet integrated)
# ----------------------------------------------------------------------
def compute_local_OF_Sk_density(n, metric, cfg):
    """Return (e_OF, e_Sk) -- local Oseen-Frank and Skyrme energy DENSITY
    (per unit physical volume, i.e. the integrand of E = 2π ∫ e · r dr dz).

    Returns shape (Nr, Nz). Already includes factor 2π·r when later summed.
    Actually returns the 2D-density in cylindrical coordinates such that
        E = ∫∫ density(r,z) · J · dxi · deta
    where J = hr·hz is the stretched-grid Jacobian. Equivalent to
        density = 2π · r · ( ½K_i(curl)² + c4(F)² )
    so the radial cumulative sum is direct.
    """
    K1, K2, K3, c4 = cfg.K1, cfg.K2, cfg.K3, cfg.c4

    n1, n2, n3 = n[0], n[1], n[2]
    rr = metric.rr
    inv_r = metric.inv_r

    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)

    div_n = n1_r + n1 * inv_r + n3_z
    curl_r = -n2_z
    curl_phi = n1_z - n3_r
    curl_z = n2_r + n2 * inv_r
    twist = n1*curl_r + n2*curl_phi + n3*curl_z
    bend_sq = curl_r**2 + curl_phi**2 + curl_z**2 - twist**2

    e_of = (0.5*K1*div_n**2 + 0.5*K2*twist**2 + 0.5*K3*bend_sq)

    cx_rz = n2_r*n3_z - n3_r*n2_z
    cy_rz = n3_r*n1_z - n1_r*n3_z
    cz_rz = n1_r*n2_z - n2_r*n1_z
    F_rz = n1*cx_rz + n2*cy_rz + n3*cz_rz

    cx_zp = -n3_z*n1
    cy_zp = -n3_z*n2
    cz_zp = n1_z*n1 + n2_z*n2
    F_zp = n1*cx_zp + n2*cy_zp + n3*cz_zp

    cx_pr = n1*n3_r
    cy_pr = n2*n3_r
    cz_pr = -n2*n2_r - n1*n1_r
    F_pr = n1*cx_pr + n2*cy_pr + n3*cz_pr

    e_sk = c4 * (F_rz**2 + inv_r**2 * (F_zp**2 + F_pr**2))

    # multiply by 2π·r and return the 2D density on the stretched grid;
    # final integration uses metric J = hr·hz and dxi·deta
    e_of_density = 2*np.pi * e_of * rr
    e_sk_density = 2*np.pi * e_sk * rr
    return e_of_density, e_sk_density


def compute_q_density(n, metric):
    """Topological charge DENSITY (2D, axisymmetric).
    Returns q(r,z) such that  Q_H = (1/4π) ∫ q · J · dxi · deta.
    This matches compute_Q_stretched (which divides by 4π and integrates).
    """
    n1, n2, n3 = n[0], n[1], n[2]
    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)
    cx = n2_r*n3_z - n3_r*n2_z
    cy = n3_r*n1_z - n1_r*n3_z
    cz = n1_r*n2_z - n2_r*n1_z
    q_density = n1*cx + n2*cy + n3*cz
    return q_density


# ----------------------------------------------------------------------
# u-channel: compute E_u DENSITY on its uniform sub-grid
# ----------------------------------------------------------------------
def compute_E_u_density_on_subgrid(n, metric, mu_c, cg_iter=5000):
    """Returns (e_u_density_2D, r_u, z_u, dr_u, dz_u) for the u-channel
    energy density on the uniform sub-grid. The 2D density is such that
        E_u = ∫∫ e_u_density · dr_u · dz_u
    (no further Jacobian -- already includes 2π·r factor).
    """
    from stretched_grid import _interp_nonuniform_to_uniform

    n3 = n[2].detach()
    n3_clamped = n3.clamp(-1.0 + 1e-10, 1.0 - 1e-10)
    sin_f = torch.sqrt((n[0]**2 + n[1]**2).detach().clamp(min=1e-20))
    f_source = torch.atan2(sin_f, n3_clamped)

    r_s = metric.rr[:, 0]
    z_s = metric.zz[0, :]
    device = n.device
    dtype = n.dtype

    inv_l_c_sq = mu_c

    Nr_u, Nz_u = 512, 1024
    L_r_u, L_z_u = 6.0, 12.0
    dr_u = L_r_u / Nr_u
    dz_u = L_z_u / Nz_u
    r_u = (torch.arange(Nr_u, device=device, dtype=dtype) + 0.5) * dr_u
    z_u = (torch.arange(Nz_u, device=device, dtype=dtype) + 0.5) * dz_u - L_z_u/2
    rr_u = r_u.unsqueeze(1).expand(Nr_u, Nz_u)
    inv_r_u = 1.0 / rr_u.clamp(min=1e-10)

    f_u = _interp_nonuniform_to_uniform(f_source, r_s, z_s, r_u, z_u)
    rhs = 2.0 * rr_u * f_u

    ghost_factor = 1.0 - dr_u / r_u[-1].item()

    def apply_B(psi):
        p_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
        p_r[1:-1] = psi; p_r[0] = -psi[0]; p_r[-1] = ghost_factor * psi[-1]
        p_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
        p_z[:, 1:-1] = psi; p_z[:, 0] = psi[:, -1]; p_z[:, -1] = psi[:, 0]
        d2r = (p_r[2:] - 2*psi + p_r[:-2]) / dr_u**2
        d1r = (p_r[2:] - p_r[:-2]) / (2*dr_u)
        d2z = (p_z[:, 2:] - 2*psi + p_z[:, :-2]) / dz_u**2
        Lpsi = d2r + inv_r_u * d1r - (inv_r_u**2 + inv_l_c_sq) * psi + d2z
        return -rr_u * Lpsi

    diag_B = rr_u * (2.0/dr_u**2 + 2.0/dz_u**2 + inv_r_u**2 + inv_l_c_sq)
    inv_diag = 1.0 / diag_B.clamp(min=1e-30)
    dA = dr_u * dz_u
    def dot(a, b): return (a * b).sum() * dA

    psi = torch.zeros(Nr_u, Nz_u, device=device, dtype=dtype)
    r_vec = rhs.clone()
    z_vec = inv_diag * r_vec
    p_vec = z_vec.clone()
    rz_old = dot(r_vec, z_vec)
    rhs_norm = dot(r_vec, r_vec).sqrt().item()
    rel_res = 1.0
    for i in range(cg_iter):
        Bp = apply_B(p_vec)
        pBp = dot(p_vec, Bp)
        if pBp.item() <= 0: break
        alpha = rz_old / pBp
        psi = psi + alpha * p_vec
        r_vec = r_vec - alpha * Bp
        rel_res = dot(r_vec, r_vec).sqrt().item() / rhs_norm
        if rel_res < 1e-8: break
        z_vec = inv_diag * r_vec
        rz_new = dot(r_vec, z_vec)
        beta = rz_new / rz_old
        p_vec = z_vec + beta * p_vec
        rz_old = rz_new
    print(f"    PCG(u-channel): {i+1} iters, rel_res={rel_res:.2e}", flush=True)

    # strain density
    p_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_r[1:-1] = psi; p_r[0] = -psi[0]; p_r[-1] = ghost_factor * psi[-1]
    p_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_z[:, 1:-1] = psi; p_z[:, 0] = psi[:, -1]; p_z[:, -1] = psi[:, 0]
    dpsi_dr = (p_r[2:] - p_r[:-2]) / (2 * dr_u)
    dpsi_dz = (p_z[:, 2:] - p_z[:, :-2]) / (2 * dz_u)
    u_r = -dpsi_dz
    u_z = inv_r_u * psi + dpsi_dr

    p_ur_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_ur_r[1:-1] = u_r; p_ur_r[0] = -u_r[0]; p_ur_r[-1] = ghost_factor * u_r[-1]
    p_ur_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_ur_z[:, 1:-1] = u_r; p_ur_z[:, 0] = u_r[:, -1]; p_ur_z[:, -1] = u_r[:, 0]
    p_uz_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_uz_r[1:-1] = u_z; p_uz_r[0] = u_z[0]; p_uz_r[-1] = ghost_factor * u_z[-1]
    p_uz_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_uz_z[:, 1:-1] = u_z; p_uz_z[:, 0] = u_z[:, -1]; p_uz_z[:, -1] = u_z[:, 0]
    eps_rr = (p_ur_r[2:] - p_ur_r[:-2]) / (2 * dr_u)
    eps_zz = (p_uz_z[:, 2:] - p_uz_z[:, :-2]) / (2 * dz_u)
    eps_ff = u_r * inv_r_u
    eps_rz = 0.5 * ((p_ur_z[:, 2:] - p_ur_z[:, :-2]) / (2 * dz_u) +
                     (p_uz_r[2:] - p_uz_r[:-2]) / (2 * dr_u))
    e_strain = eps_rr**2 + eps_zz**2 + eps_ff**2 + 2 * eps_rz**2
    # density such that E_u = sum * dr_u * dz_u
    e_u_density = 2 * np.pi * e_strain * rr_u
    return e_u_density, r_u, z_u, dr_u, dz_u


# ----------------------------------------------------------------------
# Cumulative integration over spherical shell ρ < R
# ----------------------------------------------------------------------
def cumulative_radial(density_2d, r_coords, z_coords, jacobian, dxi, deta,
                      R_grid, use_axis="r_2d"):
    """Sort cells by spherical radius ρ = √(r²+z²), accumulate.

    density_2d:  (Nr, Nz) per-cell integrand (already includes 2π·r if appropriate)
    r_coords:    (Nr, Nz)  -- physical r at each cell
    z_coords:    (Nr, Nz)  -- physical z at each cell
    jacobian:    (Nr, Nz)  -- hr·hz for stretched grid (or 1 for uniform sub-grid)
    dxi, deta:   scalars   -- uniform step in computational coords (or dr_u, dz_u for uniform)

    R_grid:      1D array of R values to evaluate cumulative at

    Returns: (cumulative_values, np-array)  same len as R_grid
    """
    rho = torch.sqrt(r_coords**2 + z_coords**2).flatten().cpu().numpy()
    vals = (density_2d * jacobian * dxi * deta).flatten().cpu().numpy()

    order = np.argsort(rho)
    rho_sorted = rho[order]
    vals_sorted = vals[order]
    cum_vals = np.cumsum(vals_sorted)

    # interpolate cumulative at each R
    out = np.interp(R_grid, rho_sorted, cum_vals, left=0.0, right=cum_vals[-1])
    return out


def angular_average_at_radius(density_2d, r_coords, z_coords,
                               jacobian, dxi, deta, R_grid, dR=0.1):
    """3D-shell-averaged radial profile:
        <f>_3D(R) = (∫_{ρ ∈ shell} f · 2π·r·J·dxi·deta) /
                    (∫_{ρ ∈ shell}     2π·r·J·dxi·deta)

    The factor 2π·r is the proper cylindrical->3D weight: a thin spherical
    shell of radius R and thickness dR has volume 4π·R²·dR, which in
    cylindrical (r,z) decomposes as ∫_{ρ ∈ shell} 2π·r dr dz. Without the
    2π·r factor the average is uniform-in-θ (arc-length on the 2D ring),
    which under-weights the equator (sin θ measure) -- wrong for spherical
    averaging.

    Used for Coulomb form factor Φ(r) = ⟨r²·(1−n_z)⟩_3D-shell.
    """
    rho = torch.sqrt(r_coords**2 + z_coords**2).flatten().cpu().numpy()
    r_flat = r_coords.flatten().cpu().numpy()
    f = density_2d.flatten().cpu().numpy()
    weights_2D = (jacobian * dxi * deta).flatten().cpu().numpy()
    weights_3D = 2 * np.pi * r_flat * weights_2D

    out = np.zeros_like(R_grid, dtype=np.float64)
    for i, R in enumerate(R_grid):
        mask = np.abs(rho - R) < dR/2
        w_sum = weights_3D[mask].sum()
        if w_sum > 1e-30:
            out[i] = (f[mask] * weights_3D[mask]).sum() / w_sum
    return out


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    print("=" * 100)
    print("α⁻¹(R) RUNNING -- direct charge measurement on canonical Cosserat-hopfion")
    print("=" * 100)
    print(f"Device:  {device}")
    print(f"Grid:    {cfg.Nr} × {cfg.Nz}, L_r={cfg.L_r}, L_z={cfg.L_z}")
    print(f"μ_c = 2π = {MU_C:.6f}")
    print(f"M₀c² = {M0C2_eV:.4f} eV")
    print()

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    # Paper NM-optimum (canonical electron)
    R_r, R_z, w = 0.6408160149362525, 0.8072875518184682, 0.7019955806536682
    print(f"Canonical electron:  R_r={R_r:.4f}, R_z={R_z:.4f}, w={w:.4f}")
    print(f"  (NM-optimum from electron_mass_minimization/result.json)")
    print()

    n = hopf_variational(rr, zz, R_r, R_z, w)
    print(f"|n| range: [{n.norm(dim=0).min():.6f}, {n.norm(dim=0).max():.6f}]")

    # ------------------------------------------------------------
    # Sanity check: total mass
    # ------------------------------------------------------------
    print("\n--- Total energies (sanity check) ---")
    e_of_d, e_sk_d = compute_local_OF_Sk_density(n, metric, cfg)
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    E_OF_total = (e_of_d * J).sum().item() * dA
    E_Sk_total = (e_sk_d * J).sum().item() * dA
    keV = M0C2_eV / 1000.0
    print(f"  E_OF = {E_OF_total*keV:.4f} keV")
    print(f"  E_Sk = {E_Sk_total*keV:.4f} keV")

    q_d = compute_q_density(n, metric)
    Q_total = (q_d * J).sum().item() * dA / (4 * np.pi)
    print(f"  Q_H  = {Q_total:.6f}  (expected ≈ ±1)")

    # u-channel density
    print("\n--- u-channel (screened PCG) ---")
    e_u_d, r_u, z_u, dr_u, dz_u = compute_E_u_density_on_subgrid(n, metric, MU_C, cfg.cg_iter)
    E_u_total = (e_u_d.sum() * dr_u * dz_u).item()
    print(f"  E_u = {E_u_total*keV:.4f} keV")

    E_tot_keV = (E_OF_total + E_Sk_total + E_u_total) * keV
    m_e_cells = (E_OF_total + E_Sk_total + E_u_total) / 1.0  # already in M₀c² units
    print(f"\n  E_total = {E_tot_keV:.4f} keV  ({m_e_cells:.3f} cells × M₀c²)")
    print(f"  expected from result.json: 446.279 keV (1039.05 cells)")

    # ------------------------------------------------------------
    # Cumulative observables on spherical radius ρ
    # ------------------------------------------------------------
    # Box diagonal = √(L_r² + (L_z/2)²) ≈ 23.7 -- extend R_grid up to that
    # to verify cumulative mass converges to full 1039 inside the box
    R_box_diag = float(np.sqrt(cfg.L_r**2 + (cfg.L_z/2)**2))
    R_grid = np.concatenate([
        np.linspace(0.05, 2.0, 40),
        np.linspace(2.0, 8.0, 50),
        np.linspace(8.0, 17.0, 50),
        np.linspace(17.0, R_box_diag, 25),
    ])
    R_grid = np.unique(R_grid)

    rr_u_2d = r_u.unsqueeze(1).expand(len(r_u), len(z_u))
    zz_u_2d = z_u.unsqueeze(0).expand(len(r_u), len(z_u))
    ones_u = torch.ones_like(rr_u_2d)

    print("\n--- Cumulative integrals on spherical radius ρ = √(r²+z²) ---")
    cum_E_OF = cumulative_radial(e_of_d, rr, zz, J, metric.dxi, metric.deta, R_grid)
    cum_E_Sk = cumulative_radial(e_sk_d, rr, zz, J, metric.dxi, metric.deta, R_grid)
    cum_Q    = cumulative_radial(q_d,    rr, zz, J, metric.dxi, metric.deta, R_grid) / (4*np.pi)
    cum_E_u  = cumulative_radial(e_u_d, rr_u_2d, zz_u_2d, ones_u, dr_u, dz_u, R_grid)

    cum_m_cells = cum_E_OF + cum_E_Sk + cum_E_u    # already in M₀c²-cells units

    def _ix(R_target):
        return int(np.argmin(np.abs(R_grid - R_target)))
    print(f"  R=1.0:   m={cum_m_cells[_ix(1.0)]:7.2f},  Q={cum_Q[_ix(1.0)]:+.4f}")
    print(f"  R=5.0:   m={cum_m_cells[_ix(5.0)]:7.2f},  Q={cum_Q[_ix(5.0)]:+.4f}")
    print(f"  R=7.5:   m={cum_m_cells[_ix(7.5)]:7.2f},  Q={cum_Q[_ix(7.5)]:+.4f}")
    print(f"  R=10.0:  m={cum_m_cells[_ix(10.0)]:7.2f},  Q={cum_Q[_ix(10.0)]:+.4f}")
    print(f"  R=17.0:  m={cum_m_cells[_ix(17.0)]:7.2f},  Q={cum_Q[_ix(17.0)]:+.4f}")
    print(f"  R={R_box_diag:.2f} (box diag):  m={cum_m_cells[-1]:7.2f},  Q={cum_Q[-1]:+.4f}")

    # ------------------------------------------------------------
    # Coulomb form factor: angle-averaged r²·(1-n_z) at each R
    # ------------------------------------------------------------
    print("\n--- Coulomb form factor Φ(R) = r²·(1-n_z) angle-averaged on spherical shell ---")
    n_z = n[2]
    rho_2d = torch.sqrt(rr**2 + zz**2)
    one_minus_nz = (1.0 - n_z)
    Phi_density = rho_2d**2 * one_minus_nz   # (1-n_z)·ρ² ; angle-averaged below
    Phi_R = angular_average_at_radius(
        Phi_density, rr, zz, J, metric.dxi, metric.deta, R_grid, dR=0.4
    )
    print(f"  Φ(R=1)  = {Phi_R[np.searchsorted(R_grid,1.0)]:.4f}")
    print(f"  Φ(R=5)  = {Phi_R[np.searchsorted(R_grid,5.0)]:.4f}")
    print(f"  Φ(R=10) = {Phi_R[np.searchsorted(R_grid,10.0)]:.4f}")
    print(f"  Φ(R=15) = {Phi_R[np.searchsorted(R_grid,15.0)]:.4f}")

    # ------------------------------------------------------------
    # α⁻¹(R) via THREE independent observables
    # ------------------------------------------------------------
    print("\n--- α⁻¹(R) via three observables ---")
    ALPHA_INV_BARE = 128.0   # = 2⁷ from dyadic geometry (paper §1.2)

    # (A) Polynomial inversion: α⁻¹ = -1 + √(16m + 17)
    arg = 16.0 * cum_m_cells + 17.0
    alpha_inv_poly = -1.0 + np.sqrt(np.maximum(arg, 0.0))

    # (B1) Topological: α⁻¹_topo = α⁻¹_bare / |Q_H(R)|²
    Q_abs = np.abs(cum_Q)
    alpha_inv_topo = np.where(Q_abs > 1e-3, ALPHA_INV_BARE / (Q_abs**2), np.nan)

    # (B2) Coulomb form factor: α⁻¹_coul = α⁻¹_bare · Φ(∞) / Φ(R)
    # Φ(∞) from outer tail (use average over R ∈ [13, 16] as proxy)
    mask_tail = (R_grid > 13.0) & (R_grid < 16.0)
    Phi_inf = np.median(Phi_R[mask_tail]) if mask_tail.any() else Phi_R[-3:].mean()
    alpha_inv_coul = np.where(Phi_R > 1e-6,
                                ALPHA_INV_BARE * Phi_inf / Phi_R,
                                np.nan)

    print(f"  Φ_∞ proxy (median over R ∈ [13,16]):  {Phi_inf:.4f}")
    print()
    print(f"  R       α⁻¹_poly   α⁻¹_topo   α⁻¹_coul")
    print(f"  ----    --------   --------   --------")
    for R_target in [1, 2, 5, 7.5, 10, 13, 17]:
        i = np.argmin(np.abs(R_grid - R_target))
        print(f"  {R_grid[i]:5.2f}   {alpha_inv_poly[i]:7.2f}    "
              f"{alpha_inv_topo[i]:7.2f}    {alpha_inv_coul[i]:7.2f}")

    # ------------------------------------------------------------
    # Save
    # ------------------------------------------------------------
    out = {
        'paper': 'alpha_running_radial -- direct measurement of α(R) for canonical electron',
        'canonical': {
            'R_r': R_r, 'R_z': R_z, 'w': w,
            'mu_c': MU_C, 'M0c2_eV': M0C2_eV,
            'grid': {'Nr': cfg.Nr, 'Nz': cfg.Nz, 'L_r': cfg.L_r, 'L_z': cfg.L_z,
                     'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z},
        },
        'totals': {
            'E_OF_keV': E_OF_total * keV,
            'E_Sk_keV': E_Sk_total * keV,
            'E_u_keV':  E_u_total  * keV,
            'E_total_keV': E_tot_keV,
            'm_e_cells': m_e_cells,
            'Q_H_total': Q_total,
        },
        'normalisation': {
            'alpha_inv_bare': ALPHA_INV_BARE,
            'Phi_inf_proxy': float(Phi_inf),
        },
        'radial': {
            'R_grid':         R_grid.tolist(),
            'cum_E_OF_cells': cum_E_OF.tolist(),
            'cum_E_Sk_cells': cum_E_Sk.tolist(),
            'cum_E_u_cells':  cum_E_u.tolist(),
            'cum_m_cells':    cum_m_cells.tolist(),
            'cum_Q_H':        cum_Q.tolist(),
            'Phi_R':          Phi_R.tolist(),
            'alpha_inv_poly': alpha_inv_poly.tolist(),
            'alpha_inv_topo': [float(x) if np.isfinite(x) else None for x in alpha_inv_topo],
            'alpha_inv_coul': [float(x) if np.isfinite(x) else None for x in alpha_inv_coul],
        },
    }

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_alpha_running.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nResult saved: {out_path}")
    print("\nDONE")


if __name__ == '__main__':
    t0 = time.time()
    main()
    print(f"\nWall time: {time.time()-t0:.1f} s")
