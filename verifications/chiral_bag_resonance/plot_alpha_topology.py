"""Measured radial profiles of the canonical hopfion (paper §3.3, §5).

Reads result_alpha_running.json and produces a 2-panel figure of the two
DIRECTLY MEASURED radial profiles:
  (a) |Q_H(R)| -- topological-charge closure (99.9% at R ~ 6.6-7 l_0 = log2 128)
  (b) m(R)     -- cumulative mass: 2^10 = 1024 BPS core, full 1039 = 2^10+2^4-1

The dyadic alpha^{-1} = 128 + 8 + 1 + 1/28 is an ALGEBRAIC dyadic assembly
(paper §5), NOT a radial RG running, so it is given in the text rather than
plotted as a curve. The screening 128 -> 137 tracks the charge closure |Q_H(R)|
shown in panel (a) (99.9% at R ~ 7 = log2 128).

Output: fig_alpha_topology_running.png
"""
import json, os, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'result_alpha_running.json')))
R = np.array(d['radial']['R_grid'])
m_R = np.array(d['radial']['cum_m_cells'])
absQ = np.abs(np.array(d['radial']['cum_Q_H']))

R_diag = float(np.sqrt(17.0**2 + 16.5**2))
idx_999 = int(np.argmax(absQ >= 0.999)) if np.any(absQ >= 0.999) else len(R) - 1
R_charge999 = float(R[idx_999])

# Measured closure radii
print(f"R(99.9% Q) = {R_charge999:.2f} l_0   (holographic log2(128) = 7)")
print(f"{'R':>6}  {'m(R)':>8}  {'|Q|':>7}")
print('-' * 28)
for R_target in [0.5, 1.0, 2.0, 5.0, 6.6, 7.5, 10.0, 17.0, 23.7]:
    i = int(np.argmin(np.abs(R - R_target)))
    print(f"  {R[i]:5.2f}  {m_R[i]:7.2f}  {absQ[i]:6.4f}")

# Two-panel figure: the two MEASURED radial profiles
fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(11, 7.5), sharex=True)

# (a) |Q(R)| topological closure
ax0.plot(R, absQ, color='C3', lw=2.5)
ax0.axhline(1.0, color='gray', ls=':', lw=0.8)
ax0.text(0.12, 1.02, r'$|Q_H| = 1$  (full closure)', fontsize=9, color='gray')
ax0.set_ylabel(r'$|Q_H(R)|$', fontsize=11, color='C3')
ax0.tick_params(axis='y', labelcolor='C3')
ax0.set_title(r'(a) Topological-charge closure $|Q_H(R)|$ — 99.9% at $R \approx 6.6\,l_0 = \log_2 128$',
              fontsize=11)
ax0.set_ylim(0, 1.08)
ax0.set_xscale('log')
ax0.set_xlim(0.1, 30)
ax0.grid(alpha=0.3)

# (b) Cumulative mass m(R)
ax1.plot(R, m_R, color='C0', lw=2.5)
ax1.axhline(1024, color='gray', ls=':', lw=0.9)
ax1.axhline(1039, color='red',  ls=':', lw=0.9)
ax1.text(0.12, 1008, r'$2^{10}=1024$  (BPS core)', fontsize=9, color='gray')
ax1.text(0.12, 1055, r'$2^{10}+2^4-1=1039$  (full bag, bare $\alpha^{-1}=128$)',
         fontsize=9, color='red')
ax1.set_ylabel(r'$m(R)/M_0c^2$  [cells]', fontsize=11)
ax1.set_title(r'(b) Cumulative mass $m(R)$ (slow shell accumulation, $R = 7.5..23.7$)',
              fontsize=11)
ax1.set_ylim(0, 1200)
ax1.set_xlabel(r'$R\;[l_0]$  (spherical radius)', fontsize=11)
ax1.grid(alpha=0.3)

# Spatial markers (charge-closure radius, ring, BPS-core, box, diagonal)
markers = [(0.64, r'$R_r$'), (R_charge999, r'$R_{99.9\%Q}$'), (7.5, r'$R_{\rm BPS}$'),
           (17, r'$L_{\rm box}$'), (R_diag, r'$R_{\rm diag}$')]
for ax in (ax0, ax1):
    for R_x, _ in markers:
        ax.axvline(R_x, color='k', ls='--', lw=0.5, alpha=0.4)
for R_x, name in markers:
    ax1.text(R_x*1.02, 35, name, rotation=90, fontsize=8, color='k', alpha=0.6)

plt.tight_layout()
out_png = os.path.join(HERE, 'fig_alpha_topology_running.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f'\nSaved: {out_png}')
