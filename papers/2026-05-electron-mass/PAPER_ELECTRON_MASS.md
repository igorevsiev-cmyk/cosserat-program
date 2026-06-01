# Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e^bare = 446.279 keV`

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-05-31
**Version:** 2
**Type:** preprint
**License:** CC-BY 4.0

---

## Abstract

The electron mass `m_e c² = 510.99895000 ± 0.00000015 keV` (CODATA 2018) is an empirical input in the Standard Model; no derivation from more fundamental constants exists.

In the present work `m_e` is computed numerically from three vacuum constants `{ε₀, μ₀, ℏ}` by minimizing the Cosserat functional `E[n, u]` of a director field `n: ℝ³ → S²` over a three-parameter Hopf ansatz with topological charge `Q_H = 1`. All constants of the functional are fixed by structural identities from the preceding work [1]:

- lattice scale `l₀⁴ = ℏ/(2π Z₀)`, with `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω`;
- base mass scale `M₀ c² = ℏc/l₀ ≈ 429.5068 eV`;
- Cosserat coupling `μ_c = η = 2π`;
- elastic anisotropy `K₃/K₁ − 1 = η`, with `K₁ = K₂ = 2`, `K₃ = 2(1 + 2π) ≈ 14.566`;
- Skyrme term `c₄ = 1`.

Minimization by the Nelder–Mead simplex method on a stretched cylindrical grid of resolution `1024 × 2048` (dyadic box `L = 17 × 33 l₀`) gives:

> `m_e^bare c² = 446.279 keV`

This value is the **bare** electron mass in the Cosserat vacuum: a direct output of the bare functional `E[n, u]`. The dimensionless minimum `Ẽ_min = E_min/M₀c² ≈ 1039` fits the dyadic form `m_e/M₀ = x² + x/2 − 1` with a single scale `x = α⁻¹/4`: at the bare `α_bare⁻¹ = 128` (`x = 32`) it gives `1024 + 16 − 1 = 1039`, at the physical `α(0)⁻¹ = 137` (`x = 34.26`) — `1189.8`, i.e. `m_e^phys ≈ 511 keV`. The same shift of the scale `x` that takes the bare `α` to the measured one takes the bare mass to the physical one (§7.2–7.3). The dyadic form is given as a numerical observation, not as a derivation.

Topology is preserved: `|Q_H| = 1` to `~4·10⁻⁵`; the sign `−1` corresponds to the electron.

---

## Logical chain of the paper

```
INPUTS (three measured vacuum constants)
 {ε₀, μ₀, ℏ}                                     [1, §6]
 │
 ▼
DERIVED CONSTANTS (from [1])
 c       = 1/√(ε₀μ₀)                              [1, §2.4]
 Z₀      = √(μ₀/ε₀) ≈ 376.73 Ω                    [1, §6]
 l₀⁴     = ℏ/(2π Z₀)  →  l₀ ≈ 4.5943 Å            [1, §7]
 M₀ c²   = ℏc/l₀  ≈ 429.5068 eV                   [1, §5.1]
 │
 ▼
COSSERAT-FUNCTIONAL PARAMETERS                   (§3)
 η       = 2π          (zero-point oscillations of spin waves)
 μ_c     = η = 2π      (Cosserat coupling)
 K₃/K₁ - 1 = η         (elastic anisotropy, K₁=K₂=2, K₃=14.566)
 c₄      = 1            (Skyrme stabilizer)
 │
 ▼
TOPOLOGICAL CONSTRAINT                            (§4)
 Q_H = 1                (Hopf invariant, π₃(S²) = ℤ)
 3-parameter Hopf ansatz n(r, z; R_r, R_z, w)
 │
 ▼
NUMERICAL MINIMIZATION                            (§5)
 Nelder-Mead on stretched grid 1024×2048
 (dyadic box L = 17 × 33 l₀)
 (R_r, R_z, w) = (0.64082, 0.80729, 0.70200) (in units of l₀)
 │
 ▼
RESULT                                            (§6)
 m_e^bare c² = M₀ c² · Ẽ_min = 429.5068 eV · 1039.05 = 446.279 keV
 — the bare electron mass in the Cosserat vacuum
 Q_H = −0.99996   (electron orientation; |Q_H| = 1 preserved to ~4·10⁻⁵)
 │
 ▼
INTERPRETATION                                    (§7)
 m_e^bare = 446.279 keV at α_bare⁻¹ = 128 (x = 32)
 Dyadic form  m_e/M₀ = x² + x/2 − 1,  x = α⁻¹/4
   bare:  32² + 16 − 1 = 1039       → 446.3 keV     (§7.2)
   phys:  34.26² + 17.1 − 1 ≈ 1190  → 511.0 keV     (§7.3)
 charge ~ x, mass ~ x²  ⟹  m_e ∝ 1/α² (leading order)
```

Minimization is reproducible via the standalone script `verifications/electron_mass_minimization/nm_minimization.py` (see Appendix A).

---

## 1. Introduction

### 1.1. The electron mass in the Standard Model

`m_e c² = 510.99895000 ± 0.00000015 keV` enters the Standard Model as an empirical parameter. The Yukawa coupling `y_e ≈ 2.94 × 10⁻⁶` is fixed by this value; its smallness relative to the top-quark Yukawa (`y_t ≈ 1`) has no independent explanation.

Earlier attempts to derive `m_e` from deeper structure (Eddington 1924 [9], Wyler 1969 [10], Atiyah 2018 [12]) were either numerological or relied on arbitrary normalization choices.

### 1.2. The Cosserat-vacuum hypothesis

The preceding work [1] showed that, under four structural identifications, the SI base reduces to a single dimension (energy), and the electromagnetic and gravitational sectors are accommodated in a single Cosserat medium. The functional `E[n, u]` in this medium admits localized minima with integer `Q_H ∈ π₃(S²) = ℤ`. The minimum `Q_H = −1` is identified with the electron.

The present work computes the mass of this minimum.

### 1.3. Approach

1. The Cosserat functional is constructed; all its constants are fixed by the triple `{ε₀, μ₀, ℏ}` (§3).
2. Minimization is performed by the Nelder–Mead method over the 3-param Hopf ansatz on a `1024 × 2048` grid (§§4–5).
3. The minimum is converted to SI units via `M₀ c² = ℏc/l₀` (§6).

The result is a **topologically protected upper bound** for the bare electron mass `m_e^bare c² ≤ 446.279 keV`. This is the minimum of the functional `E[n,u]` on the manifold of canonical Hopf configurations; the 3-param ansatz acts as an analytic regulator that cuts off the non-physical lattice modes of collapse (see §4.3 on the role of the ansatz, §7.4 on the status of the result). The value is not compared directly with the physical (measured) mass `m_e` — the derivation of the "bare → physical" relation is left as an open direction (§7).

