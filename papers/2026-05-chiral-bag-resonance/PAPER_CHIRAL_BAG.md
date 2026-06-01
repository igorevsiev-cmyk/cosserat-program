# Discrete electron mass and the fine-structure constant from a Cosserat-hopfion resonance

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-05-31
**Version:** 1
**Type:** preprint
**License:** CC-BY 4.0

---

## Abstract

The electron mass `m_e` and the fine-structure constant `α` are independent empirical parameters in the Standard Model; no derivation of both quantities from a single structure exists. The present work shows that in the parameter-free Cosserat functional `E[n, u]` — all constants fixed by the triple `{ε₀, μ₀, ℏ}` through the structural identities of the preceding works [1, 2] — at the canonical Cosserat coupling `μ_c = η = 2π` (a topological invariant of the target sphere `S²` of the director field) the topological Hopf soliton with `Q_H = −1` **simultaneously** realizes two dyadic quantities:

> `m_e^bare / M_0 c² = 2¹⁰ + 2⁴ − 1 = 1039`  (446.279 keV; at the observed `α = 1/137`, through the polynomial of §3.2, this gives 511 keV, deviation from CODATA `Δ = 0.01%`)
>
> `α⁻¹(0) = 128 + 8 + 1 + 1/28 = 3837/28 ≈ 137.036`  (Δ from CODATA `137.035999` — 0.0002%)

Four numerical verifications — a μ_c-sweep, a u-channel disable, a BPS `u ↔ B` alignment, and a Hessian box-scan — isolate a **chiral-bag** structure: a topological BPS core (`r < R_r ≈ 0.64 l_0`) + an elastic shell + a discrete boundary spectrum (a bosonic analog of the Atiyah–Patodi–Singer η-invariant). Spectral analysis at three box sizes (`L = 17, 34, 68 l_0`) leads to a **K/M theorem**: in the pure Faddeev–Skyrme theory the bag-core stiffness is positive and constant (`K ≈ 57 ± 3%`), but the inertia of perturbations diverges (`M ∝ L`) because of the massless `1/r` tail of the OF field; the short range of the u-channel, through the tensor coupling `(∇×u − Π(n))²`, cuts off the inertia and makes a discrete spectrum `ω² = K/M > 0` mathematically possible. Thus the **u-channel is a structural necessity**, not an add-on to the Faddeev–Skyrme model.

---

## Logical chain

```
INPUTS (postulates of the preceding works)
 {ε₀, μ₀, ℏ}  →  l_0⁴ = ε₀ℏc/(2π),  M_0 c² = ℏc/l_0           [1, §7]
 α_bare = π·(l_0/2)² / (4πε₀ℏc) = 2⁻⁷ = 1/128                   [1, §7.4]
 m_e^bare = 446.279 keV = 1039 · M_0 c² (NM minimization)       [2, §6]
 │
 ▼
THIS WORK: one resonance — two dyadics
 (1) μ_c-sweep over {π/2 ... 4π}      →  locking at 1039 only at μ_c = 2π
 (2) u-channel disable                →  m_e drops to 1030, dyadic breaks
 (3) BPS alignment u || B             →  cos θ → 0.99 in core, 0.2 in tail
 (4) Hessian box-scan {17, 34, 68}    →  K = const, M ∝ L  ⇒  u needed for discreteness
 │
 ▼
INTERPRETATION
 chiral bag (Brown–Rho-like architecture)
 α⁻¹ = 128 + 8 + 1 + 1/28               radial assembly (bare → screened)
 m_e: the same curve x² + x/2 − 1        bare point (1039) — prediction of this work
 │
 ▼
OPEN PROBLEMS
 Analytic BPS bound · |Q| = 2 · Hessian with u included · proton, muon
```

---

## 1. Introduction

### 1.1. Context

The Standard Model contains 19 free parameters; among them the electron mass `m_e` and the fine-structure constant `α` are the two most basic, yet independently fixed from experiment. The historical program of deriving them — Eddington 1924 [3], Wyler 1969 [4], Atiyah 2018 [5] — either relied on numerical coincidences or provided no operational mechanism. The open question remains: can **both** quantities be obtained from a single physical structure?

### 1.2. The Cosserat program

In [1] a reduction of SI to a single dimension was proposed on the basis of the **Cosserat continuum** (a micropolar elastic medium): four identifications `ρ ≡ μ₀`, `G_shear ≡ 1/ε₀`, `ℏ` (the quantum of microrotation) and `G` through Kleinert's mechanism lead to a single medium in which the electromagnetic and gravitational sectors are channels of one functional. The structural length of the vacuum:

```
l_0⁴ = ε₀ℏc / (2π),   l_0 ≈ 4.5943 Å,   M_0 c² = ℏc/l_0 ≈ 429.5068 eV
```

The director field `n: ℝ³ → S²` carries the topological Hopf invariant `Q_H ∈ π₃(S²) = ℤ`. The configuration with `Q_H = −1` — the simplest knotted soliton (Faddeev hopfion [6]) — is identified with the electron.

**Already established** [1, §7.4]: `α_bare = 1/128 = 2⁻⁷` from the geometric interpretation of the charge as the **cross-sectional** area of the Hopf knot, `e = π·(l_0/2)²` (a near-circular cross-section shape, postulate P5).

In [2], a direct Nelder–Mead minimization of the functional `E[n, u]` over a 3-parameter Hopf ansatz yielded the **bare** electron mass:

```
m_e^bare c² = 446.279 keV = 1039.05 · M_0 c²
```

on the dyadic box `L = 17 × 33 l_0`. The dimensionless value `1039 = 2¹⁰ + 2⁴ − 1` is a dyadic decomposition with an independent physical meaning for each term (§3.3).

### 1.3. Claim of the present work

The present work shows that at the canonical Cosserat coupling `μ_c = η = 2π` the functional `E[n, u]` **simultaneously** realizes:

1. the dyadic value `m_e/M_0 = 2¹⁰ + 2⁴ − 1` (through direct NM minimization);
2. the dyadic decomposition `α⁻¹ = 128 + 8 + 1 + 1/28` (through a radial assembly from the canonical geometry).

Both quantities follow from **one** canonical configuration, not fixed independently. The mechanism is identified as a **chiral bag** (topological core + elastic shell + discrete boundary spectrum) and is confirmed by four numerical verifications, the central one being the Hessian box-scan, which yields the K/M theorem on the mathematical necessity of the u-channel.

---

## 2. Model and the canonical hopfion

### 2.1. The functional `E[n, u]`

The energy is split into three physical channels:

```
E[n, u]  =  E_OF[n]  +  E_Sk[n]  +  E_u[u]  +  E_int[n, u]                  (2.1)
```

