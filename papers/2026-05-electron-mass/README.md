# Electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization

Preprint (2026-05-20).

> **Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e^bare = 446.279 keV`**
> Ihar Yeusiyevich, 2026

## Abstract (one paragraph)

The bare electron mass is computed numerically from three vacuum constants `{ε₀, μ₀, ℏ}` by Nelder–Mead minimisation of the Cosserat functional `E[n, u]` of the director field `n: ℝ³ → S²` over a three-parameter Hopf ansatz with topological charge `Q_H = −1`. All five constants of the functional (`K₁, K₂, K₃, μ_c, c₄`) are fixed by `{ε₀, μ₀, ℏ}` through the structural identities established in the preceding work [SI Reduction via the Cosserat-continuum hypothesis](../2026-05-SI-reduction/) (DOI [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)); no parameters are free. Minimisation on a `1024 × 2048` stretched grid (dyadic box `L = 17 × 33 l₀`) yields the **bare** mass `m_e^bare c² = 446.279 keV`. The dimensionless minimum `Ẽ_min ≈ 1039` fits the dyadic form `m_e/m₀ = x² + x/2 − 1` with `x = α⁻¹/4`; the same shift of `x` that runs `α⁻¹: 128 → 137` takes the bare mass to the physical `m_e ≈ 511 keV` (numerical observation). This is the bare value — a direct output of the bare functional, deliberately not compared with the physical (measured) electron mass.

## Files

- `PAPER_ELECTRON_MASS.md` — main paper (English)
- `PAPER_ELECTRON_MASS_RU.md` — Russian original
- typeset PDF versions (RU + EN) in this folder

## Key results

- Bare electron mass from three vacuum constants: `m_e^bare c² = 446.279 keV` on the dyadic box `17 × 33 l₀`.
- Zero free parameters: all five functional constants `{K₁, K₂, K₃, μ_c, c₄}` fixed by `{ε₀, μ₀, ℏ}` through the structural identities of [`SI-reduction`](../2026-05-SI-reduction/).
- Dyadic form: the dimensionless minimum `Ẽ_min ≈ 1039 = 2¹⁰ + 2⁴ − 1`; the same formula at the physical `α` gives `m_e^phys ≈ 511 keV` (numerical observation, §7).
- Topological charge preserved: `Q_H = −0.99996` (`|Q_H| = 1` to `~4·10⁻⁵`).
- Energy decomposition: `E_OF = 221.888 keV` (49.7 %), `E_Sk = 220.634 keV` (49.4 %), `E_u = 3.758 keV` (0.8 %).

## Relation to the preceding work

This paper is the second in a series developing the Cosserat-vacuum hypothesis. The dimensional reduction `{m, kg, s, A} → {energy}`, the four postulates P1–P4, the structural identities `l₀⁴ = ℏ/(2π Z₀)`, `M₀ = ℏ/(l₀c)`, `μ_c = η = 2π`, `K₃/K₁ − 1 = η`, and the canonical basis `{ε₀, μ₀, ℏ, G}` of fundamental constants are all established in:

- [**Structural reduction of the SI base of units via the Cosserat-continuum hypothesis**](../2026-05-SI-reduction/) — Zenodo DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)

The present work uses those identities to fix all functional parameters and performs the explicit numerical minimisation extracting `m_e^bare`.

## Supplementary verifications

- [`../../verifications/electron_mass_minimization/`](../../verifications/electron_mass_minimization/) — independent **Nelder–Mead minimization** that reproduces the result from a generic initial guess on the `1024 × 2048` grid, dyadic box `17 × 33`. Output: `(R_r, R_z, w) ≈ (0.64082, 0.80729, 0.70200)`, `m_e^bare = 446.279 keV`.
- [`../../verifications/canonical_derrick/`](../../verifications/canonical_derrick/) — independent **Derrick-stability scan** of the same canonical configuration, confirming that `λ = 1` is the energy minimum under spatial dilation `(R_r, R_z) → λ·(R_r, R_z)` and `|Q_H|` is preserved across the entire scan.

## Citation

- **Zenodo DOI:** [10.5281/zenodo.20205502](https://doi.org/10.5281/zenodo.20205502)
- **arXiv ID:** *pending*
- **Preceding work DOI:** [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)