---

## 2. The Cosserat functional

A Cosserat medium is characterized by two independent field variables: a microrotation described by the director `n(r) ∈ S²`, and a translational displacement `u(r) ∈ ℝ³`. The energy functional decomposes into three blocks:

```
E[n, u]  =  E_n[n]   +   E_u[u]   +   E_int[n, u]                       (2.1)
```

**Block E_n — energy of the director channel** (Frank–Oseen + Skyrme):
```
E_n[n] = ∫ d³r [
    (K₁/2) (∇·n)²                ← splay                (Frank, 1958)
  + (K₂/2) (n·∇×n)²              ← twist                (Frank, 1958)
  + (K₃/2) (n×∇×n)²              ← bend                 (Frank, 1958)
  + (c₄/4) F_ij F^ij             ← Skyrme stabilizer     (Skyrme, 1961; Faddeev–Niemi, 1997)
]                                                                       (2.2)
```

where `F_ij ≡ n · (∂_i n × ∂_j n)` is the antisymmetric 2-tensor of the topological (Hopf–Whitehead) current density; in index form `F_ij F^ij = 2·Σ_{i<j} [n·(∂_i n × ∂_j n)]²`. This is exactly the Faddeev–Skyrme stabilizer [6, 7]; it is precisely this antisymmetric contraction that is implemented in the code (see `verifications/electron_mass_minimization/stretched_grid.py`, `compute_skyrme_stretched`) and that provides the topological protection of the vortex-tube cross-sectional area against local collapse.

**Remark on the absence of a director mass term.** In (2.2) an orientation potential `V(n) ∝ (1 − n_z)` (a "mass" for `n`) is deliberately not introduced. The Faddeev–Niemi hopfion in 3D is stable in the pure Frank–Oseen + Skyrme combination without such a term [7, 8]: the Derrick balance between `K_i` (`∝ λ`) and `c₄` (`∝ λ⁻¹`) fixes the soliton scale, and the polynomial decay of the tails yields a convergent energy integral. The numerical grid convergence (§6.4) confirms this empirically. Introducing `V(n)` was considered and rejected as a redundant parametric extension not dictated by the identities of §3.

**Block E_u — energy of the translational channel** (elasticity + Yukawa mass term):
```
E_u[u] = ∫ d³r [ (μ/2) (∂u)² + (μ_c/2) u² ]                              (2.3)
```

**Block E_int — tensor Cosserat coupling of the channels `n` and `u`.** The microrotation of the director field generates a vector spin current `Π(n)`, which must contract with the macroscopic rotation of the medium `∇×u` — the antisymmetric (bend) part of the displacement gradient. The correct tensor form of the coupling is:
```
E_int[n, u] = ½ μ_c ∫ d³r | ∇×u − Π(n) |²                            (2.4)
```
where `Π(n)` is the vector "spin current" of the director (an analog of the Mermin–Ho relation in superfluid ³He-A [21]). Both `∇×u` and `Π(n)` are vectors; the square is a proper scalar. The Euler–Lagrange condition `δE/δu = 0` gives the **vector** equation `μ_c·∇×(∇×u) = μ_c·∇×Π(n)`, which in the gauge `∇·u = 0` reduces to `−μ_c·∇²u = μ_c·∇×Π(n)`.

For the axisymmetric Hopf ansatz (§4) the field `Π(n)` has a single distinguished azimuthal component proportional to the polar angle `f(n) = atan2(√(n₁²+n₂²), n_z)` of the director from the vacuum direction (0 at infinity, π at the knot center), and the response `u` reduces to a single scalar mode `ψ(r,z)`. After the reduction and integration (see §5.5) the vector equation for `u` takes the form of a screened scalar Poisson equation with source `−2·f(n)`:
```
( ∇²_φ − μ_c ) ψ  =  −2·f(n)                                        (2.4')
```
where `∇²_φ` is the vector Laplacian acting on the azimuthal component (its explicit form, with the `−1/r²` term, is given in (5.5)).

Here `n_∞ = ẑ` is the boundary value at infinity; `μ` is the base elastic modulus (`μ ≡ 1` in natural units); `μ_c` is the Cosserat coupling (§3.3, fixed by the identity `μ_c = η = 2π`).

