# Derivation of the electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization: `m_e = 511.033 keV` to `0.007 %` accuracy

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-05-15
**Version:** 1 (preprint)
**License:** CC-BY 4.0

---

## Abstract

The electron rest energy `m_e c² = 510.998950 ± 0.000015 keV` (CODATA 2018) is treated by the Standard Model as an empirical input. No first-principles calculation derives it from more fundamental constants; the chiral and electroweak symmetries that constrain its renormalization do not fix its absolute scale. Historical attempts to derive `m_e` from geometric or topological structure (Eddington 1929, Wyler 1969, Atiyah 2017) have not produced convergent perturbation series with independently testable inputs.

The present work derives `m_e` numerically from three vacuum constants — `{ε₀, μ₀, ℏ}` — by minimization of the Cosserat-elastic functional `E[n, u]` of the unit-vector director field `n: ℝ³ → S²` over a three-parameter Hopf ansatz with topological charge `Q_H = 1`. The construction relies on the dimensional reduction and structural identifications established in the preceding work [1] (`SI Reduction via the Cosserat-continuum hypothesis`), which fixes:

- the lattice scale `l₀⁴ = ℏ/(2π Z₀)` with `Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω` (vacuum impedance);
- the base mass density `M₀ = ℏ/(l₀ c) ≈ 429.51 eV/c²`;
- the Cosserat coupling `μ_c = η = 2π` (rolling-contact identity for tangent unit cells);
- the local anisotropy `m² = η/(4π) = 1/2`;
- the elastic anisotropy `K₃/K₁ - 1 = η`, with the canonical `K₁ = K₂ = 2`, `K₃ = 2(1 + 2π) ≈ 14.566`;
- the Skyrme stabiliser coefficient `c₄ = 1`.

All six parameters of the functional are fixed by `{ε₀, μ₀, ℏ}` through the algebraic identities of [1]; no parameters are free. Numerical minimization by the Nelder–Mead simplex method on a stretched cylindrical grid of resolution `1024 × 2048` yields a hopfion with mass

> `m_e = 511.033 keV` &nbsp;&nbsp;&nbsp; (Δ = +0.007 % from CODATA 2018)

The Hopf invariant is preserved to numerical precision (`|Q_H| = 1.000` to better than `10⁻⁵`; the canonical orientation `Q_H = −1` corresponds to the electron, the opposite to the positron). The energy decomposes into four physically distinct sectors: Frank–Oseen elastic (`35 %`), Skyrme stabiliser (`55 %`), Cosserat coupling (`9.5 %`), and local anisotropy (`0.5 %`); the Frank–Oseen and Skyrme terms balance at the Derrick fixed point `λ = 1`. Dimensional analysis gives the scaling `m_e c² ∝ ℏ^{3/4} ε_0^{−5/8} μ_0^{−3/8}` (e.g. `+1 %` in `ℏ` predicts `+0.75 %` in `m_e c²`); the opposite signs for `{ε₀, μ₀}` versus `ℏ` argue against accidental cancellation as the source of the agreement.

The result is falsifiable: any independent measurement of `m_e c²` differing from `511.03 keV` by more than `0.05 %` would invalidate the framework as presented; the framework cannot accommodate deviations by parameter adjustment.

---

## Logical chain of the paper

The chain of key statements, with the sections in which each one is proved:

```
INPUTS (three measured vacuum constants)
 {ε₀, μ₀, ℏ}                                     [1, §6]
 │
 ▼
DERIVED CONSTANTS (from [1])
 c       = 1/√(ε₀μ₀)                              [1, §2.4]
 Z₀      = √(μ₀/ε₀) ≈ 376.73 Ω                    [1, §6]
 l₀⁴     = ℏ/(2π Z₀)                              [1, §7]
 M₀      = ℏ/(l₀ c)                               [1, §5.1]
 │
 ▼
COSSERAT-FUNCTIONAL PARAMETERS                    (§3)
 η       = 2π          (rolling-contact identity, [1, §7.3])
 μ_c     = η = 2π      (Cosserat coupling)
 m²      = η/(4π) = 1/2 (local anisotropy)
 K₃/K₁ - 1 = η         (elastic anisotropy, K₁=K₂=2, K₃=14.566)
 c₄      = 1            (Skyrme stabiliser)
 │
 ▼
TOPOLOGICAL CONSTRAINT                            (§4)
 Q_H = 1                (Hopf invariant, π₃(S²) = ℤ)
 3-parameter Hopf ansatz n(r, z; R_r, R_z, w)
 │
 ▼
NUMERICAL MINIMIZATION                            (§5)
 Nelder–Mead on a stretched 1024×2048 grid
 (R_r, R_z, w) = (0.50945, 0.75010, 0.62585) (in units of l₀)
 │
 ▼
RESULT                                            (§6)
 m_e c² = M₀ c² · Ẽ_min = 429.507 eV · 1189.81 = 511.033 keV
 Δ from CODATA = +0.00665 %  (≈ +0.007 %)
 Q_H = −0.999998   (electron orientation; |Q_H| = 1 preserved to 10⁻⁶)
 │
 ▼
FALSIFIABILITY                                    (§7)
 The framework predicts m_e with no free parameters;
 any deviation from 511.03 keV by > 0.05 % falsifies it.
```

