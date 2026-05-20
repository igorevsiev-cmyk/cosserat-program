# Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e^bare = 446.279 keV`

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-05-20
**Type:** preprint
**License:** CC-BY 4.0

---

## Abstract

The electron mass `m_e c² = 510.998950 ± 0.000015 keV` (CODATA 2018) is an empirical input in the Standard Model; no derivation from more fundamental constants exists.

In the present work `m_e` is computed numerically from three vacuum constants `{ε₀, μ₀, ℏ}` by minimizing the Cosserat functional `E[n, u]` of a director field `n: ℝ³ → S²` over a three-parameter Hopf ansatz with topological charge `Q_H = 1`. All constants of the functional are fixed by structural identities from the preceding work [1]:

- lattice scale `l₀⁴ = ℏ/(2π Z₀)`, with `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω`;
- base mass scale `M₀ c² = ℏc/l₀ ≈ 429.5068 eV`;
- Cosserat coupling `μ_c = η = 2π`;
- elastic anisotropy `K₃/K₁ − 1 = η`, with `K₁ = K₂ = 2`, `K₃ = 2(1 + 2π) ≈ 14.566`;
- Skyrme term `c₄ = 1`.

Minimization by the Nelder–Mead simplex method on a stretched cylindrical grid of resolution `1024 × 2048` (dyadic box `L = 17 × 33 l₀`) gives:

> `m_e^bare c² = 446.279 keV`

This value is the **bare** electron mass in the Cosserat vacuum: a direct output of the bare functional `E[n, u]`. The dimensionless minimum `Ẽ_min = E_min/M₀c² ≈ 1039` fits the dyadic form `m_e/m₀ = x² + x/2 − 1` with a single scale `x = α⁻¹/4`: at the bare `α_bare⁻¹ = 128` (`x = 32`) it gives `1024 + 16 − 1 = 1039`, at the physical `α(0)⁻¹ = 137` (`x = 34.26`) — `1189.8`, i.e. `m_e^phys ≈ 511 keV`. The same shift of the scale `x` that takes the bare `α` to the measured one takes the bare mass to the physical one (§7.2–7.3). The dyadic form is given as a numerical observation, not as a derivation.

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
 Dyadic form  m_e/m₀ = x² + x/2 − 1,  x = α⁻¹/4
   bare:  32² + 16 − 1 = 1039       → 446.3 keV     (§7.2)
   phys:  34.26² + 17.1 − 1 ≈ 1190  → 511.0 keV     (§7.3)
 charge ~ x, mass ~ x²  ⟹  m_e ∝ 1/α² (leading order)
