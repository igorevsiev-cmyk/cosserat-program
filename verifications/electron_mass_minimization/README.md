# Electron-mass Nelder–Mead minimization

This folder provides a self-contained numerical verification that the
canonical Cosserat hopfion is the **energy minimum** of the full
functional `E[n, u]` over the 3-parameter Hopf ansatz `(R_r, R_z, w)`,
using only the three vacuum constants `{ε₀, μ₀, ℏ}` as input.

This is the central numerical claim of the paper
*Derivation of the electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional
minimization* (DOI: [10.5281/zenodo.20205502](https://doi.org/10.5281/zenodo.20205502)).

## What is verified

The full Cosserat functional with parameters fixed by structure:

```
K₁ = K₂ = 2,     K₃ = K₁·(1 + η) = 14.56,    η = 2π
c₄ = 1,          m² = η/(4π) = 1/2,           μ_c = η = 2π
```

is minimised over the 3-parameter Hopf ansatz `(R_r, R_z, w)` by the
Nelder–Mead simplex method on a `1024 × 2048` stretched cylindrical grid.

The result reproduces

```
m_e c² = 511.033 keV   (Δ = +0.007 % from CODATA 2018 = 510.998950 keV)
```

with no fitted parameters.

## Expected output (canonical)

| Quantity              | Value                  | Source                |
|-----------------------|------------------------|-----------------------|
| `R_r`                 | 0.50945 (units of `l₀`) | NM optimum            |
| `R_z`                 | 0.75010                 | NM optimum            |
| `w`                   | 0.62585                 | NM optimum            |
| `Q_H`                 | −0.999998               | Topological invariant |
| `E_OF` (Frank–Oseen)  | 178.93 keV  (35.0 %)    | Energy decomposition  |
| `E_Sk` (Skyrme)       | 281.03 keV  (55.0 %)    | Energy decomposition  |
| `E_u` (Cosserat)      | 48.68 keV   ( 9.5 %)    | Energy decomposition  |
| `E_mass` (anisotropy) | 2.40 keV    ( 0.5 %)    | Energy decomposition  |
| **`E_total`**         | **511.03 keV**          | Predicted `m_e c²`    |
| Deviation from CODATA | **+0.007 %** (= +34 eV) |                       |

The Skyrme term carries the **largest** share of the energy (55 %), reflecting
the standard Derrick balance for three-dimensional solitons (`E_OF ∝ λ`,
`E_Sk ∝ λ⁻¹` under uniform rescaling).

The complete result is written to `result.json` after a successful run.

## How to reproduce

```bash
# environment
pip install -r requirements.txt

# run the minimization (~ 10 minutes on RTX 2070, considerably longer on CPU)
python nm_minimization.py
```

Output: `result.json` (parameters, energy decomposition, comparison with CODATA).

The script logs intermediate progress every five Nelder–Mead evaluations.
A typical run from the generic initial guess `(0.50, 0.70, 0.60)`
converges in ~ 100–200 simplex iterations.

## Files

- `nm_minimization.py` — main minimization script (all physics + NM driver
  in a single file, so the verification is self-contained)
- `stretched_grid.py` — adaptive (sinh-stretched) grid utilities, full
  Cosserat energy (`compute_energy_cosserat_stretched`), topological charge
  (`compute_Q_stretched`), and the screened Cosserat solver
  (`compute_E_u_screened`). **Identical** to the file in
  `../canonical_derrick/` (intentionally duplicated so each verification
  folder is self-contained; do not edit one without updating the other).
- `requirements.txt` — Python dependencies (`torch`, `numpy`, `scipy`)
- `result.json` — output of a successful run (created by the script)

## Setup details

- Grid: 1024 × 2048 axisymmetric (r, z), adaptive stretched with focus
  `r = 1`, `z = 0`, sharpness `β_r = 6`, `β_z = 3`,
  domain `L_r = 24`, `L_z = 48` (in units of `l₀`).
- Optimizer: `scipy.optimize.minimize(method='Nelder-Mead', adaptive=True)`.
- u-channel: screened Cosserat solver (preconditioned conjugate gradient
  with stopping tolerance `1e-6`, typical 690 iterations per energy
  evaluation; this dominates the wall time).
- Float precision: `float64` throughout.
- Topological charge enforced exactly by ansatz (`Q_H = −1` for the
  electron orientation, `+1` for positron — both degenerate by `n → −n`).
- Energy converted to keV via

      M₀c² = (2π · ℏ³ / (c⁵ · ε₀))^(1/4) · c² / e ≈ 429.51 eV
      m_e  = E_total · M₀c² / 1000   [keV]

  All physical constants from CODATA 2018.

## Relation to the Derrick verification

This script verifies that the canonical configuration is the **NM optimum**.
The companion verification at [`../canonical_derrick/`](../canonical_derrick/)
verifies that this same configuration is a **Derrick minimum** under
spatial dilation (i.e. stable against scale collapse or expansion).

Together the two verifications close the logical loop:

1. **Existence**: NM finds a minimum at `(R_r, R_z, w) ≈ (0.509, 0.750, 0.626)`
   with `m_e ≈ 511.033 keV` (this folder).
2. **Stability**: that point is a true minimum under spatial dilation,
   not a saddle (`../canonical_derrick/`).

A small numerical difference between the two folders is expected and
documented:

| Folder                           | Grid          | `m_e` predicted | Deviation from CODATA |
|----------------------------------|---------------|-----------------|-----------------------|
| `electron_mass_minimization`     | 1024 × 2048   | 511.033 keV     | +0.007 %              |
| `canonical_derrick`              | 768 × 1536    | 510.93 keV      | +0.014 %              |

Both are within the paper's claimed precision; the higher-resolution
result is the one quoted in the paper.

## Scope of this verification

This artifact verifies that the **3-parameter Hopf ansatz**, when minimised
on the canonical functional, reproduces the experimental electron mass to
`~ 10⁻⁴` precision with no fitted parameters. It does **not** verify that
the 3-parameter ansatz captures the true global minimum of `E[n, u]` over
the full director field `n: ℝ³ → S²` — higher-dimensional ansätze
(5–8 parameters) yield slightly lower energies, with the deviation from
CODATA decreasing accordingly (paper §7.1).
