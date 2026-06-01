#!/usr/bin/env python3
"""
analysis_doubled_box.py -- repeat the analysis_three_checks.py pipeline
on a doubled box L_r = 34, L_z = 66 l_0 (paper §6.6).

Grid resolution is unchanged (Nr=1024, Nz=2048): the same memory now
covers a 4x larger physical region; stretching beta_r=6 keeps cell
density around r ~ 1, while the outer region is sampled more coarsely.

Discrimination test for the lowest Hessian modes:

  - box-edge modes:  omega^2(2L) = omega^2(L) / 4  (wavelength ~ L)
                     peak r at the new boundary ~ 34 l_0
  - bag modes:       omega^2(2L) = omega^2(L)      (physical scale fixed)
                     peak r at R_r or some fixed bulk position

Output: result_hessian_L34.json, result_hessian_L34.pt.
"""

import sys, os, json, time
os.environ['PYTHONUNBUFFERED'] = '1'
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import numpy as np
import torch

# Import shared utilities from the L=17 main script
import importlib.util
spec = importlib.util.spec_from_file_location(
    "atc", os.path.join(HERE, "analysis_three_checks.py"))
atc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atc)


class CfgDouble(atc.Cfg):
    """Doubled box -- same grid resolution, 4x larger physical region."""
    Nr = 1024; Nz = 2048
    L_r = 34.0; L_z = 66.0      # doubled vs L=17 main run
    beta_r = 6.0; beta_z = 3.0
    R_hopf = 1.0
    use_float64 = True
    n_frozen_r = 2; n_frozen_edge = 3
    K1 = 2.0; K2 = 2.0; K3 = 14.56
    c2 = 1.0; c4 = 1.0; m2 = 0.0
    cg_iter = 2000


