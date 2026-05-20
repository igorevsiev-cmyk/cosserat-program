#!/usr/bin/env python3
"""
derrick_scan.py — Derrick test for the canonical electron configuration.

Takes the canonical 3-parameter Hopf ansatz (R_r=0.64082, R_z=0.80729,
w=0.70200) — the NM optimum of the bare Cosserat functional (m^2 = 0)
on the dyadic box L = 17 x 33, from the companion
`electron_mass_minimization/` artifact — and rescales
(R_r, R_z) by lambda for lambda in [0.6, 3.0]. For each lambda the three
energy components E_OF, E_Sk, E_u are evaluated on the bare functional.
If lambda=1.0 is the minimum, the canonical configuration is at Derrick
balance; otherwise the curve shows in which direction the system would
prefer to deform.

The parameter w (chirality) is NOT rescaled — it is a dimensionless angular
parameter of the ansatz, not a length scale.

The empirical scaling laws under x -> lambda*x are:
    E_OF   ~ lambda^1     (quadratic gradients)
    E_Sk   ~ lambda^-1    (quartic Faddeev-Skyrme term)
    E_u    ~ lambda^2     (Cosserat coupling with fixed screening length l_c)

The Derrick identity dE/dlambda |_{lambda=1} = 0 becomes
    E_OF - E_Sk + 2*E_u = 0
"""

import sys, os
os.environ['PYTHONUNBUFFERED'] = '1'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import torch
import numpy as np
import time

from stretched_grid import (
    create_stretched_grid,
    compute_energy_cosserat_stretched,
    compute_E_u_screened,
    compute_Q_stretched,
)


# Base configuration container. The subclass Cfg (below) overrides the
# entries that matter for the canonical electron run; everything left at
# the default values here is harmless padding kept only so that stretched_grid
# can call getattr(cfg, ...) without raising.
class Config:
    Nr = 512; Nz = 1024
    L_r = 25.0; L_z = 50.0
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    kappa_twist = 1.0
    kappa_rz = 1.0
    gamma_c = 0.0
    use_4th_order = True
    R_hopf = 1.0
    n_steps = 500; lr = 1.0
    log_every = 10; q_min = 0.85
    lambda_Q = 1000.0
    Q_target = -1.0
    use_float64 = True

