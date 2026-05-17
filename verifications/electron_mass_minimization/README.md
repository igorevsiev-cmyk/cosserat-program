# Electron-mass Nelder–Mead minimization

This folder provides a self-contained numerical verification that the
canonical Cosserat hopfion is the **energy minimum** of the full
functional `E[n, u]` over the 3-parameter Hopf ansatz `(R_r, R_z, w)`,
using only the three vacuum constants `{ε₀, μ₀, ℏ}` as input.

This is the central numerical claim of the paper
*Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional
minimization* (DOI: [10.5281/zenodo.20205502](https://doi.org/10.5281/zenodo.20205502)).

## What is verified

The full Cosserat functional with parameters fixed by structure:

```
K₁ = K₂ = 2,     K₃ = K₁·(1 + η) = 14.56,    η = 2π
c₄ = 1,                                       μ_c = η = 2π
```

is minimised over the 3-parameter Hopf ansatz `(R_r, R_z, w)` by the
Nelder–Mead simplex method on a `1024 × 2048` stretched cylindrical grid.

The result reproduces the **bare** electron mass:

```
m_e^bare c² = 507.997 keV
```

with no fitted parameters. The physical (CODATA) electron mass
`m_e^phys c² = 510.998950 keV` differs from this by `+3.002 keV`, which is
interpreted in the paper (§7.2) as the standard QED renormalization acting
on both bare parameters of the program (`α_bare = 2⁻⁷ → α(0) = 1/137` and
`m_e^bare → m_e^phys`). A direct derivation of the `δm_e` contribution is
an open direction.

## Expected output (canonical)

| Quantity              | Value                  | Source                |
|-----------------------|------------------------|-----------------------|
| `R_r`                 | 0.51688 (units of `l₀`) | NM optimum            |
| `R_z`                 | 0.76148                 | NM optimum            |
| `w`                   | 0.62580                 | NM optimum            |
| `Q_H`                 | −0.99999                | Topological invariant |
| `E_OF` (Frank–Oseen)  | 180.985 keV (35.6 %)    | Energy decomposition  |
| `E_Sk` (Skyrme)       | 276.932 keV (54.5 %)    | Energy decomposition  |
| `E_u` (Cosserat)      | 50.080 keV  ( 9.9 %)    | Energy decomposition  |
| **`E_total`**         | **507.997 keV**         | Predicted `m_e^bare c²` |
| Gap to CODATA         | **−3.002 keV** (`−0.587 %`) | Interpreted as QED renormalization (paper §7.2) |

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
      m_e^bare = E_total · M₀c² / 1000   [keV]

  All physical constants from CODATA 2018.

## Relation to the Derrick verification

This script verifies that the canonical configuration is the **NM optimum**.
The companion verification at [`../canonical_derrick/`](../canonical_derrick/)
verifies that this same configuration is a **Derrick minimum** under
spatial dilation (i.e. stable against scale collapse or expansion).

Together the two verifications close the logical loop:

1. **Existence**: NM finds a minimum at `(R_r, R_z, w) ≈ (0.517, 0.761, 0.626)`
   with `m_e^bare ≈ 507.997 keV` (this folder).
2. **Stability**: that point is a true minimum under spatial dilation,
   not a saddle (`../canonical_derrick/`).

## Scope of this verification

This artifact verifies that the **3-parameter Hopf ansatz**, when minimised
on the canonical functional, reproduces the **bare** electron mass
`m_e^bare = 507.997 keV` with no fitted parameters. The gap of `3.002 keV`
to the physical (CODATA) value `m_e^phys = 510.999 keV` is interpreted as
the standard QED renormalization (paper §7.2). The verification does not
attempt to derive this gap from within the Cosserat program; that is left
as an open direction.

The 3-parameter ansatz also does not necessarily capture the true global
minimum of `E[n, u]` over the full director field `n: ℝ³ → S²` — higher-
dimensional ansätze (5–8 parameters) may yield slightly different bare
values, but the bare/physical distinction discussed above is the leading
effect (paper §7.1–7.2).
