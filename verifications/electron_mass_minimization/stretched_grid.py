#!/usr/bin/env python3
"""
Adaptive grid for the hopfion: clustering of points near the soliton core.

Coordinate change: physical r(xi), z(eta) are smooth monotone functions of
the uniform xi, eta. All derivatives are rescaled through the metric
coefficients hr = dr/dxi, hz = dz/deta.

Usage:
    from stretched_grid import create_stretched_grid, StretchedMetric
    rr, zz, metric = create_stretched_grid(cfg, device)

    # Instead of field_grad_r(n1, n2, n3, dr):
    field_grad_r_stretched(n1, n2, n3, metric)
"""

import torch
import numpy as np


class StretchedMetric:
    """Holds everything needed for computations on the non-uniform grid."""
    def __init__(self, rr, zz, hr, hz, dxi, deta):
        self.rr = rr        # (Nr, Nz) physical r coordinates
        self.zz = zz        # (Nr, Nz) physical z coordinates
        self.hr = hr        # (Nr, Nz) metric dr/dxi
        self.hz = hz        # (Nr, Nz) metric dz/deta
        self.dxi = dxi      # scalar: uniform xi step
        self.deta = deta    # scalar: uniform eta step
        self.inv_r = 1.0 / rr.clamp(min=1e-10)


def _sinh_stretch(xi, x0, L, beta):
    """
    sinh stretching: clusters points near x0.

    xi:   uniform coordinate in [0, 1]
    x0:   focus point (in physical units)
    L:    full domain size
    beta: clustering strength (0 = uniform, 5-10 = strong)

    Guarantee: x(0) = 0, x(1) = L, clustering near x0.

    Returns: physical coordinate x and metric dx/dxi.
    """
    xi0 = x0 / L  # focus in normalized coordinates [0, 1]

    if beta < 0.01:
        # Nearly uniform -- avoid divide-by-zero
        x = xi * L
        dx_dxi = torch.ones_like(xi) * L
        return x, dx_dxi

    # sinh stretching: s(xi) = sinh(beta * (xi - xi0))
    # Normalization: x = L * (s(xi) - s(0)) / (s(1) - s(0))
    # This guarantees x(0) = 0 and x(1) = L.
    sinh_vals = torch.sinh(beta * (xi - xi0))
    cosh_vals = torch.cosh(beta * (xi - xi0))

    s_at_0 = np.sinh(beta * (0.0 - xi0))
    s_at_1 = np.sinh(beta * (1.0 - xi0))
    denom = s_at_1 - s_at_0

    x = L * (sinh_vals - s_at_0) / denom

    # Metric: dx/dxi = L * beta * cosh(beta*(xi - xi0)) / (s(1) - s(0))
    dx_dxi = L * beta * cosh_vals / denom

    return x, dx_dxi


def create_stretched_grid(cfg, device, r_focus=None, z_focus=None,
                          beta_r=5.0, beta_z=3.0):
    """
    Builds a non-uniform grid with clustering near the hopfion core.

    Parameters:
        cfg:      configuration object with Nr, Nz, L_r, L_z, use_float64
        device:   torch device
        r_focus:  radial coordinate of the core (default: R_hopf)
        z_focus:  axial coordinate of the core (default: 0, center)
        beta_r:   r-direction clustering (5 = strong; good for the core)
        beta_z:   z-direction clustering (3 = moderate)

    Returns:
        rr, zz:   (Nr, Nz) physical coordinates
        metric:   StretchedMetric instance
    """
    dtype = torch.float64 if cfg.use_float64 else torch.float32

    if r_focus is None:
        r_focus = getattr(cfg, 'R_hopf', 1.0)
    if z_focus is None:
        z_focus = 0.0  # domain center (z runs from -L_z/2 to +L_z/2)

    Nr, Nz = cfg.Nr, cfg.Nz
    L_r, L_z = cfg.L_r, cfg.L_z

    # Uniform coordinates xi in [0, 1], eta in [0, 1]
    dxi = 1.0 / Nr
    deta = 1.0 / Nz
    xi = (torch.arange(Nr, device=device, dtype=dtype) + 0.5) * dxi
    eta = (torch.arange(Nz, device=device, dtype=dtype) + 0.5) * deta

    # Physical coordinates with stretching
    # r: domain [0, L_r], focus near r_focus
    r_1d, hr_1d = _sinh_stretch(xi, r_focus, L_r, beta_r)

    # z: domain [0, L_z] is shifted to [-L_z/2, +L_z/2].
    # Focus at z_focus=0 corresponds to L_z/2 in the [0, L_z] frame.
    z_01, hz_1d = _sinh_stretch(eta, z_focus + L_z/2, L_z, beta_z)
    z_1d = z_01 - L_z / 2

    # 2D meshgrid
    rr, zz = torch.meshgrid(r_1d, z_1d, indexing='ij')
    hr_2d = hr_1d.unsqueeze(1).expand(Nr, Nz)
    hz_2d = hz_1d.unsqueeze(0).expand(Nr, Nz)

    metric = StretchedMetric(rr, zz, hr_2d, hz_2d, dxi, deta)

    # Resolution statistics
    dr_min = hr_1d.min().item() * dxi
    dr_max = hr_1d.max().item() * dxi
    dz_min = hz_1d.min().item() * deta
    dz_max = hz_1d.max().item() * deta

    print(f"\nAdaptive grid: {Nr}x{Nz}")
    print(f"  r: [{r_1d[0].item():.4f}, {r_1d[-1].item():.4f}], "
          f"dr=[{dr_min:.5f}, {dr_max:.5f}], focus r={r_focus:.2f}")
    print(f"  z: [{z_1d[0].item():.4f}, {z_1d[-1].item():.4f}], "
          f"dz=[{dz_min:.5f}, {dz_max:.5f}], focus z={z_focus:.2f}")
    print(f"  Clustering: beta_r={beta_r}, beta_z={beta_z}")
    print(f"  Core resolution: dr_min = {dr_min:.5f} l_0 "
          f"({dr_min/0.26*100:.0f}% of r_tube)")

    return rr, zz, metric