**(1) Oseen–Frank** [7, 8] — the standard quadratic functional:
```
E_OF = ½ ∫ [K₁ (∇·n)² + K₂ (n·∇×n)² + K₃ (n×∇×n)²] dV                       (2.2)
```
with the constants of splay (`K₁`), twist (`K₂`), and bend (`K₃`).

**(2) The Skyrme stabilizer** of 4th order [9, 10] — the only way to ensure Derrick stability in 3D:
```
E_Sk = ∫ (c₄/4) F_ij F^ij dV ,    F_ij = n·(∂_i n × ∂_j n)                  (2.3)
```
where `F_ij` is the antisymmetric 2-tensor of the Hopf–Whitehead density, `F_ij F^ij = 2·Σ_{i<j} [n·(∂_i n × ∂_j n)]²`.

**(3) The Cosserat u-channel** [2, §2.3–§2.4]:
```
E_u[u]      = ∫ [(μ/2) (∂u)² + (μ_c/2) u²] dV                                (2.4)
E_int[n,u]  = ½ μ_c ∫ |∇×u − Π(n)|² dV                                       (2.5)
```
where `μ ≡ 1` is the base elastic modulus and `Π(n)` is the vector "spin current" of the director (an analog of the Mermin–Ho relation in superfluid ³He-A [11]). The mass term `(μ_c/2) u²` leads to a **Yukawa screening** of the translational field `u` with length `l_c = 1/√μ_c ≈ 0.399 l_0`.

In the axisymmetric limit with `u = ∇×(ψ·φ̂)`, `u_φ = 0`, and `Π(n) = f(n)·φ̂` (where `f(n) = atan2(√(n₁²+n₂²), n_z)` is the polar angle), the vector Euler–Lagrange equation reduces to a **screened scalar Poisson** equation [2, §5.5]:

```
( ∂²_r + (1/r) ∂_r − 1/r² + ∂²_z − μ_c ) ψ  =  −2 f(n)                       (2.6)
```

This is **not a simplifying approximation**, but an equivalent form of (2.4)–(2.5) in the class of axisymmetric configurations; it is precisely this form that is implemented in the numerical verifications (§7.3).

### 2.2. Fixed constants

All five parameters of the functional are fixed by the identities of the preceding works:

| Constant | Value | Source |
|---|---|---|
| `K₁ = K₂` | `2` | isotropy of splay/twist |
| `K₃ = K₁·(1 + η)` | `2·(1 + 2π) ≈ 14.566` | bend anisotropy; [2, §3.4] |
| `c₄` | `1` | choice of length unit, `L_Skyrme = √(c₄/c₂) ≡ l_0` |
| `μ_c = η` | `2π` | Cosserat coupling of microrotations, [1, §7.4] |

> The numerical verifications (as in [2]) use the truncated value `K₃ = 14.56` instead of `14.566`; the effect on `m_e^bare` is `< 0.1 %`.

The dimensionless coefficient `η = 2π` is a **topological invariant of the target sphere `S²`** of the director field; it is the same factor that fixes the structural identity `l_0⁴ = ε₀ℏc/(2π)` [1, §7.4].

### 2.3. The Hopf ansatz `Q_H = −1`

The 3-parameter Faddeev–Whitehead ansatz (`R_r, R_z, w`):

```
n₁ = 8 r z w / P
n₂ = -4 r Y w / P                                                            (2.7)
n₃ = (D - 4 r² w²) / P

where Y = (r/R_r)² + (z/R_z)² - 1,  D = 4(z/R_z)² + Y²,  P = D + 4(r/R_r)² w².
```

The ansatz carries `|Q_H| = 1` for any positive `(R_r, R_z, w)` and reduces to `n_z = 1` at infinity.

NM minimization on a `1024 × 2048` grid (dyadic box `17 × 33 l_0`) gives the canonical optimum [2, §5]:

```
(R_r, R_z, w) = (0.64082, 0.80729, 0.70200)                                  (2.8)
m_e^bare c² = 446.279 keV,    Q_H = −0.99996  (|Q_H| = 1 to ~4·10⁻⁵)
```

### 2.4. The geometric parameter `g = 1/2`

**Derrick's theorem** [12] in the 3D σ-model forbids localized stable configurations with terms of only 2nd order in gradients; the 4th-order Skyrme addition makes the balance possible:

```
∂E/∂λ |_{λ=1} = 0   ⇒   L_Skyrme = √(c₄/c₂) = l_0                            (2.9)
```

For the hopfion configuration with `Q_H = −1` the radius of the minimal vortex tube [1, §7.3, (7.5)]:

```
r_v = L_Skyrme / 2 = l_0 / 2                                                 (2.10)
```

**Corollary:** `g ≡ r_v/l_0 = 1/2` is the fundamental dyadic constant of the Hopf-knot geometry. Through it:
- `α_bare = g⁷ = 1/128` (cross-sectional area, P5);
- the leading term `m_e^bare/M_0 ≈ α⁻²/16 = α⁻²·g⁴ = g⁻¹⁰ = 1024` (`∝ α⁻²`; see the polynomial of §3.2).

![Fig. 1. Canonical hopfion Q_H = -1 at (R_r, R_z, w) = (0.6408, 0.8073, 0.7020): 2D slices n_z(r,z), |n_⊥|(r,z), topological density ρ_Q, 3D visualization of the torus. Reproduced by `verifications/canonical_derrick/hopfion_visualize.py`.](../../verifications/canonical_derrick/hopfion_visualize.png)

---

## 3. Dyadic discreteness of the mass

### 3.1. Main numerical result

The full NM minimization of the functional over the 3-parameter ansatz (2.7) gives [2, §6]:

```
E_OF  = 221.888 keV  (49.7 %)
E_Sk  = 220.634 keV  (49.4 %)                                                (3.1)
E_u   =   3.758 keV  ( 0.8 %)
─────────────────────────────────
m_e^bare = 446.279 keV
```

In units of the base medium cell `M_0 c² = 429.5068 eV`:

```
m_e^bare / M_0 c² = 1039.05 ≈ 1039 = 2¹⁰ + 2⁴ − 1                            (3.2)
```

Deviation from the integer value: `5·10⁻⁵` (`0.005 %`). The number `1039` is a direct output of NM minimization with no free parameters; locking onto this dyadic value occurs only at `μ_c = 2π` (see §4).

> **Status of the result** [2, §7.4]. This is a **topologically protected upper bound** for the energy of the true continuum minimum: the 3-param ansatz acts as an analytic regulator that cuts off the non-physical lattice modes of collapse (a full-field relaxation without the ansatz gives `~422 keV` due to sub-grid contraction `R_ring → 0` — a discretization artifact). The existence of a continuum minimizer of the Faddeev–Skyrme functional is guaranteed by the Lin–Yang theorem [13]; the rigid ansatz as a UV regulator is a standard device [8].

