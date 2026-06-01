#!/usr/bin/env python3
"""
plot_extended.py -- paper Figure 5 (§6.5).

Reads result_hessian_profiles.json and plots the radial densities
rho(r) = int |delta n(r,z)|^2 * 2*pi*r dz of the lowest Hessian modes
over the full grid up to r = 17 l_0 (linear + log scale). Random modes
peak at the box boundary L_r; the targeted seed v_shrink has broader
support in the bulk.

Output: fig_full_range_profiles.png
"""

import os, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))
R_R = 0.6408
L_R = 17.0


def main():
    with open(os.path.join(HERE, 'result_hessian_profiles.json'), 'r') as f:
        data = json.load(f)

    profiles = data['profiles']

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    colors = plt.cm.viridis(np.linspace(0.15, 0.85, 4))

    # Panel (a): linear scale full range
    ax = axes[0]
    for i, p in enumerate(profiles[:4]):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        ax.plot(r, rho, color=colors[i],
                label=f"random #{i}: peak r={p['peak_r']:.1f}, "
                      f"frac r>13={p['frac_gt13']*100:.1f}%",
                lw=1.5)
    p_cs = profiles[4]
    r = np.array(p_cs['r_centers'])
    rho = np.array(p_cs['rho'])
    ax.plot(r, rho, color='red', lw=2.5, linestyle='--',
            label=f"seed ∂n/∂R_r: peak r={p_cs['peak_r']:.1f}, "
                  f"frac r>13={p_cs['frac_gt13']*100:.1f}%")
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f} l₀ (BPS core)')
    ax.axvline(L_R, color='gray', lw=1.5, linestyle='-',
               alpha=0.5, label=f'L_r = {L_R:.0f} l₀ (box edge)')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r) = \int_z |\delta n|^2 \cdot 2\pi r\, dz$',
                  fontsize=12)
    ax.set_title('(a) FULL grid — modes peak AT THE BOX EDGE, not in tail')
    ax.set_xlim(0, 17.5)
    ax.legend(fontsize=8.5, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel (b): log scale full range
    ax = axes[1]
    for i, p in enumerate(profiles[:4]):
        r = np.array(p['r_centers'])
        rho = np.array(p['rho'])
        rho_safe = np.where(rho > 1e-15, rho, 1e-15)
        ax.semilogy(r, rho_safe, color=colors[i], lw=1.5,
                    label=f"random #{i}")
    r = np.array(p_cs['r_centers'])
    rho = np.array(p_cs['rho'])
    rho_safe = np.where(rho > 1e-15, rho, 1e-15)
    ax.semilogy(r, rho_safe, color='red', lw=2.5, linestyle='--',
                label='seed ∂n/∂R_r')
    ax.axvline(R_R, color='black', lw=1.2, linestyle=':',
               label=f'R_r = {R_R:.2f} l₀')
    ax.axvline(L_R, color='gray', lw=1.5, linestyle='-',
               alpha=0.5, label=f'L_r = {L_R:.0f} l₀')
    ax.set_xlabel('r  [l₀]', fontsize=12)
    ax.set_ylabel(r'$\rho(r)$ (log)', fontsize=12)
    ax.set_title('(b) Log scale — random concentrates at box edge')
    ax.set_xlim(0, 17.5)
    ax.set_ylim(1e-8, None)
    ax.legend(fontsize=9, loc='lower right')
    ax.grid(True, alpha=0.3, which='both')

    plt.suptitle('Honest picture: random LOBPCG finds BOX-EDGE modes; '
                 'targeted seed reaches the bulk',
                 fontsize=12.5, y=1.02)
    plt.tight_layout()
    out_path = os.path.join(HERE, 'fig_full_range_profiles.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f'Saved: {out_path}')
    plt.close()


if __name__ == '__main__':
    main()