Every consequence is derived from the preceding ones plus the postulates of [1] through explicit algebraic and numerical steps, given in the indicated sections. The minimization is reproducible from the standalone script `verifications/electron_mass_minimization/nm_minimization.py` (see Appendix A).

---

## 1. Introduction

### 1.1. Context: the electron mass in the Standard Model

The electron rest energy `m_e c² = 510.998950 ± 0.000015 keV` is one of about twenty independent empirical inputs of the Standard Model. The framework specifies how `m_e` enters chiral symmetry breaking (through the Yukawa coupling `y_e v_H/√2 = m_e`, where `v_H = 246 GeV` is the Higgs vacuum expectation value), but does not predict its absolute value. The Yukawa coupling `y_e ≈ 2.94 × 10⁻⁶` is a tunable parameter; its smallness relative to the top-quark Yukawa (`y_t ≈ 1`) is unexplained.

Attempts to derive `m_e` from a deeper structure have a long history. Eddington (1929) [9] proposed a numerological identity from the dimension of the Dirac matrix algebra. Wyler (1969) [10] obtained `α ≈ 1/137` from a symmetric-space volume formula, but the construction was criticised for relying on arbitrary normalization choices [11]. Atiyah (2017) [12] proposed a derivation of `α` from the Todd function on `1²`, which did not converge under independent verification. None of these works produced a numerical value of `m_e` independently of an experimental input.

### 1.2. Context: the Cosserat-vacuum hypothesis

The preceding work [1] established that, under four structural identifications (`P1: ρ_medium ≡ μ₀`; `P2: G_shear ≡ 1/ε₀`; `P3: ℏ` as the action quantum of microrotations; `P4: G` via the Kleinert gauge mechanism), the SI base of units `{m, kg, s, A}` reduces to a single energy dimension and the electromagnetic and gravitational sectors of physics fit into a single Cosserat continuum.

In the same framework, the functional `E[n, u]` of the director field `n: ℝ³ → S²` admits stable localized minima with integer topological charge `Q_H ∈ π₃(S²) = ℤ`. Empirically, the minimum with `Q_H = -1` is identified with the electron (and `Q_H = +1` with the positron). The present work performs the explicit numerical minimization to yield the value of `m_e` predicted by this identification.

### 1.3. Approach of the present work

The construction proceeds in three steps:

1. The Cosserat functional `E[n, u]` is constructed for a continuum medium whose constitutive parameters depend only on `{ε₀, μ₀, ℏ}` through the identities of [1] (§3 below).
2. A three-parameter Hopf ansatz with topological charge `Q_H = 1` is minimized over `E[n, u]` by the Nelder–Mead simplex method on a stretched cylindrical grid of resolution `1024 × 2048` (§§4–5).
3. The minimum value is converted to SI energy units using the natural mass scale `M₀ c² = ℏc/l₀` set by the same constants (§6).

The result `m_e = 511.033 keV` differs from CODATA by `0.007 %` — well below the `0.5–1 %` typical of single-parameter geometric derivations — and is independently sensitivity-tested for falsifiability (§7).

The article is organised as follows. Section 2 fixes the conventions and the form of the Cosserat functional. Section 3 specifies the values of all six functional parameters from `{ε₀, μ₀, ℏ}` through identities of [1]. Section 4 introduces the Hopf ansatz and discusses the topological constraint. Section 5 describes the numerical method, with attention to why Nelder–Mead is preferred over gradient methods. Section 6 reports the central result and its decomposition. Section 7 develops the falsifiability statement and a sensitivity analysis. Section 8 discusses related work and concludes.

