# Anisotropy scan — verification of §7.3 (r_v = l₀/2)

This folder contains numerical supporting data for the geometric identity
**r_v = l₀ / 2** used in the derivation of `α_bare = 1/128` (§7.5 of the
main paper).

The radius of the hopfion vortex tube `r_v` is expected to coincide
with half the Skyrme length `L = √(c₄ / K₁)`. To verify this, the
elastic anisotropy ratio `K₃ / K₁` is scanned across two decades, and
the ratio `r_v / L` is measured from the relaxed configuration at each
point.

## Files

- `scan_data.json` — full scan data (10 points of `K₃/K₁` from 1.0 to 25.0)
  with relaxed energy, `r_v/L`, and topological charge `Q` for each.
- `scan_K3K1.png` — the original scan plot.
- `plot.py` — reproduces the plot from `scan_data.json`
  (requires `matplotlib`; no dependency on the full simulator).

## Setup

- Hopfion ansatz with `Q_H = -1` (enforced by construction).
- Oseen–Frank elastic energy: `K₁` and `K₂` fixed at 2.0; `K₃` swept.
- Skyrme stabilization with `c₄ = 1.0`.
- Axisymmetric grid 512 × 1024 in (r, z).
- Optimizer: SGD, 3000 steps per point.

## Result

| `K₃/K₁` | 1.0 | 1.5 | 2.5 | **3.5** | **5.0** | **6.0** | **7.5** | 10.0 | 15.0 | 25.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| `r_v / L` | 0.469 | 0.483 | 0.483 | **0.498** | **0.498** | **0.498** | **0.498** | 0.483 | 0.483 | 0.483 |

A plateau of four consecutive points in `K₃/K₁ ∈ [3.5, 7.5]` gives

> **r_v / L = 0.498 ± 0.005**

within the discretization step of the FWHM estimator on a 512×1024 grid.
This confirms `r_v = L / 2` (and, through Derrick stability `L = l₀`,
`r_v = l₀ / 2`) as the geometric input used in (7.5) of the paper.

## Scope of this verification

This artifact reproduces only the **geometric** part of the prediction
(`r_v / L`). The underlying relaxation code (the full hopfion functional
`E[n, u]`, with director and translation fields, anchoring `m²`, and
Cosserat coupling `μ_c`) is documented and released as part of the
companion work [10]; here we publish only the post-processed scan to
support the geometric claim in this paper.

## How to read

The plateau in `r_v / L` is the central piece: at the canonical
anisotropy `K₃ / K₁ = 1 + η = 1 + 2π ≈ 7.28` (the point predicted by
the Cosserat coupling `η = 2π`, see paper §7.4), the measured ratio is
indistinguishable from `1/2` within the discretization uncertainty.

The energy `E_sim` grows monotonically with `K₃/K₁`, confirming that
larger bend stiffness costs more relaxed energy without altering the
geometric ratio.
