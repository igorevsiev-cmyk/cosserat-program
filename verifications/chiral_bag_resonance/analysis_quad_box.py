#!/usr/bin/env python3
"""
analysis_quad_box.py -- third point of the box-size scan: L_r = 68,
L_z = 132 l_0 (paper §6.7).

Together with L=17 (analysis_three_checks.py) and L=34
(analysis_doubled_box.py), the three data points discriminate

  random modes:      omega^2(L) propto 1/L^2  (box-edge phonons)
  v_shrink direct:   omega^2(L) propto 1/L    (bag-anchored mode with
                                                a 1/r tail in the massless
                                                Frank-Oseen field)

The K/M-theorem of paper §6.7 follows from the v_shrink scaling:
the bag-core stiffness K = omega^2 * L is constant within ~3%, while the
inertia M propto L diverges -- only the u-channel screening cuts the tail
and yields a discrete spectrum.

Output: result_hessian_L68.json, result_hessian_L68.pt.
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np
import torch

import importlib.util
spec = importlib.util.spec_from_file_location(
    "atc", os.path.join(HERE, "analysis_three_checks.py"))
atc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atc)


class CfgQuad(atc.Cfg):
    """Quadrupled box -- same grid resolution, 16x larger physical area."""
    Nr = 1024; Nz = 2048
    L_r = 68.0; L_z = 132.0      # 4x in each direction vs L=17 main run
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3
    K1 = 2.0; K2 = 2.0; K3 = 14.56
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    cg_iter = 2000


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = CfgQuad()
    K_RANDOM = 4
    MAX_ITER_RAND = 50
    MAX_ITER_SEED = 30

    print("=" * 100)
    print(f"QUAD BOX: L_r={cfg.L_r}, L_z={cfg.L_z}  (×4 vs original 17, 33)")
    print("=" * 100)
    print(f"Grid: {cfg.Nr}×{cfg.Nz}  (β_r={cfg.beta_r}, β_z={cfg.beta_z})")
    print()
    print(f"Prediction (from 2-pt fit ω²_core=1.167, C=596):")
    print(f"  v_shrink direct  ω²(L=68) ≈ 1.167 + 596/68² = "
          f"{1.167 + 596/68**2:.3f}")
    print(f"  random            ω²(L=68) ≈ 54-75 / 16 ≈ 3.4-4.7")
    print()

    rr, zz, metric = atc.create_stretched_grid(
        cfg, device, r_focus=cfg.R_hopf, z_focus=0.0,
        beta_r=cfg.beta_r, beta_z=cfg.beta_z,
    )

    with torch.no_grad():
        n_star = atc.hopf_init(rr, zz, atc.PAPER_R_R, atc.PAPER_R_Z, atc.PAPER_W)
        _, E_of, E_sk, _ = atc.compute_energy_cosserat_stretched(
            n_star, metric, cfg)
        Q = atc.compute_Q_stretched(n_star, metric).item()
    print(f"At L=68 box: E_OF={E_of.item()*atc.keV:.3f} keV, "
          f"E_Sk={E_sk.item()*atc.keV:.3f} keV, Q={Q:+.7f}")
    print()

    hvp_total = atc.make_hvp(n_star, metric, cfg, channel='total')
    zmode, _ = atc.compute_z_translation_mode(n_star, metric)

    # ------------------------------------------------------------------
    # Random init
    # ------------------------------------------------------------------
    print("─" * 100)
    print(f"Random LOBPCG, k={K_RANDOM}, on quad box")
    print("─" * 100)
    t0 = time.time()
    omega2_rand, eigvecs_rand = atc.lobpcg_generalized(
        hvp_total, k=K_RANDOM, device=device, dtype=torch.float64,
        metric=metric, n_star=n_star,
        zero_modes=[zmode],
        initial_X=None,
        max_iter=MAX_ITER_RAND, tol=1e-5, verbose=True,
    )
    t_rand = time.time() - t0
    print(f"\nDone in {t_rand:.0f}s")
    print(f"ω²_rand: {omega2_rand}")
    print()

    # Profiles
    print(f"R_r = {atc.PAPER_R_R:.4f}, L_r = {cfg.L_r}")
    print(f"{'mode':>6} | {'ω²':>10} | {'peak r':>10} | "
          f"{'frac r>34':>12} | {'frac r>50':>12} | {'frac r>60':>12}")
    print("-" * 80)
    profiles_rand = []
    for k_ in range(K_RANDOM):
        v_k = eigvecs_rand[k_].to(device)
        r_c, rho_k = atc.radial_profile(v_k, metric, n_radial_bins=300,
                                         r_max=cfg.L_r)
        peak_r = r_c[np.argmax(rho_k)]
        total = rho_k.sum()
        frac_gt34 = rho_k[r_c > 34.0].sum() / total if total > 0 else 0
        frac_gt50 = rho_k[r_c > 50.0].sum() / total if total > 0 else 0
        frac_gt60 = rho_k[r_c > 60.0].sum() / total if total > 0 else 0
        print(f"  #{k_} | {omega2_rand[k_]:>+10.4f} | {peak_r:>10.4f} | "
              f"{frac_gt34:>12.4f} | {frac_gt50:>12.4f} | {frac_gt60:>12.4f}")
        profiles_rand.append({
            'mode': k_, 'r_centers': r_c.tolist(), 'rho': rho_k.tolist(),
            'peak_r': float(peak_r),
            'frac_gt34': float(frac_gt34),
            'frac_gt50': float(frac_gt50),
            'frac_gt60': float(frac_gt60),
            'omega2': float(omega2_rand[k_]),
        })
    print()

    # ------------------------------------------------------------------
    # Collapse seed
    # ------------------------------------------------------------------
    print("─" * 100)
    print("COLLAPSE SEED on quad box")
    print("─" * 100)
    v_shrink = atc.make_shrink_seed(rr, zz, n_star, delta=0.005)
    v_shrink_norm = atc.metric_inner(v_shrink, v_shrink, metric).sqrt().item()
    v_shrink = v_shrink / max(v_shrink_norm, 1e-30)

    Hv = hvp_total(v_shrink)
    omega2_direct = atc.euclidean_inner(v_shrink, Hv).item() / \
                    max(atc.metric_inner(v_shrink, v_shrink, metric).item(), 1e-30)
    print(f"Direct Rayleigh ω² of v_shrink: {omega2_direct:+.4f}")
    print(f"  (L=17: 3.23,  L=34: 1.68,  predicted L=68 from 2pt: 1.296)")
    print()

    print(f"Refining v_shrink via LOBPCG (k=1, max_iter={MAX_ITER_SEED})...")
    initial_X = v_shrink.unsqueeze(0)
    t0 = time.time()
    omega2_collapse, eigvec_collapse = atc.lobpcg_generalized(
        hvp_total, k=1, device=device, dtype=torch.float64,
        metric=metric, n_star=n_star,
        zero_modes=[zmode],
        initial_X=initial_X,
        max_iter=MAX_ITER_SEED, tol=1e-5, verbose=True,
    )
    t_seed = time.time() - t0
    print(f"\nDone in {t_seed:.0f}s")
    print(f"Refined ω² (collapse seed): {omega2_collapse}")
    print()

    v_c = eigvec_collapse[0].to(device)
    r_c, rho_c = atc.radial_profile(v_c, metric, n_radial_bins=300,
                                     r_max=cfg.L_r)
    peak_r_c = r_c[np.argmax(rho_c)]
    total_c = rho_c.sum()
    frac_gt34_c = rho_c[r_c > 34.0].sum() / total_c if total_c > 0 else 0
    frac_gt50_c = rho_c[r_c > 50.0].sum() / total_c if total_c > 0 else 0
    frac_gt60_c = rho_c[r_c > 60.0].sum() / total_c if total_c > 0 else 0
    print(f"Collapse-seed profile: peak_r={peak_r_c:.4f}, "
          f"frac r>34 = {frac_gt34_c:.4f}, "
          f"frac r>50 = {frac_gt50_c:.4f}, "
          f"frac r>60 = {frac_gt60_c:.4f}")
    print()

    # Save
    summary = {
        'config': {
            'Nr': cfg.Nr, 'Nz': cfg.Nz,
            'L_r': cfg.L_r, 'L_z': cfg.L_z,
            'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
        },
        'random_omega2': omega2_rand.tolist(),
        'random_profiles': profiles_rand,
        'collapse_seed': {
            'direct_omega2': float(omega2_direct),
            'refined_omega2': float(omega2_collapse[0]),
            'profile': {
                'r_centers': r_c.tolist(), 'rho': rho_c.tolist(),
                'peak_r': float(peak_r_c),
                'frac_gt34': float(frac_gt34_c),
                'frac_gt50': float(frac_gt50_c),
                'frac_gt60': float(frac_gt60_c),
            },
        },
        'timing': {
            'random_lobpcg_s': t_rand,
            'seeded_lobpcg_s': t_seed,
        },
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_hessian_L68.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {out_path}")

    torch.save({
        'random': {
            'omega2': omega2_rand, 'eigvecs': eigvecs_rand,
        },
        'collapse': {
            'omega2': omega2_collapse, 'eigvec': eigvec_collapse[0],
        },
    }, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_hessian_L68.pt'))
    print(f"Saved eigvecs: result_hessian_L68.pt")
    print("\nDONE")


if __name__ == '__main__':
    main()
