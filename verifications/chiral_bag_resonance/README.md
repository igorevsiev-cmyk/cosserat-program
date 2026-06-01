# Verifications for the chiral-bag-resonance preprint

All five numerical verifications supporting
[**Discrete electron mass and fine-structure constant from a single resonant
Cosserat-hopfion**](../../papers/2026-05-chiral-bag-resonance/) live in this
folder. Flat structure: one shared `stretched_grid.py`, one
`requirements.txt`, one README; scripts and outputs named so that the
test they belong to is obvious from the filename.

## Files at a glance

| Test | Main script | Output (JSON) | Figures | Paper § |
|---|---|---|---|---|
| **1. μ_c-sweep** | `mu_c_sweep.py` | `result_mu_c_sweep.json` | — | §4 |
| **2. u-channel disable** | `nm_no_u.py` | `result_u_channel_disable.json` | — | §4.3 |
| **3. Berry u/B alignment** | `berry_u_alignment.py` | `result_berry_alignment.json` | — | §6.1–6.2 |
| **4. Hessian K/M** | `analysis_three_checks.py` (L=17), `analysis_doubled_box.py` (L=34), `analysis_quad_box.py` (L=68), `extend_profile.py` (radial profiles) | `result_hessian_L17.json`, `result_hessian_L34.json`, `result_hessian_L68.json`, `result_hessian_profiles.json` | `fig_KM_decomposition.png`, `fig_box_scaling.png`, `fig_compare_17_vs_34.png`, `fig_full_range_profiles.png` | §6.5–6.7 |
| **5. α-running radial** | `alpha_running.py` | `result_alpha_running.json` | `fig_alpha_topology_running.png` | §5 |

Plot-only helpers (read the JSONs above, regenerate the figures):
`plot_KM_decomposition.py`, `plot_box_scaling.py`, `plot_doubled_profiles.py`,
`plot_extended.py`, `plot_alpha_topology.py`.

## How to reproduce

```bash
cd verifications/chiral_bag_resonance
pip install -r requirements.txt

# Test 1: μ_c-sweep (~30 min on RTX 2070)
python mu_c_sweep.py

# Test 2: u-channel disable (~6 min)
python nm_no_u.py

# Test 3: Berry u/B alignment (~3 min)
python berry_u_alignment.py

# Test 4: Hessian K/M, three boxes
python analysis_three_checks.py    # L=17  → result_hessian_L17.{json,pt}
python analysis_doubled_box.py     # L=34  → result_hessian_L34.{json,pt}
python analysis_quad_box.py        # L=68  → result_hessian_L68.{json,pt}
python extend_profile.py           # radial profiles → result_hessian_profiles.json
python plot_KM_decomposition.py    # → fig_KM_decomposition.png
python plot_box_scaling.py         # → fig_box_scaling.png
python plot_doubled_profiles.py    # → fig_compare_17_vs_34.png
python plot_extended.py            # → fig_full_range_profiles.png

# Test 5: α-running radial (~6 sec)
python alpha_running.py            # → result_alpha_running.json
python plot_alpha_topology.py      # → fig_alpha_topology_running.png
```

All scripts import the shared Cosserat solver `stretched_grid.py` from
this directory (`sys.path` is set automatically). The hessian box-scan
scripts (`analysis_doubled_box.py`, `analysis_quad_box.py`) additionally
import `analysis_three_checks.py` as a module via `importlib`.

## What each test verifies

1. **`mu_c_sweep.py`** — 7-point scan `μ_c ∈ {π/2, π, 3π/2, 2π, 5π/2, 3π, 4π}`.
   Verifies that the dyadic structure `m_e/M₀ = 2¹⁰+2⁴−1 = 1039` appears
   **only at `μ_c = 2π`**; outside this point the constant in `2¹⁰+2⁴+k`
   drifts `+2 → −1 → −2 → −4 → −6`.

2. **`nm_no_u.py`** — full NM-minimization of `E[n,u]` with the u-channel
   disabled. Result: `m_e = 1030 ≠ 1039` and the dyadic `−1` topological
   correction is gone. Confirms u-channel is necessary for the canonical
   dyadic locking.

3. **`berry_u_alignment.py`** — computes the cosine similarity
   `cos θ(r) = (u·B) / (|u|·|B|)` between the elastic displacement `u`
   and the Berry curvature `B` of the director field. Result:
   `cos θ → 0.99` in the topological core (`r < R_r`), dilution to
   `~0.2` in the tail — empirical signature of local BPS-bound.

4. **`analysis_*.py`** (three boxes `L = 17, 34, 68`) — Hessian K/M
   decomposition. Random modes scale as `ω² ∝ 1/L²` (box-edge phonons),
   `v_shrink` mode as `ω² ∝ 1/L` (bag-anchored with `1/r` tail).
   Extracts stiffness `K = ω²·L ≈ 57` constant within 7% — proves that
   bag-core is rigid but inertia diverges without u-channel screening.

5. **`alpha_running.py`** — radial running of the *bare* effective charge
   `α⁻¹(R)` of the canonical hopfion, measured by three independent
   observables: polynomial inversion of the cumulative mass `m(R)`,
   topological `128/|Q_H(R)|²`, and the Coulomb form factor `128·Φ(∞)/Φ(R)`.
   All three converge to the bare `α⁻¹ = 128` and expose the spatial
   buildup (1024-cell core, 16-cell shell, `Q_H`-closure), each with a
   distinct radial signature. The screened value `α⁻¹(0) = 137.036` and its
   dyadic split `128 + 8 + 1 + 1/28` are the paper's interpretation layered
   on this running (§5), not a direct numerical output of this script.

## Companion verifications (in `../`)

These belong to the parent
[`2026-05-electron-mass`](../../papers/2026-05-electron-mass/) preprint
and are used here as inputs/baselines:

- [`../electron_mass_minimization/`](../electron_mass_minimization/) —
  NM-minimization producing the canonical
  `(R_r, R_z, w) ≈ (0.64082, 0.80729, 0.70200)` and `m_e^bare = 446.279 keV`.
- [`../canonical_derrick/`](../canonical_derrick/) — Derrick-stability scan
  confirming the canonical configuration is a true dilation-stable minimum.