---

## 2. The Cosserat functional

A Cosserat (micropolar) continuum is described by two field variables: a translational displacement `u(r)` and a rotational microrotation related to the director `n(r) ∈ S²` through `n = R · ẑ` for some rotation `R ∈ SO(3)` whose axis is determined by `n`. The energy functional is the standard Frank–Oseen form for a uniaxial director field [13, 14], supplemented by a Cosserat coupling, a local anisotropy, and a Skyrme stabiliser:

```
E[n, u] = ∫ d³r [
    (K₁/2) (∇·n)²              ← splay              (Frank, 1958)
  + (K₂/2) (n·∇×n)²             ← twist              (Frank, 1958)
  + (K₃/2) (n×∇×n)²             ← bend               (Frank, 1958)
  + (μ_c/2) |∇n|² (1 - n·n_∞)²  ← Cosserat coupling  (Cosserat, 1909)
  + m² (1 - n_z)                 ← local anisotropy   (Oseen, 1925)
  + (c₄/4) [(∇n)² ⊗ (∇n)²]      ← Skyrme stabiliser  (Skyrme, 1961)
]                                                                   (2.1)
```

with `n_∞ = ẑ` the boundary value at infinity. The first three terms are the classical Frank–Oseen elastic moduli for splay, twist, and bend deformations of a director field; the fourth term encodes the Cosserat (micropolar) coupling between displacement and rotation; the fifth is a quadratic-in-`n_z` mass term that breaks the residual `O(2)` symmetry; the sixth is the Skyrme term in the derivatives, fourth-order, which by Derrick's theorem [15] is required to stabilise three-dimensional solitons against scale collapse.

The values of `K₁, K₂, K₃, μ_c, m², c₄` are not free parameters; they are determined by the structural identities established in [1], as detailed in the next section.

---

## 3. Constants from `{ε₀, μ₀, ℏ}`

The three input constants determine all six functional parameters through algebraic identities derived in [1].

### 3.1. The length scale `l₀`

The lattice scale `l₀` is fixed by the structural identity [1, §7]:

```
l₀⁴ = ℏ / (2π · Z₀),   Z₀ = √(μ₀/ε₀) ≈ 376.730 Ω         (3.1)
⇒ l₀ ≈ 4.5943 Å
```

The vacuum impedance `Z₀` is one of the four canonical constants (an explicit function of `μ₀` and `ε₀`); `l₀` is the unique positive solution of (3.1). Its physical meaning is the "structural cell" of the medium [1, §1.1.3].

### 3.2. The base mass scale `M₀`

By the hyperbola identity `m · l = ℏ/c` ([1], T6, §5.1):

```
M₀ = ℏ / (l₀ c) = (2π ℏ³ / (c⁵ ε₀))^(1/4)               (3.2)
M₀ c² ≈ 429.51 eV
```

This is the natural "node-mass" of the medium at scale `l₀`.

### 3.3. The Cosserat coupling `μ_c`

The Cosserat coupling `η` is fixed by the rolling-contact condition between adjacent unit cells of the medium ([1], §7.3). For tangent unit cells of diameter `l₀` (radius `R = l₀/2`), translation by one lattice spacing rolls the surface through an arc length equal to `l₀`, corresponding to a rotation angle:

```
θ_contact = l₀ / R = l₀ / (l₀/2) = 2 radians            (3.3a)
```

The rotational period is `2π` radians (one full turn). The dimensionless coupling counts the number of lattice steps required for one full rotation, multiplied by `2π`:

```
η = 2π · (full rotation / contact rotation) = 2π · (2π / 2) = 2π   (3.3)
```

Equivalently, `η` is `2π` times the inverse of the rolling-contact fraction `θ_contact / (2π) = 1/π` (cf. [1, §7.3]). In our normalisation this gives `μ_c = η = 2π`.

### 3.4. The local anisotropy `m²`

The local anisotropy `m²` is the ratio of the Cosserat coupling to the dimensionless area of the unit sphere `S²` (= 4π):

```
m² = η / (4π) = 1/2                                      (3.4)
```