# Physical constants (CODATA 2018)
EPS_0 = 8.854187817e-12
HBAR = 1.054571817e-34
C_LIGHT = 299792458.0
E_CHARGE = 1.602176634e-19
# Natural unit conversion: m0 c^2 in eV (the simulator energy unit)
M0 = (2 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV = M0 * C_LIGHT**2 / E_CHARGE
# Cosserat coupling: mu_c = 2*pi in simulation units (= eta from theory)
MU_C = 2.0 * np.pi


class Cfg(Config):
    """Canonical configuration for the electron hopfion."""
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0          # dyadic box: L_r = log2(2^7*2^10), L_z = 2*L_r-1
    use_float64 = True; R_hopf = 1.0
    K1 = 2.0; K2 = 2.0; K3 = 14.56          # K3 = K1 * (1 + eta), eta = 2*pi
    c2 = 1.0; c4 = 1.0
    m2 = 0.0                                  # no mass term in the bare functional
    n_frozen_r = 2; n_frozen_edge = 3
    beta_r = 6.0; beta_z = 3.0                # grid stretching strength
    cg_iter = 2000                            # PCG iteration cap for u-channel


# Canonical 3-parameter Hopf ansatz (NM optimum of the bare Cosserat
# functional with m^2 = 0 on the dyadic box L = 17 x 33,
# see ../electron_mass_minimization/)
R_R_E = 0.64082
R_Z_E = 0.80729
W_E   = 0.70200


def hopf_variational(rr, zz, R_r, R_z, w):
    """Three-parameter Hopf ansatz n(r, z) on S^2."""
    r = rr / R_r
    z = zz / R_z
    Y = r * r + z * z - 1.0
    D = (2.0 * z)**2 + Y * Y
    w2 = w * w
    P = (D + 4.0 * r * r * w2).clamp(min=1e-30)
    n3 = (D - 4.0 * r * r * w2) / P
    n1 = 8.0 * r * z * w / P
    n2 = -4.0 * r * Y * w / P
    m = torch.stack([n1, n2, n3])
    return m / m.norm(dim=0, keepdim=True).clamp(min=1e-10)


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    print("=" * 100)
    print("DERRICK SCAN of the canonical electron configuration")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid:   {cfg.Nr} x {cfg.Nz}")
    print(f"K1={cfg.K1}, K2={cfg.K2}, K3={cfg.K3}, c4={cfg.c4}")
    print(f"mu_c = 2*pi = {MU_C:.6f}")
    print(f"Canonical ansatz: R_r={R_R_E}, R_z={R_Z_E}, w={W_E}")
    print()
    print("Scaling (R_r, R_z) -> lambda*(R_r, R_z), w held fixed.")
    print("A minimum at lambda=1 confirms Derrick balance of the canonical point.")
    print()

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z)

    # Sample lambda values, denser near lambda=1
    lambdas = [0.6, 0.7, 0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2, 1.4, 1.6, 2.0, 2.5, 3.0]

    print(f"{'lam':>5} {'E_OF':>8} {'E_Sk':>8} {'E_u':>8} "
          f"{'E_tot':>8} {'m_e_bare(keV)':>14} {'Q':>10} {'Derrick':>10}")
    print(f"{'':5} {'keV':>8} {'keV':>8} {'keV':>8} "
          f"{'keV':>8} {'':>14} {'':>10} {'dE/dlam':>10}")
    print("-" * 95)

    results = []
    t_start = time.time()

    for lam in lambdas:
        R_r_lam = R_R_E * lam
        R_z_lam = R_Z_E * lam

        with torch.no_grad():
            n = hopf_variational(rr, zz, R_r_lam, R_z_lam, W_E)
            E_phi_total, E_of, E_sk, _ = compute_energy_cosserat_stretched(n, metric, cfg)
            E_u = compute_E_u_screened(n, metric, MU_C, cg_iter=cfg.cg_iter).item()
            Q = compute_Q_stretched(n, metric).item()

        E_of_v = E_of.item() * M0C2_eV / 1000
        E_sk_v = E_sk.item() * M0C2_eV / 1000
        E_u_v = E_u * M0C2_eV / 1000
        E_tot_v = E_of_v + E_sk_v + E_u_v

        # Derrick residual at the current lambda.
        # Under x -> lambda*x with fixed material constants:
        #   E_OF   ~ lambda    => dE_OF/dlam = E_OF / lam
        #   E_Sk   ~ 1/lambda  => dE_Sk/dlam = -E_Sk / lam
        #   E_u    ~ lambda^2  => dE_u/dlam = 2 * E_u / lam   (l_c fixed)
        # so lambda * dE/dlam = E_OF - E_Sk + 2*E_u.
        # This residual should vanish at the Derrick minimum.
        derrick = E_of_v - E_sk_v + 2 * E_u_v

        print(f"{lam:>5.2f} {E_of_v:>8.2f} {E_sk_v:>8.2f} {E_u_v:>8.2f} "
              f"{E_tot_v:>8.2f} {E_tot_v:>14.3f} {Q:>+10.6f} {derrick:>+10.2f}",
              flush=True)

        results.append({
            'lambda': lam, 'E_OF': E_of_v, 'E_Sk': E_sk_v,
            'E_u': E_u_v, 'E_tot': E_tot_v, 'Q': Q, 'derrick': derrick,
        })

    # Locate the discrete minimum of E_tot
    energies = [r['E_tot'] for r in results]
    idx_min = int(np.argmin(energies))
    # Index of lambda = 1.0 in the list above
    idx_one = lambdas.index(1.0)
    print()
    print("=" * 105)
    print(f"Minimum E_tot: lambda = {results[idx_min]['lambda']:.2f}, "
          f"E = {results[idx_min]['E_tot']:.3f} keV "
          f"(delta from lambda=1: {results[idx_min]['E_tot'] - results[idx_one]['E_tot']:+.3f} keV)")
    print("=" * 105)

    print("\nInterpretation:")
    if idx_min == idx_one:
        print("  OK: lambda=1.0 is the discrete minimum -- Derrick balance is satisfied.")
        print("      Canonical 3-parameter ansatz lies at the energy minimum along")
        print("      the spatial-dilation direction.")
    elif results[idx_min]['lambda'] > 1.0:
        print(f"  WARNING: minimum at lambda={results[idx_min]['lambda']:.2f} (>1) -- "
              f"the system prefers to EXPAND.")
        print("      Canonical 3-parameter ansatz is NOT at Derrick balance.")
        print(f"      Lowest tabulated m_e = {results[idx_min]['E_tot']:.2f} keV.")
    else:
        print(f"  WARNING: minimum at lambda={results[idx_min]['lambda']:.2f} (<1) -- "
              f"the system prefers to SHRINK.")
        print(f"      Lowest tabulated m_e = {results[idx_min]['E_tot']:.2f} keV.")

    # CSV output
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'derrick_scan.csv')
    with open(csv_path, 'w') as f:
        f.write("lambda,E_OF,E_Sk,E_u,E_tot,Q,derrick\n")
        for r in results:
            f.write(f"{r['lambda']},{r['E_OF']:.4f},{r['E_Sk']:.4f},"
                    f"{r['E_u']:.4f},{r['E_tot']:.4f},"
                    f"{r['Q']:.6f},{r['derrick']:.4f}\n")
    print(f"\nCSV: {csv_path}")
    print(f"Total wall time: {time.time()-t_start:.0f}s")
    print("\nDONE")


if __name__ == '__main__':
    main()