### 3.2. Unifying polynomial

**Numerical observation** [2, §7.2]: the dimensionless minimum fits the form

```
m_e/M_0 = x² + x/2 − 1 ,   x = α⁻¹/4                                         (3.3)
```

on two points of one curve:

| regime | α⁻¹ | x | m_e/M_0 | m_e c² | comparison |
|---|---|---|---|---|---|
| bare | 128 | 32 | `1024 + 16 − 1 = 1039` | 446.28 keV | direct functional output |
| observed | 137.036 | 34.259 | `1173.7 + 17.1 − 1 = 1189.8` | 511.0 keV | CODATA 510.999; Δ = 0.01 % |

The polynomial is given as a numerical observation, not as a derivation from the functional — obtaining it directly is an open problem. The non-randomness of the form is supported by the fact that the coefficients `1/16 = g⁴`, `1/8 = g³` belong to the same dyadic series as `α_bare = g⁷` and `r_v = g·l_0`.

**g-notation.** In terms of the base parameter `g ≡ r_v/l_0 = 1/2` (§2.4) the polynomial is identically rewritten:

```
m_e/M_0 = g⁻¹⁰ + g⁻⁴ − 1                                                     (3.4)
```

since `x = α⁻¹/4 = g⁻⁷ · g² = g⁻⁵`. This is not a separate derivation but a statement that all elements of the formula are expressed through the single geometric constant `g = 1/2`. The exponents `(10, 4, 0)` are still empirical; their direct derivation from the leading integrals of the functional is an open problem (see also §5.2).

> **Remark on scale.** The polynomial (3.3)–(3.4) is established for the **vacuum** point on the hyperbola `m·l = ℏ/c`, as a direct consequence of the vacuum constants `{ε₀, μ₀, ℏ}` through the structural identities (`l_0⁴ = ε₀ℏc/(2π)`, `M_0 = ℏ/(l_0 c)`, `α_bare = π(l_0/2)²/(4πε_0ℏc) = 1/128`; see [1, §7]). The cell mass `M_0 ≈ 429.5 eV` and the cell length `l_0 ≈ 4.59 Å` are global constants of the **vacuum**. This is a **special case**, not a universal dependence for the electron in any state.
>
> **Consistency condition.** Identity (3.3) holds precisely because **at the vacuum point of the hyperbola one cell of medium mass (`M_0`) is identically equal to one unit of model (dimensionless) energy** — this is the boundary case of the "vacuum" knot, where both quantities (`α_bare = 1/128` and `M_0`) are derived from the same constants `{ε₀, μ₀, ℏ}`. At other points of the hyperbola (the Compton limit `m_0_local = m_e`, `l_local = ƛ_C`, where "knot = one cell"; intermediate atomic scales with `l_local ≠ l_0`) this equality breaks: one cell of medium ≠ one dimensionless unit, and **identity (3.3) for the electron no longer holds** in the same form. Numerical and analytic analysis of this spectrum is an open direction (§8.3).

### 3.3. Spatial decomposition

Radial integration of the mass density of the canonical hopfion over a spherical radius `R` gives three clearly separated contributions:

| Term | Where | Interpretation |
|---|---|---|
| `2¹⁰ = 1024` | `R ≤ 7.5 l_0` | BPS core (plateau in `m(R)`) |
| `+2⁴ = 16` | `7.5 < R ≤ 17 l_0` | mass shell around the core |
| `−1` | whole volume | topological contribution `Q_H = −1` (see §6.3 on the link with the boundary spectrum) |

The box size `L_box = 17 = 2⁴ + 1` is the minimal one containing the entire shell.

![Fig. 2. Two measured radial profiles of the canonical hopfion: (a) topological-charge closure |Q_H(R)| — 99.9% at R ≈ 6.6 l_0 = log₂128; (b) cumulative mass m(R) — a plateau at m = 1024 = 2¹⁰ (BPS core, R ≈ 7.5 l_0), the full m = 1039 = 2¹⁰+2⁴−1 near the box diagonal R_diag ≈ 23.7 l_0. The dyadic assembly α⁻¹ = 128+8+1+1/28 is algebraic (§5), not a radial curve: the topological core g⁷=128 is dressed by 9=8+1 screening cells (center + shell, §5.1). Reproduced by `verifications/chiral_bag_resonance/alpha_running.py` + `plot_alpha_topology.py`.](../../verifications/chiral_bag_resonance/fig_alpha_topology_running.png)

### 3.4. Box size `L_r × L_z = 17 × 33 l_0`

The box size is **dyadic** [2, §5.1] — it holds the mass shell around the BPS core:

```
L_r = 2⁴ + 1 = 17 l_0          — 16 mass-shell cells + 1 central cell
L_z = 2⁵ + 1 = 2·L_r − 1 = 33 l_0   — 16 cells on each side of z + center    (3.5)
```

(`r` is the radial coordinate from the symmetry axis, one-sided; `z` is the axial coordinate, two-sided through the knot center, hence twice as long.) The box fully contains the localized core `2¹⁰` + shell `2⁴`; the long-range tails of `n` do not extend beyond it and fix what is meant by the **bare** value `m_e^bare`.

**Stability with size.** Extension to `L = 34, 68` gives a weak UV drift of `m_e^bare` by `~0.5 %` (`1044, 1046`) from the `1/r` tail of the OF field; `m_e^bare ≈ 446 keV` independently of the box. The observed value `511 keV` is not the limit of `m_e^bare` under extension, but a different quantity (through the polynomial (3.3) at the screened `α = 1/137`, see §5).

---

## 4. The `μ_c = 2π` resonance

### 4.1. The μ_c sweep

A full NM minimization of (R_r, R_z, w) was performed over a grid of seven values `μ_c ∈ {π/2, π, 3π/2, 2π, 5π/2, 3π, 4π}`. For each point we recorded: the energies (`E_OF, E_Sk, E_u`), the geometry, the dyadic representation, and the Derrick balance `E_OF/(E_OF + E_Sk)`.

```
 μ_c/π    Ẽ_min     R_r     OF/Sk     Best dyadic          Δ_dyadic
 0.50    1062.91   0.620    0.484     2¹⁰ + 2⁵ + 2 = 1058    4.91
 1.00    1048.14   0.634    0.495     2¹⁰ + 2⁵ − 2 = 1054    5.86
 1.50    1042.23   0.639    0.499     2¹⁰ + 2⁴ + 2 = 1042    0.23
 2.00    1039.05   0.641    0.501     2¹⁰ + 2⁴ − 1 = 1039    0.05     ⭐
 2.50    1037.08   0.642    0.503     2¹⁰ + 2⁴ − 2 = 1038    0.92
 3.00    1035.76   0.643    0.503     2¹⁰ + 2⁴ − 4 = 1036    0.24
 4.00    1034.11   0.644    0.504     2¹⁰ + 2⁴ − 6 = 1034    0.11
```

