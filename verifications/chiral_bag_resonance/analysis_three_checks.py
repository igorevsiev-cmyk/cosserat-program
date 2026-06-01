#!/usr/bin/env python3
"""
analysis_three_checks.py -- Hessian spectral analysis around the canonical
paper electron on the dyadic box L_r = 17, L_z = 33 l_0 (paper §6.5).

Three diagnostics are produced:

  (A) Radial profile rho_k(r) of the lowest eigenmodes. Localization in the
      tail (r > R_r = 0.64 l_0) is the spectral signature of the chiral
      bag: bag-core is rigid, soft modes live in the elastic shell.

  (B) Generalized eigenproblem  H v = omega^2 M v with mass matrix
      M = diag(2*pi * r * J * d_xi * d_eta) so that eigvalues are physical
      omega^2 (volume-weighted Rayleigh quotient), directly comparable
      across box sizes (cf. analysis_doubled_box.py for L=34 and
      analysis_quad_box.py for L=68).

  (C) Targeted collapse seed v_shrink = dn/dR_r (tangent-projected) probing
      the ring-shrinking direction discussed in [electron-mass §4.3].

Pipeline:
  1. Build canonical hopfion n* on the stretched grid (paper NM optimum).
  2. Hessian-vector product via double autograd of E_OF + E_Sk.
  3. (B) Block LOBPCG, k=4 lowest physical eigvals from random init.
  4. (A) Radial profiles rho_k(r) of those eigvecs.
  5. (C) v_shrink seed: refined LOBPCG step + Rayleigh quotient.

Outputs:
  result_hessian_L17.json  -- summary (omega^2, profiles, metadata)
  result_hessian_L17.pt    -- eigvecs for downstream analysis
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np
import torch

from stretched_grid import (
    create_stretched_grid,
    compute_oseen_frank_stretched,
    compute_skyrme_stretched,
    compute_energy_cosserat_stretched,
    compute_E_u_screened,
    compute_Q_stretched,
    field_grad_z_stretched,
)


EPS_0 = 8.854187817e-12
HBAR = 1.054571817e-34
C_LIGHT = 299792458.0
E_CHARGE = 1.602176634e-19
M0 = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV = M0 * C_LIGHT**2 / E_CHARGE
MU_C = 2.0 * np.pi
keV = M0C2_eV / 1000.0

PAPER_R_R = 0.6408160149362525
PAPER_R_Z = 0.8072875518184682
PAPER_W   = 0.7019955806536682


class Cfg:
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3
    K1 = 2.0; K2 = 2.0; K3 = 14.56
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    cg_iter = 2000


def hopf_init(rr, zz, R_r, R_z, w):
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


def project_S2(n_raw):
    return n_raw / n_raw.norm(dim=0, keepdim=True).clamp(min=1e-10)


def project_tangent(v, n):
    radial = (v * n).sum(dim=0, keepdim=True)
    return v - radial * n


def metric_inner(a, b, metric):
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    rr = metric.rr
    s = (a * b).sum(dim=0)
    return 2 * np.pi * (s * rr * J).sum() * dA


def euclidean_inner(a, b):
    """Sum a·b over all DOFs without volume weighting."""
    return (a * b).sum()


def make_hvp(n_star, metric, cfg, channel='total'):
    n_star_d = n_star.detach()
    if channel == 'total':
        def E_fn(n, m, c):
            _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n, m, c)
            return E_of + E_sk
    elif channel == 'OF':
        def E_fn(n, m, c):
            E_of, _, _, _ = compute_oseen_frank_stretched(n, m, c)
            return E_of
    elif channel == 'Sk':
        def E_fn(n, m, c):
            return compute_skyrme_stretched(n, m, c)

    def hvp(delta_n):
        v_t = project_tangent(delta_n, n_star_d)
        n_var = n_star_d.clone().requires_grad_(True)
        n_proj = project_S2(n_var)
        E = E_fn(n_proj, metric, cfg)
        g = torch.autograd.grad(E, n_var, create_graph=True)[0]
        gv = (g * v_t).sum()
        Hv = torch.autograd.grad(gv, n_var)[0]
        return project_tangent(Hv, n_star_d).detach()
    return hvp


def compute_z_translation_mode(n_star, metric):
    n1, n2, n3 = n_star[0], n_star[1], n_star[2]
    n1_z, n2_z, n3_z = field_grad_z_stretched(n1, n2, n3, metric)
    dnz = torch.stack([n1_z, n2_z, n3_z])
    dnz_t = project_tangent(dnz, n_star)
    nrm = metric_inner(dnz_t, dnz_t, metric).sqrt().item()
    return dnz_t / max(nrm, 1e-30), nrm


# ----------------------------------------------------------------------
# Generalized LOBPCG: H v = ω² M v
#
# Standard Ritz (which we used previously):
#   Hs = S^T W A S, Bs = S^T W S → gives EUCLIDEAN eigvals of A in W-Ritz
#
# Generalized Ritz (for physical ω²):
#   Hs = S^T A S (Euclidean!), Bs = S^T M S = S^T W S
#   solves    A v = ω² M v
#
# This LOBPCG implements the GENERALIZED problem:
#   - Inner product for orthogonality = W (physical)
#   - Hs computed with EUCLIDEAN (no W)  ← key change!
# ----------------------------------------------------------------------
def lobpcg_generalized(hvp_fn, k, device, dtype,
                       metric, n_star,
                       zero_modes=None,
                       initial_X=None,
                       max_iter=50, tol=1e-5, verbose=True):
    """Block LOBPCG for the generalized problem A v = ω² M v
       where M = diag(2π r J dξ dη) (volume weight)."""
    if zero_modes is None:
        zero_modes = []
    Nr, Nz = n_star.shape[1], n_star.shape[2]

    def ortho(X):
        k_ = X.shape[0]
        for i in range(k_):
            for zm in zero_modes:
                ov = metric_inner(X[i], zm, metric)
                X[i] = X[i] - ov * zm
            for j in range(i):
                ov = metric_inner(X[i], X[j], metric)
                X[i] = X[i] - ov * X[j]
            X[i] = project_tangent(X[i], n_star)
            nrm = metric_inner(X[i], X[i], metric).sqrt().item()
            if nrm < 1e-12:
                X[i] = torch.randn_like(X[i])
                X[i] = project_tangent(X[i], n_star)
                for zm in zero_modes:
                    ov = metric_inner(X[i], zm, metric)
                    X[i] = X[i] - ov * zm
                for j in range(i):
                    ov = metric_inner(X[i], X[j], metric)
                    X[i] = X[i] - ov * X[j]
                X[i] = project_tangent(X[i], n_star)
                nrm = metric_inner(X[i], X[i], metric).sqrt().item()
            X[i] = X[i] / max(nrm, 1e-12)
        return X

    if initial_X is None:
        torch.manual_seed(42)
        X = torch.randn(k, 3, Nr, Nz, device=device, dtype=dtype)
    else:
        X = initial_X.clone().to(device).to(dtype)
    X = ortho(X)

    if verbose:
        print(f"  Computing initial AX (k={k})...", flush=True)
    AX = torch.stack([hvp_fn(X[i]) for i in range(k)])

    P = torch.zeros_like(X)
    AP = torch.zeros_like(AX)
    have_P = False
    eigvals_prev = None

    for it in range(max_iter):
        # Generalized Rayleigh quotient: ω² = <v, Av>_E / <v, v>_W
        rq = torch.tensor([
            euclidean_inner(X[i], AX[i]).item() /
            max(metric_inner(X[i], X[i], metric).item(), 1e-30)
            for i in range(k)
        ], device=device, dtype=dtype)

        # Residuals R = AX − M·X·diag(rq)
        # For generalized problem M^{-1}A v = ω² v, residual is (A v - ω² M v)
        # We use the W-norm of this for convergence check
        W = metric.rr * metric.hr * metric.hz  # per-cell volume (without 2π·dxidy)
        scale = 2 * np.pi * metric.dxi * metric.deta
        # W_full per-cell: scale * (metric.rr * metric.hr * metric.hz)
        R = AX - X * (rq.view(k, 1, 1, 1) * scale * W)

        # Orthogonalise R
        for i in range(k):
            for zm in zero_modes:
                ov = metric_inner(R[i], zm, metric)
                R[i] = R[i] - ov * zm
            for j in range(k):
                ov = metric_inner(R[i], X[j], metric)
                R[i] = R[i] - ov * X[j]
            R[i] = project_tangent(R[i], n_star)

        res_norms = torch.tensor([
            metric_inner(R[i], R[i], metric).sqrt().item() for i in range(k)
        ], device=device, dtype=dtype)

        if verbose:
            srt = sorted(rq.cpu().numpy().tolist())
            if len(srt) == 1:
                print(f"  [iter {it:3d}]  ω² = {srt[0]:+.5f}   "
                      f"|R|_max = {res_norms.max().item():.2e}", flush=True)
            else:
                print(f"  [iter {it:3d}]  ω²_sorted = "
                      f"[{srt[0]:+.5f}, {srt[1]:+.5f}, ..., {srt[-1]:+.5f}]   "
                      f"|R|_max = {res_norms.max().item():.2e}", flush=True)

        if eigvals_prev is not None:
            change = torch.abs(rq - eigvals_prev).max().item()
            if change < tol * max(1.0, torch.abs(rq).max().item()):
                if verbose:
                    print(f"  Converged at iter {it}", flush=True)
                break
        eigvals_prev = rq.clone()

        for i in range(k):
            if res_norms[i].item() > 1e-12:
                R[i] = R[i] / res_norms[i]

        AR = torch.stack([hvp_fn(R[i]) for i in range(k)])

        if have_P:
            S  = torch.cat([X, R, P], dim=0)
            AS = torch.cat([AX, AR, AP], dim=0)
        else:
            S  = torch.cat([X, R], dim=0)
            AS = torch.cat([AX, AR], dim=0)

        nb = S.shape[0]
        # GENERALIZED Hs: EUCLIDEAN inner product (no W)
        Hs = torch.zeros(nb, nb, device=device, dtype=dtype)
        Bs = torch.zeros(nb, nb, device=device, dtype=dtype)
        Sw = S * (metric.rr * metric.hr * metric.hz)
        const = 2 * np.pi * metric.dxi * metric.deta
        for i in range(nb):
            for j in range(nb):
                Hs[i, j] = (S[i] * AS[j]).sum()        # Euclidean!
                Bs[i, j] = (Sw[i] * S[j]).sum() * const  # Physical (W)
        del Sw
        Hs = 0.5 * (Hs + Hs.t())
        Bs = 0.5 * (Bs + Bs.t())

        Bs_reg = Bs + 1e-10 * torch.eye(nb, device=device, dtype=dtype)
        L = torch.linalg.cholesky(Bs_reg)
        Linv = torch.linalg.solve_triangular(
            L, torch.eye(nb, device=device, dtype=dtype), upper=False)
        Hs_t = Linv @ Hs @ Linv.t()
        Hs_t = 0.5 * (Hs_t + Hs_t.t())
        evals, evecs_t = torch.linalg.eigh(Hs_t)
        evecs = Linv.t() @ evecs_t

        C = evecs[:, :k]
        new_X = torch.einsum('ki...,kj->ji...', S, C)
        C_RP = evecs[k:, :k]
        if have_P:
            S_RP = torch.cat([R, P], dim=0)
            AS_RP = torch.cat([AR, AP], dim=0)
        else:
            S_RP = R
            AS_RP = AR
        new_P = torch.einsum('ki...,kj->ji...', S_RP, C_RP)
        new_AP = torch.einsum('ki...,kj->ji...', AS_RP, C_RP)

        del S, AS, Hs, Bs, Bs_reg, L, Linv, Hs_t, evecs, evecs_t, C, C_RP
        torch.cuda.empty_cache()

        new_X = ortho(new_X)
        del AX
        torch.cuda.empty_cache()
        new_AX = torch.stack([hvp_fn(new_X[i]) for i in range(k)])

        del X, R, AR
        if have_P:
            del P, AP
        torch.cuda.empty_cache()

        X = new_X; AX = new_AX
        P = new_P; AP = new_AP
        have_P = True

    eigvals = torch.tensor([
        euclidean_inner(X[i], AX[i]).item() /
        max(metric_inner(X[i], X[i], metric).item(), 1e-30)
        for i in range(k)
    ], device=device, dtype=dtype)
    return eigvals.cpu().numpy(), X.cpu()


# ----------------------------------------------------------------------
# (A) Spatial profile rho_k(r) of mode v_k
# ----------------------------------------------------------------------
def radial_profile(eigvec, metric, n_radial_bins=200, r_max=17.0):
    """
    Returns ρ_k(r) = ∫_z |δn(r, z)|² · 2π r dz, binned in r.

    eigvec: (3, Nr, Nz) tensor
    Returns: r_bin_centers (n_bins,), rho (n_bins,)
    """
    device = eigvec.device
    dtype = eigvec.dtype
    rr = metric.rr  # (Nr, Nz)
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta

    # |δn|² at each grid point
    sq = (eigvec * eigvec).sum(dim=0)  # (Nr, Nz)

    # Volume weight: 2π r J for cylindrical integration
    weighted = sq * (2 * np.pi * rr * J) * dA  # energy in each cell

    # Integrate over z for each r-row → ρ(r_i)
    rho_per_row = weighted.sum(dim=1)  # (Nr,)

    # r-coords at center of each row
    r_centers = rr[:, 0].cpu().numpy()
    rho_np = rho_per_row.cpu().numpy()

    # Bin into uniform r grid
    n_bins = n_radial_bins
    r_bins = np.linspace(0, r_max, n_bins + 1)
    r_bin_centers = 0.5 * (r_bins[:-1] + r_bins[1:])
    rho_binned = np.zeros(n_bins)
    for i in range(len(r_centers)):
        if r_centers[i] > r_max:
            break
        bin_idx = int(r_centers[i] / r_max * n_bins)
        if 0 <= bin_idx < n_bins:
            rho_binned[bin_idx] += rho_np[i]

    return r_bin_centers, rho_binned


def tail_localization_score(r_centers, rho, R_r=0.64):
    """
    Returns fraction of ∫|δn|² that lives at r > R_r.
    > 0.5 means mode is in the TAIL (bag-model evidence).
    """
    total = rho.sum()
    tail = rho[r_centers > R_r].sum()
    return tail / total if total > 0 else 0.0


# ----------------------------------------------------------------------
# (C) v_shrink seed: finite-difference dn/dR_r, projected to the tangent
#     space of S^2 at n_star.
# ----------------------------------------------------------------------
def make_shrink_seed(rr, zz, n_star, delta=0.01):
    """
    v_shrink = (n(R_r+δ) − n(R_r−δ)) / (2δ),
    then projected onto tangent of S² at n_star.

    Note: the chord between two points on S² does NOT lie in the
    tangent plane (S² curvature). We must explicitly project.
    """
    n_plus  = hopf_init(rr, zz, PAPER_R_R + delta, PAPER_R_Z, PAPER_W)
    n_minus = hopf_init(rr, zz, PAPER_R_R - delta, PAPER_R_Z, PAPER_W)
    v_shrink_raw = (n_plus - n_minus) / (2.0 * delta)
    # Project to tangent of n_star
    v_shrink = project_tangent(v_shrink_raw, n_star)
    return v_shrink


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()
    K_RANDOM = 4   # how many random-init modes to find (smaller for memory)
    MAX_ITER_RAND = 50
    MAX_ITER_SEED = 30

    print("=" * 100)
    print("ANALYSIS THREE CHECKS: tail profiles, generalized ω², collapse seed")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid: {cfg.Nr}×{cfg.Nz}")

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    with torch.no_grad():
        n_star = hopf_init(rr, zz, PAPER_R_R, PAPER_R_Z, PAPER_W)
        _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n_star, metric, cfg)
        Q = compute_Q_stretched(n_star, metric).item()
    E_of_keV = E_of.item() * keV
    E_sk_keV = E_sk.item() * keV
    print(f"E_OF={E_of_keV:.3f} keV, E_Sk={E_sk_keV:.3f} keV, "
          f"E_n_tot={E_of_keV+E_sk_keV:.3f} keV, Q={Q:+.7f}")
    print()

    hvp_total = make_hvp(n_star, metric, cfg, channel='total')
    zmode, _ = compute_z_translation_mode(n_star, metric)

    # ------------------------------------------------------------------
    # (B) Generalized eigvals with random init
    # ------------------------------------------------------------------
    print("-" * 100)
    print(f"(B) GENERALIZED LOBPCG: H v = omega^2 M v, random init, k={K_RANDOM}")
    print("-" * 100)
    t0 = time.time()
    omega2_rand, eigvecs_rand = lobpcg_generalized(
        hvp_total, k=K_RANDOM, device=device, dtype=torch.float64,
        metric=metric, n_star=n_star,
        zero_modes=[zmode],
        initial_X=None,
        max_iter=MAX_ITER_RAND, tol=1e-5, verbose=True,
    )
    t_rand = time.time() - t0
    print(f"\nDone in {t_rand:.0f}s")
    print(f"omega^2_rand (sim units): {omega2_rand}")
    # In natural Cosserat units omega^2 has dimension 1/length^2; report
    # sqrt(omega^2) as the "frequency-like" sim-unit quantity.
    omega_rand_sqrt = np.sqrt(np.abs(omega2_rand))
    print(f"sqrt(omega^2) (sim^0.5): {omega_rand_sqrt}")
    print()

    # ------------------------------------------------------------------
    # (A) Spatial profiles rho_k(r) for each random eigvec
    # ------------------------------------------------------------------
    print("-" * 100)
    print(f"(A) RADIAL PROFILES rho(r) of random eigvecs")
    print("-" * 100)
    print(f"R_r (paper) = {PAPER_R_R:.4f}")
    print(f"{'mode':>4} | {'omega^2':>10} | {'peak r':>10} | {'tail (r>R_r)':>15} | {'class':>12}")
    print("-" * 70)
    profiles_rand = []
    for k_ in range(K_RANDOM):
        v_k = eigvecs_rand[k_].to(device)
        r_c, rho_k = radial_profile(v_k, metric, n_radial_bins=200, r_max=cfg.L_r)
        peak_r = r_c[np.argmax(rho_k)]
        tail_frac = tail_localization_score(r_c, rho_k, R_r=PAPER_R_R)
        if tail_frac > 0.8:
            cls = 'TAIL ✓'
        elif tail_frac < 0.2:
            cls = 'CORE'
        else:
            cls = 'mixed'
        print(f"{k_:>4} | {omega2_rand[k_]:>+10.4f} | {peak_r:>10.4f} | "
              f"{tail_frac:>15.4f} | {cls:>12}")
        profiles_rand.append({'mode': k_, 'r_centers': r_c.tolist(),
                              'rho': rho_k.tolist(),
                              'peak_r': float(peak_r),
                              'tail_frac': float(tail_frac),
                              'omega2': float(omega2_rand[k_])})
    print()

    # ------------------------------------------------------------------
    # (C) Targeted collapse seed: v_shrink = dn/dR_r, tangent-projected
    # ------------------------------------------------------------------
    print("-" * 100)
    print("(C) COLLAPSE SEED: v_shrink = dn/dR_r (tangent-projected)")
    print("-" * 100)
    v_shrink = make_shrink_seed(rr, zz, n_star, delta=0.005)
    v_shrink_norm = metric_inner(v_shrink, v_shrink, metric).sqrt().item()
    v_shrink = v_shrink / max(v_shrink_norm, 1e-30)
    print(f"||v_shrink||_phys (before unitisation) = {v_shrink_norm:.4f}")

    # Rayleigh quotient on v_shrink WITHOUT any refinement
    Hv = hvp_total(v_shrink)
    omega2_direct_E = euclidean_inner(v_shrink, Hv).item() / \
                      max(metric_inner(v_shrink, v_shrink, metric).item(), 1e-30)
    omega2_direct_W = metric_inner(v_shrink, Hv, metric).item() / \
                      max(metric_inner(v_shrink, v_shrink, metric).item(), 1e-30)
    print(f"Raw Rayleigh of v_shrink (no refinement):")
    print(f"  generalized ω² (= <v,Hv>_E / <v,v>_W)  = {omega2_direct_E:+.4e}")
    print(f"  W-norm        λ  (= <v,Hv>_W / <v,v>_W) = {omega2_direct_W:+.4e}")
    print()

    # Run LOBPCG seeded with v_shrink (k=1) to refine
    initial_X = v_shrink.unsqueeze(0)  # (1, 3, Nr, Nz)
    print(f"Refining v_shrink via LOBPCG (k=1, max_iter={MAX_ITER_SEED})...")
    t0 = time.time()
    omega2_collapse, eigvec_collapse = lobpcg_generalized(
        hvp_total, k=1, device=device, dtype=torch.float64,
        metric=metric, n_star=n_star,
        zero_modes=[zmode],
        initial_X=initial_X,
        max_iter=MAX_ITER_SEED, tol=1e-5, verbose=True,
    )
    t_seed = time.time() - t0
    print(f"\nSeeded LOBPCG done in {t_seed:.0f}s")
    print(f"Refined ω² (collapse seed): {omega2_collapse}")
    if omega2_collapse[0] < 0:
        print(f"  ★ NEGATIVE — collapse mode confirmed!")
    elif abs(omega2_collapse[0]) < 1e-4:
        print(f"  ≈ 0 — marginal direction (boundary of stability)")
    else:
        print(f"  Positive — no collapse direction found via this seed")
    print()

    # Radial profile of collapse mode
    v_c = eigvec_collapse[0].to(device)
    r_c, rho_c = radial_profile(v_c, metric, n_radial_bins=200, r_max=cfg.L_r)
    peak_r_c = r_c[np.argmax(rho_c)]
    tail_frac_c = tail_localization_score(r_c, rho_c, R_r=PAPER_R_R)
    cls_c = 'TAIL' if tail_frac_c > 0.8 else ('CORE' if tail_frac_c < 0.2 else 'mixed')
    print(f"Collapse-seed mode profile: peak_r={peak_r_c:.4f}, "
          f"tail_frac={tail_frac_c:.4f}, class={cls_c}")
    print()

    # ------------------------------------------------------------------
    # Save everything
    # ------------------------------------------------------------------
    out_dir = os.path.dirname(os.path.abspath(__file__))
    # Eigenvectors (compressed: just save sparse representation via .pt)
    torch.save({
        'random': {
            'omega2': omega2_rand,
            'eigvecs': eigvecs_rand,  # (K_RANDOM, 3, Nr, Nz) on CPU
        },
        'collapse': {
            'omega2': omega2_collapse,
            'eigvec': eigvec_collapse[0],
        },
        'n_star_shape': list(n_star.shape),
        'meta': {
            'R_r': PAPER_R_R, 'R_z': PAPER_R_Z, 'w': PAPER_W,
            'config': {'Nr': cfg.Nr, 'Nz': cfg.Nz, 'L_r': cfg.L_r, 'L_z': cfg.L_z,
                       'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
                       'K1': cfg.K1, 'K2': cfg.K2, 'K3': cfg.K3,
                       'c4': cfg.c4, 'm2': cfg.m2, 'mu_c': MU_C},
        },
    }, os.path.join(out_dir, 'result_hessian_L17.pt'))

    summary = {
        'generalized_omega2_random': omega2_rand.tolist(),
        'sqrt_omega2_random': np.sqrt(np.abs(omega2_rand)).tolist(),
        'random_profiles': profiles_rand,
        'collapse_seed': {
            'v_shrink_norm_initial': v_shrink_norm,
            'direct_omega2': float(omega2_direct_E),
            'direct_W_norm':  float(omega2_direct_W),
            'refined_omega2': float(omega2_collapse[0]),
            'profile': {
                'r_centers': r_c.tolist(),
                'rho': rho_c.tolist(),
                'peak_r': float(peak_r_c),
                'tail_frac': float(tail_frac_c),
            },
        },
        'timing': {
            'random_lobpcg_s': t_rand,
            'seeded_lobpcg_s': t_seed,
        },
    }
    with open(os.path.join(out_dir, 'result_hessian_L17.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Saved eigvecs: result_hessian_L17.pt")
    print(f"Saved summary: result_hessian_L17.json")
    print("\nDONE")


if __name__ == '__main__':
    main()
