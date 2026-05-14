#!/usr/bin/env python3
"""
plot.py — reproduces the Derrick scan plot from derrick_scan.csv.
Requires only matplotlib (no GPU, no PyTorch).
"""

import csv
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(here, 'derrick_scan.csv')

    rows = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({k: float(v) for k, v in r.items()})

    lam = [r['lambda'] for r in rows]
    e_of = [r['E_OF'] for r in rows]
    e_sk = [r['E_Sk'] for r in rows]
    e_mass = [r['E_mass'] for r in rows]
    e_u = [r['E_u'] for r in rows]
    e_tot = [r['E_tot'] for r in rows]

    # idx of minimum E_tot
    idx_min = e_tot.index(min(e_tot))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # left: total energy
    ax1.plot(lam, e_tot, 'o-', color='black', lw=2, markersize=7,
             label=r'$E_{\rm tot}(\lambda)$')
    ax1.axvline(1.0, color='red', linestyle='--', alpha=0.5,
                label='canonical $\\lambda = 1$')
    ax1.scatter([lam[idx_min]], [e_tot[idx_min]], s=200, marker='*',
                color='red', zorder=10,
                label=f'min: $\\lambda={lam[idx_min]:.2f}$, '
                      f'$E={e_tot[idx_min]:.2f}$ keV')
    ax1.axhline(510.999, color='blue', linestyle=':', alpha=0.5,
                label=r'$m_e^{\rm exp} = 510.999$ keV')
    ax1.set_xlabel(r'$\lambda$  (size scale of canonical Hopf ansatz)', fontsize=12)
    ax1.set_ylabel(r'$E_{\rm tot}$  (keV)', fontsize=12)
    ax1.set_title('Derrick scan: total energy vs. spatial dilation',
                  fontsize=12)
    ax1.grid(alpha=0.3)
    ax1.legend(loc='upper right', fontsize=10)
    ax1.set_xlim(0.5, 3.1)

    # right: components
    ax2.plot(lam, e_of, 'o-', label=r'$E_{\rm OF}$ (Oseen–Frank, $\sim\lambda$)',
             color='tab:blue')
    ax2.plot(lam, e_sk, 's-', label=r'$E_{\rm Sk}$ (Skyrme, $\sim\lambda^{-1}$)',
             color='tab:orange')
    ax2.plot(lam, e_mass, '^-', label=r'$E_{\rm mass}$ (anisotropy, $\sim\lambda^{3}$)',
             color='tab:green')
    ax2.plot(lam, e_u, 'd-', label=r'$E_u$ (Cosserat, $\sim\lambda^{2}$)',
             color='tab:red')
    ax2.axvline(1.0, color='red', linestyle='--', alpha=0.3)
    ax2.set_xlabel(r'$\lambda$', fontsize=12)
    ax2.set_ylabel(r'energy component  (keV)', fontsize=12)
    ax2.set_title('Energy components — Derrick scaling',
                  fontsize=12)
    ax2.grid(alpha=0.3)
    ax2.legend(loc='upper left', fontsize=10)
    ax2.set_xlim(0.5, 3.1)
    ax2.set_yscale('log')

    plt.tight_layout()

    out_path = os.path.join(here, 'derrick_scan.png')
    plt.savefig(out_path, dpi=140, bbox_inches='tight')
    print(f"Saved: {out_path}")


if __name__ == '__main__':
    main()