### 4.2. Simultaneous locking by four criteria

`Δ_dyadic ≡ |Ẽ_min − nearest clean dyadic compound|`. The pattern `2¹⁰ + 2⁴ ± k` is stable at `μ_c ≥ 1.5π` (`Δ < 1.0`); below it breaks down. **Only at `μ_c = 2π`** do four criteria fire simultaneously:

1. Minimum `Δ_dyadic = 0.05` (deviation `< 5·10⁻⁵`);
2. Exact `Q_H = −1` (at the level of `4·10⁻⁵`);
3. Ideal Derrick OF/Sk = 0.501;
4. Canonical `R_r = 0.641`.

The constant in `2¹⁰ + 2⁴ + k` drifts `+2 → −1 → −2 → −4 → −6` along the scan — the value "`−1`" locks strictly at the resonance point.

> **Fig. 3 (data).** μ_c-scan: `Δ_dyadic(μ_c)` with a clear minimum at `μ_c = 2π` — the numerical values are given in the table of §4.1. Data: `verifications/chiral_bag_resonance/result_mu_c_sweep.json`; computation: `mu_c_sweep.py`. A separate figure is in preparation.

### 4.3. Disabling the u-channel

A control computation with the u-channel forced to zero (`E_u ≡ 0` in (2.1)):

```
m_e (without u) = 442.51 keV = 1030.30 cells = 2¹⁰ + 2² + 2¹                 (4.1)
```

The canonical pattern `2¹⁰ + 2⁴ − 1` **breaks down**: the `+2⁴` shell does not form, it is replaced by the compound `+2² + 2¹`, and the topological term `−1` disappears. The delta

```
ΔE_u = m_e(with u) − m_e(without u) = 446.279 − 442.51 = 3.77 keV ≈ 9 cells   (4.2)
```

— is exactly what is needed to complete `1030 → 1039 = 2¹⁰ + 2⁴ − 1`. The specific dyadic arises **only with the u-channel on**, consistent with the theorem of §6.7 on its mathematical necessity.

---

## 5. Simultaneous prediction of `α`

### 5.1. Structure of α⁻¹

```
α⁻¹(0) = 128 + 8 + 1 + 1/28 = 3837/28 ≈ 137.0357                             (5.1)
```

Five-significant-figure accuracy against CODATA `137.035999`; the experimental value of `α` is not used in the derivation.

**Physical meaning of each term.** `128 = g⁷` is the bare BPS core (topology; cross-sectional area `e = π(l_0/2)²`) and is **not counted** among the screening cells. Screening adds `137 − 128 = 9 = 1001₂` cells, dyadically `2³ + 2⁰`:

- `+1 = α·128` (`2⁰`) — point-like EM self-screening, the **center** (`log₂1 = 0`);
- `+8 = g⁴·128` (`2³`) — the dimensional elastic response of the medium (`g⁴ ∝ R_r⁴`), the **shell** around the core.

The outward order `128 → 129 → 137` (center → shell) matches the direction of the running; the larger contribution `+8 > +1` belongs to the outer shell with its larger volume. This mirrors the mass: the central cell `2⁰` enters with a `+` for screening (`+α·128`) and a `−` for the mass (`−1 = Q_H` — the topological defect removes a cell, §3.2).

| Term | Dyadic | Origin |
|---|---|---|
| `128` | `2⁷ = g⁷` | bare BPS core (cross-sectional area `e = π(l_0/2)²`); not counted in the screening |
| `+1` | `2⁰ = α·128` | central screening cell: point-like EM self-screening (`log₂1 = 0`) |
| `+8` | `2³ = g⁴·128` | screening shell: dimensional elastic response of the medium (`g⁴ ∝ R_r⁴`) |
| `+1/28` | — | log tail of the massless OF field beyond the dyadic box (`r > L_box`) |

The result `128 → 137.036` is an effect of **partial screening through the medium**: the topological core `g⁷ = 128` is dressed by `9 = 8 + 1` screening cells (center + shell), not a property of the charge by itself. The decomposition `128+8+1+1/28` is **algebraic**; we draw no radial `α⁻¹(R)` curve and do not pin the radius of `+8` — the dimensional reading (`g⁴ ∝ R_r⁴`) places it in the shell, the holographic one (`log₂8 = 3`) places it inside, the two rulers disagree (only the central `+1`, `log₂1 = 0`, is pinned).

**Link to the elasticity of the medium.** The shell physically resists the propagation of the perturbation (the charge area) — this is precisely the elastic response of the same medium that in the K/M theorem of §6.7 gives `K ≈ 57`. Therefore the screening of `α` and the K/M theorem are two manifestations of one stiffness of the vacuum Cosserat medium.

> The measured radial profiles — the charge closure `|Q_H(R)|` (99.9% at R ≈ 6.6–7 = log₂128) and the mass-shell accumulation `m(R)` — are shown in Fig. 2 (panels a, b, §3.3). The dyadic assembly `α⁻¹ = 128+8+1+1/28` remains algebraic; we do not draw a radial `α⁻¹(R)` curve. The `9 = 8 + 1` screening cells are split into a center (`+1 = α·128`) and a shell (`+8 = g⁴·128`) around the bare `g⁷` core; their exact radial placement is interpretation, not a measured curve.

### 5.2. `m_e` and `α` as two projections of one hopfion

Both formulas follow from the canonical knot with common structural elements: `g = 1/2` (§2.4) and `α_bare = g⁷ = 1/128` (the geometry `e = π(l_0/2)²`, [1, §7.4]).

| | α⁻¹ | m_e/M_0 |
|---|---|---|
| Leading (core) | `128 = 2⁷ = g⁷` | `1024 = 2¹⁰` |
| Shell | `+8 = 128·g⁴` | `+16 = g⁻⁴` |
| Central cell `2⁰` | `+1 = α·128` | `−1 = Q_H` |
| Tail (μ_c = 2π) | `+1/28` | — |

The polynomial (3.3) with `x = α⁻¹/4` has the dominant term `x² ∝ α⁻²`: the mass is **quadratic in the charge** (charge `∝ x`, mass `∝ x²`) — exactly the character of an electromagnetic self-energy `∝ e²`. This is the electromagnetic nature of our mass: `α` and `m_e` are the charge-area and the energy density of **one** Hopf structure.

**Which `α`, such the mass.** At the bare `α = 1/128` → `1039 = 446.279 keV` (direct functional output); at the observed `α = 1/137` → `1189.8 = 511 keV`. **The prediction of the present work is the bare point**, derivable from the functional with no free parameters; the point `511 keV` is the same value under the screened `α`, not a "mass with tails included" and not the limit of `m_e^bare` under box extension.