# ============================================================
# Stretched-grid gradients (4th order)
# ============================================================

def _grad4_stretched_z(tensor, metric):
    """
    df/dz = (1/hz) * df/deta
    4th order in eta with periodic BC.
    """
    deta = metric.deta
    fp2 = torch.roll(tensor, -2, dims=1)
    fp1 = torch.roll(tensor, -1, dims=1)
    fm1 = torch.roll(tensor,  1, dims=1)
    fm2 = torch.roll(tensor,  2, dims=1)
    df_deta = (-fp2 + 8*fp1 - 8*fm1 + fm2) / (12.0 * deta)
    return df_deta / metric.hz


def _grad4_stretched_r(tensor, metric, parity):
    """
    df/dr = (1/hr) * df/dxi
    4th order in xi with parity-aware reflection at the axis.
    """
    dxi = metric.dxi
    Nr = tensor.shape[0]

    # Left padding (axis r=0): parity reflection
    pad_left = parity * tensor[:2].flip(0)
    # Right padding (r_max): replicate
    pad_right = tensor[-2:].flip(0)

    padded = torch.cat([pad_left, tensor, pad_right], dim=0)

    fp2 = padded[4:]
    fp1 = padded[3:-1]
    fm1 = padded[1:-3]
    fm2 = padded[:-4]
    df_dxi = (-fp2 + 8*fp1 - 8*fm1 + fm2) / (12.0 * dxi)

    return df_dxi / metric.hr


def field_grad_r_stretched(n1, n2, n3, metric):
    """dn/dr on the stretched grid with correct parity at the axis."""
    return (_grad4_stretched_r(n1, metric, parity=-1),
            _grad4_stretched_r(n2, metric, parity=-1),
            _grad4_stretched_r(n3, metric, parity=+1))


def field_grad_z_stretched(n1, n2, n3, metric):
    """dn/dz on the stretched grid."""
    return (_grad4_stretched_z(n1, metric),
            _grad4_stretched_z(n2, metric),
            _grad4_stretched_z(n3, metric))


