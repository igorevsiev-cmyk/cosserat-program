#!/usr/bin/env python3
"""
Berry-curvature alignment test (paper §6.1-6.2): local BPS-bound u || B
in the topological core of the Cosserat hopfion at mu_c = 2*pi.

For an axisymmetric director n(r,z) in cylindrical (r, phi, z), the
Berry curvature B = curl A of the S^2-valued pullback area form has
orthonormal components

    B_r = (1/r) * n . (d_phi n  x  d_z n)
    B_phi = -n . (d_r n  x  d_z n) = -rho_Q   (topological density)
    B_z = (1/r) * n . (d_r n  x  d_phi n)

with d_phi n = z_hat x n at phi=0. The u-channel in the axisymmetric
slim model carries only (u_r, 0, u_z), so this test measures the
poloidal alignment (u_r, u_z) <-> (B_r, B_z) via:

  - global cosine similarity   C_total = int(u.B) / sqrt(int|u|^2 . int|B|^2)
  - per-component cosines       C_r, C_z
  - radial profile              cos_theta(r) averaged over z
  - bin-cumulative integrals    int_{r<R}(u.B), int_{r<R}|u|^2, int_{r<R}|B|^2

The signature of the chiral bag is cos_theta(r) -> 1 in the topological
core (r < R_r) and dilution to ~0.2 in the asymptotic tail. The toroidal
B_phi is not compensated in the slim model -- see paper §7.3.

Output: result_berry_alignment.json (7 mu_c values, full radial data).
"""

import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['PYTHONUNBUFFERED'] = '1'

import numpy as np
import torch

from stretched_grid import (
    create_stretched_grid,
    compute_E_u_screened,
    field_grad_r_stretched, field_grad_z_stretched,
    _interp_nonuniform_to_uniform,
)

EPS_0 = 8.854187817e-12
HBAR = 1.054571817e-34
C_LIGHT = 299792458.0
E_CHARGE = 1.602176634e-19
M0 = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV = M0 * C_LIGHT**2 / E_CHARGE


def hopf_variational(rr, zz, R_r, R_z, w):
    r = rr / R_r; z = zz / R_z
    Y = r * r + z * z - 1.0
    D = (2.0 * z)**2 + Y * Y
    w2 = w * w
    P = (D + 4.0 * r * r * w2).clamp(min=1e-30)
    n3 = (D - 4.0 * r * r * w2) / P
    n1 = 8.0 * r * z * w / P
    n2 = -4.0 * r * Y * w / P
    n = torch.stack([n1, n2, n3])
    return n / n.norm(dim=0, keepdim=True).clamp(min=1e-10)


def compute_berry_B(n, metric):
    """Berry curvature B = (1/2) ε_ijk n·(∂_j n × ∂_k n) in cylindrical for axisymmetric n.

    Returns B_r(r,z), B_z(r,z) — components in (r,z) plane.
    (B_φ also exists but is orthogonal to u_axisymmetric.)
    """
    n1, n2, n3 = n[0], n[1], n[2]
    inv_r = metric.inv_r

    # ∂_r n, ∂_z n via stretched grid
    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)

    # ∂_φ n at φ=0 = ẑ × n = (-n2, n1, 0)
    nphi1 = -n2
    nphi2 = n1
    nphi3 = torch.zeros_like(n3)

    # B_r = (1/r) · n·(∂_φ n × ∂_z n)
    #     ∂_φ n × ∂_z n = (nphi2·n3_z - nphi3·n2_z, nphi3·n1_z - nphi1·n3_z, nphi1·n2_z - nphi2·n1_z)
    cross_phi_z_x = nphi2 * n3_z - nphi3 * n2_z
    cross_phi_z_y = nphi3 * n1_z - nphi1 * n3_z
    cross_phi_z_z = nphi1 * n2_z - nphi2 * n1_z
    Br = inv_r * (n1 * cross_phi_z_x + n2 * cross_phi_z_y + n3 * cross_phi_z_z)

    # B_z = (1/r) · n·(∂_r n × ∂_φ n)
    cross_r_phi_x = n2_r * nphi3 - n3_r * nphi2
    cross_r_phi_y = n3_r * nphi1 - n1_r * nphi3
    cross_r_phi_z = n1_r * nphi2 - n2_r * nphi1
    Bz = inv_r * (n1 * cross_r_phi_x + n2 * cross_r_phi_y + n3 * cross_r_phi_z)

    return Br, Bz