```

Minimization is reproducible via the standalone script `verifications/electron_mass_minimization/nm_minimization.py` (see Appendix A).

---

## 1. Introduction

### 1.1. The electron mass in the Standard Model

`m_e c² = 510.998950 ± 0.000015 keV` enters the Standard Model as an empirical parameter. The Yukawa coupling `y_e ≈ 2.94 × 10⁻⁶` is fixed by this value; its smallness relative to the top-quark Yukawa (`y_t ≈ 1`) has no independent explanation.

Earlier attempts to derive `m_e` from deeper structure (Eddington 1924 [9], Wyler 1969 [10], Atiyah 2018 [12]) were either numerological or relied on arbitrary normalization choices.

### 1.2. The Cosserat-vacuum hypothesis

The preceding work [1] showed that, under four structural identifications, the SI base reduces to a single dimension (energy), and the electromagnetic and gravitational sectors are accommodated in a single Cosserat continuum. The functional `E[n, u]` in this medium admits localized minima with integer `Q_H ∈ π₃(S²) = ℤ`. The minimum `Q_H = −1` is identified with the electron.

The present work computes the mass of this minimum.

### 1.3. Approach

1. The Cosserat functional is constructed; all its constants are fixed by the triple `{ε₀, μ₀, ℏ}` (§3).
2. Minimization is performed by the Nelder–Mead method over the 3-param Hopf ansatz on a `1024 × 2048` grid (§§4–5).
3. The minimum is converted to SI units via `M₀ c² = ℏc/l₀` (§6).

The result is the bare electron mass `m_e^bare c² = 446.279 keV`. This is a direct output of the bare functional `E[n, u]`; the value is not compared with the physical (measured) mass `m_e` — the derivation of the bare → physical relation is left as an open direction (§7).

---

## 2. The Cosserat functional

A Cosserat medium is described by two independent field variables: a microrotation parameterized by the director `n(r) ∈ S²` and a translational displacement `u(r) ∈ ℝ³`. The energy functional decomposes into three blocks:

```
E[n, u]  =  E_n[n]   +   E_u[u]   +   E_int[n, u]                       (2.1)
```

**Block E_n — energy of the director channel** (Frank–Oseen + Skyrme):
```
E_n[n] = ∫ d³r [
    (K₁/2) (∇·n)²                ← splay                (Frank, 1958)
  + (K₂/2) (n·∇×n)²              ← twist                (Frank, 1958)
  + (K₃/2) (n×∇×n)²              ← bend                 (Frank, 1958)
  + (c₄/4) [(∇n)² ⊗ (∇n)²]       ← Skyrme stabilizer    (Skyrme, 1961)
]                                                                       (2.2)
```

**Block E_u — energy of the translational channel** (elasticity + Yukawa mass term):
```
E_u[u] = ∫ d³r [ (μ/2) (∂u)² + (μ_c/2) u² ]                              (2.3)
```

**Block E_int — linear n→u coupling** (geometric source from director topology):
```
E_int[n, u] = − ∫ d³r [ 2·f(n) · u ],     f(n) = atan2(√(n₁²+n₂²), n_z)  (2.4)
```

Here `n_∞ = ẑ` is the boundary value at infinity; `f(n)` is the polar angle of the director from the vacuum direction (0 at infinity, π at the knot core); `μ` is the elastic modulus (in natural units `μ = 1`).


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

The dimensionless constant `η` is defined as the **ratio of the intrinsic quantum energy of a single cell of the medium to its elastic energy**:

```
η  =  ℏω_gyro / (K · l₀³)
```

Each factor has a direct physical meaning.

**Numerator: `ℏω_gyro` — the minimum-energy quantum of the gyroscope.**
The frequency `ω_gyro` follows from the quantization of the angular momentum of a gyroscope of size `l₀`: the moment of inertia `I ~ m₀·l₀²` and the angular momentum `L ~ ℏ` give
```
ω_gyro = L/I = ℏ/(m₀·l₀²) = c/l₀
```
(using the identity `m₀·l₀ = ℏ/c`). The energy of one rotation quantum is
```
ℏω_gyro = ℏc/l₀ = M₀c² ≈ 429.5 eV
```

**Denominator: `K · l₀³` — the elastic energy of one cell.**
`K` is the Frank constant with dimensions `[energy/length]`. It is related to the base shear modulus by `K = μ · l₀`, where `μ ≡ 1/ε₀` (postulate P2 of [1]). Therefore `K · l₀³ = μ · l₀⁴` — the energy stored when the field `n` is deformed by O(1) over the volume of one cell.

**Substituting the fundamental length scale** `l₀⁴ = ε₀ℏc/(2π)` (see (3.1)) gives:

```
η  =  ℏc / (μ · l₀⁴)
   =  ℏc · ε₀ · (2π) / (ε₀·ℏc)
   =  2π
