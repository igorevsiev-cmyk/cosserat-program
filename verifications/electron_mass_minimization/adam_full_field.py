#!/usr/bin/env python3
"""
adam_full_field.py — Test: can Adam over the full director field
n(r, z) on the stretched 1024 x 2048 grid go below the canonical NM
minimum (m_e^bare = 507.997 keV)?

Historically (paper §5.2 note): "gradient methods over the full field
(Adam, L-BFGS) on a discrete grid cause Q_H drift from integer values".
This script re-tests that statement after recent grid improvements
(z-boundary linear extrapolation, etc.).

Method:
    Initialize n from the canonical Hopf ansatz at the NM optimum
    (R_r=0.51688, R_z=0.76148, w=0.62580). Adam optimizes n directly,
    with:
      - renormalization n -> n / |n| at each step (S^2 constraint)
      - Q-penalty: lambda_Q * (Q - Q_target)^2  to discourage drift
      - gradient through E_OF + E_Sk only (compute_E_u_screened detaches n)
      - E_u recomputed every CHECK_EVERY steps for monitoring

Output:
    - log of (step, E_OF, E_Sk, E_u, E_total, Q) every LOG_EVERY steps
    - final result saved to adam_full_field_result.json
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import torch

from stretched_grid import (
    create_stretched_grid,
    compute_energy_cosserat_stretched,
    compute_E_u_screened,
    compute_Q_stretched,
)


# ----------------------------------------------------------------------
# Physical constants (CODATA 2018) and natural unit conversion
# ----------------------------------------------------------------------
EPS_0    = 8.854187817e-12
HBAR     = 1.054571817e-34
C_LIGHT  = 299792458.0
E_CHARGE = 1.602176634e-19

M0       = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV  = M0 * C_LIGHT**2 / E_CHARGE     # ~ 429.51 eV
MU_C     = 2.0 * np.pi                     # Cosserat coupling


# ----------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------
class Config:
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
    Nr = 1024; Nz = 2048
    L_r = 24.0; L_z = 48.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3

    K1 = 2.0; K2 = 2.0
    K3 = 14.56
    c2 = 1.0; c4 = 1.0
    m2 = 0.0
    cg_iter = 2000


# ----------------------------------------------------------------------
# Hopf ansatz (initialization)
# ----------------------------------------------------------------------
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


def normalize_S2(n):
    return n / n.norm(dim=0, keepdim=True).clamp(min=1e-10)


# ----------------------------------------------------------------------
# Main Adam optimization loop
# ----------------------------------------------------------------------
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    # Hyperparameters for Adam
    LR            = 1e-4
    N_STEPS       = 500
    LOG_EVERY     = 10
    CHECK_EVERY   = 25       # how often to recompute E_u (expensive)
    LAMBDA_Q      = 0.0      # NO Q penalty — pure test of intrinsic Q stability
    Q_TARGET      = -1.0     # only for monitoring

    # Initial canonical Hopf
    R_R_INIT = 0.51688
    R_Z_INIT = 0.76148
    W_INIT   = 0.62580

    print("=" * 100)
    print("ADAM FULL-FIELD MINIMIZATION  (test of Q_H stability)")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid:   {cfg.Nr} x {cfg.Nz}  (L_r={cfg.L_r}, L_z={cfg.L_z}, "
          f"beta_r={cfg.beta_r}, beta_z={cfg.beta_z})")
    print(f"K1={cfg.K1}, K2={cfg.K2}, K3={cfg.K3}, c4={cfg.c4}")
    print(f"mu_c = 2 pi = {MU_C:.6f}")
    print(f"M0 c^2 = {M0C2_eV:.4f} eV   (natural mass scale)")
    print()
    print(f"Adam hyperparameters:")
    print(f"  lr            = {LR}")
    print(f"  n_steps       = {N_STEPS}")
    print(f"  log_every     = {LOG_EVERY}")
    print(f"  E_u recompute = every {CHECK_EVERY} steps")
    print(f"  Q penalty     = {LAMBDA_Q} * (Q - {Q_TARGET})^2")
    print(f"  Initial canonical (R_r, R_z, w) = ({R_R_INIT}, {R_Z_INIT}, {W_INIT})")
    print()

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    # Initialize n from canonical Hopf, then make it a free parameter
    with torch.no_grad():
        n_init = hopf_init(rr, zz, R_R_INIT, R_Z_INIT, W_INIT)
    n = n_init.clone().detach().requires_grad_(True)

    # Initial diagnostics
    with torch.no_grad():
        n_n = normalize_S2(n)
        _, E_of0, E_sk0, _ = compute_energy_cosserat_stretched(n_n, metric, cfg)
        E_u0 = compute_E_u_screened(n_n, metric, MU_C, cg_iter=cfg.cg_iter).item()
        Q0 = compute_Q_stretched(n_n, metric).item()
        keV = M0C2_eV / 1000.0
        E_of0_v = E_of0.item() * keV
        E_sk0_v = E_sk0.item() * keV
        E_u0_v  = E_u0 * keV
        E_tot0  = E_of0_v + E_sk0_v + E_u0_v

    print(f"INITIAL (canonical Hopf):")
    print(f"  E_OF = {E_of0_v:.4f} keV,  E_Sk = {E_sk0_v:.4f} keV,  "
          f"E_u = {E_u0_v:.4f} keV")
    print(f"  E_total = {E_tot0:.4f} keV    Q = {Q0:+.6f}")
    print()

    optimizer = torch.optim.Adam([n], lr=LR)
    history = []
    last_E_u = E_u0_v   # cached, recomputed every CHECK_EVERY

    t_start = time.time()

    for step in range(1, N_STEPS + 1):
        optimizer.zero_grad()

        n_norm = normalize_S2(n)
        _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n_norm, metric, cfg)
        Q = compute_Q_stretched(n_norm, metric)

        # Loss: E_of + E_sk + Q-penalty.  E_u not differentiated (PCG inside detaches).
        loss = E_of + E_sk + LAMBDA_Q * (Q - Q_TARGET)**2
        loss.backward()
        optimizer.step()

        # Periodic full diagnostics (with E_u)
        if step % CHECK_EVERY == 0 or step == 1 or step == N_STEPS:
            with torch.no_grad():
                n_n = normalize_S2(n)
                _, E_of_full, E_sk_full, _ = compute_energy_cosserat_stretched(
                    n_n, metric, cfg)
                E_u_full = compute_E_u_screened(
                    n_n, metric, MU_C, cg_iter=cfg.cg_iter).item()
                Q_full = compute_Q_stretched(n_n, metric).item()
                E_of_v = E_of_full.item() * keV
                E_sk_v = E_sk_full.item() * keV
                E_u_v  = E_u_full * keV
                E_tot_v = E_of_v + E_sk_v + E_u_v
            last_E_u = E_u_v
            history.append({
                'step':     step,
                'E_OF':     E_of_v,
                'E_Sk':     E_sk_v,
                'E_u':      E_u_v,
                'E_total':  E_tot_v,
                'Q':        Q_full,
            })
            print(f"[{step:4d}]  E_OF={E_of_v:8.4f}  E_Sk={E_sk_v:8.4f}  "
                  f"E_u={E_u_v:8.4f}  E_tot={E_tot_v:9.4f}  Q={Q_full:+.6f}",
                  flush=True)

    wall_time = time.time() - t_start

    # Final diagnostics
    with torch.no_grad():
        n_n = normalize_S2(n)
        _, E_of_f, E_sk_f, _ = compute_energy_cosserat_stretched(n_n, metric, cfg)
        E_u_f = compute_E_u_screened(n_n, metric, MU_C, cg_iter=cfg.cg_iter).item()
        Q_f = compute_Q_stretched(n_n, metric).item()
        E_of_v = E_of_f.item() * keV
        E_sk_v = E_sk_f.item() * keV
        E_u_v  = E_u_f * keV
        E_tot  = E_of_v + E_sk_v + E_u_v

    M_E_EXP = 510.998950
    NM_BARE = 507.9966
    delta_vs_NM    = E_tot - NM_BARE
    delta_vs_CODATA = E_tot - M_E_EXP

    print()
    print("=" * 100)
    print("FINAL")
    print("=" * 100)
    print(f"  E_OF    = {E_of_v:.4f} keV   ({100*E_of_v/E_tot:.2f} %)")
    print(f"  E_Sk    = {E_sk_v:.4f} keV   ({100*E_sk_v/E_tot:.2f} %)")
    print(f"  E_u     = {E_u_v:.4f} keV   ({100*E_u_v/E_tot:.2f} %)")
    print(f"  ----------------------------------")
    print(f"  E_total = {E_tot:.4f} keV")
    print(f"  Q       = {Q_f:+.6f}    (target {Q_TARGET})")
    print()
    print(f"  vs canonical NM (507.9966 keV):  delta = {delta_vs_NM:+.4f} keV")
    print(f"  vs CODATA       (510.9989 keV):  delta = {delta_vs_CODATA:+.4f} keV")
    print(f"  |Q - (-1)|                    = {abs(Q_f - Q_TARGET):.2e}")
    print()
    print(f"  NM iterations: {N_STEPS}")
    print(f"  Wall time:     {wall_time:.0f} s on {device}")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'adam_full_field_result.json')
    output = {
        'description': 'Adam full-field test of Q_H stability and energy descent below NM optimum',
        'hyperparameters': {
            'lr':            LR,
            'n_steps':       N_STEPS,
            'lambda_Q':      LAMBDA_Q,
            'Q_target':      Q_TARGET,
            'check_every':   CHECK_EVERY,
            'init_Hopf':     {'R_r': R_R_INIT, 'R_z': R_Z_INIT, 'w': W_INIT},
        },
        'grid': {
            'Nr': cfg.Nr, 'Nz': cfg.Nz,
            'L_r': cfg.L_r, 'L_z': cfg.L_z,
            'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
            'precision': 'float64',
        },
        'initial_state': {
            'E_OF':    E_of0_v, 'E_Sk': E_sk0_v, 'E_u': E_u0_v,
            'E_total': E_tot0,  'Q':    Q0,
        },
        'final_state': {
            'E_OF':    E_of_v, 'E_Sk': E_sk_v, 'E_u': E_u_v,
            'E_total': E_tot,  'Q':    Q_f,
        },
        'comparison': {
            'NM_bare_keV':        NM_BARE,
            'delta_vs_NM_keV':    delta_vs_NM,
            'CODATA_keV':         M_E_EXP,
            'delta_vs_CODATA_keV': delta_vs_CODATA,
            'Q_drift':            abs(Q_f - Q_TARGET),
        },
        'wall_time_s': wall_time,
        'device':      str(device),
        'history':     history,
    }
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Result: {out_path}")
    print("\nDONE")


if __name__ == '__main__':
    main()
