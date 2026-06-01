#!/usr/bin/env python3
"""
extend_profile.py -- recompute radial profiles rho(r) on the full
L_r = 17 l_0 grid for all eigenmodes saved in result_hessian_L17.pt
(the L=17 analysis_three_checks.py run capped its profiles at r_max=10
to save IO; here we extend to the full box).

Output: result_hessian_profiles.json (consumed by plot_extended.py).
"""

import sys, os, json
os.environ['PYTHONUNBUFFERED'] = '1'
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np
import torch

from stretched_grid import create_stretched_grid


class Cfg:
    Nr = 1024; Nz = 2048
    L_r = 17.0; L_z = 33.0
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3


def radial_profile(eigvec, metric, n_radial_bins=300, r_max=17.0):
    rr = metric.rr
    J = metric.hr * metric.hz
    dA = metric.dxi * metric.deta
    sq = (eigvec * eigvec).sum(dim=0)
    weighted = sq * (2 * np.pi * rr * J) * dA
    rho_per_row = weighted.sum(dim=1)
    r_centers_grid = rr[:, 0].cpu().numpy()
    rho_np = rho_per_row.cpu().numpy()
    n_bins = n_radial_bins
    r_bins = np.linspace(0, r_max, n_bins + 1)
    r_bin_centers = 0.5 * (r_bins[:-1] + r_bins[1:])
    rho_binned = np.zeros(n_bins)
    for i in range(len(r_centers_grid)):
        if r_centers_grid[i] > r_max:
            break
        bin_idx = int(r_centers_grid[i] / r_max * n_bins)
        if 0 <= bin_idx < n_bins:
            rho_binned[bin_idx] += rho_np[i]
    return r_bin_centers, rho_binned


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = Cfg()

    print(f"Reconstructing grid (Nr={cfg.Nr}, Nz={cfg.Nz}, L_r={cfg.L_r}, L_z={cfg.L_z})")
    rr, zz, metric = create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )
    r_grid_max = metric.rr[:, 0].max().item()
    print(f"Grid extends to r_max = {r_grid_max:.4f} l_0")
    print()

    print(f"Loading saved eigvecs from result_hessian_L17.pt ...")
    data = torch.load(os.path.join(HERE, 'result_hessian_L17.pt'),
                      weights_only=False, map_location=device)
    rand_vecs = data['random']['eigvecs'].to(device).to(torch.float64)
    rand_omega2 = data['random']['omega2']
    coll_vec = data['collapse']['eigvec'].to(device).to(torch.float64)
    coll_omega2 = data['collapse']['omega2']
    print(f"  random: shape {rand_vecs.shape}, ω²={rand_omega2}")
    print(f"  collapse: shape {coll_vec.shape}, ω²={coll_omega2}")
    print()

    R_R = 0.6408  # paper R_r
    R_MAX_FULL = 17.0
    N_BINS = 300

    profiles = []
    print(f"{'mode':>20} | {'ω²':>10} | {'peak r':>10} | "
          f"{'tail r>R_r':>12} | {'fraction r>10':>14} | {'fraction r>13':>14}")
    print("-" * 110)

    # Random modes
    for k_ in range(rand_vecs.shape[0]):
        v_k = rand_vecs[k_]
        r_c, rho_k = radial_profile(v_k, metric, N_BINS, R_MAX_FULL)
        peak_r = r_c[np.argmax(rho_k)]
        total = rho_k.sum()
        tail_R_r = rho_k[r_c > R_R].sum() / total if total > 0 else 0
        frac_gt10 = rho_k[r_c > 10.0].sum() / total if total > 0 else 0
        frac_gt13 = rho_k[r_c > 13.0].sum() / total if total > 0 else 0
        print(f"{'random #' + str(k_):>20} | {rand_omega2[k_]:>+10.3f} | "
              f"{peak_r:>10.3f} | {tail_R_r:>12.4f} | "
              f"{frac_gt10:>14.4f} | {frac_gt13:>14.4f}")
        profiles.append({'name': f'random_{k_}', 'omega2': float(rand_omega2[k_]),
                         'r_centers': r_c.tolist(), 'rho': rho_k.tolist(),
                         'peak_r': float(peak_r),
                         'tail_frac_Rr': float(tail_R_r),
                         'frac_gt10': float(frac_gt10),
                         'frac_gt13': float(frac_gt13)})

    # Collapse seed
    r_c, rho_c = radial_profile(coll_vec, metric, N_BINS, R_MAX_FULL)
    peak_r_c = r_c[np.argmax(rho_c)]
    total_c = rho_c.sum()
    tail_R_r_c = rho_c[r_c > R_R].sum() / total_c if total_c > 0 else 0
    frac_gt10_c = rho_c[r_c > 10.0].sum() / total_c if total_c > 0 else 0
    frac_gt13_c = rho_c[r_c > 13.0].sum() / total_c if total_c > 0 else 0
    print(f"{'seed ∂n/∂R_r':>20} | {coll_omega2[0]:>+10.3f} | "
          f"{peak_r_c:>10.3f} | {tail_R_r_c:>12.4f} | "
          f"{frac_gt10_c:>14.4f} | {frac_gt13_c:>14.4f}")
    profiles.append({'name': 'seed_dnR_r', 'omega2': float(coll_omega2[0]),
                     'r_centers': r_c.tolist(), 'rho': rho_c.tolist(),
                     'peak_r': float(peak_r_c),
                     'tail_frac_Rr': float(tail_R_r_c),
                     'frac_gt10': float(frac_gt10_c),
                     'frac_gt13': float(frac_gt13_c)})

    # Save extended profiles
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_hessian_profiles.json'), 'w') as f:
        json.dump({'R_r': R_R, 'r_max': R_MAX_FULL, 'profiles': profiles}, f, indent=2)
    print(f"\nSaved: result_hessian_profiles.json")
    print("\nDONE")


if __name__ == '__main__':
    main()