---

## 6. Chiral-bag interpretation

### 6.1. Local BPS alignment `u ↔ B`

The Berry curvature `B = curl A` of the field `n: ℝ³ → S²` in axisymmetry has the components (where `A` is the Berry connection):

```
B_r =  (1/r) · n · (∂_φ n × ∂_z n) = ∂_z n_z / r
B_φ = -n · (∂_r n × ∂_z n) = -ρ_Q   (topological density)                    (6.1)
B_z = -(1/r) · n · (∂_r n × ∂_φ n) = -∂_r n_z / r
```

with `∂_φ n = ẑ × n` at `φ = 0`. The reduced u-channel carries only `(u_r, 0, u_z)`. The test measures the poloidal cosine similarity `cos θ(r) = (u · B)/(|u| · |B|)`:

| `r [l_0]` | `cos θ(r)` |
|---|---|
| 0.11 | **0.9988** |
| 0.31 | 0.9896 |
| 0.51 | 0.9622 |
| 0.65 ≈ R_r | 0.885 |
| 1.00 | 0.7224 |
| 1.50 | 0.5947 |
| 3.00 | 0.3737 |
| 5.00 | 0.2168 |

In the **topological core** `cos θ → 1` (an almost perfect BPS alignment); in the tail it dilutes to `~0.2`. This is the empirical signature of a local BPS bound in the bag structure.

### 6.2. Saturation of the inner integral in the core

The norms integrated over radial bins at `μ_c = 2π`:

| `R_max [l_0]` | `∫|B|²` (% of total) | `∫(u·B)` (% of total) | local `C` |
|---|---|---|---|
| 0.5 | 76.8 % | 80.9 % | +0.868 |
| 1.0 | 95.1 % | **100.0 %** | +0.664 |
| 5.8 (full) | 100 % | 100 % | +0.532 |

**76.8 % of all `∫|B|²` is concentrated in `r < 0.5 l_0`**; `∫(u·B)` saturates already at `R ≈ 1 l_0`. The inner product is fully accumulated **in the core**, not in the tail — a physical localization of the BPS structure.

### 6.3. Identification: chiral bag, massive gauged Skyrme, boundary spectrum

The numerical picture — topological core + elastic shell + discrete boundary spectrum — **structurally corresponds** to three known constructions:

**(a) Chiral Bag Model** [Brown–Rho 1979 [14]; Vento et al. 1980]. A phenomenological model of the nucleon: quarks inside a "bag" of radius `R_bag ~ 0.7 fm`, outside — a pion field (Yukawa, ~1.4 fm), the bag boundary matching the currents. The correspondence to our structure is **structural, not literal** — the component ranges are distributed differently:
- topological core (`n` non-trivial) ↔ quark bag;
- u-channel (short range, `l_c ≈ 0.4 l_0 < R_r`) ↔ **bag wall** (it holds the structure from inside, not the pions outside);
- massless OF tail of `n` (`1/r`, long range) ↔ **pion field** (our "medium" itself plays the role of the long channel).

**(b) Massive Gauged Skyrme** [Adam et al. 2010 [15]] — a Skyrme extension with a massive gauge field. In our case the u-channel plays the role of such a massive field with `l_c = 1/√μ_c ≈ 0.4 l_0`.

**(c) Boundary spectrum** — a realization of the topology in the form of a boundary term. Formally the APS η-invariant [16] is for fermions; in our case it is a bosonic analog; the formalization is an open problem (§7.2). The dyadic decomposition (3.3) is its direct numerical signature.

**What is new in our model:**
- The bag radius is not tuned empirically (in Brown–Rho `0.7 fm`); in our case it is derived from the Derrick + Hopf balance: `r_v = l_0/2`.
- A specific **bare** mass `m_e^bare = 446.279 keV` is reproduced quantitatively.
- `μ_c = 2π` is fixed by the Cosserat coupling (§2.2), not a free parameter.

### 6.4. The critical value `μ_c = 2π`

The Yukawa screening length of the u-channel: `l_c(2π) = 1/√(2π) ≈ 0.399 l_0`.

**Hierarchy of nearby scales:**

```
l_c ≲ r_v < R_r  ≪  R_BPS  <  L_box
0.40  0.50  0.64       7.5     17                                            (6.2)
```

`l_c` lies just below the theoretical `r_v` and the numerical `R_r` — **the u-channel is screened at the scale of the topological core itself**, not outside it and not "too far" inside. This is a self-consistent condition that singles out `μ_c = 2π` physically.

**Multi-scale character of the structure.** Unlike the classical Brown–Rho bag with a single radius, our structure is multi-scale: `l_c ≈ 0.4` (Yukawa u), `r_v = 0.5` (Derrick), `R_r = 0.64` (ring), `R_BPS = 7.5` (where `m = 2¹⁰`), `L_box = 17`. When "bag core" is mentioned below, by context it is either `R_r` (ring radius) or `R_BPS` (where the mass plateaus).

![Fig. 4. Radial profiles of the Hessian-spectrum modes on the full grid [0, 17 l_0]. The random modes (4 curves) concentrate near the box edge L_r = 17; the targeted seed vector v_shrink has a broad distribution in the bulk. In the bag core r < R_r = 0.64 l_0 the amplitudes are suppressed by 8+ orders.](../../verifications/chiral_bag_resonance/fig_full_range_profiles.png)

### 6.5. Hessian spectral test

In addition to the BPS tests, we check the chiral bag **spectrally**: we compute the lowest modes of the linear Hessian `H = ∂²E/∂n∂n` around the canonical electron.

**Method** (details — Appendix C):
- canonical `n*` from the NM optimum (2.8);
- generalized problem `H v = ω² M v`, `M = diag(2π r J dξ dη)`;
- HVP via double autograd, projection `δn ⊥ n` onto `S²`;
- LOBPCG with two initializations: random and targeted `v_shrink = ∂n/∂R_r`;
- the `z`-translation zero mode is projected out explicitly.

**Result at `L = 17`:**

| mode source | `ω²` (model) | peak `r [l_0]` | `frac(r > 13)` |
|---|---|---|---|
| random #0 | 54.1 | **16.97** | 99.31 % |
| random #1 | 64.5 | **16.46** | 99.13 % |
| random #2 | 65.2 | **16.97** | 99.20 % |
| random #3 | 74.9 | **16.97** | 99.05 % |
| `v_shrink` (refined LOBPCG) | 1.27 | 16.63 | 53.0 % |

Random-initialization LOBPCG at k=4 finds **box-edge modes**: all 4 concentrate near `r ≈ L_r = 17` — the typical physics of a finite box, not the bulk modes of the bag tail.