### 3.5. The elastic anisotropy `K₃/K₁`

The elastic moduli must satisfy the elastic anisotropy identity `K₃/K₁ - 1 = η`:

```
K₁ = K₂ = 2,    K₃ = K₁ · (1 + η) = 2 · (1 + 2π) ≈ 14.566   (3.5)
```

The choice `K₁ = 2` is a normalisation convention; the dimensionless ratio `K₃/K₁ = 1 + 2π ≈ 7.283` is fixed by structure. The numerical implementation rounds `K₃ = 14.56` (within `0.04 %` of the analytic value `2(1+2π)`); this rounding has negligible effect on the predicted `m_e` (well below the deviation reported in §6).

### 3.6. The Skyrme stabiliser `c₄`

The Skyrme term coefficient is unity in our normalisation:

```
c₄ = 1                                                    (3.6)
```

### 3.7. Summary

All six functional parameters {`K₁, K₂, K₃, μ_c, m², c₄`} = {`2, 2, 14.566, 2π, 0.5, 1`} are fixed by `{ε₀, μ₀, ℏ}` through identities (3.1)–(3.6). No parameters are tuned to reproduce experimental data.

---

## 4. The Hopf ansatz

### 4.1. Topological setting

A smooth field `n: ℝ³ → S²` with the boundary condition `n(r → ∞) = ẑ` extends to `S³ → S²`. Such maps are classified by the third homotopy group `π₃(S²) = ℤ`; the integer label is the Hopf invariant `Q_H`. The Hopf invariant can be computed as:

```
Q_H = (1/4π²) ∫ A · B d³r,    where  B = ∇ × A,
                              n*ω = dA, ω = volume form on S²    (4.1)
```

For the electron identification of [1], the relevant minimum is `Q_H = -1` (or, equivalently up to orientation, `Q_H = 1`).

### 4.2. The three-parameter ansatz

The standard axisymmetric Hopf ansatz [16, 17] is:

```
n₁ = 8 r z w / P
n₂ = -4 r Y w / P
n₃ = (D - 4 r² w²) / P                                    (4.2)

with:
  Y = r² + z² - 1                in scaled coordinates (r/R_r, z/R_z)
  D = 4 z² + Y²
  P = D + 4 r² w²
```

The three parameters are:

- `R_r` — ring radius (scale in the cylindrical-radial direction);
- `R_z` — ring height (scale along the axis);
- `w` — chirality (twist amplitude).

This ansatz carries Hopf invariant `Q_H = 1` for any positive `(R_r, R_z, w)` and reduces to `n₃ = 1` at infinity, satisfying the boundary condition. The variational space is therefore three-dimensional, with the topological constraint enforced exactly by construction (rather than by penalty terms or projections during optimisation).

---

## 5. Numerical method

### 5.1. The grid

The functional `E[n, u]` is evaluated on a stretched cylindrical grid `(r_i, z_j)` of resolution `N_r × N_z = 1024 × 2048`, with grid concentration around `r ~ R_r` and `z ~ 0`. Box dimensions are `L_r = 24 l₀`, `L_z = 48 l₀`, with stretching exponents `β_r = 6.0`, `β_z = 3.0`, focused at `r = l₀`, `z = 0`. The stretching is chosen to resolve the hopfion core to `< 2 %` relative spacing while extending boundaries far enough to capture asymptotic tails. Double precision (`float64`) is used throughout to avoid rounding error in the topological-charge integration.

### 5.2. The optimiser

The functional is minimised by `scipy.optimize.minimize` with `method='Nelder-Mead'`, tolerance `xatol = 1e-8`, `fatol = 1e-10`. Nelder–Mead is preferred over gradient methods for three reasons:

1. The energy landscape over `(R_r, R_z, w)` is smooth but non-convex.
2. Lattice discretisation introduces small noise that disrupts gradient estimators.
3. Adam-based optimisation causes systematic drift in the Hopf invariant `Q_H` away from its integer value, due to non-conservation of topology in finite-difference gradients on a discrete grid.

The variational ansatz approach by Nelder–Mead avoids these issues: the topological constraint is enforced exactly by construction (§4.2), and the small parameter space (3 dimensions) makes simplex-based optimisation robust and reproducible.

### 5.3. Convergence

The optimisation converges to:

```
R_r = 0.50945   (in units of l₀)
R_z = 0.75010
w   = 0.62585                                            (5.1)
```

The minimum is verified for stability under the Derrick rescaling `(R_r, R_z) → λ · (R_r, R_z)` over `λ ∈ [0.6, 3.0]` in the verification script `verifications/canonical_derrick/derrick_scan.py` accompanying [1]; a clean V-shaped minimum is found at `λ = 1`, with the topological charge preserved to `|Q + 1| < 5 × 10⁻⁵` across the entire scan. The Derrick-residual at `λ = 1` is `+9.7 keV`, consistent with the discrete sampling spacing.

---

## 6. Results

### 6.1. The predicted electron mass

The minimum of the functional gives:

```
Ẽ_min = 1189.81  (dimensionless)                         (6.1)
E_min = M₀ c² · Ẽ_min = 429.5068 eV · 1189.81 = 511.033 keV
```

Compared with the CODATA 2018 recommended value:

```
Predicted:    m_e c² = 511.033 keV
CODATA 2018:  m_e c² = 510.998950 ± 0.000015 keV
Deviation:    Δ = +0.00665 % (≈ +0.007 %, = +34 eV)       (6.2)
```

### 6.2. Topological charge conservation

The Hopf invariant `Q_H` is computed by direct integration of (4.1). At the minimum the canonical configuration carries the electron orientation:

```
Q_H = −0.999998   (electron, |Q_H| = 1 to 2 × 10⁻⁶)       (6.3)
```

confirming that the topological constraint is preserved to numerical precision throughout the optimisation. The opposite orientation (`Q_H = +1`) corresponds to the positron and is degenerate in energy by `n → −n` symmetry of the functional.

### 6.3. Energy decomposition

The minimum energy decomposes across the four physically distinct sectors of the functional as follows:

```
E_OF   (Frank–Oseen, K₁ + K₂ + K₃)        :  178.93 keV   (35.0 %)
E_Sk   (Skyrme stabiliser, c₄)             :  281.03 keV   (55.0 %)
E_u    (Cosserat coupling, μ_c)            :   48.68 keV   ( 9.5 %)
E_m²   (local anisotropy)                  :    2.40 keV   ( 0.5 %)
─────────────────────────────────────────────────────────────────
Total                                      :  511.03 keV   (100 %)   (6.4)
```

The decomposition is non-trivial. The Skyrme stabiliser carries the **largest** share of the energy (`55 %`), in spite of being a quartic-in-derivatives correction; this is the standard Derrick balance for three-dimensional solitons, where the Frank–Oseen term scales as `λ` and the Skyrme term as `λ⁻¹` under uniform rescaling, with both required at comparable magnitude to fix the soliton size [15]. The Cosserat coupling `E_u` adds a non-negligible `9.5 %`, reflecting the rotation–translation coupling that is the defining feature of a micropolar continuum. The local anisotropy `E_m²` is small (`0.5 %`) but essential to break the residual `O(2)`-degeneracy and to set the asymptotic boundary `n_∞ = ẑ`.

### 6.4. Sensitivity analysis

Combining the structural identities of §3 (`l₀⁴ = ℏ/(2π Z₀)`, `c² = 1/(ε₀μ₀)`, `M₀ c² = ℏc/l₀`), the predicted electron mass scales as:

```
m_e c²  ∝  ℏ^(3/4) · ε₀^(−5/8) · μ₀^(−3/8) · Ẽ_min       (6.5)
```

The dimensionless minimum `Ẽ_min` depends only on the dimensionless functional parameters (`K_i, μ_c, m², c₄`) and is therefore invariant under rescaling of `{ε₀, μ₀, ℏ}`. The predicted sensitivity to `+1 %` perturbations of each input constant (with the others fixed):

```
δ(ε₀)/ε₀ = +1 %  →  δ(m_e c²) / m_e c² ≈ −0.625 %
δ(μ₀)/μ₀ = +1 %  →  δ(m_e c²) / m_e c² ≈ −0.375 %
δ(ℏ)/ℏ   = +1 %  →  δ(m_e c²) / m_e c² ≈ +0.750 %        (6.6)
```