# ============================================================
# Oseen-Frank energy on the stretched grid
# ============================================================
def compute_oseen_frank_stretched(n, metric, cfg):
    """
    E_OF = 2*pi * integral [K1/2 * (div n)^2 + K2/2 * (n . curl n)^2 + K3/2 * |n x curl n|^2] r dr dz

    On a stretched grid, dr * dz = hr * hz * dxi * deta.
    """
    K1 = getattr(cfg, 'K1', 2.0)
    K2 = getattr(cfg, 'K2', 2.0)
    K3 = getattr(cfg, 'K3', 2.0)

    n1, n2, n3 = n[0], n[1], n[2]
    rr = metric.rr
    inv_r = metric.inv_r

    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)

    # div(n)
    div_n = n1_r + n1 * inv_r + n3_z

    # curl(n)
    curl_r = -n2_z
    curl_phi = n1_z - n3_r
    curl_z = n2_r + n2 * inv_r

    # twist = n . curl(n)
    twist = n1 * curl_r + n2 * curl_phi + n3 * curl_z

    # bend^2 = |curl(n)|^2 - twist^2
    curl_sq = curl_r**2 + curl_phi**2 + curl_z**2
    bend_sq = curl_sq - twist**2

    e_splay = 0.5 * K1 * div_n**2
    e_twist = 0.5 * K2 * twist**2
    e_bend  = 0.5 * K3 * bend_sq

    # Jacobian: dA_phys = hr * hz * dxi * deta
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta

    E_splay = 2 * np.pi * (e_splay * rr * J).sum() * dA
    E_twist = 2 * np.pi * (e_twist * rr * J).sum() * dA
    E_bend  = 2 * np.pi * (e_bend * rr * J).sum() * dA

    return E_splay + E_twist + E_bend, E_splay, E_twist, E_bend


# ============================================================
# Skyrme term on the stretched grid
# ============================================================
def compute_skyrme_stretched(n, metric, cfg):
    """E_Sk = 2*pi * c4 * integral (F_rz^2 + F_zphi^2/r^2 + F_phir^2/r^2) r dr dz"""
    n1, n2, n3 = n[0], n[1], n[2]
    rr = metric.rr
    inv_r = metric.inv_r

    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)

    # F_rz
    cx_rz = n2_r*n3_z - n3_r*n2_z
    cy_rz = n3_r*n1_z - n1_r*n3_z
    cz_rz = n1_r*n2_z - n2_r*n1_z
    F_rz = n1*cx_rz + n2*cy_rz + n3*cz_rz

    # F_zphi
    cx_zp = -n3_z*n1
    cy_zp = -n3_z*n2
    cz_zp = n1_z*n1 + n2_z*n2
    F_zp = n1*cx_zp + n2*cy_zp + n3*cz_zp

    # F_phir
    cx_pr = n1*n3_r
    cy_pr = n2*n3_r
    cz_pr = -n2*n2_r - n1*n1_r
    F_pr = n1*cx_pr + n2*cy_pr + n3*cz_pr

    e4 = F_rz**2 + inv_r**2 * (F_zp**2 + F_pr**2)

    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    E_skyrme = 2 * np.pi * (cfg.c4 * e4 * rr * J).sum() * dA

    return E_skyrme


# ============================================================
# u-channel: Stokes equation L^2 psi = -2 f (locked limit)
# ============================================================

def _interp_nonuniform_to_uniform(field_2d, r_src, z_src, r_dst, z_dst):
    """
    Bilinear interpolation from a NON-UNIFORM grid to a uniform grid.

    grid_sample does not work on non-uniform grids -- it assumes
    equidistant pixels. We use searchsorted to find the correct indices.

    field_2d:     (Nr_s, Nz_s) data on the stretched grid
    r_src, z_src: 1D stretched coordinates (non-uniform)
    r_dst, z_dst: 1D uniform target coordinates

    Returns: (Nr_u, Nz_u) interpolated field.
    """
    device = field_2d.device
    dtype = field_2d.dtype
    Nr_s, Nz_s = field_2d.shape
    Nr_u = r_dst.shape[0]
    Nz_u = z_dst.shape[0]

    # For each r_dst, find the index in r_src
    idx_r = torch.searchsorted(r_src, r_dst).clamp(1, Nr_s - 1)
    # Weight along r
    r_lo = r_src[idx_r - 1]
    r_hi = r_src[idx_r]
    wr = ((r_dst - r_lo) / (r_hi - r_lo).clamp(min=1e-30)).clamp(0, 1)

    # For each z_dst, find the index in z_src
    idx_z = torch.searchsorted(z_src, z_dst).clamp(1, Nz_s - 1)
    z_lo = z_src[idx_z - 1]
    z_hi = z_src[idx_z]
    wz = ((z_dst - z_lo) / (z_hi - z_lo).clamp(min=1e-30)).clamp(0, 1)

    # Bilinear: 4 corners
    ir0 = (idx_r - 1).long()  # (Nr_u,)
    ir1 = idx_r.long()
    iz0 = (idx_z - 1).long()  # (Nz_u,)
    iz1 = idx_z.long()

    # 2D gather indices
    f00 = field_2d[ir0][:, iz0]  # (Nr_u, Nz_u)
    f10 = field_2d[ir1][:, iz0]
    f01 = field_2d[ir0][:, iz1]
    f11 = field_2d[ir1][:, iz1]

    wr2 = wr.unsqueeze(1)  # (Nr_u, 1)
    wz2 = wz.unsqueeze(0)  # (1, Nz_u)

    result = (f00 * (1 - wr2) * (1 - wz2) +
              f10 * wr2 * (1 - wz2) +
              f01 * (1 - wr2) * wz2 +
              f11 * wr2 * wz2)

    return result


