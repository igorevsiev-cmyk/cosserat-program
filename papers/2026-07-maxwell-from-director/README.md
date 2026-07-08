# Maxwell's Equations as Theorems about the Director Field

Self-contained paper of the EM sector of the Cosserat program: all four
Maxwell equations follow from the existence of a director field
`n: ℝ³·¹ → S²` — they are theorems, not postulates.

**DOI:** [10.5281/zenodo.21264016](https://doi.org/10.5281/zenodo.21264016) · **License:** CC-BY 4.0

## Files
- `PAPER_MAXWELL_FROM_DIRECTOR_RU.md` — main text (Russian edition, v2,
  extended: written to be read without prior knowledge of the program —
  a "first-time reader" primer, an intuitive picture, explanations after
  each theorem, and a glossary appendix).
- `code/verify_maxwell_v3.py` — numerical check of the Leibniz identity
  on the Belavin–Polyakov instanton (residual 0.0001%).
- `code/verify_g0_and_identity_3d.py` — audit of `g₀ ↔ e`
  (`α_w = 1/(32π)`, the `4/π` gap) plus the identity on the canonical
  3D hopfion (residual ∝ dx⁴, `term1/term2 = 0.372`).

## Main result
- **Homogeneous pair** (`∇·B = 0`, Faraday) — a Bianchi identity:
  a consequence of `dim S² = 2`. A theorem for any smooth `n`.
- **Inhomogeneous pair** (`∇·E = ρ`, Ampère) — the exact Leibniz identity
  `∂_μF^μν = n·(□n×∂^νn) + n·(∂^μn×∂_μ∂^νn) ≡ j^ν`, which *computes* the
  source current instead of postulating it.
- The current is localized on the defect (`~1/r⁵`), non-singular, and
  `∫j⁰ ∝ Q ∈ ℤ` — electric charge is topologically quantized.
- The CP¹ derivation fixes the coupling constant `g₀ = √(μ₀c₄)`
  (energy normalization: Skyrme term ≡ Maxwell term; the earlier form
  `g₀ = √(2c₂/(μ₀c₄))` is dimensionally inconsistent — corrected in §6.2).
- Maxwell is the exact far-field (IR) limit; in the defect core the same
  structure yields a finite mass instead of a divergence.

## Status of results
- Theorems 1–2 are mathematical identities; the numerical verification
  reaches the finite-difference truncation limit of the scheme
  (BP instanton, 512², 4th order — residual 0.0001%).
- Level [2] (isomorphism, no new number), with two bridges to level [3]:
  topological charge quantization and the current structure in the core
  (`term1/term2 ~ c₄/c₂` → `r_v = l₀/2` → `α_bare = 1/128`).

## Open questions
- The `4/π` factor between `α_w = 1/(32π)` (dynamical, CP¹ route) and
  `α_bare = 1/128` (geometric route): both reproduce the law
  "charge² ∝ l₀⁴", but the coefficient differs by exactly `4/π`.
- The 3D hopfion is verified at the ansatz level (residual ∝ dx⁴,
  `term1/term2 = 0.372`, §9); a check on the full-field relaxation and the
  quantitative link between `term1/term2` and the plateau `r_v` remain.
- A rigorous derivation of `c₄` from the microscopics of the medium.

## Reproduce
```bash
python3 code/verify_maxwell_v3.py          # Leibniz identity on the 2D BP instanton
python3 code/verify_g0_and_identity_3d.py  # g₀ ↔ e audit + identity on the 3D hopfion
```
The first script is self-contained (numpy). The second needs numpy + torch
(CUDA recommended for the 256³ grid).

## Provenance
This work grew out of the program's micropolar-geodynamics manifest
(Part VI, "Maxwell's equations from the topology of S²"). The
electromagnetic framework — the identification of the medium moduli with
`{ε₀, μ₀, ℏ}` and the length scale `l₀` — is set by the companion
SI-reduction paper.
