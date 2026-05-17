#!/usr/bin/env python3
"""
nm_minimization.py — Nelder-Mead minimization of the canonical Cosserat
functional E[n, u] over the 3-parameter Hopf ansatz (R_r, R_z, w).

Verifies the central numerical claim of the paper:

    m_e^bare c^2 = 507.997 keV from {epsilon_0, mu_0, hbar}
    on a 1024 x 2048 grid

(bare electron mass; physical m_e (CODATA) = 510.999 keV; the gap of
3.002 keV is interpreted as standard QED renormalization, see paper §7.2)

with no fitted parameters: all five functional constants
(K_1, K_2, K_3, mu_c, c_4) are fixed by the structural identities of
the preceding work (SI Reduction via the Cosserat-continuum hypothesis,
DOI 10.5281/zenodo.20187199).

Method:
    Start from a generic simplex around (R_r, R_z, w) ~ (0.5, 0.7, 0.6),
    minimise E_total(R_r, R_z, w) by scipy.optimize.minimize with
    method='Nelder-Mead'. The objective is the full Cosserat energy
    (Frank-Oseen + Skyrme + screened Cosserat coupling); the
    topological charge Q_H = -1 is enforced exactly by the ansatz.

Output:
    - prints per-iteration progress to stdout
    - saves the optimum and its energy decomposition to result.json

Companion: see ../canonical_derrick/derrick_scan.py for the independent
verification that the optimum is a true Derrick minimum (stable under
spatial dilation).
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import torch
from scipy.optimize import minimize

from stretched_grid import (
    create_stretched_grid,
    compute_energy_cosserat_stretched,
    compute_E_u_screened,
    compute_Q_stretched,
)


# ----------------------------------------------------------------------
# Physical constants (CODATA 2018) and natural unit conversion
# ----------------------------------------------------------------------
EPS_0    = 8.854187817e-12          # F / m
HBAR     = 1.054571817e-34          # J . s
C_LIGHT  = 299792458.0              # m / s
E_CHARGE = 1.602176634e-19          # C

# Base mass scale: M0 c^2 = (2 pi hbar^3 / (c^5 epsilon_0))^(1/4) . c^2 / e
M0       = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV  = M0 * C_LIGHT**2 / E_CHARGE     # ~ 429.51 eV

# Cosserat coupling: mu_c = eta = 2 pi (rolling-contact identity)
MU_C     = 2.0 * np.pi


# ----------------------------------------------------------------------
# Configuration container
# ----------------------------------------------------------------------
class Config:
    """Padding defaults that stretched_grid.* expect via getattr()."""
    Nr = 512; Nz = 1024
    L_r = 25.0; L_z = 50.0
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    kappa_twist = 1.0; kappa_rz = 1.0; gamma_c = 0.0
    use_4th_order = True
    R_hopf = 1.0
    n_steps = 500; lr = 1.0
    log_every = 10; q_min = 0.85
    lambda_Q = 1000.0; Q_target = -1.0
    use_float64 = True


class Cfg(Config):
    """Canonical configuration matching the paper (1024 x 2048 grid)."""
    # Grid
    Nr = 1024; Nz = 2048
    L_r = 24.0; L_z = 48.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3

    # Cosserat constants (all derived from {epsilon_0, mu_0, hbar})
    K1 = 2.0; K2 = 2.0
    K3 = 14.56                         # = K1 * (1 + 2 pi)  rounded to 4 sig.fig.
    c2 = 1.0; c4 = 1.0
    m2 = 0.0                           # no mass term in the bare functional
    cg_iter = 2000                     # PCG cap for u-channel solver


# ----------------------------------------------------------------------
# Hopf ansatz
# ----------------------------------------------------------------------
def hopf_variational(rr, zz, R_r, R_z, w):
    """Three-parameter axisymmetric Hopf ansatz n(r, z) on S^2.

    Carries Hopf invariant Q_H = +/- 1 (sign by orientation) for any
    positive (R_r, R_z, w); reduces to n = z_hat at infinity.
    """
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
# Energy functional
# ----------------------------------------------------------------------
def evaluate_energy(R_r, R_z, w, rr, zz, metric, cfg):
    """Evaluate full Cosserat energy E[n,u] of the Hopf ansatz, in keV.

    Returns: dict with components {E_OF, E_Sk, E_u, E_total} (keV)
             and the topological charge Q.
    """
    with torch.no_grad():
        n = hopf_variational(rr, zz, R_r, R_z, w)
        _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n, metric, cfg)
        E_u = compute_E_u_screened(n, metric, MU_C, cg_iter=cfg.cg_iter).item()
        Q = compute_Q_stretched(n, metric).item()

    keV = M0C2_eV / 1000.0
    return {
        'E_OF':    E_of.item()   * keV,
        'E_Sk':    E_sk.item()   * keV,
        'E_u':     E_u           * keV,
        'E_total': (E_of.item() + E_sk.item() + E_u) * keV,
        'Q':       Q,
    }


# ----------------------------------------------------------------------
# NM driver
# ----------------------------------------------------------------------
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    print("=" * 100)
    print("NELDER-MEAD MINIMIZATION of E[n, u] over (R_r, R_z, w)")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid:   {cfg.Nr} x {cfg.Nz}  (L_r={cfg.L_r}, L_z={cfg.L_z}, "
          f"beta_r={cfg.beta_r}, beta_z={cfg.beta_z})")
    print(f"K1={cfg.K1}, K2={cfg.K2}, K3={cfg.K3}, c4={cfg.c4}")
    print(f"mu_c = 2 pi = {MU_C:.6f}")
    print(f"M0 c^2 = {M0C2_eV:.4f} eV   (natural mass scale)")
    print()

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    # Counter for logging
    n_eval = [0]
    history = []

    def objective(params):
        n_eval[0] += 1
        R_r, R_z, w = float(params[0]), float(params[1]), float(params[2])

        # Penalty for non-physical (negative or near-zero) parameters
        if R_r <= 0.05 or R_z <= 0.05 or w <= 0.05:
            return 1e10

        comp = evaluate_energy(R_r, R_z, w, rr, zz, metric, cfg)
        E_total_keV = comp['E_total']

        # Check topological charge integrity
        if abs(comp['Q'] + 1.0) > 0.05 and abs(comp['Q'] - 1.0) > 0.05:
            # Topology drifted - heavy penalty
            return 1e10

        # Log every iteration
        history.append({
            'iter': n_eval[0],
            'R_r': R_r, 'R_z': R_z, 'w': w,
            'E_total_keV': E_total_keV, 'Q': comp['Q'],
        })

        if n_eval[0] % 5 == 1 or n_eval[0] == 1:
            print(f"[{n_eval[0]:4d}]  R_r={R_r:.5f}  R_z={R_z:.5f}  w={w:.5f}  "
                  f"E_tot={E_total_keV:.4f} keV  Q={comp['Q']:+.4f}", flush=True)

        return E_total_keV

    # Initial guess (generic, far from the known optimum)
    x0 = np.array([0.50, 0.70, 0.60])
    print(f"Initial guess:  R_r={x0[0]}, R_z={x0[1]}, w={x0[2]}")
    print()

    t_start = time.time()
    result = minimize(
        objective, x0,
        method='Nelder-Mead',
        options={
            'xatol':    1e-6,
            'fatol':    1e-4,         # in keV (= 0.1 eV)
            'maxiter':  500,
            'adaptive': True,
            'disp':     True,
        },
    )
    wall_time = time.time() - t_start

    R_r_opt, R_z_opt, w_opt = float(result.x[0]), float(result.x[1]), float(result.x[2])
    final = evaluate_energy(R_r_opt, R_z_opt, w_opt, rr, zz, metric, cfg)

    print()
    print("=" * 100)
    print("OPTIMUM")
    print("=" * 100)
    print(f"  R_r = {R_r_opt:.6f}    (in units of l_0)")
    print(f"  R_z = {R_z_opt:.6f}")
    print(f"  w   = {w_opt:.6f}")
    print()
    print(f"  E_OF    = {final['E_OF']:8.3f} keV   ({100*final['E_OF']/final['E_total']:5.1f} %)")
    print(f"  E_Sk    = {final['E_Sk']:8.3f} keV   ({100*final['E_Sk']/final['E_total']:5.1f} %)")
    print(f"  E_u     = {final['E_u']:8.3f} keV   ({100*final['E_u']/final['E_total']:5.1f} %)")
    print(f"  ----------------------------------")
    print(f"  E_total = {final['E_total']:8.3f} keV   (100.0 %)   (= m_e^bare)")
    print()
    print(f"  Q = {final['Q']:+.6f}    (electron orientation if -1, positron if +1)")
    print()
    M_E_EXP_keV = 510.998950
    gap_keV = M_E_EXP_keV - final['E_total']
    deviation_pct = 100.0 * (final['E_total'] - M_E_EXP_keV) / M_E_EXP_keV
    print(f"  Predicted m_e^bare c^2 = {final['E_total']:.4f} keV")
    print(f"  CODATA 2018 m_e c^2    = {M_E_EXP_keV:.4f} keV (physical/dressed)")
    print(f"  Gap (CODATA - bare)    = {gap_keV:+.4f} keV  ({deviation_pct:+.4f} %)")
    print(f"  Hypothesis: gap = standard QED renormalization (see paper §7.2)")
    print()
    print(f"  NM iterations:  {n_eval[0]}  (NM nfev = {result.nfev})")
    print(f"  Wall time:      {wall_time:.0f} s on {device}")
    print(f"  NM message:     {result.message}")

    # Save results to JSON
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'result.json')
    output = {
        'paper': 'PAPER_ELECTRON_MASS (DOI: 10.5281/zenodo.20205502)',
        'preceding_work': '10.5281/zenodo.20187199',
        'physical_constants': {
            'epsilon_0_F_per_m': EPS_0,
            'mu_0_implicit_via_c': 'c = 1/sqrt(eps0 mu0)',
            'hbar_J_s':            HBAR,
            'c_m_per_s':           C_LIGHT,
        },
        'derived_constants': {
            'M0c2_eV':       M0C2_eV,
            'mu_c':          MU_C,
            'eta':           MU_C,
            'K1':            cfg.K1,
            'K2':            cfg.K2,
            'K3':            cfg.K3,
            'c4':            cfg.c4,
        },
        'grid': {
            'Nr': cfg.Nr, 'Nz': cfg.Nz,
            'L_r': cfg.L_r, 'L_z': cfg.L_z,
            'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
            'r_focus': cfg.R_hopf, 'z_focus': 0.0,
            'precision': 'float64',
        },
        'optimisation': {
            'method':       'Nelder-Mead',
            'initial':      list(map(float, x0)),
            'xatol':        1e-6,
            'fatol_keV':    1e-4,
            'iterations':   n_eval[0],
            'nfev':         int(result.nfev),
            'success':      bool(result.success),
            'message':      str(result.message),
            'wall_time_s':  wall_time,
            'device':       str(device),
        },
        'optimum': {
            'R_r':   R_r_opt,
            'R_z':   R_z_opt,
            'w':     w_opt,
        },
        'energy_decomposition_keV': {
            'E_OF':    final['E_OF'],
            'E_Sk':    final['E_Sk'],
            'E_u':     final['E_u'],
            'E_total': final['E_total'],
        },
        'topological_charge': {
            'Q':         final['Q'],
            'abs_Q':     abs(final['Q']),
            'deviation': abs(abs(final['Q']) - 1.0),
        },
        'comparison_with_CODATA_2018': {
            'predicted_m_e_bare_keV': final['E_total'],
            'codata_m_e_phys_keV':    M_E_EXP_keV,
            'gap_keV':                gap_keV,
            'gap_eV':                 1000.0 * gap_keV,
            'gap_relative_pct':       -deviation_pct,
            'interpretation':         'bare m_e from Cosserat functional; CODATA is the physical (renormalized) m_e; the gap is interpreted as standard QED renormalization (see paper §7.2)',
        },
    }

    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResult saved: {out_path}")
    print("\nDONE")


if __name__ == '__main__':
    main()
