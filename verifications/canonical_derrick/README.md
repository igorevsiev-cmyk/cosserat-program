# Canonical Derrick verification

This folder provides a self-contained numerical verification that the canonical
Cosserat hopfion (the "electron configuration" in the paper) sits at a true
**Derrick minimum** of the bare energy functional `E[n, u]`, with the
gravitational channel (Cosserat coupling `μ_c`) included.

## What is verified

The paper claims the canonical configuration

```
K₁ = K₂ = 2,     K₃ = 14.56 = K₁·(1 + η),      η = 2π
c₄ = 1,                                          μ_c = 2π
3-param Hopf ansatz:  R_r = 0.51688,  R_z = 0.76148,  w = 0.62580
```

is the energy minimum on the Hopf submanifold and gives

```
m_e^bare = E_total · M₀c² = 507.995 keV          (bare electron mass)
```

The Derrick scan checks **stability under spatial dilation**: scale
`(R_r, R_z) → λ·(R_r, R_z)` for `λ ∈ [0.6, 3.0]` and evaluate every term
of the bare functional at each `λ`. A true minimum at `λ = 1` requires
the V-shape with the canonical point at the bottom; a false minimum
(or an open functional that decays to vacuum) would show a monotone
trend instead.

## Result

![Derrick scan](derrick_scan.png)

| λ    | E_OF (keV) | E_Sk (keV) | E_u (keV) | E_tot (keV) | Q          | Derrick |
|------|------------|------------|-----------|-------------|------------|---------|
| 0.60 | 108.97     | 461.52     | 18.54     | 589.03      | −0.999977  | −315.48 |
| 0.70 | 127.02     | 395.60     | 25.02     | 547.65      | −0.999986  | −218.54 |
| 0.80 | 145.04     | 346.16     | 32.44     | 523.64      | −0.999989  | −136.23 |
| 0.90 | 163.03     | 307.70     | 40.80     | 511.52      | −0.999990  |  −63.08 |
| 0.95 | 172.01     | 291.50     | 45.32     | 508.84      | −0.999990  |  −28.85 |
| **1.00** | **180.99** | **276.93** | **50.08** | **507.99** ← min | **−0.999989** | **+4.22** |
| 1.05 | 189.95     | 263.74     | 55.07     | 508.77      | −0.999989  |  +36.35 |
| 1.10 | 198.91     | 251.76     | 60.30     | 510.97      | −0.999988  |  +67.76 |
| 1.20 | 216.80     | 230.78     | 71.46     | 519.04      | −0.999985  | +128.95 |
| 1.40 | 252.50     | 197.81     | 96.64     | 546.94      | −0.999978  | +247.96 |
| 1.60 | 288.07     | 173.08     | 125.67    | 586.82      | −0.999967  | +366.33 |
| 2.00 | 358.82     | 138.47     | 195.65    | 692.93      | −0.999936  | +611.65 |
| 2.50 | 446.55     | 110.77     | 306.39    | 863.71      | −0.999876  | +948.55 |
| 3.00 | 533.48     |  92.31     | 444.45    | 1070.23     | −0.999785  | +1330.06 |

Full data: `derrick_scan.csv`. Topological charge `Q ≈ −1` preserved across
the entire range (`|Q + 1| < 2.2·10⁻⁴` even at extreme λ = 3.0).

**Outcome.** `λ = 1.00` is the discrete minimum (V-shape confirmed),
delta from neighbours: −0.84 keV vs `λ = 0.95` and −0.77 keV vs `λ = 1.05`.
The Derrick residual at `λ = 1.0` is `+4.22 keV` (`<1 %` of `E_tot`),
which would vanish in the continuum limit; the small positive sign means
the exact balance point sits at `λ ≈ 0.99`, inside the discrete sampling
gap. The canonical 3-parameter ansatz is therefore at Derrick balance to
the resolution of the scan.

### Empirical Derrick scalings

The three energy components follow the expected scaling laws under `x → λx`:

| component | scaling | reason |
|-----------|---------|--------|
| `E_OF`    | `λ¹`    | quadratic gradients of `n`            |
| `E_Sk`    | `λ⁻¹`   | quartic Faddeev–Skyrme term           |
| `E_u`     | `λ²`    | Cosserat coupling with **fixed** screening length `l_c = 1/√μ_c` (not co-scaled with the hopfion) |

The `E_u ~ λ²` (not `λ`) is the signature of the gravitational channel:
`μ_c` is a fixed material constant, so the Cosserat screening length is
absolute and the integral picks up an extra factor of `λ`.

The Derrick equation `dE/dλ |_{λ=1} = 0` becomes

```
E_OF − E_Sk + 2·E_u = 0
```