> Note on reproducibility. The eigenvalues `ω²` reproduce directly; the columns `peak r` and `frac` are taken from the full-window profile (`extend_profile.py` → `result_hessian_profiles.json`, `r_max = L_r`). The quantities `ω²` and the scaling `K = ω²·L` (§6.6–6.7) are independent of the radial window.

The targeted seed vector `v_shrink = ∂n/∂R_r` (the ring-shrinking direction, [2, §4.3]) gives a qualitatively different picture. The stable characteristic is the **direct Rayleigh quotient** for this direction: `ω² = 3.23`, a value anchored to the bag core that scales as `1/L` (§6.6). The LOBPCG refinement for this mode is unstable and drifts to the box edge (`ω² = 1.27 → 0.24` at `L = 17 → 34`, §6.6), so it is the direct value `3.23` that is interpreted physically.

**Channel decomposition of the Hessian:** `99.7 %` of the perturbation energy is in Oseen–Frank (`(∇n)²`), `0.3 %` in Skyrme (`(∇n)⁴`). Long-wavelength elastic modes; the topological term is almost not involved.

**Absence of a collapse mode.** `v_shrink` gives a positive `ω² > 0`; on the stretched grid `β_r = 6` the radial instability [2, §4.3] is structurally suppressed.

### 6.6. Box-scaling test

A direct check of the nature of the lowest modes: repeating the computation on doubled (`L_r = 34, L_z = 66`) and quadrupled (`L_r = 68, L_z = 132`) boxes at the same discretization `1024 × 2048`.

**Predictions:**
- box-edge modes: `ω²(2L) = ω²(L) / 4` (the wavelength scales with `L`);
- bag modes (physical scale fixed): `ω²(2L) = ω²(L)`.

**Result:**

| mode | `ω²(L=17)` | `ω²(L=34)` | ratio | verdict |
|---|---|---|---|---|
| random #0 | 54.14 | 13.64 | **0.252** | box-edge ✓ |
| random #1 | 64.49 | 16.19 | **0.251** | box-edge ✓ |
| random #2 | 65.19 | 16.36 | **0.251** | box-edge ✓ |
| random #3 | 74.88 | 18.85 | **0.252** | box-edge ✓ |
| `v_shrink` (direct) | 3.23 | 1.68 | **0.521** | mixed (bag + edge) |
| `v_shrink` (refined) | 1.27 | 0.24 | **0.189** | LOBPCG drifted to edge |

The random modes give a ratio `0.251 ± 0.001 ≡ 1/4` to 3–4 significant figures — **a strict confirmation** that these are pure `1/L²` box-edge modes.

`v_shrink` (direct Rayleigh quotient) gives a ratio `0.521`; the third point `L = 68` (`ω² = 0.86`, ratio 0.512) confirms a strict `1/L` law. This **different asymptotics** relative to the random modes reveals the physics of §6.7.

![Fig. 5. Side-by-side radial profiles at L_r = 17 (left) and L_r = 34 (right), same scale. The mode peaks **track exactly** with the box edge; the core r < R_r = 0.64 l_0 is empty in both. A visual confirmation of the box-edge interpretation of the random modes.](../../verifications/chiral_bag_resonance/fig_compare_17_vs_34.png)

### 6.7. K/M theorem: the u-channel is mathematically necessary

**Intuition.** Any eigenfrequency of a harmonic oscillator is `ω² = K/M`, where `K` is the stiffness and `M` the inertia. For the generalized problem `H v = ω² M v`:

```
ω² = ⟨v, H v⟩_E / ⟨v, v⟩_W = K / M                                           (6.3)
```

where `K = ⟨v, Hv⟩_E` is the Euclidean norm of the Hessian contribution, and `M = ⟨v, v⟩_W` is the volume-weighted norm.

**Random box-edge modes** `v ∼ sin(πr/L)`:
- `K ∼ ∫|∇v|² dV ∼ 1/L` (the gradient amplitude falls with the box);
- `M ∼ ∫|v|² dV ∼ L` (the volume grows linearly);
- `ω² = K/M ∼ 1/L²` ✓.

**Targeted `v_shrink = ∂n/∂R_r`** (centered on the soliton):
- in the massless OF theory the perturbation `v` has a **`1/r` tail** in 3D (the solution of the Laplace equation at ∞);
- `K = ⟨v, Hv⟩_E ∼ ∫|∇v|² · 2π r dr dz`: with `|∇v|² ∼ 1/r⁴` the integral **converges** → `K = const > 0`;
- `M = ⟨v, v⟩_W ∼ ∫|v|² · 2π r dr dz`: with `|v|² ∼ 1/r²` the integral **diverges linearly** → `M ∝ L`;
- `ω² = K/M = const/L ∝ 1/L` ✓.

**Numerical verification:** `K = ω²·L` from three points:

| `L` | `ω²` | `K = ω²·L` |
|---|---|---|
| 17 | 3.23 | 54.9 |
| 34 | 1.68 | 57.1 |
| 68 | 0.86 | 58.5 |

`K ≈ 57 ± 2` (stable to within 3 %) — **a direct confirmation** that the stiffness of the bag core in the ring-shrinking direction is a positive constant independent of the box size.

![Fig. 6. K/M decomposition (the main figure of §6.7). (a) Log-log scaling of ω²(L) for 3 box sizes (L_r ∈ {17, 34, 68}): the random modes match ω² ∝ 1/L² (dashed), v_shrink (direct) matches ω² = K/L → anchored to the bag core with a 1/r tail. (b) Extracted stiffness K = ω²·L for v_shrink (direct): ⟨K⟩ = 56.9 ± 2.6 % — a constant within error. A direct quantitative proof that the bag core has a positive stiffness, while ω² → 0 as L → ∞ is explained by the divergence of the inertia M ∝ L due to the 1/r tail of the massless OF field.](../../verifications/chiral_bag_resonance/fig_KM_decomposition.png)

**Main conclusion — the theorem on the necessity of the u-channel.**

> **(T1)** In the pure Faddeev–Skyrme model (without the u-channel) the Hopf soliton has a rigid core (`K > 0`, the Derrick balance is stable), but **has no discrete vibrational spectrum** of excitations: any perturbation drags along a `1/r` tail of the field, whose inertia diverges as `M ∝ L → ∞`, and the frequency `ω² = K/M → 0`.
>
> **(T2)** Introducing the u-channel with the mass term `(μ_c/2) u²` Yukawa-screens the **translational** perturbations `u` themselves at the scale `l_c = 1/√μ_c`. Through the tensor coupling `(∇×u − Π(n))²` (2.5) the long range of the `δn` perturbations is cut off **indirectly**: their inertia becomes finite, `ω² = K/M > 0` — a discrete spectrum inside the bag is opened.