def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    cfg = CfgDouble()
    K_RANDOM = 4
    MAX_ITER_RAND = 50
    MAX_ITER_SEED = 30

    print("=" * 100)
    print(f"DOUBLED BOX: L_r={cfg.L_r}, L_z={cfg.L_z}  (vs old 17, 33)")
    print("=" * 100)
    print(f"Grid: {cfg.Nr}×{cfg.Nz}  (β_r={cfg.beta_r}, β_z={cfg.beta_z})")
    print(f"Same memory, physical region 4× larger.")
    print()
    print(f"Prediction for box-edge modes:  ω²_new ≈ ω²_old / 4")
    print(f"                                peak_r → new edge ~ 34 l₀")
    print(f"Prediction for bag-modes:       ω²_new ≈ ω²_old")
    print(f"                                peak_r → R_r or fixed bulk")
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
    E_of_keV = E_of.item() * atc.keV
    E_sk_keV = E_sk.item() * atc.keV
    print(f"At doubled box: E_OF={E_of_keV:.3f}, E_Sk={E_sk_keV:.3f}, "
          f"E_n_tot={E_of_keV+E_sk_keV:.3f} keV, Q={Q:+.7f}")
    print(f"(compare to L=17 paper: E_OF=221.89, E_Sk=220.63, E_tot=442.52)")
    print()

    hvp_total = atc.make_hvp(n_star, metric, cfg, channel='total')
    zmode, _ = atc.compute_z_translation_mode(n_star, metric)

    # ------------------------------------------------------------------
    # (B) Generalized eigvals with random init
    # ------------------------------------------------------------------
    print("-" * 100)
    print(f"GENERALIZED LOBPCG, random init, k={K_RANDOM}, on DOUBLED box")
    print("-" * 100)
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
    print(f"ω²_rand (sim): {omega2_rand}")
    print(f"old L=17:      [54.14, 64.49, 65.19, 74.88]")
    print(f"prediction /4: [13.5, 16.1, 16.3, 18.7]")
    print()

    # Radial profiles on full doubled grid
    print("─" * 100)
    print(f"RADIAL PROFILES on doubled box (r → {cfg.L_r})")
    print("─" * 100)
    print(f"R_r = {atc.PAPER_R_R:.4f}, L_r = {cfg.L_r}")
    print(f"{'mode':>6} | {'ω²':>10} | {'peak r':>10} | "
          f"{'frac r>17':>12} | {'frac r>25':>12} | {'frac r>30':>12}")
    print("-" * 80)
    profiles_rand = []
    for k_ in range(K_RANDOM):
        v_k = eigvecs_rand[k_].to(device)
        r_c, rho_k = atc.radial_profile(v_k, metric, n_radial_bins=300,
                                         r_max=cfg.L_r)
        peak_r = r_c[np.argmax(rho_k)]
        total = rho_k.sum()
        frac_gt17 = rho_k[r_c > 17.0].sum() / total if total > 0 else 0
        frac_gt25 = rho_k[r_c > 25.0].sum() / total if total > 0 else 0
        frac_gt30 = rho_k[r_c > 30.0].sum() / total if total > 0 else 0
        print(f"  #{k_} | {omega2_rand[k_]:>+10.4f} | {peak_r:>10.4f} | "
              f"{frac_gt17:>12.4f} | {frac_gt25:>12.4f} | {frac_gt30:>12.4f}")
        profiles_rand.append({
            'mode': k_, 'r_centers': r_c.tolist(), 'rho': rho_k.tolist(),
            'peak_r': float(peak_r),
            'frac_gt17': float(frac_gt17),
            'frac_gt25': float(frac_gt25),
            'frac_gt30': float(frac_gt30),
            'omega2': float(omega2_rand[k_]),
        })
    print()

    # ------------------------------------------------------------------
    # (C) Collapse seed v_shrink
    # ------------------------------------------------------------------
    print("-" * 100)
    print("COLLAPSE SEED: v_shrink = dn/dR_r (tangent-projected) on doubled box")
    print("-" * 100)
    v_shrink = atc.make_shrink_seed(rr, zz, n_star, delta=0.005)
    v_shrink_norm = atc.metric_inner(v_shrink, v_shrink, metric).sqrt().item()
    v_shrink = v_shrink / max(v_shrink_norm, 1e-30)

    Hv = hvp_total(v_shrink)
    omega2_direct = atc.euclidean_inner(v_shrink, Hv).item() / \
                    max(atc.metric_inner(v_shrink, v_shrink, metric).item(), 1e-30)
    print(f"Direct Rayleigh ω² of v_shrink: {omega2_direct:+.4f}")
    print(f"  (compare to L=17:   ω² = +3.23 initial)")
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
    print(f"  (compare to L=17:   ω² = +1.27 refined)")
    print()

    # Profile of collapse mode
    v_c = eigvec_collapse[0].to(device)
    r_c, rho_c = atc.radial_profile(v_c, metric, n_radial_bins=300,
                                     r_max=cfg.L_r)
    peak_r_c = r_c[np.argmax(rho_c)]
    total_c = rho_c.sum()
    frac_gt17_c = rho_c[r_c > 17.0].sum() / total_c if total_c > 0 else 0
    frac_gt25_c = rho_c[r_c > 25.0].sum() / total_c if total_c > 0 else 0
    frac_gt30_c = rho_c[r_c > 30.0].sum() / total_c if total_c > 0 else 0
    print(f"Collapse-seed profile: peak_r={peak_r_c:.4f}, "
          f"frac r>17 = {frac_gt17_c:.4f}, "
          f"frac r>25 = {frac_gt25_c:.4f}, "
          f"frac r>30 = {frac_gt30_c:.4f}")
    print()

    # ------------------------------------------------------------------
    # Save
    # ------------------------------------------------------------------
    summary = {
        'config': {
            'Nr': cfg.Nr, 'Nz': cfg.Nz,
            'L_r': cfg.L_r, 'L_z': cfg.L_z,
            'beta_r': cfg.beta_r, 'beta_z': cfg.beta_z,
        },
        'state_at_doubled_box': {
            'E_OF_keV': E_of_keV, 'E_Sk_keV': E_sk_keV,
            'E_n_tot_keV': E_of_keV + E_sk_keV, 'Q': Q,
        },
        'random_omega2': omega2_rand.tolist(),
        'random_profiles': profiles_rand,
        'collapse_seed': {
            'direct_omega2': float(omega2_direct),
            'refined_omega2': float(omega2_collapse[0]),
            'profile': {
                'r_centers': r_c.tolist(), 'rho': rho_c.tolist(),
                'peak_r': float(peak_r_c),
                'frac_gt17': float(frac_gt17_c),
                'frac_gt25': float(frac_gt25_c),
                'frac_gt30': float(frac_gt30_c),
            },
        },
        'reference_old': {
            'L_r_old': 17.0,
            'random_omega2_old': [54.14, 64.49, 65.19, 74.88],
            'random_peak_r_old': [16.97, 16.46, 16.97, 16.97],
            'seed_omega2_old': 1.27,
            'seed_peak_r_old': 16.63,
        },
        'timing': {
            'random_lobpcg_s': t_rand,
            'seeded_lobpcg_s': t_seed,
        },
    }
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_hessian_L34.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {out_path}")

    # Save eigvecs separately
    torch.save({
        'random': {
            'omega2': omega2_rand, 'eigvecs': eigvecs_rand,
        },
        'collapse': {
            'omega2': omega2_collapse, 'eigvec': eigvec_collapse[0],
        },
    }, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'result_hessian_L34.pt'))
    print(f"Saved eigvecs: result_hessian_L34.pt")
    print("\nDONE")


if __name__ == '__main__':
    main()
