#!/usr/bin/env python3
"""
plot_KM_decomposition.py -- paper Figure 8 (§6.7).

Reads result_hessian_L17.json, result_hessian_L34.json,
result_hessian_L68.json and produces the K/M-decomposition figure:

  (a) log-log omega^2(L) for random modes (1/L^2, box-edge phonons)
      and v_shrink_direct (1/L, bag-anchored with 1/r tail);
  (b) extracted stiffness K = omega^2 * L for v_shrink_direct,
      constant within ~3% across the three boxes -- empirical proof
      that the bag core is rigid (K > 0) and omega^2 -> 0 with L
      is driven by the diverging inertia of the massless OF tail.

Output: fig_KM_decomposition.png
"""

import os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, 'result_hessian_L17.json'), 'r') as f:
        d17 = json.load(f)
    with open(os.path.join(HERE, 'result_hessian_L34.json'), 'r') as f:
        d34 = json.load(f)
    with open(os.path.join(HERE, 'result_hessian_L68.json'), 'r') as f:
        d68 = json.load(f)

    L_vals = np.array([17.0, 34.0, 68.0])
    omega2_rand = np.array([
        d17['generalized_omega2_random'],
        d34['random_omega2'],
        d68['random_omega2'],
    ]).T  # shape (4, 3)

    vs_direct = np.array([
        d17['collapse_seed']['direct_omega2'],
        d34['collapse_seed']['direct_omega2'],
        d68['collapse_seed']['direct_omega2'],
    ])
    vs_refined = np.array([
        d17['collapse_seed']['refined_omega2'],
        d34['collapse_seed']['refined_omega2'],
        d68['collapse_seed']['refined_omega2'],
    ])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    # =================================================================
    # Panel (a): ω² vs 1/L on log-log — slopes
    # =================================================================
    ax = axes[0]
    L_smooth = np.linspace(15, 75, 100)
    inv_L = 1.0 / L_smooth
    inv_L_sq = 1.0 / L_smooth**2

    # Random modes
    colors_r = plt.cm.viridis(np.linspace(0.15, 0.85, 4))
    for i in range(4):
        ax.plot(L_vals, omega2_rand[i], 'o-',
                color=colors_r[i], lw=1.5, ms=8,
                label=f'random #{i}' if i < 2 else f'random #{i}')
    # Reference: 1/L² fit through L=17 random average
    omega2_rand_17_avg = omega2_rand[:, 0].mean()
    ax.plot(L_smooth, omega2_rand_17_avg * (17.0/L_smooth)**2,
            'k--', alpha=0.5, lw=1.5, label=r'$\omega^2 \propto 1/L^2$  (random fit)')

    # v_shrink direct
    ax.plot(L_vals, vs_direct, 's-', color='blue', lw=2.5, ms=12,
            label='v_shrink direct  (K const, M∝L)')
    # Reference: 1/L fit
    K_avg = (vs_direct * L_vals).mean()
    ax.plot(L_smooth, K_avg / L_smooth,
            'b:', alpha=0.6, lw=2, label=fr'$\omega^2 = K/L,  K\approx{K_avg:.1f}$')

    # v_shrink refined
    ax.plot(L_vals, vs_refined, 'D-', color='red', lw=2, ms=10,
            label='v_shrink refined')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'Box size  $L_r$  [$l_0$]', fontsize=12)
    ax.set_ylabel(r'$\omega^2$  (sim units)', fontsize=12)
    ax.set_title('(a) Scaling of Hessian eigenvalues vs box size (log-log)',
                 fontsize=12)
    ax.legend(fontsize=8.5, loc='lower left')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xticks([17, 34, 68])
    ax.set_xticklabels(['17', '34', '68'])

    # =================================================================
    # Panel (b): K = ω²·L invariance — proof of constant stiffness
    # =================================================================
    ax = axes[1]
    K_vals = vs_direct * L_vals
    ax.bar(['L=17', 'L=34', 'L=68'], K_vals,
           color=['steelblue', 'cornflowerblue', 'lightskyblue'],
           edgecolor='black', linewidth=1.5)
    K_mean = K_vals.mean()
    ax.axhline(K_mean, color='red', linestyle='--', lw=2,
               label=fr'$\langle K \rangle = {K_mean:.1f}$')
    ax.axhline(K_mean * 1.05, color='red', linestyle=':', lw=1, alpha=0.5,
               label='+5%')
    ax.axhline(K_mean * 0.95, color='red', linestyle=':', lw=1, alpha=0.5)
    ax.set_ylabel(r'$K = \omega^2 \cdot L$   (extracted stiffness)',
                  fontsize=12)
    ax.set_title('(b) K = ω²·L invariant across box sizes — '
                 'proof of bag core stiffness  K > 0',
                 fontsize=11.5)
    ax.legend(fontsize=11, loc='lower right')
    ax.grid(True, alpha=0.3, axis='y')
    for i, k in enumerate(K_vals):
        ax.annotate(f'{k:.1f}', xy=(i, k), xytext=(0, 5),
                    textcoords='offset points', fontsize=11,
                    ha='center', fontweight='bold')

    plt.suptitle('3-point box-scan: random modes scale as 1/L² (box-edge), '
                 'v_shrink scales as 1/L (K const, M ∝ L from 1/r tail)',
                 fontsize=12, y=1.02)
    plt.tight_layout()
    out_path = os.path.join(HERE, 'fig_KM_decomposition.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved: {out_path}')
    plt.close()

    # Print summary
    print("\nSummary:")
    print(f"  K = ω²·L for v_shrink direct: "
          f"{K_vals[0]:.2f}, {K_vals[1]:.2f}, {K_vals[2]:.2f}")
    print(f"  ⟨K⟩ = {K_mean:.2f},  std/mean = {K_vals.std()/K_mean*100:.1f}%")


if __name__ == '__main__':
    main()