**Status of the result.** (T1) is numerically confirmed: in the pure `E_OF + E_Sk` theory `K = const`, `M ∝ L` at three box points. (T2) is an analytic consequence of the form (2.5) and of the Yukawa screening of u; a direct Hessian computation with the u-channel on is an open direction of verification (§8.3), indirectly confirmed in §4.3.

Thus, **the chiral-bag structure and the dyadic discreteness of the mass become physically possible only in the presence of the u-channel**.

---

## 7. Discussion

### 7.1. What is numerically confirmed

1. **The dyadic structure of `m_e` and `α⁻¹`** (§3, §5) is numerically reproducible with no free parameters.
2. **`μ_c = 2π` is the unique resonance point** by four independent criteria (§4); disabling the u-channel destroys the dyadic (§4.3).
3. **The u-channel is mathematically necessary** for a discrete spectrum — the K/M theorem of §6.7 + the local BPS alignment (§6.1–6.2) + the suppressed bag core in the Hessian profile (§6.5).

### 7.2. What is open

- **A full analytic derivation of the BPS bound** (Bogomolny transformation) for the functional `E[n, u]` — open.
- **A test in other topological sectors** (`|Q_H| = 2`, a Hopf link breaking U(1)): requires a 3D non-axisymmetric solver.
- **A bosonic analog of the APS η-invariant** requires a formal proof: formally the APS theorem is built for fermions; in our model the dyadic decomposition looks like its bosonic analog, but this is so far an interpretation, not a theorem.
- **A direct numerical check of the K/M theorem (T2)** with the u-channel on — an open direction.

### 7.3. The axisymmetric reduction: what it is and what it does not give

- The numerical verifications use the axisymmetric reduction of the full `E_u` (2.4)–(2.5) to a single scalar mode `ψ` with `u_φ = 0`; this reduction is **equivalent** to the full tensor form in the class of axisymmetric configurations [2, §5.5], not a simplification.
- The toroidal component of the Berry curvature `B_φ = −ρ_Q` (6.1) is not an "uncompressed remainder", but the topological density itself (`∫ B_φ dV = 4π·Q_H`); its presence is a feature of the Hopf structure, not a defect of the reduction.
- The real limitation of the reduction is the inability to work with **non-axisymmetric** configurations (a Hopf link for `|Q_H| = 2`); this requires a full-field 3D relaxation (prepared separately).

---

## 8. Conclusion and outlook

### 8.1. Main result

> At `μ_c = 2π = η` in the Cosserat functional `E[n, u]` a chiral bag arises that **simultaneously** fixes `m_e^bare/M_0 = 2¹⁰ + 2⁴ − 1 = 1039` and `α⁻¹(0) = 128 + 8 + 1 + 1/28 ≈ 137.036` to an accuracy of `0.01 %` and `0.0002 %` respectively — with no free parameters and no experimental input of `α`. The Hessian box-scan (§6.7) shows that the u-channel is not an add-on but a structural necessity: without the short range of the u-perturbations (translations) the inertia of the `δn` perturbations diverges (`M → ∞`) and a discrete spectrum is impossible.

### 8.2. What this changes in fundamental physics

- **Mass and coupling constant are derived** from the structure of the medium, not independent inputs of the Standard Model.
- **Numerical "coincidences" in nature** (`α, m_e, m_p, ...`) are consequences of resonances of **one medium**, not independent empirical inputs.
- **Discreteness of mass is quantization at the level of the mass itself**, not only of its excitation spectrum (atomic levels).
- **A two-channel medium `(n, u)` with a massive part is mandatory**, otherwise no stable discrete particles can exist (the K/M theorem of §6.7).

### 8.3. Open problems

1. Analytic derivation of the BPS bound (à la Bogomolny) for `E[n, u]` (§7.2).
2. A test in the `|Q_H| = 2` sector via a 3D non-axisymmetric solver.
3. A direct Hessian computation with the u-channel on — a check that `M` becomes finite.
4. Application of the same mechanism to the **proton**, the **muon**, and heavy leptons.
5. A bosonic APS theorem: a formalization of the discrete boundary spectrum.
6. **The spectrum of scales on the hyperbola `m·l = ℏ/c`**: the polynomial `m_e/M_0 = x² + x/2 − 1` is established for the **vacuum** point. The Compton limit (knot = one cell) and intermediate scales (atomic medium, `cell size ~ a_0`) are expected as other members of the family with different leading exponents; the numerical and analytic verification of this spectrum is a separate direction.

---

## Methodology and use of AI tools

In preparing this work the author used the large language model **Claude (Anthropic)** to assist with writing Python scripts for the numerical verifications (μ_c-sweep, u-channel disable, BPS `u ↔ B` alignment, Hessian box-scan, radial assembly of `α⁻¹`), with the development of supporting modules (stretched grids, boundary conditions, diagnostics of the energy components), and with stylistic editing of the manuscript text. All key physical postulates (the form of the functional, the choice of constants, the ansatz, the chiral-bag interpretation), the derivation of the K/M theorem, and the formulation of the conclusions are due to the author.

The author has thoroughly checked all generated code (grid convergence, conservation of the topological charge `Q_H`, invariance of the result under rescaling, see §6) and the manuscript text, and takes full responsibility for the final content and results of the work.

---

## Acknowledgements

The conceptual basis of this work was provided by: the ideas of **L. D. Faddeev** on topological solitons as particles, the 4th-order stabilizing term of **T. H. R. Skyrme**, the elastic theory of director media due to **C. W. Oseen** and **F. C. Frank**, the phenomenological chiral-bag model of **Brown–Rho**, and the spectral asymmetry of **Atiyah–Patodi–Singer**. Parallel programs of deriving fundamental physics from the topology of a medium — **G. E. Volovik** (³He-A) [17] and **H. Kleinert** (multivalued fields) [18] — set the mathematical context of the present work.

The computations were performed on a single NVIDIA RTX 2070 using PyTorch.

---

## References

[1] **Yeusiyevich, I. V.** (2026). *Structural reduction of the SI base of units via the Cosserat-continuum hypothesis*. Zenodo preprint. DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