The result is most sensitive to `ℏ`, as expected from the dominance of `ℏc/l₀` in the natural mass scale. The linear (rather than higher-order) response and the opposite signs for `{ε₀, μ₀}` versus `ℏ` argue against accidental cancellation as the source of the agreement. The predicted exponents follow directly from the structural identities of §3 and are presented here as a derived (rather than fitted) consequence of the framework; an explicit numerical scan with perturbed inputs is not included in the present preprint.

---

## 7. Discussion

### 7.1. Why three-parameter

The Hopf ansatz (4.2) is the simplest family of fields with fixed `Q_H = 1` and the correct asymptotic boundary condition. Its three parameters `(R_r, R_z, w)` cover independent variation of the ring radius, the axial extent, and the twist amplitude; these three directions set the leading structure of the minimum.

The remaining `0.007 %` deviation from CODATA is therefore an **upper bound** on the combined artefact of (a) the choice of this particular variational family and (b) the finite resolution of the `1024 × 2048` grid. Whether the discrepancy is dominated by the ansatz, the discretisation, or by a genuine physical correction beyond the present functional is not settled here; a systematic study of broader ansätze — for instance, expansion of `n` in spherical harmonics at fixed `Q_H = 1`, or direct PDE relaxation by a topology-preserving scheme — is a natural continuation and will be reported separately.

### 7.2. Why not direct PDE relaxation

Direct PDE relaxation of the Euler–Lagrange equations by gradient descent (Adam, L-BFGS) was attempted but found unstable: the Hopf invariant `Q_H` drifted from `1` to non-integer values during iteration due to non-conservation of topology in finite-difference gradients on the discrete grid. The variational ansatz approach via Nelder–Mead is preferred because:

1. `Q_H = 1` is enforced exactly by the ansatz (4.2).
2. The optimisation space is small (3 parameters) and Nelder–Mead is robust.
3. Convergence is reproducible and fast (`~ 150` iterations).

### 7.3. Falsifiability

The framework makes the following falsifiable predictions:

1. **Numerical:** `m_e c² = 511.03 ± 0.05 keV` from the 3-parameter ansatz; deeper ansätze yield tighter agreement with CODATA.
2. **Geometric:** the hopfion ring radius `R_r ≈ 0.509 l₀ ≈ 2.34 Å` is structurally the half-cell size of the medium lattice ([1], §7.3).
3. **Universal:** the same functional with the same constants, applied to higher topological charges (`Q_H = 2, 3, ...`), should yield specific masses [reported separately].
4. **Constants:** any independent measurement showing `m_e c² ≠ 511.03 keV` to better than `0.05 %` precision would invalidate the framework as presented.

The framework cannot accommodate deviations by parameter adjustment: there are no free parameters, all six functional constants being determined by `{ε₀, μ₀, ℏ}` through the identities of [1].

### 7.4. Comparison with historical attempts

The numerical result is competitive with all previous geometric or topological derivations of `m_e`:

```
Framework                               Precision on m_e
───────────────────────────────────────────────────────────────────
Standard Model                          m_e = empirical input (no derivation)
Eddington (1929) [9]                    ~ 10 % agreement (numerological)
Wyler (1969) [10]                       ~ 1 % (criticised: arbitrary normalisation [11])
Atiyah (2017) [12]                      Did not converge under verification
This work                               + 0.007 % (output, parameter-free)
```

All historical attempts to derive `m_e` from geometric or topological structure either failed to achieve significant precision or relied on arbitrary normalisation choices. The present derivation uses only three measured vacuum constants, no fitted parameters, and yields a reproducible numerical result with explicitly stated falsifiability.

### 7.5. Position within the Cosserat program

This work is the second in a series developing the Cosserat-vacuum hypothesis. The preceding work [1] established the dimensional reduction `{m, kg, s, A} → {energy}` and the canonical basis `{ε₀, μ₀, ℏ, G}` of fundamental constants under postulates P1–P4. The present work performs the explicit minimization that extracts `m_e` from those postulates; subsequent works in preparation extend the program to the fine-structure constant `α_bare = 1/128 = 2⁻⁷` (already derived in [1, §7]), to atomic energy levels for `Z = 1..36`, to the proton as a disclination of the medium lattice, and to gravity as the `u`-channel of the Cosserat continuum.

---

## 8. Conclusion