```

This is not a free parameter but an algebraic consequence of the triple `{ε₀, μ₀, ℏ}`. The physical meaning of the result: in the vacuum Cosserat medium the quantum "trembling" of the field `n` and the elastic stiffness of the medium are of the same order and differ by exactly the factor `2π`.

### 3.4. Elastic anisotropy `K₃/K₁`

```
K₁ = K₂ = 2,    K₃ = K₁ · (1 + η) = 2 · (1 + 2π) ≈ 14.566    (3.4)
```

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

---

## 5. Numerical method

### 5.1. Grid

A cylindrical grid `(r_i, z_j)` of size `N_r × N_z = 1024 × 2048` with clustering near `r ~ R_r` and `z ~ 0` (stretching exponents `β_r = 6.0`, `β_z = 3.0`). Box dimensions: `L_r = 17 l₀`, `L_z = 33 l₀` (`L_z = 2·L_r − 1`; justification of `L_r` below). Double precision (`float64`) throughout.

The box size is not arbitrary: it corresponds to the combined extent of the two sectors of the knot. The charge field reaches `99.9 %` of its full magnitude at `R_charge ≈ 7 l₀`; the mass sector — described by the dyadic polynomial `m_e/m₀ = x² + x/2 − 1` (`x = α⁻¹/4`, see §7.2) — is localized within `R_mass ≈ 10 l₀`; both radii are confirmed numerically. Their sum sets the radial box size:

```
L_r = R_charge + R_mass = 7 + 10 = 17
```

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

An alternative choice — periodic BC (via `torch.roll`) — is incorrect for this problem: the Hopf field is not periodic in `z`, and the periodic wrap introduces a jump at the boundaries `z = ±L_z/2`. This jump contributes to the bend term and the contribution grows with grid refinement, leading to a divergence of the result under resolution increase. With linear extrapolation the grid convergence is preserved (`< 1 eV` per doubling).

### 5.5. Computing `E_u`: elimination of the u-channel

Numerically we solve the problem honestly: for each `n` the optimal `u` is found from the Euler–Lagrange equation of the functional (2.1)–(2.4) and substituted back into the energy.

**Derivation of the equation.** The `u`-dependent part of the functional is `E_u[u] + E_int[n,u]`:
```
∫ d³r [ (μ/2)(∂u)² + (μ_c/2) u² − 2·f(n)·u ]                     (5.2)
```
with `μ = 1` in natural units. The minimization condition `δ/δu = 0` gives the linear equation
```
( ∇² − μ_c ) u  =  −2·f(n)                                       (5.3)
```
— a screened Poisson equation with screening length `l_c = 1/√μ_c ≈ 0.399 l₀`. The term `−μ_c` plays the role of a **Yukawa mass for the u-channel**: the displacement `u` is exponentially suppressed on the scale `l_c` outside the region where `n` deviates from `n_∞`. The source `−2·f(n)` is geometric and `μ_c`-independent — it reflects the pure topology of the knot.

**Axisymmetric representation.** In cylindrical geometry one introduces a stream function `ψ(r,z)` that automatically enforces `∇·u = 0`:
```
u_r = −∂ψ/∂z ,    u_z = ψ/r + ∂ψ/∂r                              (5.4)
```
Substituting (5.4) into (5.3) yields a scalar equation for `ψ`:
```
( ∂²_r + (1/r) ∂_r − 1/r² + ∂²_z − μ_c ) ψ  =  −2 f               (5.5)
```
The `−1/r²` term arises from the curvature of cylindrical basis vectors when the vector Laplacian acts on the azimuthal component.

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

**Remark on limits.** In the limit `μ_c → 0` (l_c → ∞), equation (5.3) loses its screening while the source `−2f` is retained, and `E_u` diverges in the UV like the self-energy of a point charge in classical electrodynamics. In the opposite limit `μ_c → ∞` (l_c → 0), the mass term pushes `u` toward zero faster than the source can excite it: `u ≈ 2f/μ_c → 0`, and `E_u → 0`. The canonical value `μ_c = 2π` (3.3) provides `l_c ≈ 0.4 l₀` — of order `R_r` — the regime in which the u-channel contributes a finite but small share (`~0.8 %` of the mass; see §6.3). Physically this means that **the n↔u coupling cannot be switched off by setting μ_c to zero** (this, on the contrary, drives `E_u` to infinity): the source from the topology of `n` is always present, and `μ_c` only regulates the degree of its localization.

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

The obtained `m_e^bare c² = 446.279 keV` is the **bare** electron mass — the minimum of the bare Cosserat functional `E[n, u]` over the 3-parameter Hopf ansatz. It is a direct output of the functional: the value is not calibrated against any reference. It belongs to the bare (UV) slice of the construction: the same triple `{ε₀, μ₀, ℏ}` that fixes the constants of the functional (§3) also fixes the bare fine-structure constant `α_bare = 2⁻⁷ = 1/128` [1, §7]. Thus `446.279 keV` is the electron mass corresponding to `α_bare = 1/128`; its connection to the physical mass (corresponding to the measured `α(0) = 1/137`) is treated in §7.3.

### 7.2. Dyadic form of the dimensionless minimum

The dimensionless minimum of the functional `Ẽ_min = E_min / M₀c² = 1039.05` agrees with the integer `1039` to `~5·10⁻⁵`. This integer fits the dyadic form

```
Ẽ_min  =  m_e/m₀  =  x² + x/2 − 1,        x ≡ α⁻¹/4          (7.1)
```

where `x` is the single geometric scale (the number of Compton lengths in a vacuum cell, `x = l₀/ƛ_C`). For the bare value of the fine-structure constant `α_bare⁻¹ = 128 = 2⁷` [1] the scale is `x = 32 = 2⁵`, and

```
Ẽ_min  =  32² + 32/2 − 1  =  1024 + 16 − 1  =  1039          (7.2)
```

The three terms correspond to "area + half-perimeter + point" of the reduced 2D knot: `x² = 2¹⁰` (core), `x/2 = 2⁴` (mass shell), `−1` (center). The dyadic form (7.1) was obtained in a separate analysis of the dyadic structure of the program; here it is given as a **numerical observation** — its direct derivation from the functional `E[n, u]` has not been carried out.

### 7.3. Connection to the physical mass via the running of `α`

Formula (7.1) is a function of the single scale `x = α⁻¹/4`. The bare slice corresponds to `α_bare⁻¹ = 128` (`x = 32`); the physical electron is measured at `α(0)⁻¹ = 137.036` (`x = 34.259`). The same formula (7.1) at the physical `x` gives:

```
m_e^phys / m₀  =  34.259² + 34.259/2 − 1  =  1173.68 + 17.13 − 1  =  1189.81
m_e^phys c²    =  1189.81 · M₀c²  ≈  511.0 keV
```

— which agrees with the standard electron mass `m_e = 510.999 keV`. The ratio of the two slices:

```
m_e^bare / m_e^phys  =  1039 / 1189.81  =  0.8732               (7.3)
```

Since the charge is linear in `x` (`α⁻¹ = 4x`) and the mass is quadratic (`m_e/m₀ = x² + x/2 − 1`), to leading order `m_e ∝ x² ∝ 1/α²`. The pure square `(x_bare/x_phys)² = (32/34.259)² = 0.8725` differs from the full ratio (7.3) `0.8732` by `~0.09 %` — this discrepancy is fully accounted for by the sub-terms `+x/2 − 1` of formula (7.1). In other words, **one and the same shift `x: 32 → 34.259`** (equivalently — the running `α⁻¹: 128 → 137.036`) takes both the charge and the mass from their bare values to the physical ones.

This is given as a **numerical observation** (alongside §7.2), not as a derivation: the exponent `2`, the origin of the sub-terms `+x/2 − 1`, and the running of `α` itself from the Cosserat functional are not established in the present work — their derivation is the subject of a separate forthcoming work on the dyadic unification of charge, mass, and scale.

### 7.4. Position within the Cosserat program

The present work belongs to the tradition of deriving fundamental physics from the topology of a continuous medium. The main representatives of this line are the program of **G. E. Volovik** on the analogy between superfluid ³He-A and the Standard Model [19] and the program of **H. Kleinert** on multivalued fields, describing defects as gauge fields and gravity through torsion (Einstein–Cartan) [20]. The mathematical apparatus of all three programs is essentially common: Frank–Oseen-type elasticity for a director field on the sphere (for ³He-A — the l-vector of the orbital part), topological invariants of homotopy classes of mappings, and hopfions as stable configurations.

The principal difference lies in the choice of substrate. Volovik works with a concrete quantum medium (superfluid ³He-A at millikelvin temperatures), Kleinert — with an elastic continuum carrying dislocations and disclinations. The present work takes as the medium the physical vacuum itself: four identifications of medium parameters with the fundamental constants `{ε₀, μ₀, ℏ, G}` (see [1]) turn the abstract continuum into a concrete model from which a numerical bare electron mass `m_e^bare c² = 446.279 keV` is derived with zero free parameters.

More broadly, these programs share a related mathematical apparatus (Frank–Oseen elasticity for an `S²`-target field, topological invariants, hopfions). **One possible hypothetical unifying picture** is the KTHNY cascade of topological melting (Kosterlitz–Thouless–Halperin–Nelson–Young [22, 23]): a rigid crystal (Kleinert's "World Crystal"), an intermediate hexatic phase (liquid-crystalline, Frank–Oseen), and an isotropic liquid (close to superfluid ³He-A). Under this hypothetical picture, the present work would lie in the intermediate phase with particles as topological defects. **A rigorous verification of this picture for the physical vacuum** (including the numerical correspondence of the functional `E[n, u]` to the relevant KTHNY phase) **is not performed here and is left as an open direction**; it is mentioned only as one possible broad context, not as a claim of the program.

---

## 8. Conclusion

The **bare** electron mass `m_e^bare = 446.279 keV` is obtained numerically from the triple of vacuum constants `{ε₀, μ₀, ℏ}` by minimization of the Cosserat functional over the 3-parameter Hopf ansatz on the dyadic box `L = 17 × 33 l₀`. The result is stable under grid refinement (`< 1 eV` per doubling of the resolution) and invariant under grid/code rescaling (see §6.4); the topological charge is preserved (`|Q_H| = 1` to `~4·10⁻⁵`).

The dimensionless minimum `Ẽ_min ≈ 1039` fits the dyadic form `m_e/m₀ = x² + x/2 − 1` with the single scale `x = α⁻¹/4`: at the bare `α_bare⁻¹ = 128` (`x = 32`) it gives `1024 + 16 − 1 = 1039`. The same form at the physical `α(0)⁻¹ = 137` (`x = 34.26`) gives `1189.8` — i.e. `m_e^phys ≈ 511 keV`, agreeing with the standard mass `510.999 keV`. The same shift of the scale `x` that takes the bare `α` to the measured one takes the mass from its bare value to the physical one (§7.2–7.3).

The dyadic form is given as a **numerical observation**, not as a derivation: its direct derivation from the Cosserat functional `E[n, u]` is an open direction for future work.

A full-field relaxation — minimization over the entire director field `n: ℝ³ → S²` without the restriction to the 3-parameter ansatz, requiring the gravitational `u`-channel to be coupled to a mass term of the functional — is in preparation as a separate publication.

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

[1] **Yeusiyevich, I. V.** (2026). *Structural reduction of the SI base via the Cosserat-continuum hypothesis: electromagnetic and gravitational quantities as mechanical objects of an elastic medium*. Zenodo preprint. DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

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
  + (c̃₄/4) [(∇̃n)² ⊗ (∇̃n)²]
]                                                          (B.2)

Ẽ_u[u] = ∫ d³r̃ [ (1/2)(∂̃u)² + (μ̃_c/2) u² ]                (B.3)

Ẽ_int[n, u] = − ∫ d³r̃ [ 2·f(n) · u ]                       (B.4)
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

The preprint is registered on Zenodo: [10.5281/zenodo.20205502](https://doi.org/10.5281/zenodo.20205502).

The preceding work [1] is registered with DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

---