def compute_E_u_screened(n, metric, mu_c, cg_iter=2000, return_psi=False):
    """
    u-channel energy with physical Cosserat screening (finite mu_c).

    Solves the SCREENED Stokes equation: (L^2 - 1/l_c^2) psi = -2 f,
    where l_c = sqrt(mu / mu_c), mu = 1 in natural units, so
    l_c = 1 / sqrt(mu_c).

    The solution decays as exp(-r / l_c); no Gaussian window is needed.
    mu_c enters the operator directly.

    If return_psi=True, also returns a dict with psi*, the u-subgrid info,
    and the source field -- needed for adjoint-style gradient computations.
    """
    n3 = n[2].detach()

    # Source (no Gaussian window -- screening is built into the operator)
    n3_clamped = n3.clamp(-1.0 + 1e-10, 1.0 - 1e-10)
    sin_f = torch.sqrt((n[0]**2 + n[1]**2).detach().clamp(min=1e-20))
    f_source = torch.atan2(sin_f, n3_clamped)

    r_s = metric.rr[:, 0]
    z_s = metric.zz[0, :]

    device = n.device
    dtype = n.dtype

    # Screening length
    l_c_sq = 1.0 / mu_c   # l_c^2 = mu / mu_c, mu = 1
    inv_l_c_sq = mu_c      # 1 / l_c^2

    # Uniform subgrid (compact -- the solution decays on its own)
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

    # Screened operator: B = r * (-(L^2 - 1/l_c^2)) = r * (-L^2 + 1/l_c^2)
    def apply_B(psi):
        p_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
        p_r[1:-1] = psi; p_r[0] = -psi[0]; p_r[-1] = 0.0
        p_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
        p_z[:, 1:-1] = psi; p_z[:, 0] = psi[:, -1]; p_z[:, -1] = psi[:, 0]
        d2r = (p_r[2:] - 2*psi + p_r[:-2]) / dr_u**2
        d1r = (p_r[2:] - p_r[:-2]) / (2*dr_u)
        d2z = (p_z[:, 2:] - 2*psi + p_z[:, :-2]) / dz_u**2
        # The +inv_l_c_sq term implements screening
        Lpsi = d2r + inv_r_u * d1r - (inv_r_u**2 + inv_l_c_sq) * psi + d2z
        return -rr_u * Lpsi

    # Jacobi preconditioner (updated diagonal includes the screening term)
    diag_B = rr_u * (2.0/dr_u**2 + 2.0/dz_u**2 + inv_r_u**2 + inv_l_c_sq)
    inv_diag = 1.0 / diag_B.clamp(min=1e-30)
    dA = dr_u * dz_u

    def dot(a, b):
        return (a * b).sum() * dA

    # PCG
    psi = torch.zeros(Nr_u, Nz_u, device=device, dtype=dtype)
    r_vec = rhs.clone()
    z_vec = inv_diag * r_vec
    p_vec = z_vec.clone()
    rz_old = dot(r_vec, z_vec)
    rhs_norm = dot(r_vec, r_vec).sqrt().item()

    if rhs_norm < 1e-30:
        return torch.tensor(0.0, device=device, dtype=dtype)

    rel_res = 1.0
    for i in range(cg_iter):
        Bp = apply_B(p_vec)
        pBp = dot(p_vec, Bp)
        if pBp.item() <= 0:
            break
        alpha = rz_old / pBp
        psi = psi + alpha * p_vec
        r_vec = r_vec - alpha * Bp
        rel_res = dot(r_vec, r_vec).sqrt().item() / rhs_norm
        if rel_res < 1e-6:
            break
        z_vec = inv_diag * r_vec
        rz_new = dot(r_vec, z_vec)
        beta = rz_new / rz_old
        p_vec = z_vec + beta * p_vec
        rz_old = rz_new

    status = "OK" if rel_res < 1e-6 else f"rel={rel_res:.1e}"
    print(f"    PCG(screened, l_c={np.sqrt(l_c_sq):.3f}): {i+1} iters, {status}, "
          f"|psi|={psi.abs().max().item():.4f}", flush=True)

    # Strain energy (same form as in the locked-limit case)
    p_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_r[1:-1] = psi; p_r[0] = -psi[0]; p_r[-1] = 0.0
    p_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_z[:, 1:-1] = psi; p_z[:, 0] = psi[:, -1]; p_z[:, -1] = psi[:, 0]

    dpsi_dr = (p_r[2:] - p_r[:-2]) / (2 * dr_u)
    dpsi_dz = (p_z[:, 2:] - p_z[:, :-2]) / (2 * dz_u)

    u_r = -dpsi_dz
    u_z = inv_r_u * psi + dpsi_dr

    p_ur_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_ur_r[1:-1] = u_r; p_ur_r[0] = -u_r[0]; p_ur_r[-1] = 0.0
    p_ur_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_ur_z[:, 1:-1] = u_r; p_ur_z[:, 0] = u_r[:, -1]; p_ur_z[:, -1] = u_r[:, 0]
    p_uz_r = torch.zeros(Nr_u + 2, Nz_u, device=device, dtype=dtype)
    p_uz_r[1:-1] = u_z; p_uz_r[0] = u_z[0]; p_uz_r[-1] = 0.0
    p_uz_z = torch.zeros(Nr_u, Nz_u + 2, device=device, dtype=dtype)
    p_uz_z[:, 1:-1] = u_z; p_uz_z[:, 0] = u_z[:, -1]; p_uz_z[:, -1] = u_z[:, 0]

    eps_rr = (p_ur_r[2:] - p_ur_r[:-2]) / (2 * dr_u)
    eps_zz = (p_uz_z[:, 2:] - p_uz_z[:, :-2]) / (2 * dz_u)
    eps_ff = u_r * inv_r_u
    eps_rz = 0.5 * ((p_ur_z[:, 2:] - p_ur_z[:, :-2]) / (2 * dz_u) +
                     (p_uz_r[2:] - p_uz_r[:-2]) / (2 * dr_u))

    e_strain = eps_rr**2 + eps_zz**2 + eps_ff**2 + 2 * eps_rz**2
    E_u = 2 * np.pi * (e_strain * rr_u).sum() * dr_u * dz_u

    if return_psi:
        info = {
            'psi': psi,
            'rr_u': rr_u,
            'r_u': r_u,
            'z_u': z_u,
            'dr_u': dr_u,
            'dz_u': dz_u,
            'r_s': r_s,
            'z_s': z_s,
            'l_c_sq': l_c_sq,
            'inv_l_c_sq': inv_l_c_sq,
        }
        return E_u, info
    return E_u


