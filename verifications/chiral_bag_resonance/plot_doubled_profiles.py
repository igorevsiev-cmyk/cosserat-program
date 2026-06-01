#!/usr/bin/env python3
"""
plot_doubled_profiles.py -- paper Figure 7 (§6.6).

Side-by-side comparison of the radial profiles rho(r) on the L_r=17
and L_r=34 boxes. The random-mode peaks shift from r ~ 17 to r ~ 34
in lock-step with the box boundary -- direct visual confirmation of
the box-edge interpretation.

Reads result_hessian_L34.json (L=34 mode profiles) and
result_hessian_profiles.json (L=17 extended profiles).

Output: fig_compare_17_vs_34.png
"""

import os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))
R_R = 0.6408
L_R_OLD = 17.0
L_R_NEW = 34.0


def main():
    with open(os.path.join(HERE, 'result_hessian_L34.json'), 'r') as f:
        data = json.load(f)

    profiles = data['random_profiles']
    cs = data['collapse_seed']

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, 4))

    # Panel (a): linear scale, full doubled grid
    ax = axes[0]
    for i, p in enumerate(profiles):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        ax.plot(r, rho, color=colors[i],
                label=f"random #{i}: ω²={p['omega2']:.2f}, "
                      f"peak r={p['peak_r']:.1f}",
                lw=1.5)
    r_cs = np.array(cs['profile']['r_centers'])
    rho_cs = np.array(cs['profile']['rho'])
    ax.plot(r_cs, rho_cs, color='red', lw=2.5, linestyle='--',
            label=f"seed ∂n/∂R_r: ω²={cs['refined_omega2']:.3f}, "
                  f"peak r={cs['profile']['peak_r']:.1f}")
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f} l₀ (BPS core)')
    ax.axvline(L_R_OLD, color='gray', lw=1.5, linestyle='-',
               alpha=0.6, label=f'old L_r = {L_R_OLD:.0f} l₀')
    ax.axvline(L_R_NEW, color='black', lw=2.0, linestyle='-',
               alpha=0.8, label=f'new L_r = {L_R_NEW:.0f} l₀ (box edge)')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r) = \int_z |\delta n|^2 \cdot 2\pi r\, dz$',
                  fontsize=12)
    ax.set_title('(a) Doubled box (L_r = 34) — peaks shifted to NEW edge')
    ax.set_xlim(0, 35)
    ax.legend(fontsize=8.5, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel (b): log scale, full
    ax = axes[1]
    for i, p in enumerate(profiles):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        rho_safe = np.where(rho > 1e-15, rho, 1e-15)
        ax.semilogy(r, rho_safe, color=colors[i], lw=1.5,
                    label=f"random #{i}")
    rho_cs_safe = np.where(rho_cs > 1e-15, rho_cs, 1e-15)
    ax.semilogy(r_cs, rho_cs_safe, color='red', lw=2.5, linestyle='--',
                label='seed ∂n/∂R_r')
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f} l₀')
    ax.axvline(L_R_OLD, color='gray', lw=1.5, linestyle='-',
               alpha=0.6, label=f'old L_r = {L_R_OLD:.0f}')
    ax.axvline(L_R_NEW, color='black', lw=2.0, linestyle='-',
               alpha=0.8, label=f'new L_r = {L_R_NEW:.0f}')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r)$ (log)', fontsize=12)
    ax.set_title('(b) Log scale — core (r < R_r) still empty, '
                 'peaks at new edge')
    ax.set_xlim(0, 35)
    ax.set_ylim(1e-8, None)
    ax.legend(fontsize=9, loc='lower right')
    ax.grid(True, alpha=0.3, which='both')

    plt.suptitle('Profiles on doubled box: random modes follow the box edge, '
                 'collapse seed also drifts to L_r = 34',
                 fontsize=12.5, y=1.02)
    plt.tight_layout()
    out_path = os.path.join(HERE, 'fig_doubled_profiles.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved: {out_path}')
    plt.close()

    # =================================================================
    # Bonus: side-by-side comparison L=17 vs L=34
    # =================================================================
    with open(os.path.join(HERE, 'result_hessian_profiles.json'), 'r') as f:
        d17 = json.load(f)
    profiles_17 = d17['profiles'][:4]
    cs_17 = d17['profiles'][4]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Left: L=17
    ax = axes[0]
    for i, p in enumerate(profiles_17):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        ax.plot(r, rho, color=colors[i], lw=1.5,
                label=f"random #{i}: peak {p['peak_r']:.1f}")
    r17 = np.array(cs_17['r_centers'])
    rho17 = np.array(cs_17['rho'])
    ax.plot(r17, rho17, color='red', lw=2.5, linestyle='--',
            label=f"seed: peak {cs_17['peak_r']:.1f}")
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f}')
    ax.axvline(L_R_OLD, color='black', lw=2.0, linestyle='-',
               alpha=0.8, label=f'L_r = 17 (edge)')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r)$', fontsize=12)
    ax.set_title('L_r = 17 (original box)')
    ax.set_xlim(0, 35)
    ax.legend(fontsize=9, loc='upper right')
    ax.grid(True, alpha=0.3)

    # Right: L=34
    ax = axes[1]
    for i, p in enumerate(profiles):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        ax.plot(r, rho, color=colors[i], lw=1.5,
                label=f"random #{i}: peak {p['peak_r']:.1f}")
    ax.plot(r_cs, rho_cs, color='red', lw=2.5, linestyle='--',
            label=f"seed: peak {cs['profile']['peak_r']:.1f}")
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f}')
    ax.axvline(L_R_NEW, color='black', lw=2.0, linestyle='-',
               alpha=0.8, label=f'L_r = 34 (edge)')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r)$', fontsize=12)
    ax.set_title('L_r = 34 (doubled box) — peaks follow the edge')
    ax.set_xlim(0, 35)
    ax.legend(fontsize=9, loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.suptitle('Side-by-side: profiles move with box edge → '
                 'modes are box-edge, NOT bag-localized',
                 fontsize=12.5, y=1.02)
    plt.tight_layout()
    out_path2 = os.path.join(HERE, 'fig_compare_17_vs_34.png')
    plt.savefig(out_path2, dpi=150, bbox_inches='tight')
    print(f'Saved: {out_path2}')
    plt.close()


if __name__ == '__main__':
    main()