[2] **Yeusiyevich, I. V.** (2026). *Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e^bare = 446.279 keV`*. Zenodo preprint. DOI: [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123).

[3] A. S. Eddington, *The Mathematical Theory of Relativity*, 2nd ed., Cambridge University Press (1924).

[4] A. Wyler, "L'espace symétrique du groupe des équations de Maxwell", *C. R. Acad. Sci. Paris* **269**, 743 (1969).

[5] M. Atiyah, *The Fine Structure Constant*, preprint (2018).

[6] L. Faddeev and A. J. Niemi, "Stable knot-like structures in classical field theory", *Nature* **387**, 58 (1997).

[7] C. W. Oseen, "The Theory of Liquid Crystals", *Trans. Faraday Soc.* **29**, 883 (1933).

[8] F. C. Frank, "On the Theory of Liquid Crystals", *Discuss. Faraday Soc.* **25**, 19 (1958).

[9] T. H. R. Skyrme, "A Non-linear Field Theory", *Proc. Roy. Soc. A* **260**, 127 (1961).

[10] R. A. Battye and P. M. Sutcliffe, "Knots as Stable Soliton Solutions", *Phys. Rev. Lett.* **81**, 4798 (1998); P. M. Sutcliffe, "Knots in the Skyrme–Faddeev model", *Proc. Roy. Soc. A* **463**, 3001 (2007).

[11] V. P. Mineev and G. E. Volovik, "Planar and linear solitons in superfluid ³He", *Phys. Rev. B* **18**, 3197 (1978) — Frank–Oseen functional for the l-vector in ³He-A. The Mermin–Ho relation itself: N. D. Mermin and T.-L. Ho, *Phys. Rev. Lett.* **36**, 594 (1976).

[12] G. H. Derrick, "Comments on Nonlinear Wave Equations as Models for Elementary Particles", *J. Math. Phys.* **5**, 1252 (1964).

[13] F. Lin and Y. Yang, "Existence of energy minimizers as stable knotted solitons in the Faddeev model", *Comm. Math. Phys.* **249**, 273 (2004) — existence theorem for the continuum minimizer.

[14] G. E. Brown and M. Rho, "The little bag", *Phys. Lett. B* **82**, 177 (1979); V. Vento et al., *Nucl. Phys. A* **345**, 413 (1980).

[15] C. Adam, J. Sanchez-Guillen and A. Wereszczynski, "A Skyrme-type proposal for baryonic matter", *Phys. Lett. B* **691**, 105 (2010); C. Adam, C. Naya, J. Sanchez-Guillen and A. Wereszczynski, "Nuclear binding energies from a Bogomol'nyi–Prasad–Sommerfield Skyrme model", *Phys. Rev. C* **88**, 054313 (2013).

[16] M. F. Atiyah, V. K. Patodi and I. M. Singer, "Spectral asymmetry and Riemannian geometry I–III", *Math. Proc. Camb. Phil. Soc.* **77, 78, 79** (1975–76) — the η-invariant and spectral asymmetry.

[17] G. E. Volovik, *The Universe in a Helium Droplet*, Oxford University Press (2003) — program of the analogy between superfluid ³He-A and the Standard Model.

[18] H. Kleinert, *Multivalued Fields in Condensed Matter, Electromagnetism, and Gravitation*, World Scientific (2008) — defects as gauge fields.

[19] B. Berg and M. Lüscher, "Definition and statistical distributions of a topological number in the lattice O(3) σ-model", *Nucl. Phys. B* **190**, 412 (1981); N. S. Manton and B. M. A. G. Piette, "Understanding Skyrmions using rational maps", *Prog. Math.* **201**, 469 (2001) — geometric discretization of Q_H.

[20] B. I. Halperin and D. R. Nelson, "Theory of Two-Dimensional Melting", *Phys. Rev. Lett.* **41**, 121 (1978); A. P. Young, "Melting and the vector Coulomb gas in two dimensions", *Phys. Rev. B* **19**, 1855 (1979) — the KTHNY cascade.

[21] CODATA Recommended Values of the Fundamental Physical Constants 2018, *Rev. Mod. Phys.* **93**, 025010 (2021).

---

## Appendix A. Numerical reproducibility

All five verifications for the present preprint are collected in one flat directory
[`verifications/chiral_bag_resonance/`](../../verifications/chiral_bag_resonance/),
containing a shared module `stretched_grid.py`, a unified `requirements.txt`, and a
self-contained `README.md` with a detailed description of each test.

| Test | Main script | JSON output | § | Time (RTX 2070) |
|---|---|---|---|---|
| μ_c-sweep | `mu_c_sweep.py` | `result_mu_c_sweep.json` | §4 | ~30 min |
| u-channel disable | `nm_no_u.py` | `result_u_channel_disable.json` | §4.3 | ~6 min |
| BPS alignment `u ↔ B` | `berry_u_alignment.py` | `result_berry_alignment.json` | §6.1–6.2 | ~3 min |
| Hessian K/M | `analysis_three_checks.py`, `analysis_doubled_box.py`, `analysis_quad_box.py`, `extend_profile.py` | `result_hessian_L17/L34/L68.json`, `result_hessian_profiles.json` | §6.5–6.7 | ~3 min per box |
| α-running radial | `alpha_running.py` | `result_alpha_running.json` | §5 | ~6 sec |

Figure-building scripts (they read the JSONs above): `plot_KM_decomposition.py`, `plot_box_scaling.py`, `plot_doubled_profiles.py`, `plot_extended.py`, `plot_alpha_topology.py`.

Companion verifications of the parent work [2]:
- [`verifications/electron_mass_minimization/`](../../verifications/electron_mass_minimization/) — NM minimization reproducing `m_e^bare = 446.279 keV`;
- [`verifications/canonical_derrick/`](../../verifications/canonical_derrick/) — Derrick scan of the stability of the canonical configuration.

## Appendix B. Detailed derivation of `g = 1/2`

The full derivation of the identity `r_v = l_0/2` via the Derrick balance of the full functional `E[n, u]` for `Q_H = −1` is given in [1, §7.3, (7.5)] and is numerically confirmed in the verification [`verifications/canonical_derrick/`](../../verifications/canonical_derrick/) (a V-minimum of the total energy at `λ = 1` with the topological charge preserved over the whole range `λ ∈ [0.6, 3.0]`).

## Appendix C. Computation of `M_0 c² ≈ 429.51 eV` and `l_0 ≈ 4.594 Å`

From the triple `{ε₀, μ₀, ℏ}` algebraically:

```
l_0⁴   = ε₀ℏc / (2π)                                ⇒  l_0 ≈ 4.5943 Å
M_0 c² = ℏc / l_0 = (2π ℏ³ / (c⁵ ε₀))^(1/4) c²       ⇒  M_0 c² ≈ 429.5068 eV
m_0 l_0 = ℏ/c (the mass-hyperbola identity)
```

The full derivation and discussion — [1, §7.4 (T10)].

## Appendix D. Data and code availability

The code is in the repository:

```
https://github.com/igorevsiev-cmyk/cosserat-program
```

The preprint is registered on Zenodo: *DOI pending*.

Parent works:
- [1] SI-reduction: DOI [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199);
- [2] Electron mass minimization: DOI [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123).

---