# ============================================================
# Full Cosserat energy on the stretched grid
# ============================================================
def compute_energy_cosserat_stretched(n, metric, cfg):
    """E = E_OF(K1, K2, K3) + E_Sk(c4) + E_mass(m^2)"""
    E_of, E_sp, E_tw, E_be = compute_oseen_frank_stretched(n, metric, cfg)
    E_sk = compute_skyrme_stretched(n, metric, cfg)

    E_mass = torch.tensor(0.0, device=n.device, dtype=n.dtype)
    if getattr(cfg, 'm2', 0) > 0:
        n3 = n[2]
        J = metric.hr * metric.hz
        dA = metric.dxi * metric.deta
        E_mass = cfg.m2 * 2 * np.pi * ((1.0 - n3)**2 * metric.rr * J).sum() * dA

    return E_of + E_sk + E_mass, E_of, E_sk, E_mass


# ============================================================
# Topological charge Q on the stretched grid
# ============================================================
def compute_Q_stretched(n, metric):
    """Q = (1 / 4*pi) * integral n . (dn/dr x dn/dz) dr dz (with Jacobian)."""
    n1, n2, n3 = n[0], n[1], n[2]

    n1_r, n2_r, n3_r = field_grad_r_stretched(n1, n2, n3, metric)
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)

    cx = n2_r*n3_z - n3_r*n2_z
    cy = n3_r*n1_z - n1_r*n3_z
    cz = n1_r*n2_z - n2_r*n1_z
    q_density = n1*cx + n2*cy + n3*cz

    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    I_raw = (q_density * J).sum() * dA
    Q = I_raw / (4.0 * np.pi)
    return Q


# End of module. This file is a library: there is no standalone entry point.
# To run the Derrick verification, execute `python derrick_scan.py`.
