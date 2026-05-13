"""
Plot the K3/K1 anisotropy scan from scan_data.json.

Reproduces the figure scan_K3K1.png and visualizes the plateau
r_v / L_Skyrme = 0.498 in the range K3/K1 in [3.5, 7.5],
which underlies the geometric identity r_v = l_0 / 2 used in §7.5
of the paper to derive alpha_bare = 1/128.

Usage:
    python plot.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).parent / "scan_data.json"


def main():
    with open(DATA_PATH) as f:
        scan = json.load(f)

    rows = scan["data"]
    k3k1 = [r["K3_over_K1"] for r in rows]
    rv_l = [r["r_v_over_L"] for r in rows]
    e_sim = [r["E_sim"] for r in rows]

    plateau_lo, plateau_hi = scan["result"]["plateau"]["K3_over_K1_range"]
    plateau_val = scan["result"]["plateau"]["r_v_over_L_mean"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    ax1.plot(k3k1, rv_l, "o-", color="C0", lw=1.5, ms=6)
    ax1.axhspan(0.493, 0.503, color="C0", alpha=0.15, label="plateau r_v/L ≈ 0.498")
    ax1.axvspan(plateau_lo, plateau_hi, color="C2", alpha=0.10,
                label=f"K3/K1 ∈ [{plateau_lo}, {plateau_hi}]")
    ax1.axhline(0.5, color="k", ls="--", lw=0.8, alpha=0.6, label="r_v/L = 1/2")
    ax1.set_xscale("log")
    ax1.set_xlabel("K3 / K1")
    ax1.set_ylabel("r_v / L_Skyrme")
    ax1.set_title("Vortex-tube radius vs anisotropy")
    ax1.legend(loc="lower right", fontsize=9)
    ax1.grid(alpha=0.3)

    ax2.plot(k3k1, e_sim, "s-", color="C3", lw=1.5, ms=6)
    ax2.set_xscale("log")
    ax2.set_xlabel("K3 / K1")
    ax2.set_ylabel("E_sim (relaxed energy, sim units)")
    ax2.set_title("Relaxed energy vs anisotropy")
    ax2.grid(alpha=0.3)

    fig.suptitle(
        "K3/K1 anisotropy scan — verification of §7.3 (r_v = l_0/2)",
        fontsize=11,
    )
    fig.tight_layout()

    out = DATA_PATH.parent / "scan_K3K1_reproduced.png"
    fig.savefig(out, dpi=120, bbox_inches="tight")
    print(f"Plot saved to: {out}")
    print(f"Plateau value: r_v/L = {plateau_val} on K3/K1 in [{plateau_lo}, {plateau_hi}]")


if __name__ == "__main__":
    main()
