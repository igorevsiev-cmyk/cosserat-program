# Electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization

Preprint v1 (2026-05-15).

> **Derivation of the electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e = 511.033 keV` to `0.007 %` accuracy**
> Ihar Yeusiyevich, 2026

## Abstract (one paragraph)

The electron rest energy is computed numerically from three vacuum constants `{ε₀, μ₀, ℏ}` by Nelder–Mead minimisation of a Cosserat-elastic functional of the unit-vector director field `n: ℝ³ → S²` over a three-parameter Hopf ansatz with topological charge `Q_H = 1`. All six parameters of the functional (`K₁, K₂, K₃, μ_c, m², c₄`) are fixed by `{ε₀, μ₀, ℏ}` through the structural identities established in the preceding work [SI Reduction via the Cosserat-continuum hypothesis](../2026-05-SI-reduction/) (DOI [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)); no parameters are free. Numerical minimisation on a stretched cylindrical grid of resolution `1024 × 2048` yields `m_e = 511.033 keV`, deviating from the CODATA 2018 value `510.998950 keV` by `+ 0.007 %`. The Hopf invariant is preserved to numerical precision (`Q_H = 1.000 ± 0.001`). The framework is falsifiable: any independent measurement of `m_e c²` deviating from `511.03 keV` by more than `0.05 %` would invalidate it.

## Files

- `PAPER_ELECTRON_MASS.md` — main paper (English)
- `PAPER_ELECTRON_MASS_RU.md` — Russian original

PDF versions will be added after final DOI assignment.

## Key results

- Electron rest energy from three vacuum constants: `m_e c² = 511.033 keV` (Δ = `+ 0.007 %` from CODATA 2018).
- Zero free parameters: all six functional constants fixed by `{ε₀, μ₀, ℏ}` through the structural identities of [`SI-reduction`](../2026-05-SI-reduction/).
- Topological charge preserved exactly: `Q_H = 1.000 ± 0.001`.
- Linear sensitivity response: 1 % perturbation in any input constant produces 0.25–1 % change in predicted `m_e`, excluding accidental cancellation.
- Falsifiability threshold: deviation > `0.05 %` from `m_e = 511.03 keV` invalidates the framework.

## Relation to the preceding work

This paper is the second in a series developing the Cosserat-vacuum hypothesis. The dimensional reduction `{m, kg, s, A} → {energy}`, the four postulates P1–P4, the structural identities `l₀⁴ = ℏ/(2π Z₀)`, `M₀ = ℏ/(l₀c)`, `μ_c = η = 2π`, `m² = η/(4π)`, `K₃/K₁ - 1 = η`, and the canonical basis `{ε₀, μ₀, ℏ, G}` of fundamental constants are all established in:

- [**Structural reduction of the SI base of units via the Cosserat-continuum hypothesis**](../2026-05-SI-reduction/) — Zenodo DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)

The present work uses those identities to fix all functional parameters and performs the explicit numerical minimisation extracting `m_e`.

## Supplementary verifications

- [`../../verifications/electron_mass_minimization/`](../../verifications/electron_mass_minimization/) — independent **Nelder–Mead minimization** that reproduces the result from a generic initial guess on the canonical `1024 × 2048` grid. Output: `(R_r, R_z, w) ≈ (0.50945, 0.75010, 0.62585)`, `m_e = 511.033 keV`.
- [`../../verifications/canonical_derrick/`](../../verifications/canonical_derrick/) — independent **Derrick-stability scan** of the same canonical configuration, confirming that `λ = 1` is the energy minimum under spatial dilation `(R_r, R_z) → λ·(R_r, R_z)` and `|Q_H|` is preserved across the entire scan.

## Citation

- **Zenodo DOI (v1):** [10.5281/zenodo.20205502](https://doi.org/10.5281/zenodo.20205502)
- **arXiv ID:** *pending*
- **Preceding work DOI:** [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199)
