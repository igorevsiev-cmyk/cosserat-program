# Electron-mass Nelder–Mead minimization

This folder provides a self-contained numerical verification that the
canonical Cosserat hopfion is the **energy minimum** of the full
functional `E[n, u]` over the 3-parameter Hopf ansatz `(R_r, R_z, w)`,
using only the three vacuum constants `{ε₀, μ₀, ℏ}` as input.

This is the central numerical claim of the paper
*Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional
minimization* (DOI: [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123)).

## What is verified

The full Cosserat functional with parameters fixed by structure:

```
K₁ = K₂ = 2,     K₃ = K₁·(1 + η) = 14.56,    η = 2π
c₄ = 1,                                       μ_c = η = 2π
```

is minimised over the 3-parameter Hopf ansatz `(R_r, R_z, w)` by the
Nelder–Mead simplex method on a `1024 × 2048` stretched cylindrical grid,
on the **dyadic box** `L_r × L_z = 17 × 33` (in units of `l₀`).

The result is the **bare** electron mass:

```
m_e^bare c² = 446.279 keV
```

with no fitted parameters. This bare value is **not** compared with the
physical (CODATA) electron mass — it is the output of the bare functional
as such. The NM optimum reproduces the **dyadic closed form**

```
m_e^bare c² = (2¹⁰ + 2⁴ − 1) · M₀c² = 1039 · M₀c² = 446.258 keV
```

to which the minimisation agrees to `+0.0049 %` (`+21.7 eV`).

## Expected output (canonical)

| Quantity              | Value                  | Source                |
|-----------------------|------------------------|-----------------------|
| `R_r`                 | 0.64082 (units of `l₀`) | NM optimum            |
| `R_z`                 | 0.80729                 | NM optimum            |
| `w`                   | 0.70200                 | NM optimum            |
| `Q_H`                 | −0.99996                | Topological invariant |
| `E_OF` (Frank–Oseen)  | 221.888 keV (49.7 %)    | Energy decomposition  |
| `E_Sk` (Skyrme)       | 220.634 keV (49.4 %)    | Energy decomposition  |
| `E_u` (Cosserat)      | 3.758 keV  ( 0.8 %)     | Energy decomposition  |
| **`E_total`**         | **446.279 keV**         | Predicted `m_e^bare c²` |
| Dyadic closed form    | `(2¹⁰+2⁴−1)·M₀c²` = **446.258 keV** | NM agrees to `+0.0049 %` |

On the dyadic box the Frank–Oseen and Skyrme terms carry almost equal
shares (`≈ 49.7 %` and `≈ 49.4 %`), and the screened Cosserat coupling
contributes the remaining `≈ 0.8 %`.

The complete result is written to `result.json` after a successful run.

## How to reproduce

```bash
# environment
pip install -r requirements.txt

# run the minimization (~ 6 minutes on RTX 2070, considerably longer on CPU)
python nm_minimization.py
```

Output: `result.json` (parameters, energy decomposition, dyadic closed form).

The script logs intermediate progress every five Nelder–Mead evaluations.
A typical run from the generic initial guess `(0.50, 0.70, 0.60)`
converges in ~ 90–100 simplex iterations (172 function evaluations).

## Files

- `nm_minimization.py` — main minimization script (all physics + NM driver
  in a single file, so the verification is self-contained)
- `stretched_grid.py` — adaptive (sinh-stretched) grid utilities, full
  Cosserat energy (`compute_energy_cosserat_stretched`), topological charge
  (`compute_Q_stretched`), and the screened Cosserat solver
  (`compute_E_u_screened`, Robin BC). **Identical** to the file in
  `../canonical_derrick/` (intentionally duplicated so each verification
  folder is self-contained; do not edit one without updating the other).
- `requirements.txt` — Python dependencies (`torch`, `numpy`, `scipy`)
- `result.json` — output of a successful run (created by the script)

## Setup details

- Grid: 1024 × 2048 axisymmetric (r, z), adaptive stretched with focus
  `r = 1`, `z = 0`, sharpness `β_r = 6`, `β_z = 3`,
  dyadic box `L_r = 17`, `L_z = 33` (in units of `l₀`;
  `L_r = log₂(2⁷·2¹⁰) = 17`, `L_z = 2·L_r − 1 = 33`).
- Optimizer: `scipy.optimize.minimize(method='Nelder-Mead', adaptive=True)`.
- u-channel: screened Cosserat solver (preconditioned conjugate gradient
  with Robin boundary condition, stopping tolerance `1e-8`, ~ 900 PCG
  iterations per energy evaluation; this dominates the wall time).
- Float precision: `float64` throughout.
- Topological charge enforced exactly by ansatz (`Q_H = −1` for the
  electron orientation, `+1` for positron — both degenerate by `n → −n`).
- Energy converted to keV via

      M₀c² = (2π · ℏ³ / (c⁵ · ε₀))^(1/4) · c² / e ≈ 429.51 eV
      m_e^bare = E_total · M₀c² / 1000   [keV]

  All physical constants from CODATA 2018.

## Relation to the Derrick verification

This script verifies that the canonical configuration is the **NM optimum**.
The companion verification at [`../canonical_derrick/`](../canonical_derrick/)
verifies that this same configuration is a **Derrick minimum** under
spatial dilation (i.e. stable against scale collapse or expansion).

Together the two verifications close the logical loop:

1. **Existence**: NM finds a minimum at `(R_r, R_z, w) ≈ (0.641, 0.807, 0.702)`
   with `m_e^bare ≈ 446.279 keV` (this folder).
2. **Stability**: that point is a true minimum under spatial dilation,
   not a saddle (`../canonical_derrick/`).

## Scope of this verification

This artifact verifies that the **3-parameter Hopf ansatz**, when minimised
on the canonical bare functional (`m² = 0`) over the dyadic box, reproduces
the **bare** electron mass `m_e^bare = 446.279 keV` with no fitted
parameters, and that this value matches the dyadic closed form
`(2¹⁰ + 2⁴ − 1)·M₀c²` to `0.005 %`.

This is a **bare** result: it is the output of the bare functional and is
deliberately not compared with the physical (dressed) electron mass.

The 3-parameter ansatz also does not necessarily capture the true global
minimum of `E[n, u]` over the full director field `n: ℝ³ → S²` — higher-
dimensional ansätze (5–8 parameters) and full-field relaxations may yield
slightly different bare values.