def compute_for_mu_c(mu_c, R_r, R_z, w, cfg, device):
    """Solve PCG for the u-channel stream function, extract (u_r, u_z), and
    compute (B_r, B_z) of the Berry curvature on the same uniform subgrid."""
    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )
    n = hopf_variational(rr, zz, R_r, R_z, w)

    # PCG solve for the u-channel screened Stokes equation
    E_u_sim, info = compute_E_u_screened(n, metric, mu_c, cg_iter=2000, return_psi=True)
    psi = info['psi']
    rr_u = info['rr_u']
    r_u = info['r_u']
    inv_r_u = 1.0 / rr_u.clamp(min=1e-10)
    dr_u = info['dr_u']
    dz_u = info['dz_u']

    # Reconstruct u-field from psi with Robin BC (matches compute_E_u_screened)
    ghost_factor = 1.0 - dr_u / r_u[-1].item()
    p_r = torch.zeros(psi.shape[0] + 2, psi.shape[1], device=psi.device, dtype=psi.dtype)
    p_r[1:-1] = psi; p_r[0] = -psi[0]; p_r[-1] = ghost_factor * psi[-1]
    p_z = torch.zeros(psi.shape[0], psi.shape[1] + 2, device=psi.device, dtype=psi.dtype)
    p_z[:, 1:-1] = psi; p_z[:, 0] = psi[:, -1]; p_z[:, -1] = psi[:, 0]
    dpsi_dr = (p_r[2:] - p_r[:-2]) / (2 * dr_u)
    dpsi_dz = (p_z[:, 2:] - p_z[:, :-2]) / (2 * dz_u)
    u_r = -dpsi_dz
    u_z = inv_r_u * psi + dpsi_dr

    # Berry curvature B on stretched grid
    Br_stretched, Bz_stretched = compute_berry_B(n, metric)

    # Interpolate B to uniform PCG grid (same as u)
    r_s = metric.rr[:, 0]; z_s = metric.zz[0, :]
    r_u = info['r_u']; z_u = info['z_u']
    Br_uniform = _interp_nonuniform_to_uniform(Br_stretched, r_s, z_s, r_u, z_u)
    Bz_uniform = _interp_nonuniform_to_uniform(Bz_stretched, r_s, z_s, r_u, z_u)

    # Cosine similarity (global, weighted by 2πr·dV)
    weight = rr_u * dr_u * dz_u * 2 * np.pi  # 3D volume element

    # Total
    dot_uB = ((u_r * Br_uniform + u_z * Bz_uniform) * weight).sum().item()
    norm_u = ((u_r**2 + u_z**2) * weight).sum().sqrt().item()
    norm_B = ((Br_uniform**2 + Bz_uniform**2) * weight).sum().sqrt().item()
    C_total = dot_uB / (norm_u * norm_B + 1e-30)

    # Separately r-component
    dot_ur_Br = (u_r * Br_uniform * weight).sum().item()
    norm_ur = (u_r**2 * weight).sum().sqrt().item()
    norm_Br = (Br_uniform**2 * weight).sum().sqrt().item()
    C_r = dot_ur_Br / (norm_ur * norm_Br + 1e-30)

    # Separately z-component
    dot_uz_Bz = (u_z * Bz_uniform * weight).sum().item()
    norm_uz = (u_z**2 * weight).sum().sqrt().item()
    norm_Bz = (Bz_uniform**2 * weight).sum().sqrt().item()
    C_z = dot_uz_Bz / (norm_uz * norm_Bz + 1e-30)

    # Local cos(theta(r,z)) per cell
    u_mag_local = torch.sqrt(u_r**2 + u_z**2 + 1e-20)
    B_mag_local = torch.sqrt(Br_uniform**2 + Bz_uniform**2 + 1e-20)
    cos_local = (u_r * Br_uniform + u_z * Bz_uniform) / (u_mag_local * B_mag_local)

    # Radial profile cos(theta(r)): average over z at each r
    cos_radial = cos_local.mean(dim=1).cpu().numpy()
    r_arr = r_u.cpu().numpy()

    # Also amplitude radial profiles
    u_radial = u_mag_local.mean(dim=1).cpu().numpy()
    B_radial = B_mag_local.mean(dim=1).cpu().numpy()

    # 2D norms int|u|^2 dV and int|B|^2 dV (full domain + radial bins)
    u2_full = (u_r**2 + u_z**2) * weight
    B2_full = (Br_uniform**2 + Bz_uniform**2) * weight
    int_u2_full = u2_full.sum().item()
    int_B2_full = B2_full.sum().item()

    # Cumulative bin integrals over r < R_max
    int_by_R = {}
    for R_max in [0.5, 0.64, 1.0, 1.5, 2.0, 3.0, 5.0, 5.8]:
        if R_max > r_u[-1].item(): continue
        mask = (rr_u <= R_max).float()
        int_by_R[f'R<{R_max:.2f}'] = {
            'int_u2': (u2_full * mask).sum().item(),
            'int_B2': (B2_full * mask).sum().item(),
            'int_dot': ((u_r * Br_uniform + u_z * Bz_uniform) * weight * mask).sum().item(),
        }

    # Cross-check on the stretched grid: topological density rho_Q = -B_phi
    # (the toroidal Berry component not present in the slim u-channel) and
    # the integrated Hopf charge Q_check should equal -1 for Q_H = -1.
    n_check = hopf_variational(metric.rr, metric.zz, R_r, R_z, w)
    n1c, n2c, n3c = n_check[0], n_check[1], n_check[2]
    n1c_r, n2c_r, n3c_r = field_grad_r_stretched(n1c, n2c, n3c, metric)
    n1c_z, n2c_z, n3c_z = field_grad_z_stretched(n1c, n2c, n3c, metric)
    q_density = n1c*(n2c_r*n3c_z - n3c_r*n2c_z) + n2c*(n3c_r*n1c_z - n1c_r*n3c_z) + n3c*(n1c_r*n2c_z - n2c_r*n1c_z)
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    Q_check = (q_density * J).sum().item() * dA / (4 * np.pi)
    int_qden_2 = (q_density**2 * metric.rr * J).sum().item() * dA * 2 * np.pi  # int|rho_Q|^2 dV

    return {
        'mu_c': mu_c,
        'mu_c_over_pi': mu_c / np.pi,
        'C_total': C_total,
        'C_r': C_r,
        'C_z': C_z,
        'cos_radial_at_R_r': float(cos_local[int(0.64 / dr_u), psi.shape[1]//2].item()),
        'r_profile': r_arr.tolist(),
        'cos_radial': cos_radial.tolist(),
        'u_radial': u_radial.tolist(),
        'B_radial': B_radial.tolist(),
        'E_u_sim': float(E_u_sim) if not hasattr(E_u_sim, 'item') else E_u_sim.item(),
        # 2D-norm diagnostics
        'int_u2_full': int_u2_full,
        'int_B2_full': int_B2_full,
        'int_by_R': int_by_R,
        'Q_check': Q_check,
        'int_qden_squared': int_qden_2,
    }


class Cfg:
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3
    K1 = 2.0; K2 = 2.0
    K3 = 14.56
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    cg_iter = 2000


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()
    R_r, R_z, w = 0.6408, 0.8073, 0.7020  # canonical hopfion, held fixed across all mu_c

    print("=" * 100)
    print("u vs Berry-curvature B alignment (paper §6.1-6.2)")
    print("=" * 100)
    print(f"  Canonical hopfion: R_r={R_r}, R_z={R_z}, w={w}")
    print(f"  Comparing u(mu_c) with B (Berry curvature) across mu_c values")
    print()

    pi = np.pi
    mu_c_values = [0.5*pi, 1.0*pi, 1.5*pi, 2.0*pi, 2.5*pi, 3.0*pi, 4.0*pi]

    all_results = []
    for i, mu_c in enumerate(mu_c_values):
        print(f"--- [{i+1}/{len(mu_c_values)}] mu_c = {mu_c:.4f} = {mu_c/pi:.2f}*pi ---")
        res = compute_for_mu_c(mu_c, R_r, R_z, w, cfg, device)
        all_results.append(res)
        print(f"  C_total = {res['C_total']:+.4f}   (|C|->1 = perfect BPS alignment)")
        print(f"  C_r     = {res['C_r']:+.4f}    (r-component)")
        print(f"  C_z     = {res['C_z']:+.4f}    (z-component)")
        print()

    # Summary table
    print("=" * 100)
    print("SUMMARY TABLE")
    print("=" * 100)
    print(f"{'mu_c/pi':>7} | {'C_total':>9} | {'C_r':>9} | {'C_z':>9}")
    print("-" * 50)
    for r in all_results:
        print(f"{r['mu_c_over_pi']:>7.2f} | {r['C_total']:>+9.4f} | {r['C_r']:>+9.4f} | {r['C_z']:>+9.4f}")
    print()

    max_C = max(all_results, key=lambda r: abs(r['C_total']))
    print(f"Max |C_total| at mu_c = {max_C['mu_c_over_pi']:.2f}*pi: |C| = {abs(max_C['C_total']):.4f}")

    # Global 2D norms
    print()
    print("=" * 100)
    print("FULL-DOMAIN 2D NORMS (int|u|^2 and int|B|^2)")
    print("=" * 100)
    print(f"{'mu_c/pi':>7} | {'int|u|^2':>14} | {'int|B|^2':>14} | {'ratio':>11} | {'Q_check':>9} | {'int rho_Q^2':>12}")
    print("-" * 90)
    for r in all_results:
        ratio = r['int_u2_full'] / r['int_B2_full'] if r['int_B2_full'] != 0 else 0
        print(f"{r['mu_c_over_pi']:>7.2f} | {r['int_u2_full']:>14.6e} | {r['int_B2_full']:>14.6e} | "
              f"{ratio:>11.6f} | {r['Q_check']:>+9.5f} | {r['int_qden_squared']:>12.4f}")

    # Radial-bin integrals: core localization signature
    print()
    print("=" * 100)
    print("RADIAL-BIN INTEGRALS (BPS test: core vs tail)")
    print("=" * 100)
    print("At mu_c = 2*pi (canonical):")
    can = [r for r in all_results if abs(r['mu_c_over_pi'] - 2.0) < 0.01][0]
    print(f"{'R_max':>6} | {'int|u|^2':>12} | {'int|B|^2':>12} | {'int(u.B)':>12} | {'ratio u/B':>9} | {'local C':>8}")
    print("-" * 80)
    for key in sorted(can['int_by_R'].keys()):
        d = can['int_by_R'][key]
        ratio = d['int_u2'] / d['int_B2'] if d['int_B2'] != 0 else 0
        local_C = d['int_dot'] / (d['int_u2']**0.5 * d['int_B2']**0.5 + 1e-30)
        print(f"{key:>6} | {d['int_u2']:>12.4e} | {d['int_B2']:>12.4e} | {d['int_dot']:>+12.4e} | "
              f"{ratio:>9.5f} | {local_C:>+8.4f}")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_berry_alignment.json')
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=lambda x: float(x) if hasattr(x, 'item') else x)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
