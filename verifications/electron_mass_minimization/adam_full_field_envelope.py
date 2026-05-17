#!/usr/bin/env python3
"""
adam_full_field_envelope.py — Adam over the full director field n(r, z),
with PROPER envelope-theorem gradient for the u-channel.

Compared to adam_full_field.py (which only sees E_OF + E_Sk):

  loss_simple   = E_OF + E_Sk
  loss_envelope = E_OF + E_Sk + coupling
  coupling      = -2 * integral( f(n) * psi* * 2pi*r * dr * dz ) on u-grid

The coupling term carries the gradient of E_int = -2 integral(f * u) at
the optimum u = u*(n).  By the envelope theorem this gives dE_total/dn
the correct value (the other contributions vanish at u = u*).

The PCG solver inside compute_E_u_screened still detaches its input n,
so we compute f(n) WITH gradient on the n-grid, interpolate it
DIFFERENTIABLY to the u-grid (via the existing bilinear-interp helper),
and multiply it by the detached psi* coming out of PCG.

This means PCG runs every step (instead of every 25 steps), which makes
Adam ~25x slower than adam_full_field.py.  Worth it: we now follow
the true dE_total/dn instead of dE_n/dn.
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
    _interp_nonuniform_to_uniform,
)


# ----------------------------------------------------------------------
# Physical constants
# ----------------------------------------------------------------------
EPS_0    = 8.854187817e-12
HBAR     = 1.054571817e-34
C_LIGHT  = 299792458.0
E_CHARGE = 1.602176634e-19

M0       = (2.0 * np.pi * HBAR**3 / (C_LIGHT**5 * EPS_0))**0.25
M0C2_eV  = M0 * C_LIGHT**2 / E_CHARGE
MU_C     = 2.0 * np.pi


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
    lambda_Q = 0.0; Q_target = -1.0
    use_float64 = True


class Cfg(Config):
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
# Loss with envelope-theorem coupling term
# ----------------------------------------------------------------------
def loss_envelope(n, metric, cfg, mu_c):
    """
    Returns (loss, E_OF, E_Sk, E_u, Q) with:
      loss     = E_OF + E_Sk + coupling
      coupling = -2 * integral(f(n) * psi_optimal * 2pi*r * dr * dz)

    PCG is run inside (detaches n), but we recompute f(n) WITH gradient
    on the n-grid, then differentiably interpolate to the u-grid, then
    multiply by the detached psi*.  Gradient flows back to n through
    f and the interpolation.
    """
    n_norm = normalize_S2(n)

    # --- E_n part (gradient through n) -----------------------------------
    _, E_of, E_sk, _ = compute_energy_cosserat_stretched(n_norm, metric, cfg)

    # --- u-channel solve via PCG (detaches inside) -----------------------
    E_u_val, info = compute_E_u_screened(
        n_norm, metric, mu_c, cg_iter=cfg.cg_iter, return_psi=True
    )
    psi = info['psi'].detach()
    rr_u = info['rr_u']
    r_u = info['r_u']
    z_u = info['z_u']
    dr_u = info['dr_u']
    dz_u = info['dz_u']
    r_s = info['r_s']
    z_s = info['z_s']

    # --- f(n) WITH GRADIENT on the n-grid --------------------------------
    n3_clamped = n_norm[2].clamp(-1.0 + 1e-10, 1.0 - 1e-10)
    sin_f = torch.sqrt((n_norm[0]**2 + n_norm[1]**2).clamp(min=1e-20))
    f_n_grid = torch.atan2(sin_f, n3_clamped)

    # --- Differentiable interp to u-grid ---------------------------------
    f_u_grid = _interp_nonuniform_to_uniform(f_n_grid, r_s, z_s, r_u, z_u)

    # --- Envelope coupling: -2 * integral(f * psi*) * 2pi*r * dr * dz ---
    coupling = -2.0 * 2.0 * np.pi * (f_u_grid * psi * rr_u).sum() * dr_u * dz_u

    # --- Topological charge (for monitoring) -----------------------------
    with torch.no_grad():
        Q = compute_Q_stretched(n_norm, metric).item()

    loss = E_of + E_sk + coupling
    return loss, E_of, E_sk, E_u_val, Q


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------
def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    LR        = 1e-4
    N_STEPS   = 200          # fewer steps because each does PCG
    LOG_EVERY = 10

    R_R_INIT = 0.51688
    R_Z_INIT = 0.76148
    W_INIT   = 0.62580

    print("=" * 100)
    print("ADAM FULL-FIELD WITH ENVELOPE GRADIENT  (true dE_total/dn)")
    print("=" * 100)
    print(f"Device: {device}")
    print(f"Grid:   {cfg.Nr} x {cfg.Nz}  (L_r={cfg.L_r}, L_z={cfg.L_z}, "
          f"beta_r={cfg.beta_r}, beta_z={cfg.beta_z})")
    print(f"K1={cfg.K1}, K2={cfg.K2}, K3={cfg.K3}, c4={cfg.c4}")
    print(f"mu_c = 2 pi = {MU_C:.6f}")
    print(f"M0 c^2 = {M0C2_eV:.4f} eV")
    print()
    print(f"  lr        = {LR}")
    print(f"  n_steps   = {N_STEPS}")
    print(f"  log_every = {LOG_EVERY}")
    print(f"  Initial canonical (R_r, R_z, w) = ({R_R_INIT}, {R_Z_INIT}, {W_INIT})")
    print(f"  (PCG runs every step; coupling term gives the envelope gradient)")
    print()

    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    with torch.no_grad():
        n_init = hopf_init(rr, zz, R_R_INIT, R_Z_INIT, W_INIT)
    n = n_init.clone().detach().requires_grad_(True)

    keV = M0C2_eV / 1000.0

    # Initial diagnostics
    with torch.no_grad():
        n_n = normalize_S2(n)
        _, E_of0, E_sk0, _ = compute_energy_cosserat_stretched(n_n, metric, cfg)
        E_u0 = compute_E_u_screened(n_n, metric, MU_C, cg_iter=cfg.cg_iter).item()
        Q0 = compute_Q_stretched(n_n, metric).item()
        E_of0_v = E_of0.item() * keV
        E_sk0_v = E_sk0.item() * keV
        E_u0_v  = E_u0 * keV
        E_tot0  = E_of0_v + E_sk0_v + E_u0_v
    print(f"INITIAL: E_OF={E_of0_v:.4f}  E_Sk={E_sk0_v:.4f}  "
          f"E_u={E_u0_v:.4f}  E_tot={E_tot0:.4f}  Q={Q0:+.6f}")
    print()

    optimizer = torch.optim.Adam([n], lr=LR)
    history = []
    t_start = time.time()

    for step in range(1, N_STEPS + 1):
        optimizer.zero_grad()
        loss, E_of_t, E_sk_t, E_u_val, Q = loss_envelope(n, metric, cfg, MU_C)
        loss.backward()
        optimizer.step()

        E_of_v = E_of_t.item() * keV
        E_sk_v = E_sk_t.item() * keV
        E_u_v  = E_u_val * keV
        E_tot_v = E_of_v + E_sk_v + E_u_v

        if step % LOG_EVERY == 0 or step == 1 or step == N_STEPS:
            history.append({
                'step':    step,
                'E_OF':    E_of_v,
                'E_Sk':    E_sk_v,
                'E_u':     E_u_v,
                'E_total': E_tot_v,
                'Q':       Q,
            })
            print(f"[{step:4d}]  E_OF={E_of_v:8.4f}  E_Sk={E_sk_v:8.4f}  "
                  f"E_u={E_u_v:8.4f}  E_tot={E_tot_v:9.4f}  Q={Q:+.6f}",
                  flush=True)

    wall_time = time.time() - t_start

    # Final
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
    print()
    print("=" * 100)
    print("FINAL (envelope gradient)")
    print("=" * 100)
    print(f"  E_OF    = {E_of_v:.4f} keV   ({100*E_of_v/E_tot:.2f} %)")
    print(f"  E_Sk    = {E_sk_v:.4f} keV   ({100*E_sk_v/E_tot:.2f} %)")
    print(f"  E_u     = {E_u_v:.4f} keV   ({100*E_u_v/E_tot:.2f} %)")
    print(f"  ----------------------------------")
    print(f"  E_total = {E_tot:.4f} keV")
    print(f"  Q       = {Q_f:+.6f}")
    print()
    print(f"  vs canonical NM (507.9966 keV):  delta = {E_tot - NM_BARE:+.4f} keV")
    print(f"  vs CODATA       (510.9989 keV):  delta = {E_tot - M_E_EXP:+.4f} keV")
    print(f"  |Q - (-1)|                    = {abs(Q_f + 1.0):.2e}")
    print(f"  Wall time:     {wall_time:.0f} s on {device}")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'adam_envelope_result.json')
    output = {
        'description': 'Adam with envelope-theorem coupling for u-channel (true dE_total/dn)',
        'hyperparameters': {
            'lr':         LR,
            'n_steps':    N_STEPS,
            'init_Hopf':  {'R_r': R_R_INIT, 'R_z': R_Z_INIT, 'w': W_INIT},
        },
        'grid': {
            'Nr': cfg.Nr, 'Nz': cfg.Nz,
            'L_r': cfg.L_r, 'L_z': cfg.L_z,
            'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
        },
        'initial_state': {
            'E_OF': E_of0_v, 'E_Sk': E_sk0_v, 'E_u': E_u0_v,
            'E_total': E_tot0, 'Q': Q0,
        },
        'final_state': {
            'E_OF': E_of_v, 'E_Sk': E_sk_v, 'E_u': E_u_v,
            'E_total': E_tot, 'Q': Q_f,
        },
        'comparison': {
            'NM_bare_keV': NM_BARE,
            'delta_vs_NM_keV': E_tot - NM_BARE,
            'CODATA_keV': M_E_EXP,
            'delta_vs_CODATA_keV': E_tot - M_E_EXP,
            'Q_drift': abs(Q_f + 1.0),
        },
        'wall_time_s': wall_time,
        'device':      str(device),
        'history':     history,
    }
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Result: {out_path}")
    print("DONE")


if __name__ == '__main__':
    main()