In the numerical implementation (§5.5) it is precisely the scalar reduction (2.4') that is solved; this is not a simplifying approximation but an *equivalent* form of the full tensor coupling (2.4) in the class of axisymmetric configurations. A full-field 3D relaxation without axial symmetry will require working with (2.4) directly — this is deferred to a separate forthcoming work (see §8).

---

## 3. The constants from `{ε₀, μ₀, ℏ}`

### 3.1. Length scale `l₀`

```
l₀⁴ = ℏ / (2π · Z₀),   Z₀ = √(μ₀/ε₀) ≈ 376.730 Ω         (3.1)
⇒ l₀ ≈ 4.5943 Å
```

### 3.2. Base mass scale `M₀`

```
M₀ c² = ℏc / l₀ = (2π ℏ³ / (c⁵ ε₀))^(1/4) c²              (3.2)
M₀ c² ≈ 429.5068 eV
```

### 3.3. Cosserat coupling `μ_c`

```
μ_c = η = 2π                                              (3.3)
```

The dimensionless constant `η` is a direct algebraic consequence of the definition of the scale `l₀` (3.1), not a free parameter of the functional. The rigorous, unambiguous form of the identity follows from contracting the fundamental constants into a dimensionless combination and substituting `l₀⁴ = ε₀ℏc/(2π)`:

```
η  =  ℏc·ε₀ / l₀⁴  =  ℏc·ε₀ / (ε₀ℏc/2π)  =  2π            (3.3a)
```

(`μ ≡ 1/ε₀` is postulate P2 of [1], so `ℏc·ε₀ = ℏc/μ`.) The factor `2π` here is literally the same one that appears in the definition `l₀⁴ = ℏ/(2π·Z₀)`: the identity `η = 2π` is a rewriting of the definition of `l₀`. Geometrically this `2π` corresponds to the solid angle of the target sphere `S²` (the period of the `U(1)` phase of the director).

**Physical meaning.** In the natural units of the medium (`l₀ ≡ 1`, in which the canonical identity is written) `η` reads as the ratio of two energies of a single cell — the quantum energy of rotation to the elastic one:

```
η  =  ℏω_gyro / (K · l₀)              (at l₀ = 1)         (3.3b)
```

- **Numerator** `ℏω_gyro` — the minimum-energy quantum of a "gyroscope" of size `l₀`. From the quantization of the cell's angular momentum (`I ~ M₀·l₀²`, `L ~ ℏ`): `ω_gyro = ℏ/(M₀·l₀²) = c/l₀` (via `M₀·l₀ = ℏ/c`), whence `ℏω_gyro = ℏc/l₀ = M₀c² ≈ 429.5 eV`.
- **Denominator** `K · l₀` — the elastic energy of a cell. `K` is the Frank constant with dimensions `[energy/length]`, `K = μ·l₀`. The Frank density `K|∇n|² ~ K/l₀²` over the cell volume `l₀³` gives the cell energy `K·l₀` (it is `K·l₀`, not `K·l₀³`, that has the dimension of energy).

In substance: the quantum zero-point oscillations of the field `n` and the elastic stiffness of the vacuum Cosserat medium are of the same order and differ by exactly `2π`.

> **Remark on units.** The unit-independent rigorous form is (3.3a). The energy ratio (3.3b) is exact at `l₀ = 1`, where the powers of `l₀` collapse; with explicit `l₀`-dependence the numerator `ℏc/l₀` and the denominator `μl₀²` give `η = ℏc·ε₀ = 2π` only after fixing `l₀ = 1`. The exponent of `K·l₀` in (3.3b) is therefore a matter of natural units, not an independent physical choice.

### 3.4. Elastic anisotropy `K₃/K₁`

```
K₁ = K₂ = 2,    K₃ = K₁ · (1 + η) = 2 · (1 + 2π) ≈ 14.566    (3.4)
```

> **Remark on the numerical value.** The minimization code uses the truncated value `K₃ = 14.56` (instead of `14.566`); the resulting shift in `m_e^bare` is `< 0.1 %` — within the dyadic deviation (§6.2).

### 3.5. Skyrme stabilizer `c₄`

```
c₄ = 1                                                     (3.5)
```

### 3.6. Summary

All five parameters of the functional {`K₁, K₂, K₃, μ_c, c₄`} = {`2, 2, 14.566, 2π, 1`} are fixed by `{ε₀, μ₀, ℏ}` via the identities (3.1)–(3.5).

---

## 4. The Hopf ansatz

### 4.1. Topological context

A smooth field `n: ℝ³ → S²` with `n(r → ∞) = ẑ` extends to `S³ → S²`. Such maps are classified by `π₃(S²) = ℤ`; the integer label is the Hopf invariant `Q_H`. For the electron identification the relevant minimum is `Q_H = −1`.

### 4.2. Three-parameter ansatz

```
n₁ = 8 r z w / P
n₂ = -4 r Y w / P
n₃ = (D - 4 r² w²) / P                                    (4.2)

where:
  Y = r² + z² - 1                in scaled coordinates (r/R_r, z/R_z)
  D = 4 z² + Y²
  P = D + 4 r² w²
```

Three parameters: `R_r` (ring radius), `R_z` (ring height), `w` (twist amplitude). The ansatz carries `|Q_H| = 1` for any positive `(R_r, R_z, w)` and reduces to `n₃ = 1` at infinity. The sign of `Q_H` is set by the orientation of the field; the identification with the electron uses `Q_H = −1` (positron: `+1`). The numerical implementation (§5) yields `Q_H = −0.99996` (§6.2) according to the convention used in the code.

The choice of the Hopf ansatz (4.2) is not arbitrary. A configuration with `Q_H = −1` is a closed vortex tube of the director `n`; its cross-section is a disk whose area is, in the Cosserat program [1, §7], algebraically identified with the electric charge, `e = π·(l₀/2)²` (circular cross-section geometry of radius `l₀/2`). The ansatz thereby fixes the **charge as the geometric cross-sectional area of the tube**, expressed through the scale `l₀`. The three parameters `(R_r, R_z, w)` set only the shape of the tube; in the optimization `(R_r, R_z)` are coupled — under spatial dilation they co-scale together (Derrick balance, see the companion check `canonical_derrick`), whereas `w` — a dimensionless twist amplitude — is not subject to the length scale.

### 4.3. The ansatz as a topological regulator

Although minimization over the 3-param ansatz (4.2) gives a numerically stable result (§5–6), it is important to make explicit the **role of the ansatz** in this construction.

A full-field relaxation of the entire director field `n: ℝ³ → S²` without the restriction to the parameterization (4.2) runs into a **discretization pathology** known for Faddeev–Skyrme models: at the anisotropy `K₃/K₁ = 1 + η ≈ 7.28` the bend penalty (the `K₃` term) drives the field into a regime where the core contracts toward a filament along the axis, lowering the discrete energy below any physically meaningful value. This is confirmed in our series of full-field relaxation tests (`verifications/grid_diagnostics/`): on boxes from `17×33` to `60×120` and on uniform grids without stretching, one observes a monotone contraction of the ring radius `R_ring` from `0.33 l₀` to `0.018 l₀` at preserved topological charge `|Q_H| = 1`, accompanied by a paradoxical **drop** in the discrete Skyrme contribution `E_Sk` (which physically should grow as `λ` under a contraction by `λ`, by Derrick).

This pathology has a clear nature. In the continuum limit the Lin–Yang existence theorem [24] guarantees a non-trivial minimum of the Faddeev–Skyrme functional in suitable Sobolev spaces. On a finite grid, however, the Skyrme term `c₄ F_ij F^ij` loses its ability to strictly resist collapse because of the truncation of gradients at the grid-step scale `Δx` (any difference is bounded by `π/Δx`). The continuum barrier `λ⁻¹` in the energy becomes finite; the soliton shrinks to a sub-grid size.

Our series of numerical experiments (`test2`–`test9` in the repository) — adding polar-angle stiffness, an effective Eringen-γ term, a BPS sextic `c₆(F·F)²`, and a non-local Coulomb self-action with the natural coefficient `α_bare = 1/128` — showed that these structurally motivated additions on the discrete grid **act as an independent additive penalty term**, not as a barrier: the field finds a configuration that minimizes the new term SEPARATELY from the main collapse channel, and then continues the previous scenario with the same final `E_tot − E_extra ≈ 422 keV`. Details are in the diagnostic scripts `verifications/grid_diagnostics/` (tests 2–9).

In this situation the **3-parameter Hopf ansatz** (4.2) acts as an **analytic regulator**: it restricts the optimization to the manifold of configurations with a fixed canonical geometry of a vortex tube of radius `R_r ~ l₀` and thereby cuts off the non-physical lattice modes of collapse. The obtained `m_e^bare c² = 446.279 keV` is, strictly speaking, a **topologically protected upper bound** for the energy of the true continuum minimum, realizing the physically meaningful geometry of a closed vortex tube with a given integer charge.

The "rigid ansatz as a regulator" approach is standard in numerical hopfion physics [7, 8, 25]. Removing this regularization requires a geometric discretization of the topological charge in the spirit of Berg–Lüscher [26], in which `Q_H` is computed not through local gradients but through solid angles on cells, which makes the topological sector absolutely impenetrable to numerical collapse. A full-field implementation in this style is the subject of a separate forthcoming work (see §7.4, §8).

---

## 5. Numerical method

### 5.1. Grid

A cylindrical grid `(r_i, z_j)` of size `N_r × N_z = 1024 × 2048` with clustering near `r ~ R_r` and `z ~ 0` (stretching exponents `β_r = 6.0`, `β_z = 3.0`). Box dimensions: `L_r = 17 l₀`, `L_z = 33 l₀` (`L_z = 2·L_r − 1`; justification of `L_r` below). Double precision (`float64`) throughout.

The box size is **dyadic**: the radial extent holds the 16-cell mass shell around the `2¹⁰` core plus a central cell:

```
L_r = 2⁴ + 1 = 17,    L_z = 2⁵ + 1 = 2·L_r − 1 = 33
```

(`r` is the radial coordinate from the symmetry axis, one-sided; `z` is the axial coordinate, two-sided through the knot center, hence twice as long.)

The box thus fully contains the localized core of the configuration and yields a stable **bare** value; the long-range slow tails of the field are not included in it — accounting for them is a separate problem of renormalization via charge self-screening (the `bare → phys` transition, the running of `α`, §7.3), deferred to a separate work.

The bare mass is defined precisely on this domain: `m_e^bare` is the energy of the knot localized in the dyadic box `17 × 33`. The dyadic box, covering exactly both sectors of the knot (charge + mass), is what fixes the meaning of the "bare" slice.

### 5.2. Optimizer

Minimization is performed using `scipy.optimize.minimize` with `method='Nelder-Mead'`, `xatol = 1e-6`, `fatol = 1e-4` (keV). The choice of method is motivated by the following considerations:

1. The energy landscape over `(R_r, R_z, w)` is smooth but non-convex.
2. The topological constraint `Q_H = 1` is enforced exactly by the ansatz and requires no separate monitoring.
3. Gradient-based methods over the full field (Adam, L-BFGS) on a discrete grid induce drift of `Q_H` away from its integer value.

### 5.3. Convergence

```
R_r = 0.64082   (in units of l₀)
R_z = 0.80729
w   = 0.70200                                             (5.1)
```

### 5.4. Boundary conditions in z

For the `z`-derivatives, ghost cells constructed via linear extrapolation are used:
```
padded[Nz+i] = (i+1) · tensor[Nz-1] − i · tensor[Nz-2]
```

An alternative choice — periodic BC (via `torch.roll`) — is incorrect for this problem: the Hopf field is not periodic in `z`, and the periodic wrap introduces a jump at the boundaries `z = ±L_z/2`. This jump contributes to the bend term, growing with grid refinement, and leads to a divergence of the result under resolution increase. With linear extrapolation the grid convergence is preserved (`< 1 eV` per doubling).

### 5.5. Computing `E_u`: elimination of the u-channel

Numerically, for each `n` we find the optimal scalar mode `ψ` that parameterizes the u-channel response (see below) from the Euler–Lagrange equation of the functional (2.1)–(2.4) and substitute it back into the energy.

**Axisymmetric parameterization.** For the Hopf ansatz (§4) the u-channel response is conveniently parameterized by a single scalar function `ψ(r,z)` — the azimuthal component of the vector potential: `u = ∇×(ψ·φ̂)`. The displacement is then automatically divergence-free (`∇·u = 0`), and its meridional components are:
```
u_r = −∂ψ/∂z ,    u_z = ψ/r + ∂ψ/∂r ,    u_φ = 0                  (5.4)
```
In this symmetry the source `Π(n)` from (2.4) reduces to the azimuthal vector `Π(n) = f(n)·φ̂`, where `f(n) = atan2(√(n₁²+n₂²), n_z)` is the polar angle of the director.

**Reduction to a scalar equation.** The vector Euler–Lagrange equation `δE/δu = 0` of the functional (2.3)–(2.4), after reduction to the single mode `ψ`, takes the form of a screened scalar Poisson equation:
```
( ∂²_r + (1/r) ∂_r − 1/r² + ∂²_z − μ_c ) ψ  =  −2 f(n)             (5.5)
```
The `−1/r²` term is a direct consequence of the action of the **vector** Laplacian on the azimuthal component in cylindrical coordinates (the curvature of the basis vectors `φ̂`) — without it the tensor interpretation is lost.

The screening length `l_c = 1/√μ_c ≈ 0.399 l₀` plays the role of a **Yukawa mass** for the u-channel: the displacement `u` is exponentially suppressed on the scale `l_c` outside the region where `n` deviates from `n_∞`. The source `−2·f(n)` is geometric and `μ_c`-independent — it reflects the pure topology of the knot.

Remark on methodology. The scalar `ψ` is precisely one mode of the vector response, not a "stream function in place of a vector": the original functional (2.4) is tensorial, and the reduction to (5.5) is its equivalent in the class of axisymmetric configurations (a single scalar mode exhausts the vector response in this symmetry). A full-field 3D relaxation without axial symmetry must work with (2.4) directly; that work is deferred to a separate forthcoming publication (see §8).

**Numerical solution.** Equation (5.5) is solved by preconditioned conjugate gradients (PCG, diagonal preconditioning) on a uniform subgrid `512 × 1024` with extents `L_r^{(u)} = 6 l₀`, `L_z^{(u)} = 12 l₀`. The compactness of the subgrid is justified by the exponential decay of the solution on the scale `l_c ≪ L_r^{(u)}`. The source `f` is bilinearly interpolated from the stretched `n`-grid onto the uniform `ψ`-grid. On the outer boundary `r = L_r^{(u)}` a Robin condition is imposed, consistent with the `1/r` asymptotics of the screened solution; the PCG relative residual is driven down to `10⁻⁸`. With this condition the value of `E_u` is stable under refinement of the PCG subgrid — verified on subgrids from `512 × 1024` to `2048 × 4096`.

**Energy assembly.** From the resulting `ψ` the components `(u_r, u_z)` are reconstructed via (5.4), followed by the strain tensor in axisymmetry:
```
ε_rr = ∂u_r/∂r ,   ε_zz = ∂u_z/∂z ,   ε_φφ = u_r/r ,
ε_rz = ½ (∂u_r/∂z + ∂u_z/∂r)                                     (5.6)
```
and the elastic energy density:
```
E_u = ∫ ( ε_rr² + ε_zz² + ε_φφ² + 2 ε_rz² ) · 2π r dr dz         (5.7)
```
This is the quantity `E_u = 3.758 keV` of the table in §6.3 — the gravitational self-energy of the u-channel, induced by the presence of the EM-topology `n`.

**Remark on limits.** In the limit `μ_c → 0` (l_c → ∞), equation (5.5) loses its screening, the source `−2f` is retained, and `E_u` diverges in the UV like the self-energy of a point charge in classical electrodynamics. In the opposite limit `μ_c → ∞` (l_c → 0), the mass term suppresses `u` toward zero faster than the source can excite it: `u ≈ 2f/μ_c → 0`, and `E_u → 0`. The canonical value `μ_c = 2π` (3.3) provides `l_c ≈ 0.4 l₀` — of order `R_r` — the regime in which the u-channel contributes a finite but small share (`~0.8 %` of the mass; see §6.3). Physically this means that **the n↔u coupling cannot be removed by setting μ_c to zero** (this, on the contrary, drives `E_u` to a divergence): the source from the topology of `n` is always present, and `μ_c` only regulates the degree of its localization.

---

## 6. Results

### 6.1. Predicted electron mass

The functional minimum gives:

```
Ẽ_min = 1039.05  (dimensionless)                           (6.1)
E_min = M₀ c² · Ẽ_min = 429.5068 eV · 1039.05 = 446.279 keV
```

This is the **bare** electron mass — a direct output of the bare functional `E[n, u]`. The dimensionless minimum is numerically close to an integer in dyadic notation:

```
Ẽ_min       = 1039.05
2¹⁰ + 2⁴ − 1 = 1039
deviation   = +5.0·10⁻⁵  (= +0.0049 %, or +21.7 eV)        (6.2)
```

### 6.2. Topological charge preservation

```
Q_H = −0.99996   (electron, |Q_H| = 1 to ~4·10⁻⁵)            (6.3)
```

### 6.3. Energy decomposition

```
E_OF   (Frank–Oseen, K₁ + K₂ + K₃)        :  221.888 keV  (49.7 %)
E_Sk   (Skyrme stabilizer, c₄)             :  220.634 keV  (49.4 %)
E_u    (Cosserat coupling, μ_c)            :    3.758 keV  ( 0.8 %)
─────────────────────────────────────────────────────────────────
Total                                      :  446.279 keV  (100 %)   (6.4)
```

On the dyadic box the Frank–Oseen and Skyrme terms carry nearly equal shares (`49.7 %` and `49.4 %`) — the standard Derrick balance: under uniform rescaling Frank–Oseen scales as `λ` and Skyrme as `λ⁻¹`, and both are required at comparable magnitude to fix the soliton size [15]. The screened Cosserat coupling `E_u` contributes a small share (`0.8 %`).

### 6.4. Grid convergence

Under doubling of the grid resolution the value of `m_e^bare` shifts by less than `1 eV` (`~2·10⁻⁶` of `m_e^bare`). Grid convergence is stable, as is the conservation of the topological charge (`|Q_H| = 1` to `~4·10⁻⁵`).

### 6.5. Sensitivity analysis

From the identities of §3 the predicted scaling is:

```
m_e c²  ∝  ℏ^(3/4) · ε₀^(−5/8) · μ₀^(−3/8) · Ẽ_min        (6.5)
```

The dimensionless minimum `Ẽ_min` depends only on the dimensionless parameters `(K_i, μ_c, c₄)` and is invariant under rescaling of `{ε₀, μ₀, ℏ}`. Sensitivity to `+1 %` perturbations of each input constant:

```
δ(ε₀)/ε₀ = +1 %  →  δ(m_e c²) / m_e c² ≈ −0.625 %
δ(μ₀)/μ₀ = +1 %  →  δ(m_e c²) / m_e c² ≈ −0.375 %
δ(ℏ)/ℏ   = +1 %  →  δ(m_e c²) / m_e c² ≈ +0.750 %         (6.6)
```

---

## 7. Discussion

### 7.1. The bare character of the result

The obtained `m_e^bare = 446.279 keV` is the **bare** electron mass — the minimum of the bare Cosserat functional `E[n, u]` over the 3-parameter Hopf ansatz. It is a direct output of the functional: the value is not calibrated against any reference. It belongs to the bare (UV) slice of the construction: the same triple `{ε₀, μ₀, ℏ}` that fixes the constants of the functional (§3) also fixes the bare fine-structure constant `α_bare = 2⁻⁷ = 1/128` [1, §7]. Thus `446.279 keV` is the electron mass corresponding to `α_bare = 1/128`; its connection to the physical mass (corresponding to the measured `α(0) = 1/137`) is treated in §7.3.

### 7.2. Dyadic form of the dimensionless minimum

The dimensionless minimum of the functional `Ẽ_min = E_min / M₀c² = 1039.05` agrees with the integer `1039` to `~5·10⁻⁵`. This integer fits the dyadic form

```
Ẽ_min  =  m_e/M₀  =  x² + x/2 − 1,        x ≡ α⁻¹/4          (7.1)
```

where `x = α⁻¹/4` is the dimensionless parameter of the polynomial. The identity `m_e/M₀ = l₀/ƛ_C` (since `M₀ l₀ = ℏ/c` and `m_e ƛ_C = ℏ/c` — both masses lie on the hyperbola `m·l = ℏ/c`) gives an independent geometric interpretation of `Ẽ_min` itself, not of the variable `x`. For the bare value of the fine-structure constant `α_bare⁻¹ = 128 = 2⁷` [1] the scale is `x = 32 = 2⁵`, and

```
Ẽ_min  =  32² + 32/2 − 1  =  1024 + 16 − 1  =  1039          (7.2)
```

The three terms correspond to "area + half-perimeter + point" of the reduced 2D knot: `x² = 2¹⁰` (core), `x/2 = 2⁴` (mass shell), `−1` (center). The dyadic form (7.1) was obtained in a separate analysis of the dyadic structure of the program; here it is given as a **numerical observation** — its direct derivation from the functional `E[n, u]` has not been carried out.

> **Remark on scale.** Formula (7.1) is a **special case for the vacuum**, not a universal dependence for the electron in any state. It holds precisely because at the vacuum point of the hyperbola `m·l = ℏ/c` **one cell of medium mass (`M₀`) is identically equal to one unit of model (dimensionless) energy**: this is the boundary case of the "vacuum" knot, where both quantities (`α_bare = 1/128` and `M₀ = ℏ/(l₀c)`) are derived from the same constants `{ε₀, μ₀, ℏ}`. At other points of the hyperbola (the Compton limit `m_0_local = m_e`, `l_local = ƛ_C`, where "knot = one cell"; intermediate atomic scales) this equality breaks: one cell of medium ≠ one dimensionless unit, and **identity (7.1) in the same form no longer holds**.

### 7.3. Connection to the physical mass via the running of `α`

Formula (7.1) is a function of the single scale `x = α⁻¹/4`. The bare slice corresponds to `α_bare⁻¹ = 128` (`x = 32`); the physical electron is measured at `α(0)⁻¹ = 137.036` (`x = 34.259`). The same formula (7.1) at the physical `x` gives:

```
m_e^phys / M₀  =  34.259² + 34.259/2 − 1  =  1173.68 + 17.13 − 1  =  1189.81
m_e^phys c²    =  1189.81 · M₀c²  ≈  511.0 keV
```

— which agrees with the standard electron mass `m_e = 510.999 keV`. The ratio of the two slices:

```
m_e^bare / m_e^phys  =  1039 / 1189.81  =  0.8732               (7.3)
```

Since the charge is linear in `x` (`α⁻¹ = 4x`) and the mass is quadratic (`m_e/M₀ = x² + x/2 − 1`), to leading order `m_e ∝ x² ∝ 1/α²`. The pure square `(x_bare/x_phys)² = (32/34.259)² = 0.8725` differs from the full ratio (7.3) `0.8732` by `~0.09 %` — this discrepancy is fully accounted for by the sub-terms `+x/2 − 1` of formula (7.1). In other words, **one and the same shift `x: 32 → 34.259`** (equivalently — the running `α⁻¹: 128 → 137.036`) takes both the charge and the mass from their bare values to the physical ones.

This is given as a **numerical observation** (alongside §7.2), not as a derivation: the exponent `2`, the origin of the sub-terms `+x/2 − 1`, and the running of `α` itself from the Cosserat functional are not established in the present work — their derivation is the subject of a separate forthcoming work on the dyadic unification of charge, mass, and scale.

### 7.4. The nature of the obtained minimum: an ansatz-regularized upper bound

The obtained `m_e^bare c² = 446.279 keV` should be treated as the **minimum of the functional `E[n,u]` on the topological manifold of canonical Hopf configurations** (ansatz (4.2)), not as a global minimum in the unrestricted function space `n: ℝ³ → S²`. This distinction is essential for two reasons.

**First**, it makes the result a rigorous **upper bound** for the true continuum minimum: any additional freedom in the shape of the configuration can only lower the energy. This is consistent with the Lin–Yang existence theorem [24] for the continuum Faddeev–Skyrme minimum.

**Second**, it fixes **what exactly we compute** — not "the bare mass of a free particle as the global minimum of the functional", but the energy of a **canonically parameterized** configuration with `Q_H = ±1`, identified with the electron in the Cosserat vacuum. The 3-param ansatz (4.2) acts as an analytic regulator that cuts off the non-physical lattice modes of collapse (see §4.3).

**Numerical justification of the regulator's role.** The accompanying series of full-field L-BFGS relaxation tests (`verifications/grid_diagnostics/`, tests 2–9) shows:

- *Removing the ansatz* (full-field L-BFGS, same box `17×33`, same grid) lowers the energy to `~422 keV` (−5.4 % from 446). This is **not the true minimum** of the functional, but a discretization artifact: the ring radius `R_ring` contracts from the canonical `0.33 l₀` to the sub-grid values `0.02–0.1 l₀` depending on box/grid, with `E_Sk` paradoxically *dropping* (it should grow by Derrick).

- *Structural additions* — polar-angle stiffness `K_e|∇θ|²`, an effective Eringen γ `|∇×Π|²`, a BPS sextic `c₆(F·F)²`, a non-local Coulomb self-action with `α_bare = 1/128` — **do not prevent collapse** on the discrete grid. Each addition functions as an independent additive penalty term: the field finds a configuration minimizing the new term separately from the main collapse channel, and then continues the previous scenario with the same final `E_tot − E_extra ≈ 422 keV`. Physically this is tied to the UV catastrophe on the grid: barriers that diverge analytically as `R → 0` are, on a finite grid, truncated by the scale `Δx`, turning an infinite barrier into a finite penalty term.

- *Switching to a uniform grid* (Test 5c, `17×33`) aggravates the collapse to `R_ring = 0.018 l₀` with `E_tot = 393 keV`: a stretched grid with focusing `β_r = 6` near `r ~ R_r ~ l₀` provides **additional numerical protection** against sub-grid collapse by giving poor resolution at small `r`.

Thus the value `446.28 keV` is not a continuum minimum that happens to coincide with the ansatz, but a **physically meaningful quantity obtained precisely thanks to the ansatz as a regulator**. The discrete Faddeev–Skyrme theory without the ansatz loses its minimum on any finite grid (details in the technical appendix `grid_diagnostics/`).

**Path to removing the regularization.** Moving to full-field minimization without the ansatz requires two ingredients:

1. **Geometric discretization of the topological charge** in the spirit of Berg–Lüscher [26]: computing `Q_H` through solid angles on cells, not through local gradients — this makes the topological sector absolutely impenetrable to numerical collapse (any attempt to change `Q_H` requires passing through a Dirac singularity on a separate cell).

2. **Structural tuning of the functional** — moving into the BPS regime via the sixth-order term `c₆ (F·F)²` (Adam–Sanchez-Guillen–Wereszczynski [27, 28]), or an explicit account of the non-local electromagnetic stiffness. Our preliminary analysis (tests 6, 8, 9) shows that the standard forms of such additions without geometric discretization are ineffective; the structurally correct formulation remains an open question.

An implementation in this style is the subject of a separate forthcoming work. In the present work we fix `m_e^bare c² ≤ 446.279 keV` as a **topologically protected upper bound** obtained with ansatz regularization.

### 7.5. Position within the Cosserat program

The present work belongs to the tradition of deriving fundamental physics from the topology of a continuous medium. The main representatives of this line are the program of **G. E. Volovik** on the analogy between superfluid ³He-A and the Standard Model [19] and the program of **H. Kleinert** on multivalued fields, describing defects as gauge fields and gravity through torsion (Einstein–Cartan) [20]. The mathematical apparatus of all three programs is essentially common: Frank–Oseen-type elasticity for a director field on the sphere (for ³He-A — the l-vector of the orbital part), topological invariants of homotopy classes of mappings, and hopfions as stable configurations.

The principal difference lies in the choice of substrate. Volovik works with a concrete quantum medium (superfluid ³He-A at millikelvin temperatures), Kleinert — with an elastic continuum carrying dislocations and disclinations. The present work takes as the medium the physical vacuum itself: four identifications of medium parameters with the fundamental constants `{ε₀, μ₀, ℏ, G}` (see [1]) turn the abstract continuum into a concrete model from which a numerical bare electron mass `m_e^bare c² = 446.279 keV` is derived with zero free parameters.

More broadly, these programs share a related mathematical apparatus (Frank–Oseen elasticity for an `S²`-target field, topological invariants, hopfions). **One possible hypothetical unifying picture** is the KTHNY cascade of topological melting (Kosterlitz–Thouless–Halperin–Nelson–Young [22, 23]): a rigid crystal (Kleinert's "World Crystal"), an intermediate hexatic phase (liquid-crystalline, Frank–Oseen), and an isotropic liquid (close to superfluid ³He-A). Under this hypothetical picture, the present work would lie in the intermediate phase with particles as topological defects. **A rigorous verification of this picture for the physical vacuum** (including the numerical correspondence of the functional `E[n, u]` to the relevant KTHNY phase) **is not performed here and is left as an open direction**; it is mentioned only as one possible broad context, not as a claim of the program.

---

## 8. Conclusion

A **topologically protected upper bound** for the bare electron mass `m_e^bare c² ≤ 446.279 keV` is obtained numerically from the triple of vacuum constants `{ε₀, μ₀, ℏ}` by minimization of the Cosserat functional over the 3-parameter Hopf ansatz on the dyadic box `L = 17 × 33 l₀`. The result is stable under grid refinement (`< 1 eV` per doubling of the resolution) and invariant under grid/code rescaling (see §6.4); the topological charge is preserved (`|Q_H| = 1` to `~4·10⁻⁵`).

The 3-parameter Hopf ansatz acts as an **analytic regulator** that fixes the canonical geometry of a vortex tube with `Q_H = ±1` and cuts off the non-physical lattice modes of collapse, which inevitably arise in the discrete Faddeev–Skyrme model at large anisotropies `K₃/K₁` (§4.3, §7.4). The "rigid ansatz as a UV regulator" approach is standard in numerical hopfion physics [7, 8, 25] and does not diminish the significance of the obtained number as a **physically meaningful upper bound** for the continuum minimum, whose existence is guaranteed by the Lin–Yang theorem [24].

The dimensionless minimum `Ẽ_min ≈ 1039` fits the dyadic form `m_e/M₀ = x² + x/2 − 1` with the single scale `x = α⁻¹/4`: at the bare `α_bare⁻¹ = 128` (`x = 32`) it gives `1024 + 16 − 1 = 1039`. The same form at the physical `α(0)⁻¹ = 137` (`x = 34.26`) gives `1189.8` — i.e. `m_e^phys ≈ 511 keV`, agreeing with the standard mass `510.999 keV`. The same shift of the scale `x` that takes the bare `α` to the measured one takes the mass from its bare value to the physical one (§7.2–7.3).

The dyadic form is given as a **numerical observation**, not as a derivation: its direct derivation from the Cosserat functional `E[n, u]` is an open direction for future work.

A full-field relaxation without ansatz regularization — minimization over the entire director field `n: ℝ³ → S²` with a geometric discretization of the topological charge in the spirit of Berg–Lüscher [26] and structural tuning of the functional (likely via the sixth-order BPS term [27, 28] or an explicit non-local self-action channel) — is in preparation as a separate publication. Our series of diagnostic tests (`verifications/grid_diagnostics/`, tests 2–9) shows that the **standard forms** of structural additions (polar gradient, effective Eringen-γ, local BPS variants, Coulomb self-action with the natural `α_bare`) **do not prevent collapse on the current finite-difference discretization** — each functions as an independent additive penalty term due to the UV truncation of analytic divergences by the grid step. This result is itself of interest as a quantitative characterization of the **known numerical pathology of Faddeev–Skyrme models**.

---

## Methodology and use of AI tools

In preparing this work the author used the large language model **Claude (Anthropic)** to assist with writing Python scripts for the numerical minimization of the Cosserat functional, with the development of supporting modules (stretched grids, boundary conditions, diagnostics of the energy components), and with stylistic editing of the manuscript. All key physical postulates (the form of the functional, the choice of constants, and the ansatz), the interpretation of the results, and the conclusions are due to the author.

The author has thoroughly checked all generated code (grid convergence, conservation of the topological charge `Q`, invariance of the result under code/grid rescaling, see §6) and the manuscript text, and takes full responsibility for the final content and results of the work.

---

## Acknowledgements

The conceptual basis of this work draws on the ideas of **L. D. Faddeev** on topological solitons as particles, the fourth-derivative stabilizing term introduced by **T. H. R. Skyrme**, and the elastic theory of director media due to **C. W. Oseen** and **F. C. Frank**.

The computations were performed on a single NVIDIA RTX 2070 using PyTorch.

The discretization bug in the z-boundary conditions was identified through comparison of results across multiple grid resolutions during a diagnostic session on 2026-05-16.

---

## References

[1] **Yeusiyevich, I. V.** (2026). *Structural reduction of the SI base of units via the Cosserat-continuum hypothesis: electromagnetic and gravitational quantities as mechanical objects of an elastic medium*. Zenodo preprint. DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

[2] F. and E. Cosserat, *Théorie des corps déformables*, Hermann, Paris (1909).

[3] A. C. Eringen, *Microcontinuum Field Theories. I: Foundations and Solids*, Springer, New York (1999).

[4] C. W. Oseen, "The Theory of Liquid Crystals", *Trans. Faraday Soc.* **29**, 883 (1933).

[5] F. C. Frank, "On the Theory of Liquid Crystals", *Discuss. Faraday Soc.* **25**, 19 (1958).

[6] T. H. R. Skyrme, "A Non-linear Field Theory", *Proc. Roy. Soc. A* **260**, 127 (1961).

[7] L. Faddeev and A. J. Niemi, "Stable knot-like structures in classical field theory", *Nature* **387**, 58 (1997).

[8] R. A. Battye and P. M. Sutcliffe, "Knots as Stable Soliton Solutions in a Three-dimensional Classical Field Theory", *Phys. Rev. Lett.* **81**, 4798 (1998).

[9] A. S. Eddington, *The Mathematical Theory of Relativity*, 2nd ed., Cambridge University Press (1924).

[10] A. Wyler, "L'espace symétrique du groupe des équations de Maxwell", *C. R. Acad. Sci. Paris* **269**, 743 (1969).

[11] B. Robertson, "Wyler's expression for the fine-structure constant α", *Phys. Rev. Lett.* **27**, 1545 (1971).

[12] M. Atiyah, *The Fine Structure Constant*, preprint (2018).

[13] P. G. de Gennes and J. Prost, *The Physics of Liquid Crystals*, 2nd ed., Oxford University Press (1993).

[14] M. Kléman and O. D. Lavrentovich, *Soft Matter Physics: An Introduction*, Springer (2003).

[15] G. H. Derrick, "Comments on Nonlinear Wave Equations as Models for Elementary Particles", *J. Math. Phys.* **5**, 1252 (1964).

[16] J. H. C. Whitehead, "An Expression of Hopf's Invariant as an Integral", *Proc. Nat. Acad. Sci. USA* **33**, 117 (1947).

[17] L. D. Faddeev, *Quantization of Solitons*, preprint IAS-75-QS70 (1975).

[18] CODATA Recommended Values of the Fundamental Physical Constants 2018, *Rev. Mod. Phys.* **93**, 025010 (2021).

[19] G. E. Volovik, *The Universe in a Helium Droplet*, Oxford University Press (2003). — analogy program between superfluid ³He-A and fundamental physics; emergent fermions and gauge fields from the topology of Fermi points.

[20] H. Kleinert, *Multivalued Fields in Condensed Matter, Electromagnetism, and Gravitation*, World Scientific, Singapore (2008). — multivalued fields; dislocations/disclinations as gauge fields; gravity via torsion (Einstein–Cartan).

[21] V. P. Mineev and G. E. Volovik, "Planar and linear solitons in superfluid ³He", *Phys. Rev. B* **18**, 3197 (1978). — Frank–Oseen functional for the l-vector in ³He-A.

[22] B. I. Halperin and D. R. Nelson, "Theory of Two-Dimensional Melting", *Phys. Rev. Lett.* **41**, 121 (1978). — KTHNY theory: melting via the unbinding of topological defect pairs; the intermediate hexatic phase.

[23] A. P. Young, "Melting and the vector Coulomb gas in two dimensions", *Phys. Rev. B* **19**, 1855 (1979). — cascade of phase transitions through dissociation of dislocations and disclinations; completion of the KTHNY picture.

[24] F. Lin and Y. Yang, "Existence of energy minimizers as stable knotted solitons in the Faddeev model", *Comm. Math. Phys.* **249**, 273 (2004). — rigorous proof of the existence of topologically non-trivial minimizers of the Faddeev functional in suitable Sobolev spaces.

[25] P. M. Sutcliffe, "Knots in the Skyrme–Faddeev model", *Proc. Roy. Soc. A* **463**, 3001 (2007). — review of numerical results for hopfions and discussion of the difficulties of discretizing topologically non-trivial configurations.

[26] B. Berg and M. Lüscher, "Definition and statistical distributions of a topological number in the lattice O(3) σ-model", *Nucl. Phys. B* **190**, 412 (1981); N. S. Manton and B. M. A. G. Piette, "Understanding Skyrmions using rational maps", *Prog. Math.* **201**, 469 (2001). — geometric discretization of the topological charge through solid angles on cells and the rational-map ansatz for lattice Skyrme/σ-models.

[27] C. Adam, J. Sanchez-Guillen and A. Wereszczynski, "A Skyrme-type proposal for baryonic matter", *Phys. Lett. B* **691**, 105 (2010). — BPS Skyrme model with a sixth-order stabilizer giving exact-BPS solitons of fixed geometry.

[28] C. Adam, C. Naya, J. Sanchez-Guillen and A. Wereszczynski, "Nuclear binding energies from a Bogomol'nyi–Prasad–Sommerfield Skyrme model", *Phys. Rev. C* **88**, 054313 (2013). — application of the BPS formulation to nuclear matter; the role of the sixth-order term as a structural stiffness stabilizer.

---

## Appendix A. Reproducibility recipe

```
verifications/electron_mass_minimization/
├── nm_minimization.py     # main minimization script
├── stretched_grid.py      # grid utilities, energy, Cosserat solver
├── requirements.txt
├── README.md
└── result.json            # output (created upon run)
```

Reproduction in three commands:

```bash
cd verifications/electron_mass_minimization
pip install -r requirements.txt
python nm_minimization.py
```

The script builds the Cosserat functional and minimizes by Nelder–Mead on the `1024 × 2048` grid from the standard initial simplex `(0.50, 0.70, 0.60)`.

Expected canonical output:

```
R_r ≈ 0.64082,    R_z ≈ 0.80729,    w ≈ 0.70200
Q_H ≈ −0.99996
E_OF = 221.888 keV (49.7 %)   E_Sk = 220.634 keV (49.4 %)
E_u  =   3.758 keV ( 0.8 %)
E_total = 446.279 keV  (= m_e^bare;  Ẽ_min ≈ 2¹⁰+2⁴−1, see §7.2)
```

A typical run converges in `~ 90` simplex iterations (`172` function evaluations); wall time on a single NVIDIA RTX 2070 is of order `6` minutes.

---

## Appendix B. The functional in dimensionless form

In dimensionless variables (`r̃ = r/l₀`) the functional of §2 takes the form:

```
Ẽ[n, u]  =  Ẽ_n[n]  +  Ẽ_u[u]  +  Ẽ_int[n, u]              (B.1)

Ẽ_n[n] = ∫ d³r̃ [
    (K̃₁/2) (∇̃·n)²
  + (K̃₂/2) (n·∇̃×n)²
  + (K̃₃/2) (n×∇̃×n)²
  + (c̃₄/4) F̃_ij F̃^ij           ,  F̃_ij = n·(∂̃_i n × ∂̃_j n)
]                                                          (B.2)

Ẽ_u[u] + Ẽ_int[n, u] = ½ μ̃_c ∫ d³r̃ | ∇̃×u − Π(n) |²        (B.3)

(in the axisymmetric reduction — `Π(n) = f(n)·φ̂`,
`u = ∇̃×(ψ·φ̂)`, and (B.3) reduces to the screened
scalar Poisson equation (5.5))                            (B.4)
```

with dimensionless coefficients `{K̃₁, K̃₂, K̃₃, μ̃_c, c̃₄} = {2, 2, 14.566, 2π, 1}` (§3).

The mass in physical units: `m_e^bare c² = M₀ c² · Ẽ_min`.

---

## Appendix C. Data and code availability

The code is in the repository:

```
https://github.com/igorevsiev-cmyk/cosserat-program
```

Supplementary materials in `papers/2026-05-electron-mass/`. The preprint is accompanied by numerical checks:

- `verifications/electron_mass_minimization/` — the Nelder-Mead minimization (reproduces `m_e^bare = 446.279 keV`);
- `verifications/canonical_derrick/` — Derrick stability scan.

The preprint is registered on Zenodo: [10.5281/zenodo.20477123](https://doi.org/10.5281/zenodo.20477123).

The preceding work [1] is registered with DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

---