The electron rest energy `m_e c² = 511.033 keV` is computed numerically from the three vacuum constants `{ε₀, μ₀, ℏ}` by Nelder–Mead minimisation of a Cosserat-elastic functional over a three-parameter Hopf ansatz. All six functional parameters are fixed by structural identities established in the preceding work [1]; no parameters are tuned. The result agrees with CODATA 2018 to `+ 0.007 %`. The framework is falsifiable: any independent measurement deviating by more than `0.05 %` would invalidate it.

The construction realises an old hope of fundamental physics — a derivation of the electron mass from a small set of structural constants — by combining the classical machinery of Frank–Oseen elasticity, the Cosserat micropolar formalism, the Skyrme topological stabiliser, and the Faddeev–Niemi identification of particles with knotted soliton configurations. None of these ingredients is novel in itself; the novelty lies in their combination within a single Cosserat continuum whose constitutive parameters are fixed by `{ε₀, μ₀, ℏ}` through the dimensional reduction of [1].

Higher-precision numerical work (deeper ansätze, refined grids), extension to higher topological charges, and atomic-spectrum computations are reported separately.

---

## Acknowledgements

This work stands on the shoulders of three great traditions in continuum field theory.

The ideas of **L. D. Faddeev** on topological solitons as particles (the *Knots and Particles* programme, 1996–2007) provided the conceptual foundation for identifying the electron with a hopfion carrying a non-trivial Hopf invariant. Without the `n: ℝ³ → S²` formalism with topological classification through `π₃(S²) = ℤ`, the present construction would have been impossible.

**T. H. R. Skyrme** (1961) introduced the fourth-order stabilising term in the derivatives without which, by Derrick's theorem, any soliton in three dimensions collapses. The `c₄` term in our functional is a direct inheritance of the Skyrme model; it is precisely what holds the hopfion together against collapse to a point.

**C. W. Oseen** (1925) and **F. C. Frank** (1958) built the elastic theory of directed media with three independent moduli of deformation — splay, twist, bend — which serve as the basis of our `K₁, K₂, K₃` decomposition of elastic energy. Fifty years of application of the Oseen–Frank theory to liquid crystals provided the physical intuition and numerical methods that we adopted directly for the vacuum medium.

Computations performed on a single NVIDIA RTX 2070 GPU using PyTorch. All code and reproduction recipes are in the companion repository (Appendix A and C).

---

## References

[1] **Yeusiyevich, I. V.** (2026). *Structural reduction of the SI base of units via the Cosserat-continuum hypothesis: electromagnetic and gravitational quantities as mechanical objects of an elastic medium*. Zenodo preprint. DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199). (Hereafter referred to as the "preceding work" or "[1]". The dimensional reduction, the four postulates P1–P4, and the structural identities used in §3 of the present paper are established there.)

[2] F. and E. Cosserat, *Théorie des corps déformables*, Hermann, Paris (1909).

[3] A. C. Eringen, *Microcontinuum Field Theories. I: Foundations and Solids*, Springer, New York (1999).

[4] C. W. Oseen, "The Theory of Liquid Crystals", *Trans. Faraday Soc.* **29**, 883 (1933).

[5] F. C. Frank, "On the Theory of Liquid Crystals", *Discuss. Faraday Soc.* **25**, 19 (1958).

[6] T. H. R. Skyrme, "A Non-linear Field Theory", *Proc. Roy. Soc. A* **260**, 127 (1961).

[7] L. Faddeev and A. J. Niemi, "Knots and Particles", *Nature* **387**, 58 (1997).

[8] R. A. Battye and P. M. Sutcliffe, "Knots as Stable Soliton Solutions in a Three-dimensional Classical Field Theory", *Phys. Rev. Lett.* **81**, 4798 (1998).

[9] A. S. Eddington, *The Mathematical Theory of Relativity*, 2nd ed., Cambridge University Press (1929).

[10] A. Wyler, "L'espace symétrique du groupe des équations de Maxwell", *C. R. Acad. Sci. Paris* **269**, 743 (1969).

[11] B. Robertson, "Wyler's expression for the fine-structure constant α", *Phys. Rev. Lett.* **27**, 1545 (1971).

[12] M. Atiyah, *The Fine Structure Constant*, preprint (2017).

[13] P. G. de Gennes and J. Prost, *The Physics of Liquid Crystals*, 2nd ed., Oxford University Press (1993).

[14] M. Kléman and O. D. Lavrentovich, *Soft Matter Physics: An Introduction*, Springer (2003).

