#!/usr/bin/env python3
"""
mu_c-sweep (paper §4): tests whether the dyadic structure
m_e/M_0 = 2^10 + 2^4 - 1 = 1039 of the bare electron mass appears
*only* at the canonical Cosserat coupling mu_c = 2*pi = eta.

For each mu_c in {pi/2, pi, 3*pi/2, 2*pi, 5*pi/2, 3*pi, 4*pi}:
  - Run a full Nelder-Mead minimization of E[n, u] over the 3-param
    Hopf ansatz (R_r, R_z, w), as in [electron-mass §5].
  - Record geometry, energy decomposition (E_OF, E_Sk, E_u),
    bare mass m_e = M_0 c^2 * E_tilde_min, and the closest clean
    dyadic compound 2^10 + 2^4 + k.

A discrete "dyadic locking" only at mu_c = 2*pi is the empirical
signature of the chiral-bag resonance.

Output: result_mu_c_sweep.json (7 mu_c values, full minimization data).
"""

import sys, os, json, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['PYTHONUNBUFFERED'] = '1'

import numpy as np
import torch
from scipy.optimize import minimize

from stretched_grid import (
    create_stretched_grid,
    compute_energy_cosserat_stretched,
    compute_E_u_screened,
    compute_Q_stretched,
)

# Constants
EPS_0 = 8.854187817e-12
HBAR = 1.054571817e-34
C_LIGHT = 299792458.0
E_CHARGE = 1.602176634e-19
M0 = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV = M0 * C_LIGHT**2 / E_CHARGE
keV = M0C2_eV / 1000.0


class Cfg:
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3
    K1 = 2.0; K2 = 2.0
    K3 = 14.56
    c2 = 1.0; c4 = 1.0
    m2 = 0.0
    cg_iter = 800     # 4-digit accuracy is sufficient for the sweep comparison


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


def evaluate_energy(R_r, R_z, w, rr, zz, metric, cfg, mu_c):
    with torch.no_grad():
        n = hopf_variational(rr, zz, R_r, R_z, w)
        _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n, metric, cfg)
        E_u = compute_E_u_screened(n, metric, mu_c, cg_iter=cfg.cg_iter).item()
        Q = compute_Q_stretched(n, metric).item()
    return {
        'E_OF': E_of.item() * keV,
        'E_Sk': E_sk.item() * keV,
        'E_u':  E_u * keV,
        'E_total': (E_of.item() + E_sk.item() + E_u) * keV,
        'Q': Q,
    }


def analyze_dyadic(E_tilde):
    """Find the closest dyadic compound 2^a + 2^b + c (small a, b, c)."""
    best = None
    for a in range(8, 12):
        for b in range(0, 8):
            for c in [-2, -1, 0, 1, 2]:
                val = 2**a + 2**b + c
                d = abs(val - E_tilde)
                if best is None or d < best['delta']:
                    best = {'a': a, 'b': b, 'c': c, 'val': val, 'delta': d}
    return best


