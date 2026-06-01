#!/usr/bin/env python3
"""
plot_box_scaling.py -- paper Figure 6 (§6.6).

Reads result_hessian_L17.json and result_hessian_L34.json, plots
omega^2(L) for random and v_shrink modes, and shows that the random
modes scale as 1/L^2 (box-edge phonons) while v_shrink is a mixed
mode capturing part of the bag-anchored direction.

Output: fig_box_scaling.png
"""

import os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # Load both runs
    with open(os.path.join(HERE, 'result_hessian_L17.json'), 'r') as f:
        d17 = json.load(f)
    with open(os.path.join(HERE, 'result_hessian_L34.json'), 'r') as f:
        d34 = json.load(f)

    # Random modes
    omega2_17 = d17['generalized_omega2_random']
    omega2_34 = d34['random_omega2']

    # v_shrink direct (un-refined Rayleigh)
    vs_17_direct = d17['collapse_seed']['direct_omega2']
    vs_34_direct = d34['collapse_seed']['direct_omega2']

    # v_shrink refined
    vs_17_refined = d17['collapse_seed']['refined_omega2']
    vs_34_refined = d34['collapse_seed']['refined_omega2']

    L_values = np.array([17.0, 34.0])

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # =================================================================
    # Panel (a): scaling of ω² with L (log-log)
    # =================================================================
    ax = axes[0]

    # Random modes (4 of them)
    for i in range(4):
        ax.plot(L_values, [omega2_17[i], omega2_34[i]],
                'o-', color=plt.cm.viridis(0.15 + 0.2 * i), lw=1.5, ms=8,
                label=f'random #{i}')

    # v_shrink direct
    ax.plot(L_values, [vs_17_direct, vs_34_direct],
            's-', color='blue', lw=2, ms=10,
            label='v_shrink direct Rayleigh')

    # v_shrink refined
    ax.plot(L_values, [vs_17_refined, vs_34_refined],
            'D-', color='red', lw=2, ms=10,
            label='v_shrink refined (LOBPCG)')

    # Reference lines: ω² ∝ 1/L² (box-edge) and ω² = const (bag-mode)
    L_ref = np.linspace(15, 36, 50)

    # Pure box scaling from omega2_17 average
    omega2_17_avg = np.mean(omega2_17)
    ax.plot(L_ref, omega2_17_avg * (17.0 / L_ref)**2,
            'k--', alpha=0.5, label=r'$\omega^2 \propto 1/L^2$ (box-edge)')

    # Pure bag-mode (constant) for reference at v_shrink direct level
    ax.plot(L_ref, vs_17_direct * np.ones_like(L_ref),
            'k:', alpha=0.5, label=r'$\omega^2 = $ const (bag-mode)')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Box size  L_r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\omega^2$  (sim units)', fontsize=12)
    ax.set_title('(a) Scaling of Hessian eigvalues vs box size — '
                 'log-log plot')
    ax.legend(fontsize=8.5, loc='lower left')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xticks([17, 25, 34])
    ax.set_xticklabels(['17', '25', '34'])

    # =================================================================
    # Panel (b): ratios — direct test
    # =================================================================
    ax = axes[1]

    ratios = []
    labels = []
    colors_bar = []

    for i in range(4):
        ratios.append(omega2_34[i] / omega2_17[i])
        labels.append(f'random #{i}')
        colors_bar.append(plt.cm.viridis(0.15 + 0.2 * i))

    ratios.append(vs_34_direct / vs_17_direct)
    labels.append('v_shrink\n(direct)')
    colors_bar.append('blue')

    ratios.append(vs_34_refined / vs_17_refined)
    labels.append('v_shrink\n(refined)')
    colors_bar.append('red')

    y_pos = np.arange(len(ratios))
    ax.barh(y_pos, ratios, color=colors_bar, alpha=0.7)
    ax.axvline(0.25, color='black', linestyle='--', lw=1.5,
               label=r'1/4  $\Leftrightarrow$ pure box-edge')
    ax.axvline(1.00, color='black', linestyle=':', lw=1.5,
               label=r'1.0  $\Leftrightarrow$ pure bag-mode')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel(r'Ratio  $\omega^2(L=34) \; / \; \omega^2(L=17)$',
                  fontsize=12)
    ax.set_xlim(0, 1.1)
    ax.invert_yaxis()
    ax.set_title('(b) Empirical ratio — proximity to 1/4 vs 1.0')
    ax.legend(fontsize=10, loc='lower right')
    ax.grid(True, alpha=0.3, axis='x')

    # Annotate
    for i, r in enumerate(ratios):
        ax.annotate(f'{r:.3f}', xy=(r, i), xytext=(5, 0),
                    textcoords='offset points', fontsize=10,
                    va='center', fontweight='bold')

    plt.suptitle('Box-size scan: random modes scale exactly as 1/L² '
                 '(pure box-edge); v_shrink intermediate (mixed)',
                 fontsize=12, y=1.02)
    plt.tight_layout()
    out_path = os.path.join(HERE, 'fig_box_scaling.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved: {out_path}')
    plt.close()


if __name__ == '__main__':
    main()