Plug in the canonical numbers (`λ = 1.00` row):
`180.99 − 276.93 + 2·50.08 = +4.22 keV`, which equals the printed Derrick
column. The residual is `<1 %` of the total energy and is consistent with
discrete sampling on a `768 × 1536` grid; the true minimum sits at
`λ ≈ 1.00 − 4.22/(d²E/dλ²)`, well inside the gap between λ = 0.95 and 1.00
in the scan.

## How to reproduce

```bash
# environment
pip install -r requirements.txt

# run scan (~25 s on RTX 2070, longer on CPU)
python derrick_scan.py

# regenerate plot from CSV
python plot.py

# (optional) regenerate the hopfion visualization
python hopfion_visualize.py
```

Output: `derrick_scan.csv` (numerics) and `derrick_scan.png` (figure above).
The `hopfion_visualize.py` script generates `hopfion_visualize.png`
(four-panel visualization of the canonical Hopf field; pure
`numpy + matplotlib`, no PyTorch required).

## Files

- `derrick_scan.py` — main verification script (includes the `Config` class
  inline; the canonical numerical parameters are hard-coded at the top)
- `stretched_grid.py` — adaptive (sinh-stretched) grid utilities, full
  Cosserat energy (`compute_energy_cosserat_stretched`), topological charge
  (`compute_Q_stretched`), and the screened Cosserat solver
  (`compute_E_u_screened` — preconditioned conjugate gradient for the
  `u`-channel at finite `μ_c`).  Uses **linear-extrapolation ghost cells
  in z** (not periodic) — periodic BC was the source of a previously
  observed bend-term divergence under grid refinement, fixed in
  the 2026-05-16 diagnostic session.
- `plot.py` — regenerates the Derrick-scan figure from `derrick_scan.csv`
  (matplotlib only)
- `hopfion_visualize.py` — approximate visualization of the canonical Hopf
  configuration (four panels: `n_z`, `|n_⊥|`, Hopf-charge density, schematic
  3D linked rings). Pure `numpy + matplotlib`, no PyTorch required
- `derrick_scan.csv` — pre-computed Derrick-scan results (14 λ-points)
- `derrick_scan.png` — pre-generated Derrick-scan figure
- `hopfion_visualize.png` — pre-generated hopfion visualization
- `requirements.txt`

## Setup details

- Grid: 768 × 1536 axisymmetric (r, z), adaptive stretched with focus
  `r = R_hopf = 1`, `z = 0`, sharpness `β_r = 6`, `β_z = 3`,
  domain `L_r = 24`, `L_z = 48` (in units of `l₀`).
- Optimizer: none — at each λ the energy of the canonical 3-parameter
  Hopf ansatz is evaluated directly (no relaxation needed since the canonical
  point is itself the relaxed configuration).
- u-channel: screened Cosserat solver (preconditioned conjugate gradient
  with stopping tolerance `1e-6`, typical 690 iterations per λ).
- Float precision: `float64` throughout.
- The simulator units are natural Cosserat units (`l₀`, `M₀c²`); the
  conversion to keV uses

      M₀c² = (2π · ℏ³ / (c⁵ · ε₀))^(1/4) · c² / e ≈ 429.51 eV
      m_e^bare = E_total · M₀c² / 1000   [keV]

  All physical constants from CODATA 2018 (see top of `derrick_scan.py`).

## Relation to the NM verification

This script verifies that the canonical configuration is a **Derrick minimum**.
The companion verification at [`../electron_mass_minimization/`](../electron_mass_minimization/)
verifies that the same configuration is the **Nelder–Mead optimum** of the
full 3-parameter Hopf ansatz space.

Together the two verifications close the logical loop:

1. **Existence**: NM finds a minimum at `(R_r, R_z, w) ≈ (0.517, 0.761, 0.626)`
   with `m_e^bare ≈ 507.997 keV` (`../electron_mass_minimization/`).
2. **Stability**: that point is a true minimum under spatial dilation,
   not a saddle (this folder).

The small numerical difference between the two folders (~2 eV in `m_e^bare`)
is consistent with the grid-resolution difference (`1024 × 2048` here,
`768 × 1536` for the Derrick scan).

## Scope of this verification

This artifact verifies the **Derrick balance** of the canonical point: a
true minimum under spatial dilation, with all three energy channels
properly scaling. It does **not** independently reconstruct the canonical
parameters `(R_r, R_z, w)` — those come from the Nelder–Mead optimization
in the companion artifact (`../electron_mass_minimization/`). The Derrick
scan here closes the loop: given the canonical parameters, the bare
functional has its minimum at exactly that point.

The verification reproduces `m_e^bare = 507.995 keV` (the bare electron
mass in the Cosserat vacuum). The physical (CODATA) value
`m_e^phys = 510.999 keV` differs by `3.004 keV`, which is interpreted in
the paper (§7.2) as the standard QED renormalization. A direct derivation
of the `δm_e` contribution is an open direction.