def run_at_mu_c(mu_c, device, cfg, rr, zz, metric, x0):
    """Full Nelder-Mead minimization of E[n, u] at the given mu_c."""
    n_eval = [0]

    def objective(params):
        n_eval[0] += 1
        R_r, R_z, w = float(params[0]), float(params[1]), float(params[2])
        if R_r <= 0.05 or R_z <= 0.05 or w <= 0.05:
            return 1e10
        comp = evaluate_energy(R_r, R_z, w, rr, zz, metric, cfg, mu_c)
        if abs(comp['Q'] + 1.0) > 0.05 and abs(comp['Q'] - 1.0) > 0.05:
            return 1e10
        if n_eval[0] % 20 == 1:
            print(f"  [{n_eval[0]:3d}] R_r={R_r:.4f} R_z={R_z:.4f} w={w:.4f} "
                  f"E={comp['E_total']:8.3f} Q={comp['Q']:+.4f}", flush=True)
        return comp['E_total']

    t0 = time.time()
    result = minimize(objective, x0, method='Nelder-Mead',
                      options={'xatol': 1e-4, 'fatol': 1e-2, 'maxiter': 200,
                              'adaptive': True, 'disp': False})
    t = time.time() - t0
    R_r_opt, R_z_opt, w_opt = float(result.x[0]), float(result.x[1]), float(result.x[2])
    final = evaluate_energy(R_r_opt, R_z_opt, w_opt, rr, zz, metric, cfg, mu_c)
    return {
        'mu_c': mu_c,
        'mu_c_over_pi': mu_c / np.pi,
        'R_r': R_r_opt, 'R_z': R_z_opt, 'w': w_opt,
        'E_OF': final['E_OF'], 'E_Sk': final['E_Sk'],
        'E_u': final['E_u'], 'E_total': final['E_total'],
        'E_tilde': final['E_total'] * 1000 / M0C2_eV,
        'Q': final['Q'],
        'nfev': n_eval[0],
        'wall_s': t,
        'dyadic_fit': analyze_dyadic(final['E_total'] * 1000 / M0C2_eV),
        'derrick_OF_Sk_ratio': final['E_OF'] / (final['E_OF'] + final['E_Sk']),
        'l_c': 1.0 / np.sqrt(mu_c),  # Cosserat coupling length
    }


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()
    print("=" * 100)
    print("mu_c sweep -- looking for the dyadic locking point (paper §4)")
    print("=" * 100)

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    # Canonical NM optimum from [electron-mass §5] as initial guess
    x0 = np.array([0.6408, 0.8073, 0.7020])

    # mu_c grid (canonical 2*pi at index 3)
    pi = np.pi
    mu_c_values = [0.5*pi, 1.0*pi, 1.5*pi, 2.0*pi, 2.5*pi, 3.0*pi, 4.0*pi]

    all_results = []
    for i, mu_c in enumerate(mu_c_values):
        print()
        print(f"--- [{i+1}/{len(mu_c_values)}] mu_c = {mu_c:.4f} = {mu_c/pi:.2f}*pi ---")
        res = run_at_mu_c(mu_c, device, cfg, rr, zz, metric, x0)
        all_results.append(res)
        print(f"  RESULT: m_e = {res['E_total']:.4f} keV, E_tilde = {res['E_tilde']:.3f} cells")
        print(f"          R_r = {res['R_r']:.5f}, R_z = {res['R_z']:.5f}, w = {res['w']:.5f}")
        print(f"          Q = {res['Q']:+.5f}, OF/Sk = {res['derrick_OF_Sk_ratio']:.3f}")
        print(f"          closest dyadic: 2^{res['dyadic_fit']['a']} + 2^{res['dyadic_fit']['b']} + ({res['dyadic_fit']['c']}) = {res['dyadic_fit']['val']}, delta={res['dyadic_fit']['delta']:.3f}")
        print(f"          NM: {res['nfev']} evals, {res['wall_s']:.0f} s")

    # Summary table
    print()
    print("=" * 100)
    print("SUMMARY TABLE")
    print("=" * 100)
    print(f"{'mu_c/pi':>7} | {'m_e (keV)':>10} | {'E_tilde':>10} | {'R_r':>7} | {'R_z':>7} | {'OF/Sk':>6} | {'dyadic':>20} | {'delta(1039)':>11}")
    print("-" * 105)
    for r in all_results:
        d = r['dyadic_fit']
        c_sign = '+' if d['c'] >= 0 else '-'
        print(f"{r['mu_c_over_pi']:>7.2f} | {r['E_total']:>10.4f} | {r['E_tilde']:>10.4f} | "
              f"{r['R_r']:>7.4f} | {r['R_z']:>7.4f} | {r['derrick_OF_Sk_ratio']:>6.3f} | "
              f"2^{d['a']}+2^{d['b']}{c_sign}{abs(d['c'])} (d={d['delta']:5.2f}) | "
              f"{r['E_tilde']-1039:>+11.4f}")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_mu_c_sweep.json')
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, default=lambda x: float(x) if hasattr(x, 'item') else x)
    print(f"\nSaved: {out_path}")


if __name__ == '__main__':
    main()
