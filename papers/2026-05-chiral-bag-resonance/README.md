# Discrete electron mass and the fine-structure constant from a Cosserat-hopfion resonance at `μ_c = 2π`

Preprint, v1 (2026-05-31).

> **Дискретная масса электрона и постоянная тонкой структуры из резонанса Cosserat-хопфиона при `μ_c = 2π`**
> Ihar Yeusiyevich, 2026

## Abstract (one paragraph)

In the parameter-free Cosserat functional `E[n, u]` — all constants fixed by `{ε₀, μ₀, ℏ}` through the structural identities of the two preceding works ([SI-reduction](../2026-05-SI-reduction/), [electron-mass](../2026-05-electron-mass/)) — the canonical Hopf soliton with `Q_H = −1` at the critical Cosserat coupling `μ_c = η = 2π` **simultaneously** realizes two dyadic quantities: the bare electron mass `m_e^bare / M₀c² = 2¹⁰ + 2⁴ − 1 = 1039` (446.279 keV) and the fine-structure constant `α⁻¹(0) = 128 + 8 + 1 + 1/28 = 3837/28 ≈ 137.036`. Four numerical verifications — μ_c-sweep, u-channel disable, BPS `u ↔ B` alignment, and a Hessian box-scan — identify a **chiral-bag** structure (topological BPS core + elastic shell + discrete boundary spectrum) and yield a **K/M theorem**: in the pure Faddeev–Skyrme theory the bag-core stiffness is positive and box-independent (`K ≈ 57`), but the inertia of perturbations diverges (`M ∝ L`) because of the massless `1/r` tail of the director field; the short-ranged u-channel cuts off the inertia and makes a discrete spectrum `ω² = K/M > 0` possible. The u-channel is therefore a structural necessity, not an add-on.

## Files

- `PAPER_CHIRAL_BAG_RU.md` — main paper (Russian)
- `DRAFT_OUTLINE_RU.md` — detailed working outline (section structure, data tables, figure captions)
- typeset PDF version(s) in this folder *(once compiled)*

## Key results

- One canonical configuration at `μ_c = 2π` fixes **both** `m_e` and `α` — not two independent fits.
- `m_e^bare / M₀c² = 2¹⁰ + 2⁴ − 1 = 1039` → 446.279 keV (direct NM output, [electron-mass]). The same polynomial `m_e/M₀ = x² + x/2 − 1`, `x = α⁻¹/4`, at the physical `α` gives `m_e ≈ 511.0 keV` vs CODATA 510.999 keV — **Δ = 0.01 %**.
- `α⁻¹(0) = 128 + 8 + 1 + 1/28 ≈ 137.0357` vs CODATA 137.035999 — **Δ = 0.0002 %**; the experimental `α` is not used as input.
- **K/M theorem (§6.7):** stiffness `K = ω²·L ≈ 57 ± 3 %` constant across boxes `L = 17, 34, 68 l₀`; the u-channel is mathematically necessary for a discrete excitation spectrum.
- Both quantities trace to a single geometric ratio `g = r_v/l₀ = 1/2` (Derrick balance + Hopf topology), with `α_bare = g⁷ = 1/128`.

## Mechanism: chiral bag

- **Topological core** (`r < R_r ≈ 0.64 l₀`): local BPS alignment `u ∥ B`, numerically `cos θ → 0.9988`.
- **Yukawa-screened elastic shell** (`r > R_r`): the u-channel acts as a massive field with screening length `l_c = 1/√μ_c ≈ 0.40 l₀`.
- **Discrete boundary spectrum** at `μ_c = 2π`: dyadic corrections `+2⁴ − 1` — a bosonic analog of the APS η-invariant (formalization is an open problem, §7.2).

## Supporting numerical verifications

All collected in [`../../verifications/chiral_bag_resonance/`](../../verifications/chiral_bag_resonance/) (one shared `stretched_grid.py`, one `requirements.txt`, one `README.md`):

| Test | Main script | Verifies |
|---|---|---|
| μ_c-sweep | `mu_c_sweep.py` | dyadic `1039` locks **only at μ_c = 2π** |
| u-channel disable | `nm_no_u.py` | without u: `1030 ≠ 1039`, dyadic pattern destroyed |
| `u ↔ B` alignment | `berry_u_alignment.py` | local BPS `u ∥ B` in core, dilution in tail |
| Hessian K/M | `analysis_three_checks.py` (L=17), `analysis_doubled_box.py` (L=34), `analysis_quad_box.py` (L=68), `extend_profile.py` (full-range profiles) | `K = const`, `M ∝ L` ⇒ u-channel needed for discreteness |
| α-running (radial) | `alpha_running.py` | radial running of the **bare** `α⁻¹(R)` (→ 128) via three independent observables; spatial buildup of core / shell / `Q_H`-closure |

Companion verifications from the parent [electron-mass](../2026-05-electron-mass/) preprint, used here as inputs/baselines:

- [`../../verifications/electron_mass_minimization/`](../../verifications/electron_mass_minimization/) — NM-minimization reproducing `m_e^bare = 446.279 keV`
- [`../../verifications/canonical_derrick/`](../../verifications/canonical_derrick/) — Derrick-stability scan of the canonical configuration

## Relation to the preceding work

Third paper in the Cosserat-vacuum series. It builds on:

- [**SI-reduction**](../2026-05-SI-reduction/) — DOI [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199): the `{ε₀, μ₀, ℏ, G}` basis, the Cosserat functional, and the geometric `g = 1/2`, `α_bare = 1/128`.
- [**electron-mass**](../2026-05-electron-mass/) — DOI [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123): the bare numerical result `m_e^bare = 446.279 keV = 1039 · M₀c²`.
- [**dyadic-closed-forms**](../2026-05-dyadic-closed-forms/) — the dyadic `α`-expansion `128 + 8 + 1 + 1/28`.

This is the **synthesis** paper: it unifies `m_e` and `α` as two projections of one resonant chiral-bag at `μ_c = 2π`, with an explicit physical mechanism (the K/M theorem).

## Citation

- **Zenodo DOI:** *pending*
- **arXiv ID:** *pending*
- **Preceding work DOIs:** [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199) (SI-reduction), [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123) (electron-mass)