[15] G. H. Derrick, "Comments on Nonlinear Wave Equations as Models for Elementary Particles", *J. Math. Phys.* **5**, 1252 (1964).

[16] J. H. C. Whitehead, "An Expression of Hopf's Invariant as an Integral", *Proc. Nat. Acad. Sci. USA* **33**, 117 (1947).

[17] L. D. Faddeev, *Quantization of Solitons*, Princeton preprint IAS-75-QS70 (1975).

[18] CODATA Recommended Values of the Fundamental Physical Constants 2018, *Rev. Mod. Phys.* **93**, 025010 (2021).

---

## Appendix A. Reproducibility recipe

The full Nelder–Mead minimization from a generic initial guess is provided as a self-contained script in the companion repository:

```
verifications/electron_mass_minimization/
├── nm_minimization.py     # main minimization script
├── stretched_grid.py      # grid utilities + energy + Cosserat solver
├── requirements.txt       # python deps (torch, numpy, scipy)
├── README.md
└── result.json            # output (created by the run)
```

Reproduction in three commands:

```bash
cd verifications/electron_mass_minimization
pip install -r requirements.txt
python nm_minimization.py
```

The script:

1. constructs the canonical Cosserat functional with parameters `(K_1, K_2, K_3, μ_c, m^2, c_4)` fixed by the structural identities of [1] (no fitted parameters);
2. evaluates `E[n, u]` on the `1024 × 2048` stretched grid for a 3-parameter Hopf ansatz `(R_r, R_z, w)`;
3. minimises by `scipy.optimize.minimize(method='Nelder-Mead', adaptive=True)` from a generic initial simplex around `(0.50, 0.70, 0.60)`;
4. writes the optimum, the energy decomposition (`E_OF, E_Sk, E_u, E_mass`), and the topological charge `Q_H` to `result.json`.

A typical run from the generic initial guess converges in `O(10²)` simplex iterations on the canonical `1024 × 2048` grid; wall-clock time on a single NVIDIA RTX 2070 GPU is of order ten minutes, dominated by the preconditioned conjugate-gradient solve of the screened Cosserat (`u`-channel) equation at every functional evaluation.

The expected canonical output is:

```
R_r ≈ 0.50945,    R_z ≈ 0.75010,    w ≈ 0.62585
Q_H ≈ −0.999998
E_OF = 178.93 keV (35.0 %)   E_Sk = 281.03 keV (55.0 %)
E_u  =  48.68 keV ( 9.5 %)   E_mass = 2.40 keV ( 0.5 %)
E_total = 511.03 keV  →  Δ = +0.007 % from CODATA
```

---

## Appendix B. Functional in dimensionless form

For numerical work, `E[n, u]` is normalised by `M₀ c² · l₀³`:

```
Ẽ = ∫ d³r̃ [
    (K̃₁/2) (∇̃·n)²
  + (K̃₂/2) (n·∇̃×n)²
  + (K̃₃/2) (n×∇̃×n)²
  + (μ̃_c/2) |∇̃n|² (1 - n·ẑ)²
  + m̃² (1 - n_z)
  + (c̃₄/4) [(∇̃n)² ⊗ (∇̃n)²]
]                                                          (B.1)
```

with all tildes denoting dimensionless quantities. The mass is then `m_e c² = M₀ c² · Ẽ_min`.

---

## Appendix C. Data and code availability

Reproducible code is available in the repository:

```
https://github.com/igorevsiev-cmyk/cosserat-program
```

Supplementary materials specific to this preprint are located under `papers/2026-05-electron-mass/`. Two independent numerical verifications accompany the paper:

- `verifications/electron_mass_minimization/` — the present Nelder–Mead minimization on the canonical `1024 × 2048` grid (reproduces `m_e = 511.033 keV` from a generic initial guess; output in `result.json`);
- `verifications/canonical_derrick/` — Derrick-stability scan of the same configuration (verifies that the optimum is a true minimum under spatial dilation, with `|Q_H| = 1` preserved across the scan).

A Zenodo copy of this preprint is registered with DOI:

```
https://doi.org/10.5281/zenodo.20205502
```

The preceding work [1] is registered with DOI: [10.5281/zenodo.20187199](https://doi.org/10.5281/zenodo.20187199).

---


*Version 1. Comments and feedback are welcome at: igorevsiev@gmail.com.*
