# Maxwell's Equations as Theorems about the Director Field `n: ℝ³·¹ → S²`

**All four equations of electromagnetism are derived from a single assumption: every point of the vacuum has a direction. The homogeneous pair is a consequence of the two-dimensionality of the sphere of directions; the inhomogeneous pair is an exact identity that itself computes the source current. Electromagnetism is not postulated but proved.**

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-07-02
**Version:** 2 (preprint; extended edition)
**License:** CC-BY 4.0
**DOI:** [10.5281/zenodo.21264016](https://doi.org/10.5281/zenodo.21264016)

---

## Abstract

**In brief, without formulas.** Maxwell's equations — the four equations describing all of electricity, magnetism, and light — are accepted in standard physics as laws of nature: confirmed by experiment, but derived from nothing. This work shows that if one assumes each point of the vacuum has a *direction* (a unit arrow `n`, a "director", as in the molecules of a liquid crystal), then all four Maxwell equations cease to be postulates and become **mathematical theorems** — consequences of the pure geometry of the field of arrows. Two of the equations (the absence of magnetic charges and Faraday's law) follow from a single fact: the sphere of directions is two-dimensional. The other two (the Coulomb–Gauss law and Ampère's law) follow from the schoolbook product rule for differentiation — and, unlike in the standard theory, they *themselves compute* what the electric charge and current are: knots and swirls of the field of arrows. The charge then comes out automatically integer — because one cannot wind a sphere onto a sphere "one and a half times". The claims are verified numerically: the identity holds to 0.0001% (the accuracy limit of the numerical scheme).

**Now rigorously.** In the Cosserat program [SI-reduction; electron-mass] the physical vacuum is modelled as a micropolar continuum whose orientational channel is described by a field of unit directors `n(x): ℝ³·¹ → S²`. From the director one builds an antisymmetric tensor — the pullback of the area form of the sphere:

```
F_μν ≡ n · (∂_μ n × ∂_ν n)
```

Two statements are proved for it:

1. **The homogeneous pair** (`∇·B = 0`, Faraday's law) — a **Bianchi identity** holding for *any* smooth field `n`. The reason is purely geometric: all derivatives `∂_μ n` lie in the two-dimensional tangent plane to the sphere, and the scalar triple product of three vectors of a two-dimensional space vanishes identically. The homogeneous Maxwell equations are a consequence of `dim S² = 2`.

2. **The inhomogeneous pair** (`∇·E = ρ`, Ampère's law) — an **exact Leibniz identity**

   ```
   ∂_μ F^μν = n·(□n × ∂^ν n) + n·(∂^μ n × ∂_μ ∂^ν n) ≡ j^ν
   ```

   again valid for *any* `n` and *defining* the source current `j^ν`. The current is localized on the defect (falloff `~1/r⁵` for the test configuration — the Belavin–Polyakov instanton), integrates to a topological charge (`∫ j⁰ d²x ∝ Q ∈ ℤ`), and contains no singularities. An independent derivation via the CP¹ formulation (varying the composite potential `A_μ` as an auxiliary field, the formalism of D'Adda et al., 1978) identifies the current with the current of charged matter and fixes the coupling constant to the physical fields by an energy normalization (Skyrme term ≡ Maxwell `F²/4μ₀`): `g₀ = √(μ₀c₄)`.

The Leibniz identity is confirmed numerically on the Belavin–Polyakov instanton (grid `512²`, 4th-order finite differences): **residual `0.0001%`** — the accuracy limit of the scheme; at every radius `r = 0.7–7.8` the profile residual is `0.00%`. For a harmonic map the first term of the current vanishes analytically and numerically (`‖term1‖/‖term2‖ ≈ 2×10⁻⁶`).

Physical picture: far from the defect core (`r ≫ l₀`) the current vanishes and Maxwell's equations are an *exact* description of the far field; inside the core the nonlinear terms dominate, ensuring a finite mass where linear electrodynamics diverges. The ratio of the two current terms `|term1|/|term2| ~ c₄/c₂` injects the medium scale into the structure of the current inside the particle and participates in fixing the radius of the vortex tube `r_v ≈ l₀/2` — the very one that in [SI-reduction §7] yields the bare fine-structure constant `α_bare = 1/128`.

The epistemic status is honest: the work **does not derive a new number** — it proves that a known structure (Maxwell) is a *theorem* about the field `n`, and precisely localizes where this structure breaks down (the defect core) and what replaces it (nonlinear dynamics that produce mass).

**Addendum (check of 2026-07-02, §6.2 and §9):** the cross-check `g₀ ↔ e` has been carried out. The dynamical charge of the CP¹ quantum gives the exact `q_w² = ℏε₀c/8 = (π/4)·l₀⁴` and `α_w = 1/(32π) ≈ 1/100.5` — the same law "charge² ∝ l₀⁴" as the geometric route (`α_bare = 1/128`); the discrepancy is exactly a factor of `4/π ≈ 1.27` (open). The Leibniz identity is also confirmed on the canonical **3D hopfion**: the residual falls as `dx⁴` (0.59% → 0.13% on grids 192³→288³), and for the first time the Skyrme contribution to the current is seen numerically, `‖term1‖/‖term2‖ = 0.372`.

**Keywords:** Maxwell's equations, Cosserat continuum, director field, CP¹ sigma model, Bianchi identity, Faddeev–Skyrme model, topological charge, emergent electrodynamics.

---

## For the reader new to the program

This section is optional for the specialist, but the article is written so that it can be read **without** familiarity with the earlier works of the program. Here is the minimal context.

### What Maxwell's equations are

Four equations (1861–1865) from which the whole classical theory of electricity, magnetism, and light follows:

| Equation | What it says in plain words |
|---|---|
| `∇·B = 0` | Magnetic charges (monopoles) do not exist: magnetic field lines are always closed |
| `∇×E + ∂B/∂t = 0` | A changing magnetic field twists the electric one (Faraday's law — the generator principle) |
| `∇·E = ρ` | The source of the electric field is electric charge (Coulomb–Gauss law) |
| `∇×B − ∂E/∂t = j` | Current and a changing electric field twist the magnetic one (Ampère's law) |

The first pair is called **homogeneous** (it has no sources — the right-hand side is zero), the second **inhomogeneous** (charge `ρ` and current `j` stand on the right). In standard physics all four are **postulates**: they generalize experiment but are derived from nothing, and what `ρ` and `j` are the theory does not say — they are put in by hand.

### What the program assumes

One thing: the vacuum is not emptiness but an elastic medium of a special kind (the Cosserat continuum, 1909), each point of which has not only a position but also its **own orientation** — as if space were filled with tiny coupled gyroscopes. The orientation of a point is a unit vector `n` (a "director", a term from liquid-crystal physics). Three constants of the medium are identified with three measured constants of the vacuum: the density with the magnetic constant `μ₀`, the stiffness with the reciprocal electric constant `1/ε₀`, and the quantum of twist with Planck's constant `ℏ`. From them one builds the medium's own length scale `l₀ ≈ 0.46 nm` [SI-reduction]. Nothing more from the program is needed to read this article.

### The key distinction on which the article is built: law vs identity

- **A law** is a statement about nature that could have been otherwise and is tested by experiment. `F = ma` is a law.
- **An identity** is a statement true automatically, by construction. `(a+b)² = a² + 2ab + b²` is an identity; it is meaningless to "test it experimentally".

The central claim of the work: Maxwell's equations, considered laws for 160 years, turn out — when viewed through the field `n` — to be **identities**: they cannot fail to hold if a field of directions exists. The physical content does not disappear but moves elsewhere (exactly where — §7.3).

### What mathematics is needed

The cross product `a × b`, the scalar triple product `a·(b × c)` (= the volume of the parallelepiped on three vectors), partial derivatives, and the product rule for differentiation (the Leibniz rule). Both proofs in the article take a few lines each and use only this.

---

## Logical chain of the work

```
INPUT (from [SI-reduction])
 Cosserat medium: ρ = μ₀, μ_el = 1/ε₀, ℏ; l₀⁴ = ε₀ℏc/(2π)
 Orientational channel = director field n: ℝ³·¹ → S²
 │
 ▼
DEFINITION (§3)
 F_μν = n·(∂_μ n × ∂_ν n)          — "how much sphere area the field sweeps"
 E_i = F_0i,  B_i = −½ε_ijk F_jk   — identification of the fields
 │
 ▼
THEOREM 1 (§4) — for ANY smooth n
 ∂_[λ F_μν] = 0                     ⟸ the sphere of directions is two-dimensional
 ⟹ ∇·B = 0, ∇×E + ∂B/∂t = 0      (homogeneous pair)
 │
 ▼
THEOREM 2 (§5) — for ANY smooth n (Leibniz rule)
 ∂_μ F^μν = n·(□n×∂^ν n) + n·(∂^μ n×∂_μ∂^ν n) ≡ j^ν
 ⟹ ∇·E = ρ, ∇×B − ∂E/∂t = j      (inhomogeneous pair; current COMPUTED)
 Numerically: residual 0.0001% (BP instanton, 512²)
 │
 ▼
CP¹ DERIVATION (§6) — independent check + coupling constant
 δL/δA_μ = 0 → ∂F ∝ j (current = charged matter)
 g₀ = √(μ₀c₄) (energy normalization);  q_w² = (π/4)l₀⁴ → α_w = 1/(32π)
 Q = ∫ j⁰ = topological charge ∈ ℤ  (charge quantized — a theorem)
 │
 ▼
PHYSICS (§7–8)
 far from the defect: j → 0 — Maxwell is exact
 in the defect core:  nonlinearity — finite mass instead of divergence
 balance of current terms → r_v ≈ l₀/2 → α_bare = 1/128
```

---

## Epistemic label (read first)

The program uses a four-level scale of statement strength (introduced in [gravity-second-channel]): **[1]** metaphor → **[2]** isomorphism (reproduces something known, but with no new number) → **[3]** prediction of a number → **[4]** prediction of a new effect.

The present work is **level [2] in its strongest form**: not an "analogy with Maxwell", but two mathematical proofs that Maxwell's equations are identities for the field `n: ℝ³·¹ → S²`, plus a numerical verification at the accuracy limit of the scheme. There are no new numbers here — and this must be said up front, so the reader does not look for them. The value lies elsewhere:

- **the equations cease to be postulates** — of the four Maxwell equations, zero remain axioms once the existence of the field `n` is accepted;
- **charge acquires an explanation of its quantization** — it is topological (an integer number of windings of the sphere onto the sphere), and integrality is not postulated;
- **the boundary of applicability** of linear electrodynamics is precisely localized: the defect core, where the same structure that produces Maxwell gives a finite mass instead of a divergence.

Two places where the work touches level [3] (the numbers themselves are derived in [SI-reduction] and [electron-mass]; here — the structural basis for them): the topological quantization of charge, and the balance of current terms that fixes `r_v ≈ l₀/2` and hence `α_bare = 1/128`.

> **Historical frame.** Maxwell obtained his equations (1861–62) precisely from a mechanical model of the ether — but by postulating the structure of the medium *ad hoc*, to fit the answer. Here the move is the reverse and stricter: only a Cosserat medium with an orientational channel is postulated (three constants `{ε₀, μ₀, ℏ}` [SI-reduction]), and Maxwell's equations arise as theorems about its director field — together with the boundary of their applicability.

---

## 1. Introduction

### 1.1. The intuitive picture

Imagine that each point of space carries a small arrow `n` — a direction, a unit vector. The arrows of neighbouring points are elastically coupled: to sharply turn one relative to its neighbours costs energy. Then:

- **Light** is a ripple of coordinated turns of the arrows, running through the medium (like a wave across a field of grain).
- **The electron** is a knot: a configuration of arrows that cannot be "combed" flat to a uniform one by any smooth deformation. The knot cannot be undone — that is why the electron is stable; knots exist only with an integer number of "windings" — that is why charge is quantized.
- **The electric and magnetic fields** are two projections of one quantity: the rate and direction with which the arrows turn from point to point.

The question of the article: what equations must such a "ripple of arrows" obey? The answer: **exactly Maxwell's equations** — and not because we put them in, but because it can obey nothing else. This claim is proved, not illustrated.

### 1.2. The place of the work in the program

A Cosserat (micropolar) continuum is an elastic medium each point of which carries, besides a displacement `u`, an independent orientation `n`. The program's hypothesis [SI-reduction]: the physical vacuum is such a medium, and observed physics is its deformations and topological defects. Two channels of deformation:

```
n-channel (director n: ℝ³ → S²)  — orientation  → electromagnetism (this work)
u-channel (displacement u ∈ ℝ³)  — translation  → gravity [gravity-second-channel]
```

Previous works of the program established: the reduction of the SI base of units to a single dimension and the medium's two algebraic "hyperbolas" [SI-reduction]; the bare electron mass `m_e^bare = 446.279 keV`, computed by minimizing the knot's energy with no free parameters [electron-mass]; the structure of the gravitational sector [gravity-second-channel]. In all these works it was tacitly assumed that the n-channel "is responsible for electromagnetism". The present work settles this debt: it proves that **the equations of electromagnetism — Maxwell's equations — are mathematical consequences of the existence of the director field**, and indicates what replaces them where they cease to work.

### 1.3. What exactly is claimed

The claims of the work are of different logical rank, and it is important to separate them at once:

| Claim | Rank | Where |
|---|---|---|
| The homogeneous Maxwell pair — an identity for any smooth `n` | **theorem** | §4 |
| The inhomogeneous pair — a Leibniz identity defining the current `j^ν` | **theorem** | §5 |
| The current `j^ν` is localized, non-singular, `∫j⁰ ∝ Q ∈ ℤ` | theorem + numerical check | §5.3 |
| CP¹ derivation: current = charged matter, `g₀ = √(μ₀c₄)`, `α_w = 1/(32π)` | standard procedure + identification | §6 |
| Maxwell — the exact far-zone limit; nonlinear dynamics in the core | corollary | §7 |
| Balance of current terms → `r_v ≈ l₀/2` → `α_bare = 1/128` | bridge to [SI-reduction §7] | §8 |

The first two rows are the heart of the work. We stress their special status: they depend neither on the energetics of the medium, nor on the equations of motion, nor even on whether the Cosserat interpretation of the vacuum is correct at all. These are facts of differential geometry — they hold for any field of directions, wherever it lives: in the vacuum, in a liquid crystal, in a ferromagnet. The Cosserat medium is needed for the third step — the identification of `F_μν` with the physical `E`, `B` and of the coefficients with the medium's moduli.

### 1.4. Relation to what is known

The composite tensor `F_μν = n·(∂_μn × ∂_νn)` and its connection to the topological charge are classics of sigma-model theory (Belavin–Polyakov 1975; Faddeev 1975; D'Adda, Di Vecchia, Lüscher 1978; textbook review — Rajaraman 1982). The contribution of the present work is not in inventing these objects, but in three things:

1. **assembling the complete derivation of all four equations** in one frame, with an explicit split into "geometry (Bianchi)" / "Leibniz identity (source)";
2. **a non-singular form of the current** — through the vector `n` itself, rather than through the complex coordinate `z`, which has a coordinate singularity (like a pole on a geographic map). It is precisely the non-singular form that passes the numerical check to 0.0001%, whereas the "beautiful" textbook forms give, in practice, residuals of 40–86% (§5.4 — a methodological lesson);
3. **the physical identification** in the Cosserat medium: the coupling constant `g₀` from the medium's moduli, charge as the cross-sectional area of a defect, and the boundary of applicability as the particle core.

---

## 2. The medium and the director field

### 2.1. Postulates (recap of [SI-reduction])

Three parameters of the elastic medium are identified with three measured constants of the vacuum:

```
ρ    = μ₀       — density of the medium ↔ magnetic constant
μ_el = 1/ε₀     — shear modulus (stiffness) ↔ reciprocal electric constant
ℏ               — quantum of action of the micro-rotations ↔ Planck's constant
```

The first consequence — the speed of a transverse elastic wave of such a medium `c = √(μ_el/ρ) = 1/√(ε₀μ₀)` coincides with the speed of light: this is the very coincidence from which Maxwell in 1862 concluded that light is an electromagnetic wave. The second — from the three constants one builds a unique length scale, `l₀⁴ = ε₀ℏc/(2π)`, `l₀ ≈ 0.46 nm` — the "structural step" of the medium. It will be needed in §7–8.

The orientation of a point of the medium is a unit vector `n(x, t)`. The set of all possible directions of a three-dimensional arrow is the surface of the unit sphere; its standard notation is `S²`. The director field is the map

```
n: ℝ³·¹ → S²,   |n|² = 1
```

(the notation `ℝ³·¹` means: the argument is a point of space-time, three spatial coordinates plus time).

The condition `|n| = 1` is not an approximation but a definition: `n` is a direction, and a direction has no "length". From it a single line yields the property on which the whole article is built. Differentiate `n·n = 1`:

```
∂_α(n·n) = 2 n·∂_α n = 0   ⟹   n ⊥ ∂_α n   for any direction α
```

Intuitively: as you walk on the globe, your velocity is always tangent to the surface, one cannot step "outward" from the sphere. So here too: however the field `n` changes from point to point, the change vector `∂_α n` always lies in the **tangent plane** to the sphere at the point `n`. And the tangent plane to the sphere is **two-dimensional**. This is the single geometric fact needed for Theorem 1.

### 2.2. Energy of the field (the Faddeev–Skyrme Lagrangian)

For completeness we give the energetics of the medium — though, we stress in advance, it is **not needed** for the theorems of §4–5. The energy/action density of the orientational channel in the long-wavelength limit:

```
L[n] = (c₂/2)|∂_μ n|² + (c₄/4) F_μν F^μν                                    (1)
```

The first term is ordinary elasticity: the energy grows when neighbouring arrows are misaligned (the coefficient `c₂` is the stiffness). The second is the so-called Skyrme term (Skyrme 1962; Faddeev 1975): it switches on only under very rapid turns of the field and prevents the knot from collapsing to a point; its coefficient `c₄` is fixed by the condition `√(c₄/c₂) = l₀` — "a knot cannot be smaller than the medium's structural step". The tensor `F_μν` of the second term is defined in the next section.

> **Remark (Skyrme term = Maxwell energy).** Getting ahead of ourselves: the `F_μν` of the second term is precisely the electromagnetic field (§3.2), so `(c₄/4)F_μνF^μν` is the same invariant as the Maxwell Lagrangian `−(1/4μ₀)F²_phys`. The Skyrme energy of the knot is literally **the energy of its own electromagnetic field** (for a static knot — magnetostatic, `~∫B²`). The stabilization mechanism then reads physically: by Derrick, under compression of the knot the elastic term falls and the Skyrme term grows — that is, *the elasticity of the medium wants to collapse the knot, and the energy of its own EM field refuses to be compressed*. The century-old problem of EM self-energy is inverted: for Abraham–Lorentz the self-energy tore the classical electron apart (Poincaré stresses were needed to hold it), whereas here it is the stabilizer, and the medium does the holding. Quantitatively this is not a trifle: in the canonical computation [electron-mass] the Skyrme contribution `E_Sk = 220.6 keV` out of `E_total = 446.3 keV` — **49.4%, almost exactly half of the bare electron mass is the energy of its own EM field** (a reincarnation of Abraham's "electromagnetic mass" program, but with a finite answer). The coincidence of the coefficients (`c₄/4` against `g₀²/4μ₀`) under the energy normalization `g₀ = √(μ₀c₄)` is exact by construction (§6.2); the non-trivial part of the cross-check has moved into the charge and is closed up to a factor `4/π` (§6.2, §9).

The order of logic matters: `F_μν` is defined in §3 **before** and **independently of** the Lagrangian; the theorems of §4–5 are identities valid for any field `n`, regardless of (1). The Lagrangian is needed only in §6 (coupling constant) and §8 (structure of the current inside the particle).

---

## 3. The tensor `F_μν`: how much sphere area the field sweeps

### 3.1. Definition and meaning

```
F_μν ≡ n · (∂_μ n × ∂_ν n)                                                  (2)
```

Let us take the construction apart step by step. Move from the point `x` a small step in the direction `μ` — the arrow turns by `∂_μ n`; move in the direction `ν` — it turns by `∂_ν n`. Both turn vectors lie in the tangent plane to the sphere (§2.1). Their cross product `∂_μ n × ∂_ν n` is a vector perpendicular to that plane, i.e. directed along `±n`, and its length is the area of the parallelogram spanned by the two turns. The scalar product with `n` extracts this area with a sign.

In sum: **`F_μν` is the oriented area on the sphere of directions that the arrow "sweeps out" under a shift along the pair of directions `(μ, ν)` in space-time.** In the language of differential geometry such a construction is called the *pullback of the area form* of `S²` (the area form of the sphere on a pair of tangent vectors `a, b` equals `n·(a×b)` — the oriented area of the parallelogram projected onto the normal `n`); but for reading the article the picture of the swept area suffices. Where the field winds the sphere quickly (the defect core), `F` is large; where the arrows are nearly parallel, `F` is small.

The "area on the sphere" has a decisive property: the total area of the sphere is finite (`4π`), and a closed surface in space can cover it only an integer number of times. From this the quantization of charge will grow (§6.3).

### 3.2. Identification with E and B

The physical fields are defined from `F_μν` in the standard way for field theory, with a single dimensional constant `g₀` (its value — §6.2):

```
F_μν^phys = g₀ F_μν;    E_i = F_0i^phys,   B_i = −½ ε_ijk F_jk^phys          (3)
```

Concretely: `F_μν` is an antisymmetric 4×4 matrix (indices: `0` — time, `1,2,3` — space), and its six independent cells are precisely E and B:

```
        ν=0      ν=1      ν=2      ν=3
μ=0   ⎡  0      E_x      E_y      E_z  ⎤     time row → E
μ=1   ⎢ −E_x     0      −B_z      B_y  ⎥
μ=2   ⎢ −E_y    B_z       0      −B_x  ⎥     spatial block → B
μ=3   ⎣ −E_z   −B_y      B_x       0   ⎦
```

In words: **the electric field** is the area swept by the arrow under a shift "time + spatial direction" (how fast the arrow rotates in time); **the magnetic field** is the area under a shift along a pair of spatial directions (how twisted the field of arrows is in space). `E` and `B` are not two different entities but two projections of one object: the split depends on the choice of the "time row", and upon passing to a moving frame they mix — this is just a rotation within one table.

### 3.3. The composite potential (for §6)

A direction of the arrow can be encoded by a single complex number `z = (n₁ + i n₂)/(1 + n₃)` — the stereographic projection, the same trick by which the spherical Earth is drawn on a flat map. Through `z` one builds from `n` a **composite** gauge potential:

```
A_μ = Im(z̄ ∂_μ z)/(1 + |z|²),      ∂_μ A_ν − ∂_ν A_μ = ½ F_μν               (4)
```

The 4-potential `A_μ`, familiar from electrodynamics, is here not an independent field but a function of the director: a derivative of the way of encoding it. The `U(1)` gauge freedom (the possibility of shifting the phase of `A_μ` without changing anything in the physics) is a trace of the arbitrariness in choosing the point of projection on the sphere.

One warning, important for what follows: like any flat map of the Earth, the parametrization `z` has a defective point — the "south pole" `n₃ = −1`, where `z → ∞` (like the pole on a Mercator map, where the meridians converge). All proofs below are carried out in the non-singular variables `n`; the encoding (4) is used only where it is safe (§6). Ignoring this warning cost two failed versions of the numerical check (§5.4).

---

## 4. Theorem 1: the homogeneous pair — a consequence of the two-dimensionality of the sphere

> **Theorem 1.** For any smooth field `n: ℝ³·¹ → S²`
>
> ```
> ∂_λ F_μν + ∂_μ F_νλ + ∂_ν F_λμ = 0                                          (5)
> ```
>
> (in field theory a relation of this form is called a Bianchi identity).

**Proof.** Expand `∂_λ F_μν` by the product (Leibniz) rule:

```
∂_λ F_μν = ∂_λ n · (∂_μ n × ∂_ν n)
         + n · (∂_λ∂_μ n × ∂_ν n)
         + n · (∂_μ n × ∂_λ∂_ν n)
```

Add three such expressions over the cycle `(λ, μ, ν) → (μ, ν, λ) → (ν, λ, μ)`. The terms with second derivatives cancel pairwise: mixed derivatives are symmetric (`∂_λ∂_μ = ∂_μ∂_λ` — the order of differentiation does not matter), while the cross product is antisymmetric (it changes sign under a swap of the factors). What remains is

```
Σ_cyc ∂_λ n · (∂_μ n × ∂_ν n)
```

— the scalar triple product of the three vectors `∂_λ n, ∂_μ n, ∂_ν n`, i.e. the volume of the parallelepiped spanned by them. But by §2.1 all three vectors lie in **one two-dimensional plane** — the tangent plane to the sphere. A parallelepiped all of whose edges are pressed into one plane is flat: its volume is zero. ∎

**Corollary (in 3+1 components).** Substituting the identification (3) into (5) gives exactly the homogeneous Maxwell pair:

```
∇·B = 0                     (no magnetic monopoles)
∇×E + ∂B/∂t = 0             (Faraday's law)
```

### 4.1. What happened here

The homogeneous pair of Maxwell's equations turned out to be **a consequence of a single number: the dimension of the sphere of directions equals 2**. Neither the medium's energy, nor the equations of motion, nor any physics were used — only two facts: the director is a unit (hence its derivatives are tangent to the sphere) and the sphere is two-dimensional (hence any three tangent vectors lie in one plane and form no volume).

Let us unfold what this changes. In standard electrodynamics `∇·B = 0` and Faraday's law are postulated — or, equivalently, the existence of a 4-potential `A_μ` is postulated. Here the potential is not postulated: it *automatically exists* (formula (4)), because `F_μν` is assembled from a map into the sphere. The absence of magnetic monopoles ceases to be a mysterious empirical fact about a separate entity, "magnetic charge", and becomes a geometric property of the field of directions: a swept area has no bulk sources.

And the flip side, which lends the statement falsifiability: were the internal space of orientations three-dimensional (say, an arrow with free length, or `n ∈ S³`), the identity (5) would break — three tangent vectors would no longer be coplanar. **The homogeneous Maxwell equations are an experimental test of the two-dimensionality of the internal space of the vacuum, and the vacuum passes it.** The discovery of a magnetic monopole would refute Theorem 1 — and with it the whole construction (§9).

---

## 5. Theorem 2: the inhomogeneous pair — an identity that computes the current

The second Maxwell pair (`∇·E = ρ`, Ampère's law) consists of equations **with a source**: charge and current stand on the right. Standard electrodynamics introduces `ρ` and `j` by hand, as external data. Here they are not introduced — they are **computed** from the field itself.

### 5.1. The exact identity

> **Theorem 2.** For any smooth field `n: ℝ³·¹ → S²`
>
> ```
> ∂_μ F^μν = n·(□n × ∂^ν n) + n·(∂^μ n × ∂_μ∂^ν n)                            (6)
> ```
>
> (`□ = ∂_μ∂^μ` — the wave operator, the d'Alembertian; repeated indices are summed).

**Proof.** Expand the left-hand side by the Leibniz rule — the derivative acts in turn on each of the three factors of `n·(∂^μn × ∂^νn)`:

```
∂_μ F^μν = (∂_μ n)·(∂^μ n × ∂^ν n)  +  n·(□n × ∂^ν n)  +  n·(∂^μ n × ∂_μ∂^ν n)
```

The first term is identically zero — for the same reason as in Theorem 1: the three vectors `∂_μ n, ∂^μ n, ∂^ν n` lie in the two-dimensional tangent plane, and their scalar triple product is the volume of a flat parallelepiped. Two terms remain. ∎

The right-hand side of (6) is precisely the current. Let us give it a name and label its terms:

```
j^ν ≡ n·(□n × ∂^ν n) + n·(∂^μ n × ∂_μ∂^ν n)   ≡ term1 + term2               (7)
```

In 3+1 components (with the identification (3)) equation (6) is exactly the inhomogeneous Maxwell pair:

```
∇·E = ρ,        ∇×B − ∂E/∂t = j,        where ρ = g₀ j⁰,  j_i = g₀ j^i
```

We stress the status: (6) is an **identity**, not an equation of motion. It holds for any configuration `n`, including ones never realized in nature. The dynamics (the medium's energy) will appear later — it will determine *what* the current is for the real configurations (§6, §8), but the form "`∂F = j`" itself does not depend on the dynamics. In the standard theory the form of the equations and the content of the source are two independent postulates; here the form is an identity, and the source is a computable function of the field.

### 5.2. The simplest case: term1 = 0

The first term of the current contains `□n` — the "acceleration" of the field. For a broad class of configurations it drops out. A **harmonic map** is a configuration minimizing the pure elastic energy `∫|∂n|²` (an analogue of a soap film: the shape the field takes "by itself", without external forces); for such fields `□n = −|∂n|² n`, i.e. `□n` is parallel to `n` itself. Then:

```
term1 = n·(□n × ∂^ν n) = −|∂n|² · n·(n × ∂^ν n) = 0        (since n × n = 0)
```

and the whole current is carried by the second term:

```
j^ν = n·(∂^μ n × ∂_μ∂^ν n)
```

The numerical check (§5.4) confirms: `‖term1‖/‖term2‖ ≈ 2×10⁻⁶` on the test harmonic configuration. The case where term1 switches on (a real particle with the Skyrme term) — §8.

### 5.3. Properties of the current

1. **Localized on the defect.** The current is built from second derivatives of the field and falls off rapidly: for the test configuration (§5.4) — as `~1/r⁵`. The entire source is concentrated in the core of the knot; far from it `j → 0`, and Maxwell's equations become free. The "empty space" of electrodynamics is the region where the arrows turn smoothly.

2. **Integrates to a topological charge.** `∫ j⁰ d²x ∝ Q`, where `Q ∈ ℤ` is the number of windings of the sphere onto the sphere (the degree of the map). The integrality of the electric charge is not postulated — it is topological (§6.3).

3. **Non-singular.** The form (7) is written through the vector `n` itself — it contains no "south pole" defective point of §3.3. This is not cosmetics but a condition of fitness for computation: §5.4.

4. **Exact.** The identity (6) is not an expansion in a small parameter and not an approximation; it holds for any smooth `n` at every point.

### 5.4. Numerical verification and a methodological lesson

The identity is checked on the **Belavin–Polyakov (BP) instanton** — the standard test configuration of sigma-model theory: it is the simplest "texture" that winds the plane onto the sphere of directions exactly once (`Q = −1`). Its value for the test is a known exact formula: both sides of (6) can be computed independently and compared pointwise.

Parameters: scale `λ = 2`, grid `512²`, box `L = 10`, 4th-order finite differences; script `code/verify_maxwell_v3.py`. One honest detail: the numerical integral of the charge over the finite box gives `Q = −0.881`, not `−1` — the missing 12% sit in the slowly decaying tail of the charge density beyond the box boundary. This does not affect the check of the identity itself: it is pointwise.

| Quantity | Result |
|---|---|
| Global residual `‖∂_μF^μν − j^ν‖/‖j^ν‖` | **0.0001%** (accuracy limit of the finite-difference scheme) |
| Profile residual over radii `r = 0.7–7.8` | 0.00% at every radius |
| `‖term1‖/‖term2‖` (harmonicity of BP) | `2×10⁻⁶` |

The history of the check is instructive and is deliberately given below:

| Version | Form of the current | Residual | Diagnosis |
|---|---|---|---|
| v1 | through the complex coordinate `z` | 86% | coordinate singularity of the "south pole" (`n₃ = −1`) |
| v2 | Noether `U(1)` current | 40% | not the right current (coincides with (7) only on the constraint `A = A[n]`) |
| **v3** | **identity (7) through `n` itself** | **0.0001%** | ✓ |

The lesson: the "right" object is neither the potential nor the current from a beautiful textbook formulation, but the non-singular identity in the field's original variables. The 40–86% residuals of the first versions are not numerical errors but wrongly chosen analytic forms; the six-order drop of the residual in v3 confirms the diagnosis.

---

## 6. The CP¹ derivation: why the current is charged matter, and what the coupling constant equals

The identity (6) gives the form of the equations but leaves two questions. First: the right-hand side (7) is merely "what is left over from Leibniz"; why is it legitimate to call it the current of *charged matter*? Second: what is the dimensional constant `g₀` between the geometric `F_μν` and physical volts and teslas? Both are answered by the reformulation through the complex encoding of §3.3 — in the literature it is called the CP¹ formulation (CP¹ is the mathematical name of the sphere described by a complex coordinate).

### 6.1. Varying the composite potential

In the variables `w = z/√(1+|z|²)` the Lagrangian (1) is rewritten exactly (D'Adda, Di Vecchia, Lüscher 1978; Eichenherr 1978):

```
L = 2c₂ |D_μ w|² + (c₄/4) F_μν F^μν,      D_μ w = (∂_μ − iA_μ) w             (8)
```

A reader familiar with field theory recognizes the form (8) instantly: it is **the Lagrangian of a charged scalar field `w` coupled to the electromagnetic field `A_μ`** — the template of all electrodynamics of matter. The only difference from the textbook: here `A_μ` is not an independent field but a function of `n` (4).

Standard trick: temporarily treat `A_μ` as an independent auxiliary field and vary with respect to it. We obtain:

```
c₄ ∂_ν F^νμ = 2c₂ j^μ_CP¹,      j^μ_CP¹ = i(w̄ D^μ w − w \overline{D^μ w})    (9)
```

— the inhomogeneous Maxwell equations, where on the right stands the canonical current of a charged scalar field. (The numerical prefactor in (9) depends on the conventions `F = 2(∂A−∂A)` and the normalization of `w`; it is not needed in what follows — the physical normalization of the charge is fixed by the covariant derivative, §6.2.)

**Why the trick is legitimate** (the standard justification for CP¹ models): equation (9), regarded as an equation for `A`, is algebraic, with no derivatives of `A`; its solution reproduces exactly the definition `A = A[z]` of (4). That is, varying with respect to `A` adds no new physics — it returns the very definition of `A`. Analogy: having introduced the notation `s = a + b`, one may "vary with respect to `s`" — one gets `s = a + b` back; the notation has not thereby become a new entity.

The current `j^μ_CP¹` coincides with the current (7) from the Leibniz identity (on the constraint `A = A[n]`) — but is written through the singular encoding and is therefore unfit for computation (§5.4). Its value is interpretive: **the source in Maxwell's equations behaves exactly like charged matter, although there is no separate "matter" in the theory — there is only the field of arrows.** The field–particle duality here is literal: both the "photon" part (`F_μν`) and the "charge" part (`j^μ`) are assembled from one `n`.

### 6.2. The coupling constant and the cross-check with the geometric charge (verified 2026-07-02)

The normalization `g₀` is fixed by **matching energies**: the Skyrme term of the Lagrangian (1) must coincide with the Maxwell term. Writing `F_μν = 2G_μν` (where `G_μν = ∂_μA_ν − ∂_νA_μ`, formula (4)) and `F_phys = γG` (i.e. `A_phys = γA`), from the equality `(c₄/4)F² = C₄G² = (1/4μ₀)F_phys²` we obtain:

```
γ = 2√(μ₀ c₄),      g₀ = γ/2 = √(μ₀ c₄)                                      (10)
```

The constant linking the geometry to volts and teslas is **not free** — it is expressed through the stiffness `c₄` and the density `μ₀` of the medium. At the canonical value `c₄ = 2ℏc` (the code convention, `c₄ = 1` in sim-units) the Skyrme term is **identically** equal to the Maxwell energy density — the remark of §2.2 becomes, at this normalization, an exact equality by construction.

> ⚠ **Correction.** In an early version of the derivation the constant was written as `g₀ = √(2c₂/(μ₀c₄))` — from matching the source equation under the additional assumption that "the current is rescaled by the same constant as the field". The audit of 2026-07-02 showed that this form is dimensionally incompatible with the energy normalization; the correct form is (10). The rescaling of the current is a separate constant, fixed by the charge, not by the field.

**From `g₀` to the charge.** The minimal coupling in (8): `D_μ = ∂_μ − iA_μ = ∂_μ − i(A_phys,μ/γ)`. Comparison with the SI form `D = ∂ − i(q/ℏ)A_phys` gives the charge of the quantum of the field `w`:

```
q_w = ℏ/γ = ℏ/(2√(μ₀c₄))   ⟹   q_w² = ℏ²/(4μ₀c₄) = ℏε₀c/8 = (π/4)·l₀⁴
```

(the last equality by the structural identity `l₀⁴ = ε₀ℏc/2π`). The corresponding fine-structure constant comes out **exact and universal** — ℏ and the medium's impedance cancel:

```
α_w = q_w²/(4πε₀ℏc) = 1/(32π) ≈ 1/100.53
```

**Comparison of the two routes** (script `code/verify_g0_and_identity_3d.py`, all identities to 15 digits):

| | dynamical (CP¹, this work) | geometric [SI-reduction §7] | agreement |
|---|---|---|---|
| law | `q_w² = (π/4)·l₀⁴` | `e² = (π²/16)·l₀⁴` | **charge² ∝ l₀⁴ — both** ✓ |
| `α` | `1/(32π) = 1/100.5` | `1/128` | gap exactly `4/π ≈ 1.273` |
| effective radius | `0.531·l₀` | `0.500·l₀` (plateau `r_v = 0.498`) | 6% |

Structural upshot: **the CP¹ dynamics independently reproduces "charge = area ∝ l₀²"** — the form of Hyperbola II — from the Lagrangian normalization alone, without geometric arguments about the vortex tube. The coefficient, however, differs by exactly `4/π`. In passing — the exact identity `q_w² = e·l₀²` (the charge of the `w`-quantum is the geometric mean of the defect area and the cell area; recorded as an observation, not a derivation). Determining which object the elementary charge belongs to — the field quantum `w` or the vortex tube of the defect — and deriving the factor `4/π` is the refined form of the open question of §9.

### 6.3. Charge is quantized — a theorem, not an observation

The integral charge of a configuration:

```
Q = ∫ j⁰ d³x ∝ ∮ F₁₂ d²x = 4π × (number of windings of n: S² → S²) ∈ 4πℤ
```

Meaning: going around a closed surface about the defect, the arrow `n` runs over the whole sphere of directions some number of times — and this number must be **integer**: one cannot wind a sphere onto a sphere "one and a half times" without tearing the field. Electric charge is quantized because the winding is quantized. The sign of the charge is the direction of the winding (particle and antiparticle — opposite windings).

Compare with standard physics: there the quantization of charge is an empirical fact without explanation (or the Dirac argument, which requires the existence of a magnetic monopole — which nobody has seen). Here it is a theorem about continuous maps, and no monopole is needed for it; on the contrary, it is forbidden by Theorem 1.

---

## 7. The physical picture: where Maxwell is exact and where it ends

### 7.1. The far zone: exact electrodynamics

Far from the defect core (`r ≫ l₀`) the arrows turn smoothly, the current (7) falls off faster than any Coulomb term (`~1/r⁵` for the test configuration), and

```
∂_μ F^μν → 0
```

— the free Maxwell equations. **In the far zone Maxwell's equations are an exact, not an approximate, description**: the corrections are not "small relative to something", they are concentrated in the core and simply do not reach the far zone. The topological charge of the defect acts as a point source of the far field — this is the familiar "point charge" of electrostatics.

The photon in this picture is a linear wave of the field `n` on a uniform background: a ripple of arrows without winding (the sector `Q = 0`). Its masslessness (light does not decay or disperse in the vacuum) is consistent with the strict experimental bounds on the photon mass (`< 10⁻²⁷` eV) and on the dependence of the speed of light on frequency (`Δc/c < 10⁻²⁰`, Fermi GBM gamma-ray bursts) — a detailed dispersion analysis is deferred to a separate work of the program.

### 7.2. The core: finite mass instead of a divergence

Classical electrodynamics has a century-old disease: the self-energy of a point charge is infinite (a field `~1/r²` as `r → 0` gives a divergent energy integral). Here at `r ≲ l₀` the picture is different: the nonlinear terms of the field `n` dominate, and **the same structure that gives Maxwell in the far zone gives a finite energy in the core**. Numerical minimization of the total energy of the knot gives a finite bare electron mass `m_e^bare = 446.279 keV` [electron-mass]. Not two different mechanisms ("electrodynamics" plus a "regularization" stitched onto it), but one object — the field `n`: its linear tail is called electromagnetism, its nonlinear core is the mass of the particle.

Hierarchy of descriptions:

```
dynamics of the field n (fundamental everywhere)
   ⊃ Maxwell's equations (exact in the far zone, r ≫ l₀)
   ⊃ the Coulomb field of a point charge (the leading term of the far zone)
```

### 7.3. Why this is not "repackaging"

Let us pre-empt an objection: "since the equations are identities valid for any `n`, they are contentless — you have predicted nothing, you have merely rewritten the known." Answer: the content has not disappeared, it has **moved from the equations into the carrier**. Compare the lists of postulates:

| | Standard electrodynamics | This work |
|---|---|---|
| Form of the 4 equations | postulate | identity (theorems 1–2) |
| What `ρ`, `j` are | external data, put in by hand | a computable function of the field (7) |
| Quantization of charge | an unexplained fact | a theorem about windings (§6.3) |
| Coupling constant | measured | formula (10) from the medium's moduli |
| Behaviour as `r → 0` | divergence | finite mass (§7.2) |
| Magnetic monopole | admissible (even desirable) | **forbidden** (§4.1) |

The falsifiability has moved to the same place: the picture can be broken by showing that the real source current is *not* localized on defects, that charge is *not* topological, or that deviations from Maxwell at small scales have the wrong structure (§9).

### 7.4. The free field as an oscillator of the medium: displacement current = elasticity

The far zone (§7.1) is the free field `n` on a uniform background. Here it is useful to read the derived equations in the **mechanical dictionary** of the Cosserat medium [SI-reduction], where the medium's parameters and the field's components are identified as follows:

```
1/ε₀ = G (shear modulus),   μ₀ = ρ (density)
E ↔ σ (stress),   D ↔ γ (strain),   H ↔ v (velocity),   B ↔ ρv (momentum density)
```

(`D ↔ γ` follows from `[Q] ↔ [m²]`: then `[D] = C/m²` is dimensionless — a fraction of strain; [SI-reduction §6].)

**Two energy densities — elastic and kinetic.** Substituting the dictionary into the Maxwell densities gives identically:

```
electric   ½ε₀E²  =  ½σγ    — elastic (potential)
magnetic   ½B²/μ₀ =  ½ρv²   — kinetic
```

(check: `½ε₀E² = ½σ²/G = ½σγ` by Hooke `γ = σ/G`; `½B²/μ₀ = ½(ρv)²/ρ = ½ρv²`.) The electric sector of the medium is elastic, the magnetic one is inertial.

**Displacement current = rate of elastic strain.** In this dictionary the Maxwell displacement current reads as

```
J_disp = ∂D/∂t  ↔  ∂γ/∂t      (strain rate)
```

— not a transport of charge, but the **elastic response** of the medium: a strain changing in time. In covariant notation (§5) it is part of `∂_μ F^μν` (the field's own variation), not the source `j^ν`; in vacuum `j = 0`, and the field sources itself — that is the wave.

**The free field is a harmonic oscillator.** The two source-free curl pairs,

```
∇×H = ∂D/∂t ,     ∇×E = −∂B/∂t ,
```

link the elastic sector (`E`, `½σγ`) with the inertial one (`B`, `½ρv²`): the energy sloshes between them. Eliminating one pair through the other gives the wave equation with

```
ω² = (G/ρ) k² = c² k² ,     c = √(G/ρ)
```

— a transverse elastic wave of the medium, identical to light (the very coincidence of §2.1). **The photon = a free oscillation of the medium between its elasticity (`E`) and its inertia (`B`)**, and the displacement current is the "spring" term: without it there is no return stroke, and hence no wave. Maxwell's very addition of it (1861–62) closes the oscillator.

**The lumped limit = the `LC` circuit.** The same oscillator in a circuit: capacitor (elasticity, stores `½σγ`) ↔ inductor (inertia, stores `½ρv²`), `ω = 1/√(LC)` — the discrete analogue of `ω = ck`. Dissipation (the conduction current of the knots, §5–6) is viscous friction: the medium's resistivity has units of viscosity, `Ω·m = Pa·s`.

**Status.** This is a **mechanical reading** of the already-derived field equations (via the dictionary of [SI-reduction]), not a new theorem: level [2] (isomorphism), no new number. It clarifies the physics of the free sector — light as an elastic wave of the medium, displacement current as its elasticity — and is consistent with the core (§7.2), where the same medium is nonlinear and gives birth to mass.

---

## 8. The structure of the current in the core: a bridge to `r_v = l₀/2` and `α`

This section links the article to the numerical results of the program; a reader interested only in the derivation of Maxwell may skip it.

Two words of context. A **hopfion** is a three-dimensional knot of the field `n` (a twist closed into a ring, topologically irremovable); in the program the hopfion with `Q = −1` is identified with the electron. The **fine-structure constant** `α ≈ 1/137` is a dimensionless measure of the strength of the electromagnetic interaction; in [SI-reduction §7] its bare value `α_bare = 1/128` is derived from the geometry of the knot: charge = the cross-sectional area of a vortex tube of radius `r_v = l₀/2`. Question: where does the radius `r_v` itself come from? A partial answer is given by the structure of the current (7).

The equation of motion of the field `n` from the Lagrangian (1) (with a Lagrange multiplier for the constraint `|n| = 1`):

```
c₂ □n + c₄ ∂_μ[F^μρ (∂_ρ n × n)] = λ n                                       (11)
```

Without the Skyrme term (`c₄ = 0`) the solutions are harmonic, `□n ∥ n`, and term1 in the current (7) vanishes (§5.2). But in a real hopfion `c₄ ≠ 0`: the Skyrme term tilts `□n` away from the direction of `n`, and term1 switches on. Expressing it from (11):

```
term1 = n·(□n × ∂^ν n) = −(c₄/c₂) ∂^ν n · (n × ∂_μ[F^μρ(∂_ρ n × n)])
```

The ratio of the two current terms:

```
|term1| / |term2| ~ c₄/c₂ = l₀²
```

(up to a numerical factor of order unity depending on the normalization; in the lattice normalization `c₄/c₂ = l₀²/12`). In words: **the structural step of the medium `l₀` enters directly into the make-up of the electromagnetic current inside the particle.** The balance term1 + term2 determines how the charge is distributed over the vortex tube, and with it the radius of the tube. Numerically: `r_v = 0.498 · l₀` — a plateau, stable under variation of the anisotropy `K₃/K₁ = 3.5–7.5` and a 16-fold variation of `c₄`. Hence the chain:

```
identity (6) → structure of the current (term1/term2 ~ c₄/c₂) → r_v = l₀/2 → e = π(l₀/2)² → α_bare = 1/128
```

The first arrow is this work; the rest are [SI-reduction] and [electron-mass]. The chain is given to show that the derivation of Maxwell is not an isolated bit of prettiness but a load-bearing element of the same construction that yields `α` and the electron mass.

---

## 9. Boundaries, open problems, falsifiability

**What is proved.** Theorems 1–2 are mathematical facts about smooth maps into `S²`; their numerical verification is at the accuracy limit of the scheme. The CP¹ derivation is a standard procedure with a known justification.

**What is identified but not carried to completion.**

1. **Consistency of `g₀` and `e = π(l₀/2)²` — ✓ checked 2026-07-02, partially closed (§6.2).** The energy normalization `g₀ = √(μ₀c₄)` is unique; the dynamical charge `q_w² = (π/4)·l₀⁴` reproduces the law "charge² ∝ l₀⁴" (the structure of Hyperbola II confirmed dynamically), `α_w = 1/(32π)` against `α_bare = 1/128` — a factor of exactly `4/π` remains. The derivation of this factor is open; the candidate for the resolution is the difference between the objects "field quantum `w`" ↔ "vortex tube of the defect".
2. **Verification on the 3D hopfion — ✓ carried out 2026-07-02 at the ansatz level (script `code/verify_g0_and_identity_3d.py`).** The identity (6) is checked on the canonical hopfion (`R_r = 0.641, R_z = 0.807, w = 0.702` [electron-mass]) in full 3D: the residual `0.595% → 0.204% → 0.130%` on grids `192³/256³/288³` — falls as `dx⁴` (the order of the finite-difference scheme), i.e. it is purely a discretization effect; `E_Sk(3D)` coincides with the canonical 2D value to `0.12%`. For the first time the regime term1 ≠ 0 is seen numerically: `‖term1‖/‖term2‖ = 0.372` (stable across grids) — the Skyrme contribution to the current is switched on, as §8 predicts. What remains: a check on the full-field relaxation (not the ansatz) and the quantitative link of `term1/term2` to the plateau `r_v`.
3. **Derivation of `c₄` from the microscopics.** The Skyrme coefficient is fixed by the condition `√(c₄/c₂) = l₀` phenomenologically; a rigorous derivation from the medium's lattice Hamiltonian is an open problem of the program.
4. **Maxwell with dimensional coefficients.** The full writing `∇·E = ρ/ε₀` etc. with restored SI units and an end-to-end check of the numerical factors (`½` from (4), `4π` from §6.3) — a technical but mandatory piece of work.

**How the picture is falsified.**

- The discovery of a **magnetic monopole** would refute Theorem 1 (it would require an internal space of dimension above 2). A rare case where the program is *stricter* than the Standard Model: there a monopole is admissible and even expected in extensions, here it is forbidden.
- A **non-integer** free electric charge (not a multiple of the confinement-sector fractions) would destroy the topological interpretation of §6.3.
- Deviations from Maxwell's equations at small scales must have a **specific structure** (7)/(11) and the scale `l₀`; nonlinearity of a different structure would contradict the model.

---

## 10. Summary

| # | Claim | Status |
|---|---|---|
| 1 | `∇·B = 0`, Faraday's law — a Bianchi identity from the two-dimensionality of `S²` | theorem (§4) |
| 2 | `∇·E = ρ`, Ampère's law — a Leibniz identity with the computed current (7) | theorem (§5) |
| 3 | The current is localized (`1/r⁵`), non-singular, `∫j⁰ ∝ Q ∈ ℤ` | theorem + numerical ✓ (§5.3–5.4) |
| 4 | Numerical residual of the identity on the BP instanton | **0.0001%** (§5.4) |
| 5 | CP¹: current = matter, `g₀ = √(μ₀c₄)`, `α_w = 1/(32π)` exactly | derivation + check ✓ (§6) |
| 6 | Charge is quantized topologically (windings of the sphere onto the sphere) | theorem (§6.3) |
| 7 | Maxwell is exact in the far zone; the core gives a finite mass | corollary (§7) |
| 8 | term1/term2 ~ `c₄/c₂` → `r_v = l₀/2` → `α_bare = 1/128` | bridge to [SI-reduction] (§8) |
| 9 | `g₀` ↔ `e`: the law `charge² ∝ l₀⁴` — both routes ✓ | factor `4/π` **open** (§6.2) |
| 10 | Check of (6) on the 3D hopfion: residual ∝ `dx⁴`, term1/term2 = 0.372 | ✓ at the ansatz level (§9) |

In one line: **if every point of the vacuum has a direction, then Maxwell's electromagnetism is not a law of nature but a theorem of geometry; what remains a law of nature is the medium itself.**

---

## Appendix A. Glossary

| Term | Meaning in this article |
|---|---|
| **Director `n`** | A unit vector "arrow", the orientation of a point of the medium. A term from liquid-crystal physics |
| **`S²`** | The surface of the unit sphere = the set of all directions of a three-dimensional arrow |
| **`ℝ³·¹`** | Space-time: 3 spatial coordinates + time |
| **Identity vs law** | An identity is true automatically, by construction; a law is a statement about nature, testable by experiment |
| **Bianchi identity** | The general name for relations of the form `∂_[λ F_μν] = 0` holding for geometric reasons |
| **Leibniz rule** | The product rule for differentiation: `(fg)' = f'g + fg'` |
| **Scalar triple product `a·(b×c)`** | The volume of the parallelepiped on three vectors; zero ⟺ the vectors lie in one plane |
| **Pullback of the area form** | Transfer of a form from the target of a map back to the source; here: the area on the sphere of directions swept by the arrow under a shift along a pair of directions in space-time (the oriented area of the parallelogram projected onto the normal `n`) (§3.1) |
| **Harmonic map** | A field configuration minimizing the pure elastic energy (an analogue of a soap film); satisfies `□n = −|∂n|²n` |
| **Belavin–Polyakov (BP) instanton** | The simplest exactly known texture winding the plane onto the sphere once; the standard test object (§5.4) |
| **Hopfion** | A three-dimensional knot of the field `n` — a closed twist, irremovable by smooth deformation; the candidate for the electron in the program |
| **Topological charge `Q`** | The integer number of windings of the sphere onto the sphere; in this picture = electric charge in units of `e` |
| **CP¹** | The encoding of the sphere by a single complex number (stereographic projection); convenient, but has a defective point — the "pole of the map" |
| **Skyrme term (`c₄`)** | The energy term that switches on under rapid turns of the field; prevents the knot from collapsing to a point |
| **`l₀`** | The medium's own length scale, `≈ 0.46 nm`; built from `{ε₀, μ₀, ℏ}` [SI-reduction] |
| **`α` (fine-structure constant)** | A dimensionless measure of the strength of the electromagnetic interaction, `≈ 1/137`; the program's bare value `α_bare = 1/128` |
| **Far zone / core** | `r ≫ l₀` (Maxwell exact) / `r ≲ l₀` (nonlinearity dominates, mass is born). In the literature: the IR and UV regimes |

---

## Reproducibility

```bash
python3 code/verify_maxwell_v3.py            # identity (6) on the 2D BP instanton
python3 code/verify_g0_and_identity_3d.py    # g₀ ↔ e audit + identity on the 3D hopfion
```

The first script is self-contained (numpy): it builds the BP instanton `Q = −1` on a `512²` grid, computes both sides of the identity (6) by 4th-order finite differences, and prints the global and radial residuals and `‖term1‖/‖term2‖`.

The second (numpy + torch, CUDA desirable): part A — the audit of the normalizations of §6.2 in pure SI (all identities `q_w² = ℏε₀c/8 = (π/4)l₀⁴ = e·l₀²`, `α_w = 1/(32π)` — to 15 digits); part B — the canonical hopfion `(R_r, R_z, w) = (0.641, 0.807, 0.702)` from [electron-mass] on a 3D grid `256³`: the identity (6), `E_Sk`/`E_OF` against the canonical 2D values, `‖term1‖/‖term2‖`.

---

## Methodology and use of AI tools

In preparing this work the author used the large language model **Claude (Anthropic)** for the following auxiliary tasks: writing Python scripts for the numerical verification of the identities (§5.4 — the Leibniz identity on the Belavin–Polyakov instanton, residual `0.0001%`; §6.2 and §9 — the audit of the energy normalization `g₀ ↔ e` and the check of the identity on the canonical 3D hopfion, residual `∝ dx⁴`), stylistic proofreading and editing of the manuscript, and checking bibliographic references and formatting tables.

All key positions of the work — the framing of Maxwell's equations as identities for the director field `n: ℝ³·¹ → S²`, the assembly of the complete derivation of all four equations in one frame (Theorem 1: the homogeneous pair from `dim S² = 2`; Theorem 2: the Leibniz identity that computes the current), the non-singular form of the current through the vector `n` itself, the physical identification in the Cosserat medium and the energy normalization `g₀ = √(μ₀c₄)`, the topological quantization of charge and the bridge to `r_v = l₀/2` and `α_bare = 1/128`, and the precise localization of the boundary of applicability of linear electrodynamics — belong to the author (the classic sigma-model objects are attributed in §1.4).

The author has carefully checked all generated code (by independent reproduction of the numerical residuals and identities) and the manuscript text, and takes full responsibility for the final content and results of the work.

---

## References

**How to cite this work:** Yeusiyevich I. V., *Maxwell's Equations as Theorems about the Director Field `n: ℝ³·¹ → S²`* (2026). DOI: [10.5281/zenodo.21264016](https://doi.org/10.5281/zenodo.21264016).

1. J. C. Maxwell, *On Physical Lines of Force*, Phil. Mag. (1861–62) — the original mechanical derivation of the equations.
2. E. Cosserat, F. Cosserat, *Théorie des corps déformables*, Paris (1909).
3. A. C. Eringen, *Linear Theory of Micropolar Elasticity*, J. Math. Mech. **15** (1966).
4. T. H. R. Skyrme, *A unified field theory of mesons and baryons*, Nucl. Phys. **31** (1962).
5. L. D. Faddeev, *Quantization of solitons*, Princeton preprint IAS-75-QS70 (1975).
6. A. A. Belavin, A. M. Polyakov, *Metastable states of two-dimensional isotropic ferromagnets*, JETP Lett. **22** (1975) 245.
7. A. D'Adda, M. Lüscher, P. Di Vecchia, *A 1/n expandable series of non-linear σ-models with instantons*, Nucl. Phys. B **146** (1978) 63.
8. H. Eichenherr, *SU(N) invariant non-linear σ-models*, Nucl. Phys. B **146** (1978) 215.
9. R. Rajaraman, *Solitons and Instantons*, North-Holland (1982), ch. 4 — a textbook exposition of the CP¹ formalism.
10. [SI-reduction] Yeusiyevich I. V., *Structural reduction of the SI base units via the Cosserat-continuum hypothesis* (2026), DOI: 10.5281/zenodo.20187199.
11. [electron-mass] Yeusiyevich I. V., *Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}`* (2026), DOI: 10.5281/zenodo.20477123.
12. [gravity-second-channel] Yeusiyevich I. V., *Gravity as the second channel of the Cosserat medium* (2026), Cosserat-program preprint.
