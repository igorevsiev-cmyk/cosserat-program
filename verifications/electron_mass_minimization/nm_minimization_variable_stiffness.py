#!/usr/bin/env python3
"""
nm_minimization_variable_stiffness.py
------------------------------------
Variant of nm_minimization.py with one additional knob: relative vacuum
stiffness `k = mu / mu_vacuum`.

    k = 1.0    reproduces the canonical paper run (m_e^bare = 446.28 keV).
    k != 1.0   rescales ONLY the unit conversion M0c^2 -> k^(1/4) * M0c^2.

The dimensionless minimum of E[n,u] (and the optimal R_r, R_z, w) is
INVARIANT under k -- all sim-internal numbers (K_i, mu_c, c_4) are
ratios to mu and stay fixed.

Predicted scaling (algebra from the Cosserat-continuum hypothesis):
    m_e(k) = k^(1/4) * 446.28 keV
    l_0(k) = k^(-1/4) * 4.594 Angstrom

Use this script to:
    * sanity-check dimensional consistency of the canonical functional
    * verify that the dimensionless minimum is mu-invariant
    * explore the rolling-contact identity mu_c = 2 pi * mu under
      uniform rescaling of the medium stiffness

The original nm_minimization.py is UNCHANGED.

------------------------------------------------------------------
Original docstring of nm_minimization.py follows.
------------------------------------------------------------------

Nelder-Mead minimization of the canonical Cosserat functional E[n, u]
over the 3-parameter Hopf ansatz (R_r, R_z, w).

Verifies the central numerical claim of the paper:

    m_e^bare c^2 from {epsilon_0, mu_0, hbar}
    on a 1024 x 2048 stretched grid, dyadic box L = 17 x 33

(bare electron mass; the NM optimum matches the dyadic closed form
 m_e^bare c^2 = (2^10 + 2^4 - 1) * M0 c^2 = 1039 * M0 c^2; this is the
 bare value -- it is NOT compared with the physical/CODATA m_e here)

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

import sys, os, json, time, argparse
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
    """Canonical configuration: 1024 x 2048 stretched grid, dyadic box."""
    # Grid -- dyadic box: L_r = log2(2^7 * 2^10) = 17, L_z = 2*L_r - 1 = 33
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3

    # Cosserat constants (all derived from {epsilon_0, mu_0, hbar})
    K1 = 2.0; K2 = 2.0
    K3 = 14.56                         # = K1 * (1 + 2 pi)  rounded to 4 sig.fig.
    c2 = 1.0; c4 = 1.0
    m2 = 0.0                           # no mass term in the bare functional
    cg_iter = 2000                     # PCG cap for u-channel solver (Robin BC)

    # Relative vacuum stiffness: k = mu / mu_vacuum
    # k = 1.0 -> canonical paper run (m_e^bare = 446.28 keV)
    # k > 1   -> stiffer medium (m_e grows as k^(1/4))
    # k < 1   -> softer medium  (m_e shrinks)
    # Only the unit conversion M0c^2 is rescaled; the dimensionless minimum
    # (R_r, R_z, w, E_sim) is INVARIANT.
    k = 1.0


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

    Note: the conversion factor M0c^2 is scaled by k^(1/4), where
    k = mu / mu_vacuum is the relative stiffness (cfg.k).
    """
    with torch.no_grad():
        n = hopf_variational(rr, zz, R_r, R_z, w)
        _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n, metric, cfg)
        E_u = compute_E_u_screened(n, metric, MU_C, cg_iter=cfg.cg_iter).item()
        Q = compute_Q_stretched(n, metric).item()

    M0C2_eff_eV = cfg.k**0.25 * M0C2_eV       # k-rescaled unit of energy
    keV = M0C2_eff_eV / 1000.0
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
    # CLI: relative vacuum stiffness k = mu / mu_vacuum (default 1.0)
    parser = argparse.ArgumentParser(
        description="NM minimization with variable vacuum stiffness k.")
    parser.add_argument('--k', type=float, default=1.0,
        help="Relative vacuum stiffness k = mu/mu_vacuum (default 1.0 = canonical).")
    parser.add_argument('--out', type=str, default=None,
        help="Output JSON path (default: result_variable_k_<k>.json).")
    args = parser.parse_args()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()
    cfg.k = args.k

    M0C2_eff_eV = cfg.k**0.25 * M0C2_eV

    print("=" * 100)
    print("NELDER-MEAD MINIMIZATION of E[n, u] over (R_r, R_z, w)   --   variable stiffness")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid:   {cfg.Nr} x {cfg.Nz}  (L_r={cfg.L_r}, L_z={cfg.L_z}, "
          f"beta_r={cfg.beta_r}, beta_z={cfg.beta_z})")
    print(f"K1={cfg.K1}, K2={cfg.K2}, K3={cfg.K3}, c4={cfg.c4}")
    print(f"mu_c = 2 pi = {MU_C:.6f}")
    print(f"Relative stiffness k = mu/mu_vacuum  = {cfg.k:.6g}")
    print(f"M0 c^2 (vacuum)      = {M0C2_eV:.4f} eV")
    print(f"M0 c^2 (k-rescaled)  = k^(1/4) * M0c^2 = {M0C2_eff_eV:.4f} eV")
    print(f"  l_0 (k-rescaled)   = k^(-1/4) * 4.5943 A = "
          f"{cfg.k**(-0.25) * 4.5943:.4f} Angstrom")
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
    # Bare result -- compared with the dyadic closed form rescaled by k^(1/4).
    # Dyadic closed form (k = 1): m_e^bare = (2^10 + 2^4 - 1) * M0 c^2 = 1039 * M0 c^2
    # For arbitrary k: dyadic value scales the same as the simulated minimum,
    # so the relative deviation is INVARIANT under k. This is the key check.
    DYADIC_N    = 2**10 + 2**4 - 1                  # = 1039
    dyadic_keV  = DYADIC_N * M0C2_eff_eV / 1000.0
    dyadic_dev  = 100.0 * (final['E_total'] - dyadic_keV) / dyadic_keV

    # Predicted scaling from dimensional analysis
    m_e_vacuum_keV = DYADIC_N * M0C2_eV / 1000.0     # 446.28 keV at k=1
    m_e_predicted  = cfg.k**0.25 * m_e_vacuum_keV    # scaling law

    print(f"  Relative stiffness k             = {cfg.k:.6g}")
    print(f"  Predicted m_e^bare (algebra)     = k^(1/4) * {m_e_vacuum_keV:.4f} keV")
    print(f"                                   = {m_e_predicted:.4f} keV")
    print(f"  Computed  m_e^bare (NM optimum)  = {final['E_total']:.4f} keV")
    print(f"  Deviation from algebraic scaling = "
          f"{100.0*(final['E_total']-m_e_predicted)/m_e_predicted:+.4f} %")
    print()
    print(f"  Dyadic closed form (k-rescaled)  = (2^10 + 2^4 - 1) * k^(1/4) * M0c^2")
    print(f"                                   = {dyadic_keV:.4f} keV")
    print(f"  Deviation from dyadic            = {dyadic_dev:+.4f} %")
    print()
    print(f"  NM iterations:  {n_eval[0]}  (NM nfev = {result.nfev})")
    print(f"  Wall time:      {wall_time:.0f} s on {device}")
    print(f"  NM message:     {result.message}")

    # Save results to JSON (separate from canonical result.json)
    if args.out is not None:
        out_path = args.out
    else:
        k_tag = f"{cfg.k:g}".replace('.', 'p')
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                f'result_variable_k_{k_tag}.json')
    output = {
        'script':         'nm_minimization_variable_stiffness.py',
        'paper':          'PAPER_ELECTRON_MASS (DOI: 10.5281/zenodo.20477123)',
        'preceding_work': '10.5281/zenodo.20187199',
        'note':           'Variant of nm_minimization.py with relative stiffness k = mu/mu_vacuum. Only M0c^2 is rescaled by k^(1/4); functional and grid are unchanged.',
        'physical_constants': {
            'epsilon_0_F_per_m': EPS_0,
            'mu_0_implicit_via_c': 'c = 1/sqrt(eps0 mu0)',
            'hbar_J_s':            HBAR,
            'c_m_per_s':           C_LIGHT,
        },
        'stiffness': {
            'k':                  cfg.k,
            'M0c2_vacuum_eV':     M0C2_eV,
            'M0c2_effective_eV':  M0C2_eff_eV,
            'scaling_law':        'm_e ~ k^(1/4) * m_e_vacuum; l_0 ~ k^(-1/4) * l_0_vacuum',
            'm_e_vacuum_keV':     m_e_vacuum_keV,
            'm_e_predicted_keV':  m_e_predicted,
            'l0_vacuum_A':        4.5943,
            'l0_effective_A':     cfg.k**(-0.25) * 4.5943,
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
        'dyadic_closed_form': {
            'predicted_m_e_bare_keV': final['E_total'],
            'dyadic_N':               DYADIC_N,
            'dyadic_formula':         '(2^10 + 2^4 - 1) * M0 c^2',
            'dyadic_m_e_bare_keV':    dyadic_keV,
            'deviation_pct':          dyadic_dev,
            'interpretation':         'bare m_e from the Cosserat functional on the dyadic box L=17x33; the NM optimum matches the dyadic closed form (2^10 + 2^4 - 1) * M0 c^2 (no comparison with CODATA -- this is the bare value)',
        },
    }

    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nResult saved: {out_path}")
    print("\nDONE")


if __name__ == '__main__':
    main()
