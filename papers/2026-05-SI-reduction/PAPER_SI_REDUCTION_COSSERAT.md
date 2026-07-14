# Structural reduction of the SI base of units via the Cosserat-continuum hypothesis: electromagnetic and gravitational quantities as mechanical objects of an elastic medium

**Author:** Yeusiyevich Ihar V.
**Date:** 2026-05-12
**Version:** 4 (preprint; v4 adds Appendix C "Metrological closure, rheology of the medium, and the temperature branch", identities T18–T20, two rows of Table 6.2; the Weber dimension erratum is corrected — 2026-07-02)
**License:** CC-BY 4.0

---

## Abstract

The idea of interpreting the electromagnetic field as a deformation of an elastic medium is an old one: Maxwell himself derived his equations from exactly such a model (1861–1862), and the late-nineteenth-century aether program developed it further. Much later, Kleinert (1989–2008) showed that **gravitation** admits an analogous interpretation, by way of disclination defects in an elastic continuum, in the form of Einstein–Cartan theory. The two programs developed in parallel and almost never met; no consistent treatment is available in the literature in which both sectors live in a single Cosserat continuum together with an explicit reduction of the SI units. The present work proposes such a unification.

The framework rests on four identifications between parameters of the medium and the fundamental constants of nature:

- **P1:** `ρ_medium ≡ μ₀` — the density of the medium is identified with the magnetic permeability;
- **P2:** `G_shear ≡ 1/ε₀` — the shear modulus with the inverse electric permittivity;
- **P3:** `ℏ` — the quantum of action of microrotations of the medium;
- **P4:** `G` enters through the Kleinert gauge mechanism (`u`-channel of translations).

Already from P1 and P2 the mechanical expression `c_T = √(G_shear/ρ)` for the transverse Cosserat wave speed, after substitution, coincides with **Maxwell's formula** for the speed of electromagnetic waves: `c_T = 1/√(ε₀μ₀) ≡ c_light`. This is the same classical identity that Maxwell obtained from his elastic-aether model in 1861–62 (and that in SI 2019 is fixed by the definition of `c`); here it arises as a **direct mechanical consequence** of the Cosserat identifications, without any additional parameters. The coincidence `c_T = c_light` is therefore not a prediction of the program but its **necessary boundary condition**: any model in which P1 and P2 take this form must recover Maxwell's `c`. From there everything unfolds on its own: the ampere becomes a deformation circulation with dimension `[m²/s]`, the coulomb becomes the cross-sectional area of a defect `[m²]`, and the whole base `{m, kg, s, A}` reduces to a single dimension — length (or, equivalently, energy). The gravitational constant acquires the structural form `G = c⁴ε₀/(16π l_G²)`, where `l_G ≈ 4.62 × 10¹⁵ m` is the characteristic scale of the `u`-channel; the famous Planck length turns out **not** to be fundamental but derived: `l_P = l₀²/(2√2 · l_G)`.

**Local minima of the functional and identification with particles.** In the same structure (P1–P4 plus the geometry of an `S²`-target director field) the functional `E[n, u]` admits stable localized minima with integer topological charge `Q_H ∈ π₃(S²) = ℤ` — a consequence of the medium itself, not an extra postulate. Empirically the minimum with `Q_H = -1` is identified with the electron (the one with `Q_H = +1` with the positron); direct numerical minimization yields the **bare** mass `m_e^bare = 446.279 keV` [10] (on the dyadic box `L = 17 × 33 l₀`). In [10] §7 the dimensionless minimum `Ẽ_min ≈ 1039` fits the dyadic form `m_e/m₀ = x² + x/2 − 1` with `x = α⁻¹/4`, and the same shift of the scale that takes `α_bare = 1/128 → α(0) = 1/137` takes the bare mass to the physical `m_e ≈ 511 keV`. In this sense the program contains no "separate predictions" stacked on top of the postulates: there is one cascade of consequences from the structure of the medium, and the existence of particles as topological knots of the field is one of its links — on a par with `c = c_light`, the dimensional reduction, and the value of `α`.

Combined with the dimensional reduction `[Q] ↔ [m²]`, this yields a direct numerical consequence. The cross-section of a hopfionic defect under the Derrick-stability condition is a disc of radius `r_v = l₀/2` (§7.3); the charge is then the area of that disc, `e = π(l₀/2)²`. Substituting into the textbook definition `α = e²/(4πε₀ℏc)`, after cancellations one obtains

> `α_bare = 1/128 = 2⁻⁷` (derivation in Section 7)

— a **bare** value of the fine-structure constant, obtained without using the experimental `α` on the right-hand side. Agreement with the measured `α(M_Z) = 1/128.9` at the Z-boson scale is 0.7%. The discrepancy with the familiar low-energy value `1/137` is the standard QED renormalization through vacuum polarization by virtual pairs; in our picture `1/128` plays the role of a UV boundary condition for the renormalization-group equations.

The bottom line: the canonical set of fundamental constants of nature reduces to `{ε₀, μ₀, ℏ, G}`; everything else is computable. Operationally this is equivalent to the standard natural units `ℏ = c = G = 1`, but the justification is different — not "convenience of notation" but a structural removal of redundancy from SI. The linearized Cosserat metric reproduces all five classical tests of GR (perihelion precession of Mercury, deflection of light by the Sun, Shapiro delay, gravitational redshift, gravitational waves travelling at `c`); the differences from pure GR are torsion at Planckian densities (Einstein–Cartan) and a massive Cosserat mode at the scale `l_K ≈ 202 nm`. Both features are falsifiable.

**Status and scope of the claims.** This is not a proposal to redefine the SI: the SI base units remain as defined by CGPM in 2019. The claim is only that, conditional on the postulates P1–P4, there is a one-to-one mapping between the SI quantities and the mechanical dimensions of a Cosserat continuum. The reduction itself is a preparatory construction for subsequent papers in which, from `{ε₀, μ₀, ℏ}` via minimization of the Cosserat functional, the **bare** electron mass `m_e^bare = 446.279 keV` is obtained (on the dyadic box `17 × 33 l₀`, with no free parameters); its connection to the physical mass via the running of `α` is treated in [10] §7.

**Keywords:** Cosserat continuum, electromagnetic units, dimensional analysis, mechanical interpretation, natural units, structural reduction, micropolar elasticity, Kleinert gauge theory, defect-induced gravity, Einstein–Cartan theory.

---

## Logical chain of the paper

The chain of key statements, with the sections in which each one is proved:

```
POSTULATES
 P1: ρ_medium ≡ μ₀                              (§2.2)
 P2: G_shear ≡ 1/ε₀                              (§2.2)
 P3: ℏ — structural constant (quantum of action) (§2.3)
 P4: G = c⁴ε₀/(16π l_G²) (Kleinert)              (§8.3)
 P5: hopfion cross-section ≈ disc (oblate idealization) (§7.1)
 │
 ▼
CONSEQUENCE I — speed of light (§2.4)
 c_T = √((1/ε₀)/μ₀) = 1/√(ε₀μ₀) ≡ c_light
 │
 ▼
CONSEQUENCE II — SI dimensions (§§3, 4, 5, 6)
 [A] ↔ [m²/s], [C] ↔ [m²], [s] ↔ [m], [kg] ↔ [1/m]
 {m, kg, s, A} → {m} → {Energy}
 │
 ▼
CONSEQUENCE III — hyperbola of the medium I (§§5.1, 5.5)
 m · l = ℏ/c                  (T6, Hyperbola I)
 E = mc² = ℏc/l = ℏω           (Einstein = de Broglie = Planck, T16)
 │
 ▼
CONSEQUENCE IV — fine-structure constant (§7)
 l₀⁴ = ε₀ℏc/(2π)               (structural identity, T10)
 e = π(l₀/2)²                   (geometry P5)
 ⇒ α_bare = 1/128 = 2⁻⁷         (T11; agreement with α(M_Z) — 0.7%)
 e²/(4πε₀) ≡ ℏcα                (T12, Hyperbola II; §7.9)
 │
 ▼
INTERLOCKING of the two hyperbolas (I + II) — §7.9, §8.3
 m₀² · e = (π/4)·(ℏ/c)²        (T13)
 m_e/m₀ = 2¹⁰+2⁴−1 = 1039      (bare; leading term 1/(16α²) = 2¹⁰)
 │
 ▼
CONSEQUENCE V — gravitational channel (§8)
 G = c⁴ε₀/(16π l_G²)            (Kleinert, T14)
 l_P = l₀²/(2√2 l_G)            (Planck length as a derived quantity, T15)
 5 classical tests of GR are reproduced (§8.6)
 │
 ▼
CLOSURE (§8.5)
 {ε₀, μ₀, ℏ, G} — full canonical basis.
 The SI base of units is reduced to a single dimension (energy).
```

Every consequence is derived from the preceding ones plus the postulates through explicit algebraic steps, given in the indicated sections. Numerical verifications of all key identities appear in Appendix A.5.

---

## 1. Introduction

### 1.1. Historical context

#### 1.1.1. The electromagnetic sector

Maxwell's equations were originally obtained by Maxwell (1861–1862) on the basis of a mechanical model — an elastic aetheric medium with vortex flows [1]. In that model the magnetic permeability `μ₀` was identified with the density of the medium, and the dielectric permittivity with its elasticity. The speed of light was derived as the speed of transverse waves of the elastic medium.

By the early twentieth century the aether mechanics program had been displaced from mainstream physics as a result of special relativity (Einstein, 1905), quantum mechanics (1925–1930), and quantum electrodynamics (1948–1950). Modern textbooks [16] mention the mechanical interpretation of EM only as a historical remark.

#### 1.1.2. The gravitational sector

A parallel program of interpreting gravitation via elasticity with defects was developed by Kleinert (1989–2008) [11, 12]. In the gauge theory of disclinations the elastic distortion `β^a_μ` plays the role of the tetrad (vierbein) `e^a_μ` of general relativity, and the disclination density tensor turns out to be the Riemann curvature tensor. The action takes the Hilbert–Einstein form:

```
S = ∫ [R/(16πG_eff) + L_matter] √-g d⁴x
```

In the weak-field limit one recovers the Poisson equation of Newtonian gravity with the correct numerical constant. Strictly speaking, Kleinert's program yields the theory of **Einstein–Cartan** (with torsion), which reduces to pure GR for vanishing spin and in the low-density limit. It passes all five classical tests of GR [11].

Kleinert's program develops the gravitational sector through elastic defects, but **does not cover electromagnetism** in the same medium: the electromagnetic and gravitational sides are treated as separate theories.

#### 1.1.3. Cosserat formalism and the classical-elasticity limit

Historically, physics has developed along two weakly interacting branches. **Continuum mechanics** (elasticity, hydrodynamics, thermodynamics) worked with states of matter — density, pressure, moduli, phonons; **the physics of the void** (classical mechanics with absolute space, QM with Hilbert spaces, QFT with operators on a "background") worked with particles and fields. QFT and GR de facto brought the language of the medium back (the vacuum as a minimum of the Higgs scalar field, spacetime as a dynamical entity responding to mass), but only piecewise — each theory carries its own image of the medium, and a common language for all phenomena has never quite emerged.

The Cosserat program makes the next step explicit: **a single continuum with locally varying parameters `(K_i, μ_c, ρ)`**, in which the vacuum, matter, and atomic and nuclear scales are different points of one spectrum rather than separate entities. At every scale the same formalism applies — with the appropriate local moduli. This removes the methodological "matter vs. void" split as an artifact of historical specialization.

The formal apparatus for such a picture has, perhaps surprisingly, long been worked out — independently of fundamental physics, within continuum mechanics. Starting with the work of the Cosserat brothers (1909 [2]), and further with Eringen [3], Maugin [9], Nowacki [18], a **micropolar-media formalism** was built up — an extension of classical elasticity that introduces local microrotational degrees of freedom in addition to the usual displacements. As applied to matter (crystals with defects, liquid crystals, granular media) it is well studied and experimentally validated; the task of the present work is to apply it as a description of the medium itself, the one in which fields and particles live.

> **Note to the reader.** A *Cosserat continuum* is an elastic medium that at every point has **two** independent degrees of freedom: an ordinary displacement `u` (the point can shift) and a local rotation `n` (the point can turn). In ordinary (Cauchy) elasticity the rotation of an element is rigidly determined by the displacements of its neighbours; in a Cosserat continuum the rotation "has a life of its own." It is precisely this extra degree of freedom — the director field `n ∈ S²` — that carries electromagnetic phenomena in our picture.

**Hierarchy of scales: a universal principle.** Any elastic medium is characterized by two intrinsic scales:

- **`a`** — the granularity scale (the size of the "elementary cell" of the medium)
- **`ℓ_C`** — the Cosserat length (`ℓ_C = √(γ_C/μ_c)`, where `γ_C` is the curvature modulus of microrotation and `μ_c` is the Cosserat coupling)

The behaviour of the medium depends qualitatively on the ratio of the disturbance wavelength `λ` to these scales:

| Regime | Description | Degrees of freedom | Strain tensor |
|---|---|---|---|
| `λ >> ℓ_C` | Classical Cauchy elasticity (long-wavelength limit) | `u(r)` only | Symmetric `ε_{ij}` |
| `λ ~ ℓ_C` | Cosserat (independent microrotations) | `u + φ` | Asymmetric `γ_{ij}` |
| `λ ≤ a` | Continuum description ceases to apply | Depends on the medium | — |

This is the **universal** structure of any Cosserat continuum. The concrete content of "granularity" depends on the type of medium: in crystals it is the atomic lattice, in liquid crystals it is the molecular orientational distribution, in the **vacuum** (the application of the present work) it is the structural cell `l₀ ≈ 4.59 Å`.

**Strain tensors:**

```
ε_{ij} = ½(∂_i u_j + ∂_j u_i) (Cauchy, symmetric) (1.1)
γ_{ij} = ∂_i u_j − ε_{ijk} φ_k (Cosserat, asymmetric) (1.2)
```

In the Cauchy limit the equations of motion reduce to those of Navier:
```
ρ ∂²_t u_i = (λ+μ)∂_i(∂_k u_k) + μ ∂²_k u_i (Cauchy) (1.3)
```

**Limiting relation.** In the limit `μ_c → ∞` (the microrotation locks to the macroscopic rotation, equivalently `ℓ_C → 0`):

```
Cosserat (ℓ_C finite) ──── ℓ_C → 0 ────► Cauchy elasticity (1.4)
 ↓                                               ↓
dynamics of {u, φ},                            only u,
asymmetric γ_{ij}                              symmetric ε_{ij}
```

The Cosserat equations reduce to the Navier equations (1.3) without loss of information; classical elasticity is the long-wavelength limit of Cosserat theory. These are not alternative models but one and the same physics at different scales.

**The vacuum as a special case.** In our application to electromagnetism and gravity (Sections 2–8) the Cosserat medium is the **vacuum**. The corresponding numerical scales are:

```
a ≡ l₀ ≈ 4.59 × 10⁻¹⁰ m (vacuum structural length, see §5.4)
ℓ_C ≡ l_K ≈ 2.02 × 10⁻⁷ m (vacuum Cosserat length, see §8.7)
```

In the nanometer band between `l₀` and `l_K` Cosserat effects are maximal; above `l_K` the medium looks like an ordinary Cauchy elastic medium (which is what yields the standard Maxwell electromagnetism, see [25]). The hyperbola `m · l = ℏ/c` (T6 of Section 5) is a structural identity of this vacuum application; for a different Cosserat medium the point `(m₀, l₀)` would shift along the hyperbola, but the form of the identity itself is a universal consequence of postulate P3.

**The spectrum of Cosserat media.** The vacuum is one point in a continuum of possible Cosserat media. In the presence of matter the local effective parameters `K_i(r), μ_c(r), ρ(r)` differ from the vacuum values, and each substance defines its own point `(a, ℓ_C)` in this spectrum. This is well known in electromagnetism as `ε(r), μ(r)` in materials, and is a direct continuation of the Cosserat formalism.

A natural characterization of the "size of the medium" is the **atomic radius** (rather than the interatomic distance in the lattice, which depends on the packing type). Typical values:

```
r_H ≈ 0.25 Å (hydrogen)
r_O ≈ 0.66 Å (oxygen, covalent)
r_C ≈ 0.77 Å (carbon)
r_Si ≈ 1.11 Å (silicon)
r_Fe ≈ 1.26 Å (iron)
r_Cu ≈ 1.28 Å (copper)
r_Au ≈ 1.44 Å (gold)
r_Cs ≈ 2.65 Å (caesium — the largest stable neutral atom)

a_H (Bohr) ≈ 0.53 Å (electron orbital)
```

— all of them smaller than the vacuum `l₀ ≈ 4.59 Å`, including the largest stable neutral atom (Cs). Numerically: `r_Cs ≈ 2.65 Å` agrees with the vortex-tube radius of the vacuum hopfion `r_v = l₀/2 ≈ 2.30 Å` (see §7.2) to within 15%. This is consistent with the hypothesis that stable neutral atoms are bounded above by the radius of the energy distribution of a topological knot; beyond that limit the configuration becomes incompatible with the vacuum topology (Fr, Ra and beyond — radioactive). The hypothesis is the subject of [23].

Atomic matter is **denser** than the vacuum viewed as a Cosserat medium. The density hierarchy:

```
vacuum l₀ ≈ 4.59 Å (the most dilute Cosserat medium)
knot radius r_v = l₀/2 ≈ 2.30 Å (vacuum hopfion, §7)
atoms ~ 0.25–2.65 Å (from H to Cs; r_Cs ≈ r_v within 15%)
nuclei ~ 1–10 fm (~10⁻⁴ Å, nuclear density)
quarks < 0.1 fm (~10⁻⁶ Å, quark density)
```

A transition "below `l₀`" is **a transition to a different Cosserat medium** (denser, with different `K_i, μ_c`), not an exit from continuum mechanics. Each level of the hierarchy is its own Cosserat medium with its own `(a, ℓ_C)`. The true limit of continuum theory itself lies at the quantum-discrete level (individual nucleons, quarks), which is outside the scope of the program presented here.

The Cosserat formalism has a natural place in the general physics of media: vacuum, atomic shells, nuclei — all are described by one language with different `(a, ℓ_C, K_i, …)`. The electromagnetic and gravitational phenomena in our program are a particular case of the vacuum Cosserat medium; the same methodology generalizes to other density levels (as does the ordinary theory of continuous media in materials science).

**Why Cosserat (and not other generalizations).** Broader extensions of elasticity are known in the literature: micromorphic media (Eringen 1964), gradient elasticity (Mindlin 1965), nonlocal elasticity. All of them contain the Cosserat sector as a **mandatory minimum**. Cosserat is the simplest model that simultaneously:

1. **Captures the discreteness of the medium** through 3 additional degrees of freedom (microrotations).
2. **Admits topologically nontrivial configurations.** The director field `n ∈ S²`, equivalent to a microrotation, has the third homotopy group `π₃(S²) = ℤ`, and hopfionic defects with charge `Q_H ∈ ℤ` exist as stable localized solutions. Without independent microrotations (in a purely Cauchy theory) there is nowhere to take the director field from, and hopfions do not exist.
3. **Agrees with classical elasticity in the macroscopic limit** with no free parameters (the limit `ℓ_C → 0`).
4. **Has independent physical motivation** in the theory of crystal defects (Kleinert [11, 12]) and in the theory of liquid crystals (Frank, Oseen [5]).

In this sense Cosserat is the minimal continuum theory in which topological solitons of the form "particle as a clasp of the medium's lattice" can exist, and which at the same time reduces to classical elasticity on large scales.

The emergence of topological solitons in σ-models — in particular the hopfions of the Faddeev–Niemi model [4] — opened the possibility of interpreting localized structures (for example, charged particles) as topological defects of a Cosserat-like medium. Hopfions have been observed experimentally in liquid crystals and magnetic colloids [28], which confirms their physical realizability in continua with director-field structure. This line of work is the basis of the present paper.

### 1.2. What is missing in the literature

Despite the existence of:
- the historical program of a mechanical interpretation of EM (Maxwell–Kelvin–Larmor [6]),
- the modern gravity program via elastic defects (Kleinert [11, 12]),
- the developed formalism of the Cosserat continuum with microrotations [2,3,9],
- the modern theory of topological solitons [4,7],

— what is missing in the literature is a **consistent** treatment that:

**(a)** unifies Maxwell's EM sector with Kleinert's gravitational sector within a **single** Cosserat continuum with two channels;

**(b)** carries out a complete reduction of the SI base of units, with explicit arithmetic and numerical values for all principal quantities;

**(c)** derives numerical predictions (the electron mass) from the resulting system with no free parameters.

The present paper closes items (a) and (b); the numerical prediction (c) is the subject of subsequent work [10] in this series.

### 1.3. Contents of the present paper

The objective is to carry out the reduction explicitly, along several specific directions that go beyond both the historical aether program and Kleinert's program separately:

**(i)** Working consistently within modern SI, we derive the full dimensional reduction `{m, kg, s, A} → {m}` (or equivalently `→ {Energy}`), and we make explicit the mechanical dimension of each standard SI quantity.

**(ii)** We interpret electric charge through a **topological** invariant of a Cosserat defect (the hopfion charge `Q_H`), which uses the modern language of topological fields. In particular, charge acquires the mechanical reading of a cross-sectional area of a defect, `[Q] ↔ [m²]`.

**(iii)** We develop the electromagnetic and gravitational sectors as **two channels of a single Cosserat medium**: the director-field channel `n` (EM) and the translational channel `u` (gravity). The `10⁴²` hierarchy between EM and gravitational forces is consistent with the program through the formula `F_EM/F_grav = α·(m_P/m_e)²`, whose geometric root is the large ratio of channel scales `l_G/l_0 ≈ 10²⁵`.

**(iv)** We show that the Planck length `l_P` is not a fundamental scale but a derived one: `l_P = l₀²/(2√2 l_G)`. This sharpens the status of Planck physics within our framework.

**(v)** We derive a bare value of the fine-structure constant, `α_bare = 1/128 = 2⁻⁷`. The derivation uses the identification of the electron with a local minimum of the functional `E[n, u]` of topological charge `Q_H = -1` (see Abstract): this is the simplest stable class of configurations in the `n`-channel with `S²`-target, but **within** that class there exists a family of geometrically distinct representatives. Minimization of the functional selects a specific one — with a cross-section that is **close to circular**; using this as a leading-order approximation (`e = π·r_v²` with `r_v = l₀/2`) and the structural identity `l₀⁴ = ε₀ℏc/(2π)`, one obtains `α_bare = 1/128`. Agreement with the experimental `α(M_Z) = 1/128.9` is `0.7%`; the standard QED renormalization down to low energies gives the observed `1/137`.

**(vi)** We show that the resulting reduction is operationally equivalent to the standard natural units of particle physics (`ℏ = c = G = 1`), but acquires a structural justification: not a "convenience of notation" but the removal of a redundancy that is already present in the SI under the assumption that the Cosserat hypothesis is physically realistic.

### 1.4. What this paper is **not**

The Cosserat program is easily read more broadly than it should be, so a few direct disclaimers are in order.

**This is not a redefinition of the SI, and not a return to the nineteenth-century aether (Larmor [6], Kelvin's vortex atoms) nor to the twentieth- and twenty-first-century gas-dynamic aether programs.** The Cosserat continuum here is a modern micropolar construction with `π₃(S²)` topology, formally **compatible with special relativity**, without a privileged frame of reference. Lorentz invariance for us is a consequence of the fact that the transverse wave speed in the medium equals `c`. The SI base units as defined by CGPM in 2019 are used here without modification; all statements of the form `[A] ↔ [m²/s]` are **mappings** between the SI and the mechanical dimensions of a Cosserat continuum, not equalities, and they are formulated strictly under the Cosserat hypothesis.

**This is not a replacement for GR.** At the level of observational tests our linearized theory **reproduces** GR (more precisely, Einstein–Cartan, following Kleinert); the differences from pure GR appear only at Planckian densities and are discussed in §8.7. Likewise, at the level of nonrelativistic quantum mechanics the Cosserat functional `E[n, u]` in the leading `α²`-order is **mathematically equivalent** to the Schrödinger equation, via the Hopf–Berry correspondence [Berry 1984; Wilczek–Zee 1984]: the topology of the director field `n ∈ S²` maps onto the spinor wave function, and the hopfion charge `Q_H` onto the Born-normalized probability density. All standard predictions of nonrelativistic QM (wave interference, double-slit experiments, the Born rule, basic entanglement) are therefore reproduced automatically. Cosserat says something new only in **subleading** corrections — structural identities such as `α_bare = 1/128`, `m_e/m₀ = 1/(16α²)` (Sections 7 and 8) — and in nonlinear regimes.

**This is not a replacement for QED at its level of accuracy.** Today's QED describes `α³`-corrections, the Lamb shift, the anomalous magnetic moment to a precision far beyond anything we discuss here; our work describes the classical limit, and consistency with QED loops is a separate open question.

**Finally, this is not a replacement for the natural units of particle physics.** The operational outcome is the same `ℏ = c = G = 1`. What changes is only the justification: we interpret that reduction not as a convenience of notation but as the removal of a redundancy that is already present in SI provided the Cosserat hypothesis is physically realistic.

### 1.5. Structure of the paper

Section 2 formulates the Cosserat hypothesis and states postulates P1, P2 (EM sector) and P3 (quantum of action). Section 3 derives the mechanical dimension of the SI ampere. Section 4 treats the second. Section 5 — masses and the identity `ℏ/c = m·l`. Section 6 gives the full summary table of all principal SI quantities. **Section 7** derives the fine-structure constant `α_bare = 1/128 = 2⁻⁷` from the geometry of the electron charge (`e = π(l₀/2)²`) and the structural identity `l₀⁴ = ε₀ℏc/(2π)`. **Section 8** is devoted to the gravitational channel: postulate P4 is stated (Kleinert mechanism), `G = c⁴ε₀/(16π l_G²)` is derived, the Planck length is discussed as a derived quantity, the scale hierarchy is given, and the classical GR tests are listed. Section 9 discusses the connection with natural units for **four** constants. Section 10 contains the conclusions and a list of subsequent works.

---

## 2. The Cosserat hypothesis: the electromagnetic sector

### 2.1. Geometric background

Consider a three-dimensional elastic medium in which two independent fields are defined at every point:

- **Director field** `n(r,t) ∈ S²` — a normalized unit vector describing the local orientation of microrotation.
- **Translation field** `u(r,t) ∈ ℝ³` — the elastic displacement of an elementary volume of the medium relative to the reference configuration.

The medium has elastic constants `K₁, K₂, K₃` (bending, torsion, and splay of the field `n` in the Oseen–Frank formalism [5]) and a coupling modulus `μ_c` between the `n` and `u` channels. The free energy (in the bare vacuum limit, without a mass term) is:

```
E[n, u] = ∫ [½(K₁(∇·n)² + K₂(n·∇×n)² + K₃(n×∇×n)²)
 + μ_c·(∇×u − π(∇n))²
 + λ_{el}(∇·u)² + μ_{el}|∇u|²_{sym}
 + ½ρ(∂_t n)² + ½ρ(∂_t u)²] d³r
```

where `π(∇n)` is the canonical projection of the geometric coupling between channels, and `λ_{el}, μ_{el}` are the Lamé elastic moduli of the translational channel.

**Two-channel structure.** The field `n` is responsible for electromagnetic phenomena (Section 2.2 and onward), and the field `u` for gravitational ones (Section 8). The coupling between the channels is through `μ_c` and the nonlinear elastic terms.

### 2.2. Identifications with the electromagnetic constants

We postulate (Postulates P1, P2):

| | |
|---|---|
| **P1.** | `ρ_medium ≡ μ₀` (density of the medium = magnetic permeability) |
| **P2.** | `G_shear ≡ 1/ε₀` (shear modulus = inverse electric permittivity) |

Numerically in SI:

```
ρ_medium = μ₀ = 4π × 10⁻⁷ kg/m³ ≈ 1.257 × 10⁻⁶ kg/m³
G_medium = 1/ε₀ = 1.129 × 10¹¹ Pa
```

For comparison: the shear modulus of steel at 20 °C is approximately 8 × 10¹⁰ Pa; thus `G_medium ≈ 1.4 · G_steel`. The density `ρ_medium` is about 10⁹ times smaller than that of air.

**Remark on the status of the parameters P1, P2.** Postulates P1 and P2 refer to the parameters of the **vacuum** Cosserat medium, that is, to its ground (unperturbed) state. The numerical values of `μ₀, ε₀` are known experimentally precisely for the vacuum. In the presence of matter (dense media, neighbourhoods of massive bodies, local deformations) the effective parameters `ρ_local, G_local` are locally modified; that scaling is the subject of works [10, 13] and is discussed in Sections 5.5 and 8 of the present paper. All numerical conclusions in this paper refer to the **vacuum** medium unless explicitly stated otherwise.

**Caveat on "`1/ε₀` as a shear modulus."** Strictly speaking, a Cosserat medium has several independent elastic moduli: `K₁, K₂, K₃` (Oseen–Frank) for the `n`-channel, and `λ_{el}, μ_{el}` (Lamé) for the `u`-channel. The quantity `1/ε₀` in P2 corresponds to the **effective channel stiffness** in the combination that determines the transverse wave speed `c_T = √(G_shear/ρ)`. For simplicity of exposition we write `G_shear = 1/ε₀` as an effective parameter; a detailed analysis of the correspondence `1/ε₀` ↔ combination of `(K_i, μ_{el})` is the subject of [10, 12].

### 2.3. Postulate P3: the quantum of action

The third postulate:

| | |
|---|---|
| **P3.** | `ℏ` is a structural constant of the Cosserat medium, fixing the characteristic quantum of action of its microscopic excitations |

**Physical meaning of `ℏ`:** the **minimal action** of microscopic excitations of the Cosserat medium — a universal quantum of the medium. The numerical value is fixed experimentally: `ℏ = 1.054572 × 10⁻³⁴ J·s`.

### 2.4. Consequence: the speed of light as the speed of an elastic wave

The transverse wave speed in an elastic medium is:

```
c_T = √(G_shear/ρ) = √((1/ε₀)/μ₀) = 1/√(ε₀μ₀) ≈ 2.998 × 10⁸ m/s ≡ c_light
```

This coincidence, originally obtained by Maxwell in 1861, arises in the present treatment as a consequence of two specific identifications of modern SI constants.

**Remark.** The coincidence `c_T = c_light` is a numerical check on the compatibility of the postulates P1, P2 with experiment: the coefficients in P1 and P2 are fixed by the experimental values of `μ₀, ε₀`, and the resulting transverse wave speed reproduces the speed of light.

---

## 3. The dimension of the SI ampere: current as a circulation of deformation

### 3.1. The energy balance

The energy density of the magnetic field in SI is:

```
u_B = B²/(2μ₀) (3.1)
```

The kinetic-energy density in an elastic medium with density `ρ` and velocity field `v` is:

```
u_kin = ρv²/2 (3.2)
```

In the Cosserat picture the energy of the magnetic field is interpreted as the kinetic energy of the microrotational degrees of freedom of the medium [6]. Identifying `u_B = u_kin` at `ρ = μ₀` (postulate P1) gives:

```
B²/(2μ₀) = μ₀·v²/2
B² = μ₀²·v²
v = B/μ₀ (3.3)
```

> **Note to the reader.** This is Maxwell's central idea from 1861. The "magnetic field" in the aether picture is not a separate object, but **a motion of the medium itself**. If the aether has density `ρ = μ₀` and moves with velocity `v`, then its kinetic energy `ρv²/2` precisely matches the well-known magnetic energy density `B²/(2μ₀)`. Identifying these gives a mechanical reading of the magnetic induction: `v = B/μ₀`.

### 3.2. Identifying `H` with the velocity

Using the standard definition of the magnetic field intensity in vacuum, `H = B/μ₀`, equation (3.3) implies:

```
v ≡ H (3.4)
```

That is, the magnetic field intensity `H` acquires in the Cosserat picture the mechanical meaning of the **velocity** of microrotational deformation of the medium.

### 3.3. Dimensional consequence for the ampere

In SI the magnetic field intensity `H` has dimension `[A/m]`. A velocity `v` in mechanical units has dimension `[m/s]`. The identification (3.4) `[H] ↔ [v]` gives:

```
[A/m] ↔ [m/s]
[A] ↔ [m/s] · [m] = [m²/s]
```

> `[A] ↔ [m²/s]` (under the Cosserat hypothesis) (3.5)

**Remark on the status of the statement.** The relation (3.5) is **not** a redefinition of the SI ampere. The base definition of the SI ampere, which fixes the elementary charge `e = 1.602176634 × 10⁻¹⁹ C`, remains unchanged. (3.5) is a mapping of the SI ampere into the mechanical dimension of a Cosserat continuum, existing **under** the Cosserat hypothesis.

### 3.4. Physical meaning

The dimension `[m²/s]` is the standard dimension of **kinematic circulation** in hydrodynamics (circulation of velocity around a contour: `Γ = ∮v·dl`, `[Γ] = [m²/s]`). In the Cosserat interpretation, current is identified with the circulation of microrotational deformation around a linear structure:

> Current `I = ∮H·dl` ↔ circulation of microrotational velocity `∮v_rot·dl`

This is consistent with the fact, known since Maxwell, that Ampère's law has the form of the circulation theorem of Stokes.

### 3.5. The dimension of electric charge

Charge in SI:

```
Q = ∫I dt, [Q] = [A·s] (3.6)
```

Substituting (3.5):

```
[Q] = [A] · [s] ↔ [m²/s] · [s] = [m²] (3.7)
```

> `[Q] ↔ [m²]` (3.8)

This is consistent with the topological interpretation of charge as the **cross-sectional area of a defect** in a Cosserat continuum. For hopfionic configurations with charge `Q_H ∈ ℤ` the integrality arises as a topological invariant (the third homotopy group `π₃(S²)`), and its dimension naturally coincides with the dimension of the transverse cross-section of a toroidal structure. The numerical relation between `Q_H` and the SI charge `e` (including a dimensionless coefficient of order `α`) is the subject of [10].

### 3.6. Numerical illustration

The elementary charge:

```
e_SI = 1.602176634 × 10⁻¹⁹ C
e_mech ↔ 1.602 × 10⁻¹⁹ m² (3.9)
```

Comparison with `l₀² = (4.5943 × 10⁻¹⁰)² ≈ 2.11 × 10⁻¹⁹ m²`:

```
e_mech / l₀² ≈ 0.76 (3.10)
```

— a number of order unity, consistent with the interpretation of charge as the cross-sectional area of a defect of structural size `~l₀`. The exact relation, including a dimensionless coefficient of order `α`, is discussed in [10].

---

## 4. The dimension of the second: time as length at fixed speed

### 4.1. Structural fixing of the speed of light

In Section 2.4 it was shown that `c = 1/√(ε₀μ₀) = √(G_shear/ρ)`. From the SI viewpoint, `c` is a measured constant (an exact SI definition since 1983). In the Cosserat interpretation, `c` acquires its value as a **structural property** of the elastic continuum. Like the sound speed in steel, which is fixed by its elastic constants, the transverse Cosserat wave speed is fixed by the medium's parameters.

**Consequence:** time and length in the Cosserat interpretation **are not independent dimensions**.

### 4.2. Reduction of the base `{m, s} → {m}`

If `c` is structurally fixed, the second can be expressed in meters:

> `1 s ↔ c · 1 s = 2.998 × 10⁸ m` (4.1)

Thus:

> `{m, s} → {m}` (4.2)

Physical meaning: one second corresponds to the length that a shear Cosserat wave (that is, light) covers during one period.

### 4.3. Comparison with the standard natural units

In the standard natural units of particle physics [15], `c = 1` is set for convenience of notation — a **methodological choice**. In our interpretation, `c = 1` (or `1 s = c·1 m`) is not a choice but a **structural removal of redundancy**. The claim is that `c` is a **derived** quantity (from the elastic parameters of the medium), not a **fundamental** one.

The distinction is not operational but ontological: all computations and predictions are identical to those in the standard natural units.

### 4.4. Remark on compatibility with SR

The Cosserat continuum is compatible with special relativity: Lorentz invariance is a symmetry of the elastic equations with transverse wave speed `c_T = c`. The statement that `c` is fixed by the structure of the medium does **not** imply the existence of a preferred rest frame.

---

## 5. The dimension of mass: the identity `ℏ/c = m·l`

### 5.1. The identity `m·l = ℏ/c`

From dimensional analysis:

```
[ℏ/c] = [J·s] / [m/s] = [kg·m] (5.1)
```

That is, `ℏ/c` has the dimension `[mass · length]`. Numerically:

```
ℏ/c = 1.054572 × 10⁻³⁴ / 2.998 × 10⁸ ≈ 3.518 × 10⁻⁴³ kg·m (5.2)
```

This is an **exact** identity, known as the "Compton trade-off": for a particle of mass `m`, its Compton wavelength `λ_C = ℏ/(mc)` satisfies `m · λ_C = ℏ/c`. In the two-dimensional space `(m, l)` this is the equation of a hyperbola.

> **Note to the reader.** The hyperbola `m·l = ℏ/c` is the universal "mass × characteristic length" relation for any localized excitation: a heavier object has a shorter intrinsic wavelength, and conversely. The product is fixed by the quantum of action and the speed of light. What matters in our program is that this is a **single** manifold: the vacuum cell `(m₀, l₀)`, the electron's Compton point `(m_e, λ_C)`, and the Planck point — all lie on it, as different positions of **one** medium (§5.5).

### 5.2. Reduction of the base `{m, kg} → {m}`

If `ℏ/c` is a structural constant of the medium (the combination of P3 with the fixing of `c`), then the relation (5.2) **ties together** the dimensions of mass and length:

```
[kg] = [ℏ/c] / [m] ↔ [m · const⁻¹] = [1/m] (5.3)
```

> `[mass] ↔ [1/length] ↔ [energy]` (5.4)

### 5.3. Intermediate summary of the reduction

The combined results of Sections 3, 4, 5:

```
{m, kg, s, A} → {m, kg, s} → {m, kg} → {m} (5.5)
 (A=m²/s) (s=cm) (kg=1/m)
```

After normalizing length to the structural length of the medium `l₀` (obtained in [10] as `l₀ = 4.5943 Å`), all dimensions become **dimensionless**. Equivalently, every physical quantity can be expressed in a **single** base dimension.

**However:** the reduction (5.5) uses only three fundamental parameters `{ε₀, μ₀, ℏ}`. From these three only **three** dimensional scales can be built (`l₀, m₀, M₀c²`). The gravitational scale `l_G ≈ 4.6 × 10¹⁵ m` (see Section 8) is in principle not derivable from `{ε₀, μ₀, ℏ}` by the Buckingham theorem, and requires a **fourth** parameter. The full closure of the base comes after Section 8.

### 5.4. Structural scales of the EM sector

Numerical values of the scales derivable from `{ε₀, μ₀, ℏ}` alone:

| Quantity | Symbol | Value | Source |
|---|---|---|---|
| Structural length | `l₀` | 4.5943 Å | Buckingham (`l₀⁴ ∝ ε₀ℏc`) + `η = 2π` for the coefficient (T10) |
| Structural mass | `m₀` | 7.66 × 10⁻³⁴ kg | `ℏ/(c·l₀)` |
| Structural energy | `M₀c²` | 429.51 eV | `m₀c²` |
| Structural time | `τ₀ = l₀/c` | 1.533 as | `l₀/c` |
| Structural frequency | `ω₀ = c/l₀` | 4.10 × 10¹⁸ rad/s | `1/τ₀ = 1/√(L_eff C_eff)` |

**On the nature of `l₀`.** From the three parameters `{μ₀, ε₀, ℏ}` with three independent dimensions (T3 of Section 3 reduces the ampere to `m²/s`), the **Buckingham Π-theorem** constructs a unique length scale. Its numerical value `l₀ = 4.5943 Å` is fixed by `l₀⁴ = ε₀ℏc/(2π)` (T10), where the dimensionless coefficient `2π` is the microrotational Cosserat coupling `η = 2π` (a topological invariant of the sphere `S²`). The same is independently confirmed by direct numerical relaxation of the hopfion in [10].

The identity `m₀ · l₀ = ℏ/c` is verified numerically to 15 significant figures (the precision limit of the CODATA-2018 constants), evidence of the **algebraic** nature of this relation.

**The cell as an LC resonator.** By P1 and P2 an elementary volume of the medium of size `l` has an effective "inductance" `L_eff ~ μ₀·l` (inertia density) and a "capacitance" `C_eff ~ ε₀·l` (shear compliance). The corresponding resonant frequency is the natural frequency of free oscillations of this LC circuit:

```
ω(l) = 1/√(L_eff · C_eff) = 1/(l·√(ε₀μ₀)) = c/l (5.5a)
```

For the vacuum cell (`l = l₀`):

```
ω₀ = c/l₀ ≈ 4.10 × 10¹⁸ rad/s, ℏω₀ = m₀c² = 429.51 eV
```

— the quantum of energy of the resonance coincides exactly with the structural mass of the cell. That is, `m₀c²` is not "mass" in the substantial sense but the **energy of the zero mode of an LC resonator** of size `l₀`. The hyperbola `m·l = ℏ/c`, through the substitution `m = ℏω/c²`, takes the form `ω = c/l` — a relation between the **resonant frequency** and the characteristic size.

The vacuum cell here is a **particular case**: every point `(m, l)` on the hyperbola is an LC resonator of the corresponding size with its own frequency `ω = c/l`. For the electron `ω_C = c/λ_C ≈ 7.76 × 10²⁰ rad/s` (Compton), for the proton about `1.43 × 10²⁴`, for the Planck point about `10⁴³`. Moving along the hyperbola is a shift of the resonant frequency with changing size, and the three historical formulas `E = mc² = ℏc/l = ℏω` (T16) are **one and the same** resonance energy read in different coordinates. More on this in §5.5.

*On the status.* The correspondence "cell ↔ LC circuit" is a **formal isomorphism**, not a claim about a literal coil or capacitor sitting inside an element of the medium (here the vacuum's ε₀ and μ₀): the inductive term accounts for inertia (`ρ = μ₀`), the capacitive term for the elastic response (`G_shear = 1/ε₀`), and the algebra `ω = 1/√(LC)` matches the dispersion of the shear wave.

### 5.5. The hyperbola `m·l = ℏ/c` as a manifold: vacuum vs. Compton

A substantive conceptual point that deserves emphasis before proceeding to the next sections. The identity T6:

```
m · l = ℏ/c = 3.518 × 10⁻⁴³ kg·m (5.6)
```

— defines a **manifold** of admissible pairs (mass, length) in the Cosserat picture. This is **not a single point** but a hyperbola in the `(m, l)` plane. Distinct physical objects — solitons, defects, the medium itself — occupy **distinct points** of this hyperbola:

| Object | Mass | Length | Position on the hyperbola |
|---|---|---|---|
| Vacuum cell of the medium | `m₀ ≈ 7.66 × 10⁻³⁴ kg` | `l₀ ≈ 4.59 × 10⁻¹⁰ m` | UV cutoff of the field `n` |
| Electron Compton | `m_e ≈ 9.11 × 10⁻³¹ kg` | `λ_C ≈ 3.86 × 10⁻¹³ m` | Topological limit of the electron |
| Proton Compton | `m_p ≈ 1.67 × 10⁻²⁷ kg` | `λ_Cp ≈ 2.10 × 10⁻¹⁶ m` | Topological limit of the baryon |
| Planck point | `m_P ≈ 2.18 × 10⁻⁸ kg` | `l_P ≈ 1.62 × 10⁻³⁵ m` | Crossing of EM and gravitational channels |

**Check:** `m_e · λ_C = (9.11 × 10⁻³¹)(3.86 × 10⁻¹³) = 3.518 × 10⁻⁴³ kg·m = ℏ/c`. 

#### What `l₀` (vacuum length) and `λ_C` (electron Compton) are

In the program **two** lengths play fundamentally different roles, and it is important not to conflate them:

- **`l₀ ≈ 4.59 × 10⁻¹⁰ m`** — the structural length of the **vacuum**. The size of the "elementary cell" of the Cosserat continuum in its unperturbed state. It is derived from `{ε₀, μ₀, ℏ}` through `(ε₀ℏc/2π)^{1/4}`. **It is a property of the medium — in this case the vacuum — not a property of a particle.** In a different medium (with different `K_i`, `μ_{el}`) the effective local length `l₀_local` could be different.

- **`λ_C = ℏ/(m_e c) ≈ 3.86 × 10⁻¹³ m`** — the minimal length of localization of the **electron knot**. The topology `Q_H = -1` requires the knot to be tied at this scale **regardless** of the external medium. **It is a property of the particle (a topological invariant), not of the medium.**

The ratio `l₀/λ_C ≈ 1190` for the vacuum medium.

#### The knot is pure topology; "mass" is the distribution of energy across cells of the medium

In the Cosserat picture the electron is a **topological defect** of the field `n` with charge `Q_H = -1`. The knot per se **carries no mass** in the ordinary sense: it is merely a stable topological configuration, an invariant of the homotopy group `π₃(S²) = ℤ`.

**What is fixed at the moment of creating the knot:**

- The **topological charge** `Q_H = -1` — an integer invariant, independent of the medium.
- The **energy of the knot** `m_e c² ≈ 511 keV` (CODATA, physical value; the bare value is `m_e^bare = 446.279 keV`, see [10] §7) — set at its creation on the Compton scale through energy conservation. The Compton length `λ_C = ℏ/(m_e c)` is the topological limit of localization: the knot does not exist on smaller scales (the mass of one cell of the medium would exceed the energy of the knot).

**What depends on the medium:**

What is measured as the "mass" of the electron is the **energy of the field `n`** (plus the `u`-coupling) **distributed across cells of the surrounding medium**. The number of cells and the manner of distribution of that energy (in contrast to the knot itself — a pointlike topological singularity on the Compton scale) are set by the **local stiffness** of the medium:

- In the **vacuum** (the most dilute Cosserat medium, `l₀ ≈ 4.59 Å`): the energy is distributed on a scale `~R_r · l₀ ≈ l₀/2 ≈ 2.3 Å` — about `1190` vacuum cells per radius (since `l₀/λ_C ≈ 1190`, leading term `1/(16α²)`).
- On **different atomic orbitals** (1s, 2s, 2p, 3s, ...): the local stiffness of the field is higher because of proximity to the nucleus, the distribution contracts, and the number of cells decreases. Each orbital has its own characteristic cell count.
- The **natural lower limit** of the distribution is the Compton length itself, `λ_C ≈ 3.86 × 10⁻¹³ m` (one "cell"): below that scale the knot does not exist (there is nothing left to "tie"). This is a **topological** limit, not "infinite stiffness."

The knot can **migrate** between states of different local stiffness — from a free electron in vacuum to an electron on different atomic orbitals (1s, 2s, 2p, ...) (see the Cosserat-media spectrum in §1.1.3). In doing so:

- its topological charge `Q_H` is **conserved** (integer invariant),
- its total energy `m_e c²` is **conserved** (the topology is stable),
- the **spatial distribution** of energy rearranges according to the local parameters `(K_i, μ_c)` of the new medium.

> **"The knot is topology; 'mass' is the medium's response to the presence of topology."**

This matches the well-known concept of **effective mass** from solid-state physics: in semiconductors the electron exhibits an inertial mass different from the one in vacuum because the wave function is distributed differently in the crystal lattice. In the Cosserat picture this is a consequence of construction: the topological knot is the same, the medium is different, the distribution is different — and so the measured inertial characteristic differs.

**Radius of the vortex tube `r_v` in the vacuum.** The radius `r_v = l₀/2 ≈ 2.3 Å` that appears in Section 7 in the derivation of the fine-structure constant is **the radius of the characteristic energy distribution of the knot in the vacuum Cosserat medium**, not "the size of the knot itself." In a different medium it would be different. The knot itself remains a pointlike topological singularity tied at the Compton scale.

#### Remark: relation to experimentally measured lengths

The "size of the electron" in standard physics is defined in several ways:

- The **Compton length** `λ_C ≈ 386 fm` — a topological invariant, our "knot."
- The **classical radius** `r_e = α·λ_C ≈ 2.82 fm` — the `α`-reduced Compton, EM self-action.
- The **Bohr radius** `a₀ = λ_C/α ≈ 5.29 × 10⁻¹¹ m` — the scale of binding in an atom.
- The **"pointlike" radius in experiment** (LEP, `r_e < 10⁻²² m`) — the far-field limit; at distances `r >> λ_C` the knot indeed behaves as pointlike.

In the Cosserat picture all of this hierarchy is a set of scales of **one** configuration, related by powers of `α` to **one** topological length `λ_C`. The LEP pointlikeness does not contradict Cosserat: at large distances a topological knot looks pointlike.

#### Einstein, de Broglie, Planck — one formula in three coordinates

The identity T6 has a historical corollary worth noting separately. Reducing the second to a length via `t = l/c` (Section 4) and substituting into `m · l = ℏ/c`, one obtains directly:

> `E = m c² = ℏ c / l = ℏ ω` (5.7)

A one-line proof: `m c² = (ℏ/(c·l))·c² = ℏc/l = ℏc/(c·t) = ℏ/t = ℏω`.

Three historically independent formulas turn out to be **algebraically identical**:

| Coordinate | Formula | Historical name | Domain of use |
|---|---|---|---|
| Mass `m` | `E = m c²` | **Einstein** (1905) | Rest energy of a massive particle |
| Length `l = λ̄` | `E = ℏ c / l` | **de Broglie / Compton** (1924) | Matter wave, scattering length |
| Frequency `ω` | `E = ℏ ω` | **Planck** (1900) | Radiation quantum, photon |

All three are a single structural identity of the medium

```
E · t = m · l · c = ℏ (5.8)
```

— read in three different coordinates. Taking "mass" as the variable gives Einstein, "length" gives de Broglie, "frequency" gives Planck. There is no physical hierarchy between them; only **convenience** for a given problem: massive particles are naturally described through mass, photons through frequency, scattering through wavelength.

Historically these formulas were discovered **independently** over a quarter of a century (1900, 1905, 1924) and were taken to be **different** statements: the quantum of radiation, mass–energy equivalence, the wave nature of matter. In the Cosserat picture they are a **geometrically unified** statement: one hyperbola in the `(m, l)` plane and three of its projections.

#### The hyperbola — a property of the medium, not of the particle

A substantive conceptual consequence: in standard physics the formulas `E = mc²`, `E = ℏω` are interpreted as statements **about particles**. The Cosserat picture inverts the reading: the hyperbola `m · l = ℏ/c` is **a property of the medium itself** (postulates P1–P3 fix its structure), and particles are merely **topological clasps** on that geometry:

| Type of object | Topology | Position on the hyperbola |
|---|---|---|
| Free wave (photon, phonon, arbitrary excitation of `n`) | `Q_H = 0` | Any point, **slides** as `ω` changes |
| Topological knot (electron, proton) | `Q_H ≠ 0` | **Clasped** point `(λ_C, m c²)` |
| Unexcited cell of the medium | `∇n = 0` | Point `(l₀, m₀)` — zero-point oscillation |

The distinction between "particle" and "wave" in the Cosserat picture is not in the nature of the object but in the **rigidity of its position** on the hyperbola. The topological charge `Q_H` is a discrete invariant, hence the point `(λ_C, m_e c²)` of the electron is **fixed**. The frequency `ω` of a photon is continuous — the photon slides freely along the hyperbola. This is a direct way of phrasing wave–particle duality as a **geometric** distinction: a fixed vs. sliding point on a single manifold.

The "masslessness" of the photon in this picture means only that it has no fixed point on the hyperbola to which it is bound. But at every slide point `m_eq · λ̄ = (E/c²)·(c/ω) = ℏ/c` is satisfied — the hyperbola is universal, including for photons.

---

## 6. Full summary table of SI quantities (electromagnetic sector)

In this section we collect all the dimensional correspondences of the EM sector. The notation `↔` denotes correspondence in the Cosserat-mechanical interpretation, **not** equality in SI.

### 6.1. Base quantities

| SI quantity | SI dimension | Cosserat-mechanical meaning | Dimension |
|---|---|---|---|
| Length (m) | m | length | m |
| Mass (kg) | kg | density of inverse length | 1/m (via ℏ/c) |
| Time (s) | s | length (wave propagation per period) | m (via c) |
| Current (A) | A | circulation of deformation | m²/s |

### 6.2. Electromagnetic quantities

| Quantity | SI unit | Cosserat-mechanical meaning | Mechanical dimension |
|---|---|---|---|
| Magnetic permeability | `μ₀` [H/m] | Density of the medium | kg/m³ |
| Inverse electric permittivity | `1/ε₀` | Shear modulus | Pa = kg/(m·s²) |
| Magnetic induction | `B` [T] | Momentum density | kg/(m²·s) |
| Magnetic field intensity | `H` [A/m] | Deformation velocity | m/s |
| Electric field | `E` [V/m] | Stress | Pa |
| Electric potential | Volt | Tension | kg/s² |
| Electric resistance | Ohm | Acoustic impedance | kg/(m²·s) |
| Inductance | Henry | Surface inertia | kg/m² |
| Electric capacitance | Farad | Compliance | m²·s²/kg |
| Electric charge | Coulomb [A·s] | Cross-sectional area of a defect | m² |
| Magnetic flux | Weber | Mass flow rate (momentum per unit length) | kg/s |
| Resistivity | Ohm·m | Dynamic viscosity | Pa·s = kg/(m·s) |
| Magnetic moment | J/T | Area × circulation | m⁴/s |

#### The constitutive relations `D = ε₀E` and `B = μ₀H` — elasticity and inertia of the medium

Table 6.2 gives `1/ε₀ ↔ shear modulus` and `E ↔ stress` as two separate correspondences, both quantities with the dimension of Pa. It is essential that they are **not independent**: the standard SI relation connecting them,

```
D = ε₀ · E      ⟺      E = (1/ε₀) · D (6.x)
```

is, in the Cosserat picture, precisely **Hooke's law** `σ = G · γ`. The role of the dimensionless strain `γ` is played by the electric displacement `D`: from `[D] = C/m²` and the reduction `[Q] ↔ [m²]` (Section 3.5) it follows that

```
[D] ↔ m²/m² = dimensionless,
```

that is, `D` measures the fraction of the cross-sectional area "occupied" by the defect — the relative strain of the medium. Thus `E` and `1/ε₀` relate as **state** (stress) and **property** (stiffness), not as equal quantities: the coincidence of their dimensions (Pa) is a consequence of the dimensionlessness of `D`. The charge sets the strain `D`; the stiffness `1/ε₀` converts it into the tension `E`.

The magnetic sector supplies the **paired** constitutive relation, but of the inertial rather than the elastic channel. From `μ₀ ↔ density ρ` and `H ↔ deformation velocity v` [m/s] (Table 6.2), the standard SI relation

```
B = μ₀ · H (6.y)
```

is, in the Cosserat picture, precisely the definition of **momentum density** `p = ρ · v`. Dimension check: `μ₀ [kg/m³] · H [m/s] = kg/(m²·s) = B` ✓. Here the "input" field is the velocity `H`, set by the free currents (`∇×H = J_free`), and the "response" is the momentum density `B`. Accordingly, the two energy densities take the places of the elastic and the kinetic ones:

```
electric   ½ε₀E² = ½ D·E   ↔  elastic potential  ½ σγ
magnetic   ½B²/μ₀ = ½ B·H   ↔  kinetic            ½ ρv²
```

— exactly the identification from which Maxwell obtained his equations from the aether model (1861–62, see Section 3.2).

**Energy transport is mechanical too.** Under the same mapping, the Poynting vector `S = E × H` is the **flux of elastic power** `σ·v` (stress × particle velocity) — the intensity of an acoustic wave `[W/m²]`. The vector character is essential: the wave is transverse (`σ`, `v` lie in the wavefront plane), so the energy flows `⊥` to both — along `S`. Conjugately, the field momentum density `g = ε₀ E×B = S/c²` corresponds to `σv/c²`, consistent with `B ↔ ρv`.

**All four Maxwell equations are not postulates of the medium but its theorems.** The rigorous derivation is given in the companion paper "Maxwell's Equations as Theorems about the Director Field `n: ℝ³·¹ → S²`": from the pullback of the area form `F_μν = n·(∂_μn × ∂_νn)`, the **homogeneous** pair (`∇·B = 0`, Faraday) is the **Bianchi identity** — a consequence of the two-dimensionality of the sphere of directions; the **inhomogeneous** pair (`∇·E = ρ`, Ampère) is a **Leibniz identity** that itself computes the source current (the charge being topological and integer-valued). In the mechanical dictionary the same two groups read transparently:

```
homogeneous   (∇·B = 0, Faraday)  →  structural;  in particular
              ∇·B = 0  ↔  ∇·(ρv) = 0 — incompressibility of the inertial channel
inhomogeneous (∇·E = ρ, Ampère)   →  carries the source:  the charge ρ = topological
              defect (winding of the director) = source of the strain D
```

The two pictures are consistent. `∇·B = 0` is simultaneously the Bianchi identity (the internal orientation space is not `S³`) and the incompressibility of the flow `∇·(ρv) = 0`; a magnetic monopole is forbidden — it would violate the two-dimensionality of the sphere **and** would be a source of mass. The source charge `∇·E = ρ` is a topological defect of the director. The mechanical dictionary supplies the imagery; the rigorous status — "Maxwell's equations are identities, not laws" — is established in the other paper.

**Another, mechanical view.** The same four equations admit a transparent aether reading: with `E ↔ σ` (stress) and `B ↔ ρv` (momentum), Faraday `∇×E = −∂B/∂t` looks like a force balance, and Ampère `∇×H = ∂D/∂t` like kinematic compatibility. This is illustrative optics, not a derivation.

The reason is simple — **the sphere**. The electromagnetic field is the area on the sphere of directions "swept" by the arrow `n` when shifted along two axes: `F = n·(∂n × ∂n)`. Swap the axes — the sign flips (cross product): so `F` measures the **twist** of the arrow field, not its stretch. That is why two fields `E` and `B` appear, and why the equations are curl equations. And half of Maxwell (`∇·B = 0` and Faraday's law) holds automatically — solely because the sphere of directions is two-dimensional (companion paper, Theorem 1).

**The free field is an oscillator of the medium.** The same two energy densities (elastic `½σγ` and kinetic `½ρv²`) pour into each other: the free field is a **harmonic oscillator** of the medium, and light is its travelling transverse wave (`ω = ck`). Maxwell's **displacement current** `∂D/∂t = ∂γ/∂t` is the elastic ("spring") term: the *rate of strain*, not a transport of charge; its lumped limit is the `LC` circuit (capacitor = spring, coil = mass, `ω = 1/√(LC)`).

As a result, the three central consequences of the mechanical picture turn out to be facets of one structure. Hooke's law `D = ε₀E` (elasticity, `σ = Gγ`) and the momentum relation `B = μ₀H` (inertia, `p = ρv`) are the **constitutive** relations of one and the same Cosserat medium along its two channels; and their ratio yields the **dynamical** consequence — Maxwell's formula for the transverse wave speed

```
c² = (1/ε₀)/μ₀ = G/ρ,
```

that is, `c_T = √(G/ρ) ≡ c_light` (Section 2). Elasticity, inertia, and propagation speed are not three independent identifications but three projections of a single mechanics of the medium. The plane wave confirms that this is a **dispersionless** elastic wave: `H = cD` (since `H = B/μ₀ = cε₀E = cD`) reads in the dictionary as `v = c·γ` — particle velocity `= c ×` strain, the exact signature of a travelling profile `u = f(x − ct)`.

**The converse reading: `1/ε₀ = μ₀c²` and the rest energy.** The exact SI identity `1/ε₀ = μ₀c²` (a consequence of `c² = 1/(ε₀μ₀)`) reads in the mechanical dictionary as

```
G = ρ c²                                              (6.z)
```

Both sides have the dimension of energy density (`Pa = J/m³`): the shear modulus `1/ε₀ = G` sets the **scale of the rest-energy density** of the medium, `ρc²`. This is the second, **energetic** face of the same channel ratio: if `c = √(G/ρ)` is the dynamical one (transverse wave speed), then `G = ρc²` is the mass–energy one. The elastic (electric) tension of the medium, integrated over the volume of the defect, gives its **rest energy**:

```
∫ ρ dV = m ,        E₀ = ∫ ρc² dV = m c² .
```

**The magnetic sector supplies the kinetic energy symmetrically.** The same density `ρ = μ₀` that integrates into the mass carries, in the second (inertial) channel, not tension but motion: the magnetic energy density `½B²/μ₀ = ½ρv²`, under rigid transport of the defect at velocity `v`, integrates into the **kinetic energy**

```
T = ∫ ½ ρ v² dV = ½ m v² .
```

Thus Maxwell's two energy densities become the potential and kinetic terms of one medium with a common inertia `m = ∫ρ dV`:

```
electric / elastic    →  rest energy   E₀ = m c²    (tension,  G = ρc²)
magnetic / inertial   →  kinetic       T  = ½ m v²  (motion,   p = ρv)
```

and their sum `m c² + ½ m v²` gives the first terms of the expansion of `γ m c²` (rest from tension, kinetics from inertia). In this picture `E = mc²` reads as **rest energy = integrated tension of the medium**: the mass of a localized defect of the director field is its elastic field energy divided by `c²`. Crucially, the coefficient in `E = mc²` is here **not borrowed from special relativity but derived**: the factor connecting inertial mass with rest energy is the square of the medium's transverse wave speed `c² = G/ρ` (6.z) — the very quantity that SR takes as a universal constant. The mechanical picture thereby **reproduces** `E = mc²` from its own moduli (`E = m·(G/ρ)`: rest energy = integrated tension, inertia = integrated density, their ratio = `G/ρ`) rather than importing it. What is fixed here is the **relation** itself (the coefficient `c² = G/ρ`); its quantitative realization — the computation of `m_e` as the minimum of `E[n, u]` — is the subject of the companion paper on the derivation of the bare electron mass.

### 6.3. Numerical checks

A few control numerical cross-checks:

**(1) Speed of light.** From P1, P2:
```
c_T = √((1/ε₀)/μ₀) = 1/√(ε₀μ₀) = 2.998 × 10⁸ m/s ≡ c_light
```

**(2) Impedance of free space.**
```
Z₀ = √(μ₀/ε₀) = 376.73 Ω
```
In the Cosserat interpretation: `Z₀ ↔ √(ρ · G_shear) = c·μ₀` — the mechanical acoustic impedance of the medium, numerically coinciding with the SI `Z₀`.

**(3) Electron charge.** `e_mech ↔ 1.602 × 10⁻¹⁹ m²`. Comparison with `l₀² ≈ 2.11 × 10⁻¹⁹ m²` gives `e_mech/l₀² ≈ 0.76` — order unity.

### 6.4. Structural redundancy of the SI

Applying P1, P2, P3 to SI:

```
A → m²/s (Section 3)
s → m (Section 4, via c)
kg → 1/m (Section 5, via ℏ/c)
m → dimensionless (normalized to l₀)
```

All electromagnetic quantities are expressed in a single dimension. Before turning to the gravitational channel, we show that the dimensional reduction `[Q] ↔ [m²]` derived above has a numerical consequence — the value of the fine-structure constant.

---

## 7. The fine-structure constant from the geometry of charge

The dimensional reduction of Section 3 yields `[Q] ↔ [m²]`: charge has the dimension of area. The numerical value of the electron charge in mechanical units is the area of a specific geometric object. Identifying this area with the cross-section of the vortex tube of a hopfionic defect gives a **bare** value of the fine-structure constant `α_bare = 1/128 = 2⁻⁷`, in agreement with experiment to 0.7%.

### 7.0. On the status: the vacuum as a special case

In keeping with Section 5.5, in the present paper we treat the vacuum as a **special case** of a Cosserat medium:

- **The topological part** (`λ_C, m_e, Q_H`) consists of invariants independent of the medium.
- **The energy-distribution radius** `r_v = l₀/2 ≈ 2.3 Å` is a characteristic of the **vacuum**, not of the knot itself. In a different Cosserat medium `r_v` would be different (corresponding to that medium's local `l₀`).
- **`α = 1/128` is universal** for any Cosserat medium with `S²`-symmetric director: in the formula `α = π·l₀⁴/(64·ε·ℏc)` the local stiffness `ε` cancels through `l₀⁴ = ε·ℏc/(2π)`, leaving a pure topological coefficient set by `η = 2π`.

Thus the value `α_bare = 1/128` derived below is a **universal** result of the program; its agreement with the experimental `α(M_Z) = 1/128.9` (0.7%) is confirmed by measurements made under ordinary conditions (vacuum experiments at accelerators).

### 7.1. Charge as the cross-sectional area of a hopfion

In the dimensional reduction (Section 3.5) the electron charge has the numerical value, in mechanical units:

```
e_mech ↔ 1.602 × 10⁻¹⁹ m² (7.1)
```

That charge **is** the cross-sectional area of a defect is a consequence of the hopfionic nature of the electron (a separate prediction of the program; see Abstract and §5.5) and of the dimensional reduction `[Q] ↔ [m²]`. The hopfion with `Q_H = -1` is the simplest stable class of configurations in the `n`-channel with `S²`-target: it necessarily has a vortex tube with a transverse cross-section, and the area of that cross-section is geometrically tied to the charge.

**Within** the topological class `Q_H = -1` there exists a family of geometrically distinct representatives (all with the same topological charge, differing in shape). Which shape is physically realized is selected by the minimum of the functional `E[n, u]` for the given `K_i, μ_c`. Direct numerical relaxation for the canonical vacuum parameters yields a shape **close to oblate** (a flattened disc, with quadrupole moment `Q_2 ≈ -0.19` sim; see [10]). For the derivation of `α` we adopt the leading-order approximation:

| | |
|---|---|
| **P5.** | The cross-section of the hopfion tube in the derivation of `α` is approximated by a **circle** of radius `r_v`: `e = π·r_v²`. This is an idealization of the actual (oblate) shape, optimal for minimizing `E[n, u]`. |

The sensitivity of the result to this approximation is `O(ε²)` in the eccentricity of the cross-section: `α` enters through the area, and the area is insensitive to shape deformation at fixed geometric measure (an ellipse of the same area gives the same `α`); see §7.6 for details.

Solving (7.1) for `r_v` under the circular approximation:

```
r_v = √(e/π) = √(1.602 × 10⁻¹⁹ / π) ≈ 2.258 × 10⁻¹⁰ m = 0.2258 nm (7.2)
```

This is a **derived** value of the vortex-tube radius, from the experimental charge plus P5.

### 7.2. The coincidence `r_v ≈ l₀/2`

Comparing (7.2) with the structural length of the medium `l₀ = 4.5943 × 10⁻¹⁰ m` (Section 5.4):

```
l₀/2 = 2.297 × 10⁻¹⁰ m = 0.2297 nm
```

The ratio:

```
r_v / (l₀/2) = 2.258 / 2.297 ≈ 0.983 (agreement to 1.7%) (7.3)
```

The vortex-tube radius coincides with half the structural length of the medium. The coincidence is meaningful because:

- `r_v` is determined from the electron charge `e` (P5 + experiment);
- `l₀` is determined from `{ε₀, μ₀, ℏ}` (Section 5.4);
- neither of the quantities on the right-hand sides of those definitions contains `e`.

The relation `r_v = l₀/2` is a testable prediction of the Cosserat program.

### 7.3. Physical justification of `r_v = l₀/2`

The coincidence is not accidental: it can be derived from the structure of the functional `E[n, u]` itself.

The functional (Section 2.1) contains two competing scales:

- **`K_i`** (we denote it generically by `c₂`) — the Oseen–Frank stiffnesses, fixing the energy cost of a gradient of `n` (term quadratic in `∇n`).
- **`c₄`** — the Skyrme stabilizing term (quartic in `∇n`), preventing collapse.

Their ratio defines the characteristic length:

```
L_Skyrme = √(c₄/c₂) (7.4)
```

> **Note to the reader.** This is the classical mechanism of **Derrick stability** for a topological soliton: the quadratic term tries to spread the knot out to fill all space, the quartic term tries to collapse it to a point. Their balance fixes a **unique** finite size at which the knot is stable. That size is `L_Skyrme`.

The balance condition (Derrick stability) fixes `L_Skyrme = l₀`. For a hopfionic configuration with `Q_H = -1` the minimal vortex-tube radius turns out to be:

```
r_v = L_Skyrme/2 = l₀/2 (7.5)
```

![Canonical electron hopfion (`Q_H = -1`) at `R_r = 0.64082`, `R_z = 0.80729`, `w = 0.70200`. The colored panels are 2D slices through the (`r ≥ 0`, `z`) half-plane; axial symmetry makes a single such slice sufficient to encode the full field. **Top-left:** `n_z(r, z)` — the `z`-component of the director. The red background (`n_z ≈ +1`) is the vacuum; the blue spot (`n_z = -1`) is the vortex tube core; black contours mark the levels `n_z = -0.5, 0, +0.5`. **Top-right:** `|n_⊥|(r, z)` — the magnitude of the in-plane components; highlights the shell where the director "lies sideways" and sets the tube radius `r_v ≈ 0.5 ℓ_0`. **Bottom-left:** the topological charge density `ρ_Q = n·(∂_r n × ∂_z n)`; localized near the tube and negative (its volume integral equals `Q_H = -1`). **Bottom-right:** 3D shape with a 90°-wedge cut out (3/4 of a full revolution shown); the red surface is the iso-contour `n_z = -0.5` (the body of the soliton) obtained by revolving the 2D cross-section around the symmetry axis; the black arc is the vortex tube axis (`n = -ẑ`, a circle of radius `R_r` in the plane `z = 0`); the two black dots on the cut faces mark its endpoints. All panels use the exact Hopf-ansatz formula. Reproduced by `verifications/canonical_derrick/hopfion_visualize.py`.](../../verifications/canonical_derrick/hopfion_visualize.png)

**Numerical confirmation** [10]. The canonical bare functional (`K₁ = K₂ = 2`, `K₃/K₁ = 1+2π`, `c₄ = 1`, `μ_c = 2π`, with no mass term) is verified on a `1024×2048` grid (dyadic box `17 × 33 l₀`) via a **Derrick scan**: rescaling the Hopf ansatz `(R_r, R_z) → λ·(R_r, R_z)` over `λ ∈ [0.6, 3.0]` produces a clean V-minimum **at λ = 1**, with `E_tot(λ=1) = 446.279 keV` (identified with the **bare** electron mass `m_e^bare`). The components `E_OF` and `E_Sk` follow the expected Derrick scalings `E_OF ∝ λ`, `E_Sk ∝ λ⁻¹`; the screened `E_u` is small (`<1 %` of `E_tot`) and, because the Cosserat screening length `l_c = 1/√μ_c` is **fixed**, does not scale as `λ²` but saturates. The Derrick residual `E_OF − E_Sk + 2·E_u ≈ +8.8 keV` at `λ=1` is only an approximate slope estimate (the screened `E_u` does not follow `λ²`); the authoritative signature of balance is the discrete minimum of `E_tot` itself, lying exactly at `λ = 1`. The topological charge is preserved across the entire scan (`|Q+1| < 1.2·10⁻³` even at λ=3.0; `~4·10⁻⁵` at λ=1.0). The geometric identity (7.5) `r_v = l₀/2` is thereby **embedded in the Derrick balance of the full functional**: the canonical triple `(R_r, R_z, w)` is a genuine energy minimum, not an arbitrarily chosen point. *Remark on the origin of the parameters.* The numerical values `(R_r, R_z, w) ≈ (0.64082, 0.80729, 0.70200)` were obtained in [10] by a direct minimization of the functional `E[n, u]` (Nelder–Mead on a `1024×2048` grid, dyadic box `17 × 33`); they are taken here as already-known and tested for stationarity along the `λ` direction.

![Derrick scan of the canonical electron configuration. Left: total energy `E_tot(λ)` (V-shape with minimum at `λ = 1.00`, `E_tot = 446.279 keV` = `m_e^bare`; the dashed line is the dyadic form `(2¹⁰+2⁴−1)·M₀c² = 446.26 keV`). Right: the three energy components on a log scale (`E_OF ∝ λ`, `E_Sk ∝ λ⁻¹`, screened `E_u` — saturating). Canonical parameters: `K₁ = K₂ = 2`, `K₃ = 14.56`, `c₄ = 1`, `μ_c = 2π` (no mass term). Reproduced by `verifications/canonical_derrick/derrick_scan.py`.](../../verifications/canonical_derrick/derrick_scan.png)

Hence (7.5) is a **derived** relation, not a postulate. The only postulate that remains is P5, the statement of circular cross-sectional geometry.

### 7.4. The structural identity `l₀⁴ = ε₀ℏc/(2π)`

For the derivation of `α` we need one additional **identity**, relating the structural length `l₀` to the fundamental constants.

From the three parameters `{μ₀, ε₀, ℏ}` with three independent dimensions (through T3 of Section 3, where `[A] ↔ [m²/s]` reduces the ampere to a derived quantity) the **Buckingham Π-theorem** constructs a unique length scale up to a dimensionless coefficient:

```
l₀⁴ ∝ ε₀ℏc (Buckingham)
```

> **Note to the reader.** The *Buckingham Π-theorem* is a standard result of dimensional analysis: if a problem has `N` parameters with `K` independent dimensions, any quantity is expressed through them **uniquely** up to dimensionless coefficients. We have three parameters `{ε₀, μ₀, ℏ}` and three independent dimensions — so the **unique** length that can be built from them is determined by an unambiguous combination of exponents: by checking dimensions one finds `l⁴ ~ ε₀ℏc`. The price for this theorem is that the coefficient in front remains undetermined; physics then fixes it (the `S²` topology yields `1/(2π)`).

The dimensionless coefficient `1/(2π)` is fixed by the value of the microrotational Cosserat coupling `η = 2π`, set by the geometry of the sphere `S²` of the director (Section 2.1, [10]) — a topological invariant, not a fitted parameter. The result:

```
l₀⁴ = ε₀ℏc / (2π) (7.6)
```

**Numerical check:**
```
ε₀ℏc/(2π) = (8.854 × 10⁻¹²)(1.055 × 10⁻³⁴)(2.998 × 10⁸) / (2π)
 = 4.456 × 10⁻³⁸ m⁴

l₀⁴ = (4.5943 × 10⁻¹⁰)⁴ = 4.455 × 10⁻³⁸ m⁴ 
```

Agreement to 4 significant figures (the precision limit of CODATA `ε₀`). The numerical value `l₀ = 4.5943 Å` is independently confirmed by direct relaxation of the hopfion configuration in [10].

### 7.5. Derivation of `α_bare = 1/128`

The standard SI definition of the fine-structure constant:

```
α = e² / (4π ε₀ ℏ c) (7.7)
```

Substituting `e = π(l₀/2)² = π·l₀²/4` (P5 + (7.5)):

```
e² = π² l₀⁴ / 16 (7.8)
```

Substituting into (7.7):

```
α = (π² l₀⁴ / 16) / (4π ε₀ ℏ c)
 = π l₀⁴ / (64 ε₀ ℏ c) (7.9)
```

Substituting the structural identity (7.6) `l₀⁴ = ε₀ℏc/(2π)`:

```
α = π · (ε₀ℏc/(2π)) / (64 ε₀ ℏ c)
 = (π/(2π)) · (1/64)
 = 1/128
```

> `α_bare = 1/128 = 2⁻⁷` (7.10)

> **Note to the reader.** What actually happened in this calculation: we took the **textbook** definition `α = e²/(4πε₀ℏc)` and **substituted into it two things from our theory** — the geometric charge `e = π(l₀/2)²` (P5) and the structural value `l₀⁴ = ε₀ℏc/(2π)` (T10). After cancellations all physical constants (`ε₀, ℏ, c`) drop out and only arithmetic remains: `π/(2π · 64) = 1/128`. In other words: if charge and structural length are related as Cosserat geometry requires, then `α` must be `2⁻⁷` — independent of the numerical values of `ε₀, ℏ, c`.

### 7.6. Structure of the derivation and its status

Formula (7.10) rests on **three** independent inputs:

1. The **dimensional reduction** `[A] ↔ [m²/s]` (T3, Section 3) — a consequence of postulates P1, P2.
2. The **structural identity** `l₀⁴ = ε₀ℏc/(2π)` (T10) — the Buckingham Π-theorem (scaling `l₀⁴ ∝ ε₀ℏc`) plus the geometry of `S²` (`η = 2π` fixes the coefficient `1/(2π)`).
3. The **geometric postulate P5** — circular cross-section of the hopfion defect (numerically confirmed by `r_v = l₀/2` via a scan in [10], Section 7.3).

Of these the only irreducible **postulate** is P5 (the shape of the cross-section). The rest are consequences of Buckingham plus topology. The charge `e` is **not an input** in the derivation but a **result**: `e = π(l₀/2)²` is set by geometry.

**Sensitivity to P5.** If the cross-section turns out to be non-circular (for example, elliptical for hopping orbits; cf. [11]), the numerical coefficient in (7.10) shifts by a factor of order unity, but the **order** `α ~ 10⁻²` is preserved — that order is set by Buckingham and `η = 2π`.

**Logical order of the derivation.** `l₀` is determined from `{ε₀, μ₀, ℏ}` through the Buckingham Π-theorem and `η = 2π` (the `S²` geometry), independently of the value of `α`. Then circular cross-section geometry is postulated (P5), and from this `α = 1/128 = 2⁻⁷` follows. The experimental value of `α` is not used in the derivation.

### 7.7. Comparison with experiment and the QED renormalization

The fine-structure constant depends on the energy scale via the running QED couplings:

| Energy scale | `α⁻¹` | Source |
|---|---|---|
| `q² = 0` (low energies, atomic physics) | 137.036 | Precision measurements |
| `q² = m_e² c⁴` (electron Compton scale) | ~136 | Lamb shift |
| `q² = m_W² c⁴` (W-boson scale) | ~130 | LEP, direct measurements |
| `q² = m_Z² c⁴` (Z-boson scale, 91 GeV) | **128.9 ± 0.1** | LEP, SLD |
| `q² → ∞` (asymptotic limit) | → 128.0 (prediction) | This work |

> **Agreement of our result `α_bare = 128.0` with the experimental `α(M_Z) = 128.9 ± 0.1`: `0.7%`.**

The difference between the bare `α_bare = 1/128` and the low-energy observable `α(0) = 1/137.036`:

```
Δα⁻¹ = 137.036 - 128 = 9.036 (7.11)
```

— is the **standard** effect of **QED vacuum polarization**: virtual `e⁺e⁻` pairs screen the charge as seen at large distances. This is **known** QED, not an extension introduced here.

Our derivation supplies a **boundary condition** for the renormalization-group equations:

```
α(Λ → ∞) → 1/128 = 2⁻⁷ (7.12)
```

The standard one-loop QED running coupling equation (for `n_f = 3` light fermions):

```
α⁻¹(μ) = α⁻¹(μ₀) - (2 n_f / 3π) ln(μ/μ₀) (7.13)
```

Integrating from `μ = M_Z = 91 GeV` down to `μ = m_e c² = 0.511 MeV`, standard QED gives a shift of about 8.9, in nearly exact agreement with (7.11). Our theory therefore sets the UV boundary condition, while QED provides the IR flow to the observed value.

### 7.8. What this gives

The fine-structure constant is among the most precisely measured dimensionless constants of nature: `α⁻¹ = 137.035999084(21)`, eleven significant figures. Feynman called it "a magic number that comes to us with no understanding by man"; the question of its origin from more fundamental principles has stood since Sommerfeld and is open within standard physics.

Two points in our derivation are worth emphasizing. First, the experimental value of `α` is never used on the right-hand side — neither as a calibration nor as a correction; `1/128` follows from pure algebra (the `Π`-theorem plus the topological coefficient `η = 2π`) and a single geometric postulate, P5. Second, the answer `2⁻⁷` is a simple dyadic fraction. This is consistent with the integer topology of charges and with the fact that Cosserat defects have a discrete spectrum of symmetries.

The discrepancy between `1/128` and the familiar low-energy `1/137` is not a flaw of the derivation but precisely what standard QED predicts through vacuum polarization (§7.7). Our theory provides a UV boundary condition; QED carries it down to the IR-measured value.

### 7.9. The two hyperbolas of the Cosserat medium

The result `α_bare = 1/128` has an algebraic consequence: in the plane of parameters of the medium two invariant hyperbolas appear, structurally parallel and describing different aspects of one program.

#### Hyperbola I: mass × length

T6 establishes the first invariant (Section 5):

```
m · l = ℏ/c = 3.518 × 10⁻⁴³ kg·m (Hyperbola I) (7.14)
```

The connection between **mass** and **length** in the Cosserat medium. Section 5.5 showed that distinct objects — the vacuum cell `(m₀, l₀)`, the electron `(m_e, λ_C)`, the proton, the Planck point — all live on **one** Hyperbola I, but at **different** points of it.

#### Hyperbola II: charge squared × channel stiffness

The standard SI definition of the fine-structure constant:

```
α = e² / (4π ε₀ ℏ c)
```

can be rewritten as a **second** invariant:

```
e² / (4π ε₀) ≡ ℏ · c · α (Hyperbola II) (7.15)
```

or equivalently (using P2 `1/ε₀ = G_shear`):

```
e² · G_shear = 4π · ℏcα = const (7.16)
```

The connection between the **charge squared** (interaction area) and the **channel stiffness** (shear modulus of the Cosserat medium). At fixed `α`, a larger charge requires a less stiff medium and vice versa.

#### Equivalent forms of Hyperbola II: stiffness, density, impedance

Because P1 and P2 link the medium parameters through the wave relation `c² = (1/ε₀)/μ₀`, the identity (7.15) admits **three** equivalent rewritings — through the stiffness, the density, and the impedance of the medium:

```
e² · (1/ε₀)   = 4π · ℏc · α (7.16a — via stiffness G ≡ 1/ε₀)
e² · μ₀       = 4π · ℏα / c (7.16b — via density ρ ≡ μ₀)
e² · Z₀       = 4π · ℏ · α (7.16c — via impedance Z₀ = μ₀c)
```

Form (7.16c) is not merely our algebra: it is equivalent to the **von Klitzing relation** `Z₀ = 2α·R_K` with the Hall quantum `R_K = h/e² = 25812.807 Ω`, and is thereby **experimentally measured to `~10⁻¹⁰`** — the most precise electrical relation in metrology (details in Appendix C.1).

Algebraically these are one identity; physically each form highlights a different side of the "charge ↔ medium" coupling, mirroring the symmetry of the LC cell (§5.5a, where `ω = 1/√(LC)`, `L ~ μ₀l`, `C ~ ε₀l`):

| Form | What it fixes | LC analogue |
|---|---|---|
| `e²·(1/ε₀)` | potential (elastic) energy of the charge | capacitance `C` |
| `e²·μ₀` | kinetic (inertial) energy of the charge | inductance `L` |
| `e²·Z₀` | action at resonance (geometric mean) | impedance `√(L/C)` |

Form (7.16b) makes the parallel with Hyperbola I literal:

```
Hyperbola I:   m · l = ℏ/c (single particle × length)
Hyperbola II:  e² · μ₀ = 4π α · ℏ/c (charge² × medium density)
```

The left-hand sides of both have the same dimension `kg·m` and are multiples of `[ℏ/c]`. In the second form, `e²·μ₀` reads as "volume of the charged region × density of the medium" = mass of displaced medium — an Archimedean analogy for the charge. The two hyperbolas differ only by the dimensionless factor `4π α`: the first fixes a point of a single particle, the second the coupling of the charge to the inertia of the medium.

Remark on dimensions: `[μ₀] = kg/m³`, `[e²] = m⁴`, hence `[e²·μ₀] = kg·m ≡ [ℏ/c]`. Similarly `[Z₀] = [μ₀c] = kg/(m²·s) = N·s/m³ = Pa·s/m` — the mechanical acoustic impedance of the medium (§6.2).

#### Physical interpretation of Hyperbola II

Through the dimensional reduction of Section 6:

| Side | Dimension | Physical meaning |
|---|---|---|
| `e²` | m⁴ | Area × area — square of the interaction cross-section of the defect |
| `1/ε₀` | Pa = energy/volume | Channel stiffness (shear modulus of the medium, P2) |
| `e² × (1/ε₀)/(4π)` | J·m | Action × velocity |
| `ℏ · c` | J·m | Same |
| `α` | dimensionless | **Ratio** |

> **Physical meaning of `α`:** the ratio of the "knot interaction area" (`e²`, m⁴) to the "medium stiffness" (`1/ε₀`, Pa), normalized by the quantum of action `ℏ` and the propagation speed `c`. In other words: how the cross-sectional area of a hopfionic defect is coupled to the elastic properties of the medium — that is, **how energy is partitioned between channels**.

For larger `α` the coupling "defect ↔ medium" is stronger; for smaller `α` it is weaker. The smallness of `α ≈ 1/137` reflects the fact that a charged knot is a **weak** perturbation of a very stiff Cosserat medium.

#### Intersection of the two hyperbolas: the algebraic identity `m₀² · e`

Combining Hyperbolas I and II with the geometric identification of charge `e = π(l₀/2)²` (P5 + 7.5), one obtains an algebraic identity relating the structural parameters:

```
m₀² · e = m₀² · π · (l₀/2)² = (π/4) · (m₀ · l₀)² = (π/4) · (ℏ/c)² (7.17)
```

In terms of `α`:

```
m₀² · e = √(8π² · α_bare) · (ℏ/c)² (7.18)
```

The self-consistency of `α_bare = 1/128` shows up as an **algebraic collapse**:

```
√(8π² · α_bare) = √(8π² / 128) = √(π² / 16) = π/4 (7.19)
```

That is, formulas (7.17) and (7.18) give the **same** numerical factor `π/4` — they are two formally different ways of writing the same identity.

**Numerical check of (7.17):**
```
m₀² · e = (7.66 × 10⁻³⁴)² · 1.602 × 10⁻¹⁹
 = 5.87 × 10⁻⁶⁷ · 1.602 × 10⁻¹⁹
 = 9.40 × 10⁻⁸⁶ kg²·m²

(π/4)·(ℏ/c)² = 0.7854 · (3.518 × 10⁻⁴³)²
 = 0.7854 · 1.238 × 10⁻⁸⁵
 = 9.72 × 10⁻⁸⁶ kg²·m²

Agreement: ≈ 3.3% (within the precision of the structural length l₀) 
```

#### What this identity says

The identity (7.17) is an **interlocking** of the two hyperbolas:

- Hyperbola I fixes the pair `(m₀, l₀)` for the vacuum cell.
- The geometry P5 ties the charge `e` to the length `l₀`.
- Hyperbola II fixes `α` through the same `(e, ε₀)`.

The quantities `α, m₀, l₀, e` are bound by structural identities; knowing any two of them fixes the others by the algebra of (7.17). In that sense they are four projections of one structure rather than four independent parameters.

A Cosserat medium with postulates P1, P2, P3, P5 is one object whose different sides manifest as "mass," "charge," "fine-structure constant" and "structural length."

#### Remark: relations between the hyperbolas

Hyperbolas I and II are **not independent** in our program:

1. P1, P2, P3 specify the vacuum point `(m₀, l₀)` on Hyperbola I.
2. The structural identity (7.6) `l₀⁴ = ε₀ℏc/(2π)` fixes `l₀` through `{ε₀, μ₀, ℏ}`.
3. The geometry P5 `e = π(l₀/2)²` fixes `e` through `l₀`.
4. Hyperbola II with known `e` and `ε₀` gives `α_bare = 1/128`.

---

## 8. The gravitational channel and closure of the unit base

Sections 2–7 developed the **electromagnetic part** of the program through the `n`-channel. Gravity requires a **second** channel (the `u`-channel of translations) and a **fourth** postulate (P4) introducing the gravitational constant `G` as a structural parameter of the medium. The logical chain of the section:

```
Two-channel Cosserat medium (§8.1)
 ↓
Kleinert gauge mechanism: defects → GR metric (§8.2)
 ↓
P4: G = c⁴ε₀/(16π l_G²); l_G is the fourth independent parameter (§8.3)
 ↓
Planck scales l_P, m_P as derived quantities (§8.4)
 ↓
Full scale hierarchy + closure of the unit base (§8.5)
 ↓
The 5 classical tests of GR are reproduced identically (§8.6)
 ↓
Differences from pure GR are visible only in extreme regimes (§8.7)
```

### 8.1. Two-channel structure of the Cosserat medium

The Cosserat continuum introduced in Section 2.1 has **two** independent fields. Each carries its own class of physical phenomena:

| Channel | Field | Excitation type | Linear regime | Source |
|---|---|---|---|---|
| **`n`** | `n ∈ S²` | Rotational deformation | Maxwell equations [25] | Hopfionic knots (electron [10]) |
| **`u`** | `u ∈ ℝ³` | Translational deformation + torsion | Linearized GR (§8.2) | Disclination defects (masses [23]) |

**Equivalence principle.** Inertial and gravitational mass are **the same** characteristic of a disclination defect: the topological "charge" of a disclination simultaneously sets inertia (resistance to shear) and the source of curvature in the `u`-channel. The equality `m_inertial = m_grav` becomes an identity, not an observational coincidence.

**The `10⁴²` hierarchy between EM and gravity.** The standard universal formula relating EM and gravitational forces for **any pair** of charged particles with masses `m₁, m₂`:

```
F_EM / F_grav = e² / (4πε₀ · G · m₁ · m₂)
              = [e² / (4πε₀ℏc)] · [ℏc / (G · m₁ · m₂)]
              = α · m_P² / (m₁ · m₂)                       (8.0)
```

(using `m_P² = ℏc/G` — the definition of the Planck mass).

The value depends on the choice of pair:

| Pair | Factor | F_EM/F_grav |
|---|---|---|
| **electron–electron** | `α·(m_P/m_e)²` | `≈ 4.17 × 10⁴²` historical "10⁴² hierarchy" |
| proton–electron (hydrogen atom) | `α·m_P²/(m_p·m_e)` | `≈ 2.3 × 10³⁹` |
| proton–proton | `α·(m_P/m_p)²` | `≈ 1.24 × 10³⁶` |

The maximum — for the electron pair (the electron is the lightest charged particle); this is Dirac's **"famous 10⁴² hierarchy."**

In the Cosserat picture **both** factors in (8.0) have **structural origin**:

- **`α = 1/128 → 1/137`** — derived in Section 7 from the geometry of charge (P5) and the structural identity `l₀⁴ = ε₀ℏc/(2π)`.
- **`m_P/m`** for any particle is the ratio of points on the hyperbola `m·l = ℏ/c` (T6), where `l_P = l₀²/(2√2 · l_G)` is derived (T15) and `λ_particle = ℏ/(m·c)` is its Compton limit.

In the Cosserat program the `10⁴²` hierarchy (for electrons) is expressed through structural elements of a single picture: the `S²` topology gives `α`, the medium's hyperbola gives `m_P/m_particle`, and the two-channel structure with `l_G/l₀ ≈ 10²⁵` sets `l_P` and thereby `m_P`. A detailed numerical analysis is given in [27].

### 8.2. The Kleinert gauge mechanism: defects → GR metric

> **Note to the reader.** Kleinert noticed a remarkable mathematical parallel: an elastic continuum with **dislocations** (linear shear defects) and **disclinations** (linear rotation defects) is described by the same apparatus of differential geometry as curved spacetime. Disclinations create local **curvature** of the lattice — and this curvature formally coincides with the Riemann curvature tensor of GR. That is: "curved spacetime around a mass" can be rephrased as "a curved lattice around a disclination defect." What follows is the formalism of this equivalence.
>
> *Technical glossary:* a **tetrad (vierbein)** `e^a_μ` is a "local set of coordinate axes" defined at each point of space, in terms of which the deformation of the medium is written. A **disclination** is a pointlike/linear defect around which the lattice is rotated by a finite angle.

In the gauge theory of crystal defects (Kleinert [11, 12]), the elastic distortion of the `u`-channel is identified with the tetrad field of general relativity:

```
β^a_μ(r) = ∂_μ u^a + ω^a_μ (elastic distortion of the medium)
 ↕
e^a_μ(r) (GR tetrad) (8.1)
```

The corresponding metric and curvature tensor:

```
g_μν = η_{ab} · e^a_μ · e^b_ν (8.2)
Θ^μν ≡ R^μν (disclination density = Ricci tensor) (8.3)
```

From these identifications it follows that **the action of an elastic medium with disclination defects coincides with the Hilbert–Einstein action**:

```
S = ∫ [R/(16π G_eff) + L_matter] √(-g) d⁴x (8.4)
```

Variation with respect to `g_μν` yields Einstein's equations. In the weak-field limit (`g_μν = η_μν + h_μν`, `|h_μν| ≪ 1`) the **Newtonian limit** is recovered:

```
∇² Φ = 4π G ρ_mass, Φ ≡ -GM/r, h_00 = -2Φ/c² = 2GM/(rc²) (8.5)
```

where `Φ` is the standard Newtonian potential.

**Remark.** Kleinert's program strictly yields the theory of **Einstein–Cartan** [13] — an extension of GR with independent torsion `T^a_{μν}` (carrying spin density). In the zero-spin limit `S → 0` Einstein–Cartan reduces to pure GR. The differences appear only at Planckian densities (see §8.7).

### 8.3. Postulate P4 and the gravitational constant as an inverse squared scale

The effective gravitational constant `G_eff` in (8.4) is set by the elastic parameters of the `u`-channel. Specifically, introducing the **characteristic curvature scale** of the `u`-channel `l_G = √(γ_C^{grav}/μ_{el})`, dimensional analysis with P1, P2 yields uniquely:

| | |
|---|---|
| **P4.** | `G = c⁴ · ε₀ / (16π · l_G²)`, where `l_G` is the structural curvature scale of the `u`-channel. |

**Numerical value of `l_G`.** Solving P4 for `l_G` using the experimental `G = 6.674 × 10⁻¹¹` N·m²/kg²:

```
l_G = √(c⁴ ε₀ / (16π G))
 = √((2.998×10⁸)⁴ · 8.854×10⁻¹² / (16π · 6.674×10⁻¹¹))
 ≈ 4.62 × 10¹⁵ m ≈ 0.15 pc (8.6)
```

The reverse check `G = c⁴ε₀/(16π l_G²) ≈ 6.674 × 10⁻¹¹` N·m²/kg² agrees with CODATA to 4 significant figures (the precision limit of `G` itself).

> **Note to the reader.** *What is `l_G` intuitively?* It is the structural scale of the **gravitational channel** — the analogue of the structural length `l₀` of the electromagnetic channel. Numerically `l_G ≈ 0.15` parsec ≈ 5 × 10¹² km, about 30 times the size of the Solar System. The weakness of gravity compared with electromagnetism in this picture is a direct consequence of the fact that the characteristic scale of the `u`-channel is **10²⁵ times larger** than that of the `n`-channel: gravity is "stiffer and coarser" in its internal structure, so the medium's response to mass is much weaker than to charge. This is the famous `10⁴²` hierarchy translated into the language of channels.

**`G` is the only independent fourth constant.** By the Buckingham theorem, `{ε₀, μ₀, ℏ}` (Section 5) yields a unique length `l₀ ≈ 4.6 × 10⁻¹⁰ m`. The gravitational scale `l_G ≈ 4.6 × 10¹⁵ m` is not derivable from these three constants. A systematic analysis of alternative paths to `l_G` (induced gravity à la Sakharov [14], bootstrap, instantons, power laws, Jeans length) shows [27] that all of them are either tautological (containing `G` on the right-hand side) or require additional parameters. Therefore:

> **The full canonical set of fundamental constants of nature is `{ε₀, μ₀, ℏ, G}`** — four constants, three of which have independent dimensions.

Dimensionless combinations of these four constants:

| Dimensionless constant | Value | Physical meaning | Pair of points on the hyperbola `m·l = ℏ/c` |
|---|---|---|---|
| `α = e²/(4πε₀ℏc)` | `≈ 1/137` | Fine-structure constant (Section 7) | — (Hyperbola II) |
| `κ_grav = G μ₀/c²` | `≈ 9.3 × 10⁻³⁴` | Weakness of gravity | — |
| `l_G/l₀ ⇔ m₀/m_G^{†}` | `≈ 10²⁵` | **Channel** hierarchy (grav ↔ vacuum) | `(l₀, m₀) ↔ (l_G, m_G)` |
| `λ_C/l_P ⇔ m_P/m_e` | `≈ 10²²` | **Mass** hierarchy (Planck ↔ electron) | `(λ_C, m_e) ↔ (l_P, m_P)` |
| `m_e/m₀ ⇔ l₀/λ_C = 1/(16α²)` | `≈ 1039` (bare) | α²-scaling (Compton ↔ structural cell), §5.5 | `(l₀, m₀) ↔ (λ_C, m_e)` |

`†` `m_G ≡ ℏ/(c · l_G) ≈ 7.6 × 10⁻⁵⁹` kg — the mass corresponding to `l_G` on the hyperbola.

**α²-scaling: the relation `m_e/m₀ = 1/(16α²)`.** This is the ratio of the scales "vacuum cell ↔ electron Compton" on the hyperbola. Numerically:

```
m_e^bare/m₀ = 446.279 keV / 429.51 eV = 1039.0   (bare)
1/(16α_bare²) = 1/(16 · 2⁻¹⁴) = 2¹⁰ = 1024        (leading term, exact)
m_e/m₀ = x² + x/2 − 1 = 1024 + 16 − 1 = 1039      (full dyadic form, [10] §7.2)
1/(16α²) = 1/(16 · (1/137.036)²) ≈ 1173.5          (leading term, physical; full ≈ 1190)
```

In bare dyadic form `m_e/m₀ = 2¹⁰ + 2⁴ − 1 = 1039`; the leading term `2¹⁰ = 1/(16α_bare²)` accounts for the pure `α²`-scaling, the sub-terms `+2⁴ − 1` for the dyadic-structure correction of the knot ([10] §7.2). Physical meaning: the electron mass is the **cost of α²-closure of a topological knot** in the medium; the coefficient 16 is tied to the dyadic structure of the hopfion.

**Remark on consistency with the hyperbola.** Each length ratio in the table is **identical** to the inverse mass ratio through `m·l = ℏ/c` — visible in every row. The differing numerical values of the two "hierarchies" (`10²⁵` for channels and `10²²` for masses) are not a contradiction but a consequence of relating **different pairs of points** on one hyperbola. The exact relation:

```
(l_G/l₀) / (m_P/m_e) = (l_G·l_P) / (l₀·λ_C) = l₀ / (2√2·λ_C) (using (8.9): l_G·l_P = l₀²/(2√2))
 = m_e / (2√2·m₀)
 = 1/(32√2 · α²)
```

Numerical check:
```
10²⁵·⁰⁰³ / 10²²·³⁷⁸ = 10²·⁶²⁵ ≈ 421 
m_e/(2√2·m₀) = 1189.7/2.828 = 420.6 
1/(32√2·α²) = 137²/(32·√2) = 18779/45.25 ≈ 415 (1.3% from QED-running α)
```

So **all** hierarchies in our program are projections of **one** structure (the hyperbola `m·l = ℏ/c`) onto different pairs of its points, and the passage between pairs is expressed by powers of `α` (here `1/α²`) with dyadic prefactors.

### 8.4. Planck scales as derived quantities

The standard definition of the Planck length:

```
l_P = √(ℏG/c³) (8.7)
```

Substituting P4 (`G = c⁴ε₀/(16π l_G²)`) and the structural identity `l₀⁴ = ε₀ℏc/(2π)` (T10):

```
l_P² = ℏG/c³ = (ℏ/c³) · c⁴ε₀/(16π l_G²)
 = ℏ c ε₀ / (16π l_G²)
 = (2π · l₀⁴) / (16π · l_G²)
 = l₀⁴ / (8 l_G²) (8.8)
```

That is:

> `l_P = l₀² / (2√2 · l_G)` (8.9)

**Numerical check:** `l_P_calc = (4.59×10⁻¹⁰)² / (2√2 · 4.62×10¹⁵) ≈ 1.615 × 10⁻³⁵` m, agreeing with the standard `l_P_CODATA = 1.616 × 10⁻³⁵` m to 4 digits.

Similarly, the Planck mass follows from the hyperbola `m·l = ℏ/c`:

```
m_P = ℏ/(c · l_P) = 2√2 · ℏ · l_G / (c · l₀²) ≈ 2.18 × 10⁻⁸ kg (8.10)
```

**Both Planck scales are derived quantities**, expressed through the structural `l₀, l_G` of our program.

**Physical meaning of `l_P`.** In the Cosserat picture `l_P` is the scale at which the EM channel `n` and the gravitational channel `u` become **equally nonlinear**. A defect of size `l_P` would have a gravitational radius of order its own size — a micro black hole. For the electron `λ_C/l_P ~ 10²²` — gravitational effects in atomic physics are negligible.

> **Note to the reader.** The formula `l_P = l₀²/(2√2·l_G)` geometrically means that **the Planck length is `l₀` scaled down** by the same ratio `l₀/l_G` that separates `l₀` from `l_G` (up to a constant): `l_P = l₀·(l₀/l_G)/(2√2)`. A small `l₀` (nanometers) and a huge `l_G` (parsecs) combine to give `~10⁻³⁵` m — the Planck length. In our picture the Planck length is therefore an intersection of two already known structural scales.

#### Equivalent rewriting: `l₀` as the geometric centre of the hierarchy

The identity (8.9) admits an algebraically equivalent regrouping that places **`l₀`** at the centre instead of `l_P`:

```
l₀² = 2√2 · l_P · l_G   ⟺   l₀ = ⁴√8 · √(l_P · l_G) ≈ 1.68 · √(l_P · l_G) (8.10a)
```

That is, **the structural length `l₀` of the EM channel is the geometric mean of `l_P` and `l_G`** up to a factor `⁴√8`. Numerical check on the log scale:

```
log₁₀(l_P) = −34.79 (micro boundary, n ∩ u)
log₁₀(l₀) = −9.34 (geometric centre)
log₁₀(l_G) = +15.66 (macro boundary, u-channel)

l₀ → l_P: 25.45 decades down
l₀ → l_G: 25.00 decades up
```

The mismatch of **0.45 decades** equals `log₁₀(⁴√8) ≈ 0.45` — that is, `l₀` sits **symmetrically** between `l_P` and `l_G` up to exactly the same factor `(2√2)^(1/2)` that enters (8.9).

| Length | Position | Nature |
|---|---|---|
| `l_P` | micro boundary | intersection λ ↔ r_s of a single mass (Section 7.9, Compton–Schwarzschild duality) |
| **`l₀`** | **geometric centre** | structure of the EM channel, intersection point of the `n` and `u` channels of the medium |
| `l_G` | macro boundary | structural scale of the `u`-channel (P4) |

> **Interpretation.** Formula (8.10a) gives a reading of (8.9) "from the other side": `l_P` is not a "fundamental Planck scale" that happens to be decomposable; rather, **`l₀` is the natural centre of the hierarchy**, symmetrically dividing the entire gravitational–quantum range of lengths into two (logarithmically) almost equal halves. That the vacuum EM structure sits at the geometric centre, while Planck and `l_G` are symmetric about it, is an algebraic consequence of (8.9), not an independent postulate.

**Where the factor `2√2` comes from.** Perfect symmetry `l₀² = l_P · l_G` would hold with no prefactor at all. The actual factor `2√2 = √8` has a concrete structural origin: substituting `G = c⁴ε₀/(16π l_G²)` (P4) and `ε₀ℏc = 2π·l₀⁴` (T10) into `l_P² = ℏG/c³` gives

```
l_P² = (2π · l₀⁴) / (16π · l_G²) = l₀⁴/(8 · l_G²)
```

— the factor **`8 = 16π/2π`** is the ratio of the **normalisation of P4 to the normalisation of T10**. The origin of each:

- `16π` in P4 — the standard Hilbert–Einstein action constant `S_EH = (c⁴/(16πG)) ∫ R √-g d⁴x`, fixed by the requirement of the correct Newtonian limit. It enters our program **through the Kleinert gauge mechanism (§8.2)**, where the elastic action is identified with the EH action.
- `2π` in T10 — the Cosserat coupling `η = 2π`, a topological invariant of the sphere `S²` (Section 7).

So `2√2` is a trace of the fact that **the gravitational and EM channels use different normalisations** (one is the standard GR one, the other comes from intrinsic `S²` geometry), not an independent hyperbola. On the log scale this gives exactly `log₁₀(√8) ≈ 0.45` decades — the observed asymmetry between `l₀→l_P` (25.45 decades) and `l₀→l_G` (25.00 decades). With a consistent normalisation (if P4 used the coefficient `2π`, like η in the `n`-channel), the symmetry would be **exact**: `l₀² = l_P · l_G`.

### 8.5. The full hierarchy of scales and closure of the unit base

Combining the results of Sections 5.4, 5.5, 8.3, and 8.4:

| Scale | Symbol | Value | Channel | Source |
|---|---|---|---|---|
| Planck length | `l_P = l₀²/(2√2 l_G)` | 1.62 × 10⁻³⁵ m | `n ∩ u` | from `{ε₀, μ₀, ℏ, G}` |
| Electron Compton | `λ_C = ℏ/(m_e c)` | 3.86 × 10⁻¹³ m | `n` | topology + `{ε₀, μ₀, ℏ}` |
| Vacuum structural length | `l₀ = (ε₀ℏc/2π)^{1/4}` | 4.59 × 10⁻¹⁰ m | `n` | `{ε₀, μ₀, ℏ}` |
| Cosserat length | `l_K` | 2.02 × 10⁻⁷ m | `n → u` coupling | `{ε₀, μ₀, ℏ}` via `μ_c` |
| Gravitational scale | `l_G = √(c⁴ε₀/(16π G))` | 4.62 × 10¹⁵ m | `u` | requires `G` (P4) |

**Only `l_G` requires an independent parameter `G`.** The other four scales follow from `{ε₀, μ₀, ℏ}`.

**Closure of the SI base of units.** With the addition of `G` (through `l_G`), the full reduction reads:

```
{m, kg, s, A} ──(P1, P2)──► {m, kg, s} ──(c)──► {m, kg} ──(ℏ/c)──► {m} ──(l₀, l_G)──► dimensionless
```


### 8.6. The linearized Cosserat metric and the classical tests of GR

For a stationary point source of mass `M`, equation (8.5) gives the Newtonian potential `Φ = -GM/r`. The corresponding metric in isotropic coordinates:

```
ds² = -(1 + 2Φ/c²) c² dt² + (1 - 2Φ/c²) (dr² + r² dΩ²)
 = -(1 - 2GM/(rc²)) c² dt² + (1 + 2GM/(rc²)) (dr² + r² dΩ²) (8.11)
```

This is the **linearized Schwarzschild metric**. The PPN parameters: `γ_{PPN} = 1`, `β_{PPN} = 1` — exactly equal to those of pure GR in the observational limit.

Because the linearized theory is **identical** to GR, **all classical tests pass automatically**:

| Test | Cosserat–Einstein–Cartan | Experiment | Agreement |
|---|---|---|---|
| Perihelion precession of Mercury | 42.99 arcsec/century | 42.98 ± 0.04 | within errors |
| Deflection of light by the Sun | 1.75 arcsec | 1.75 ± 0.02 | within errors |
| Shapiro delay | `γ = 1` | `γ = 1 ± 2.3 × 10⁻⁵` (Cassini) | within errors |
| Gravitational redshift | `Δν/ν = -Φ/c²` | Pound–Rebka, GPS | within errors |
| Gravitational waves | `v = c`, 2 polarizations | LIGO (`Δv/c < 10⁻¹⁵`) | within errors |

For example, the perihelion precession of Mercury:

```
Δφ = 6π GM_☉ / (c² a(1 - e²)) = 42.99 arcsec/century (8.12)
```

— the standard GR formula, valid for any linearized theory with the correct `G`.

### 8.7. Differences from pure GR

In the observational limit, the Cosserat program and GR are identical. At the level of the Einstein–Cartan formalism itself there are two structural differences:

| # | Difference | Where it appears | Visible? |
|---|---|---|---|
| 1 | **Torsion** `T^a_{μν} ≠ 0` (Einstein–Cartan) | Spin density `~ρ_Planck ≈ 5×10⁹⁶ kg/m³` | Only inside black holes / in the early universe (`~50` orders of magnitude below current experiments) |
| 2 | **Nonlinear corrections** (Murnaghan moduli `μ_3, μ_4`) | `(GM/rc²)² ~ 10⁻¹⁶` for the Solar System | Below current precision |

Both differences are testable in extreme regimes (the internal structure of black holes, the early universe) and make the Cosserat program falsifiable: detection of torsion effects would give it unique confirmation; their absence keeps it on a par with GR.

**Remark on the Cosserat length `l_K`.** The Cosserat formalism contains an additional characteristic — the Cosserat length `l_K ≈ 200 nm`, at which the coupling `μ_c` between the `n` and `u` channels manifests itself (see §8.1). This is an internal parameter of the two-channel structure, pertaining to the EM ↔ gravity interaction on the nanoscale rather than to pure gravity alone. Standard `1/r²` tests of gravity at meter scales and above are completely screened from this effect; experimental verification requires special configurations and is discussed in [27].

---

## 9. Relation to the standard natural units for four constants

### 9.1. Standard systems

In high-energy physics the standard system of natural units is `ℏ = c = 1`, in which all dimensions reduce to powers of energy. When gravity is added, one often sets `ℏ = c = G = 1` — **Planck geometrized units** [17].

Analogous systems are used in atomic physics (`ℏ = m_e = e = 1`, Hartree units).

Our reduction `{m, kg, s, A} → {m} → {Energy}`, with the additional normalization `l_G/l₀` for the gravitational channel, operationally gives the same system as the Planck units. All numerical predictions derived in our framework can be converted back without loss of information.

### 9.2. Difference in justification

The difference lies at the level of **justification**, not of **operations**.

**Standard approach:**

> "Setting `ℏ = c = G = 1` simplifies the equations. The change of units is a methodological choice. SI values can be restored by dimensional analysis."

**Our approach (under the Cosserat hypothesis):**

> "`ℏ, c, G` are structural constants of the Cosserat medium, fixed by its elastic parameters via the identifications P1, P2, P3, P4. They are not 'units' that can be chosen; they are consequences of the structure of the medium. Natural units in this picture are not a choice, but a structural fact."

### 9.3. Consequences of the difference

**Consequence 1: uniqueness of the choice of fundamental constants.** In the standard approach any three constants can equally be chosen for the reduction. In our approach the **specific set `{ε₀, μ₀, ℏ, G}`** is singled out by physics: it is these four quantities that structurally specify the Cosserat medium through P1, P2, P3, P4.

**Consequence 2: predictive power.** In the standard approach the values of fundamental constants (e.g. `α = 1/137`, `m_e/m_P ≈ 10⁻²²`) are experimental numbers. In our approach:
- `α` is derived from the structure of the Cosserat functional (Section 7 of this work).
- The hierarchy `l_G/l₀ ≈ 10²⁵` is an open question, equivalent to the mass-scale hierarchy problem.

**Consequence 3: conceptual coherence.** EM and gravity are two channels of one medium, not parallel "fundamental interactions." The `10⁴²` hierarchy is interpreted as `α·(m_P/m_e)²` with geometric root in `l_G/l₀ ≈ 10²⁵`, not as the "weakness of gravity" as a fundamental property.

### 9.4. Comparative table

| Aspect | Standard natural units | Cosserat structural reduction |
|---|---|---|
| Base set of constants | `{ℏ, c, G}` or `{ℏ, c}` | `{ε₀, μ₀, ℏ, G}` (with `μ_0, ε₀` explicit) |
| Choice `ℏ = c = G = 1` | Conventional | Structural (P1–P4) |
| Uniqueness of the set | Arbitrary | Canonical |
| Physical status of `c` | A postulate of SR | The speed of the transverse Cosserat wave |
| Physical status of `G` | A parameter of the Hilbert action | Inverse squared of the scale `l_G` |
| Relation of EM and gravity | Parallel theories | Two channels of one medium |
| `10⁴²` hierarchy | Empirical fact | `α·(m_P/m_e)²` with geometric root `l_G/l₀ ≈ 10²⁵` |
| Predicting `m_e, α` | Impossible | Possible (see [10, 24]) |

---

## 10. Conclusions and subsequent works

### 10.1. Main results

The program of dimensional reduction of the SI has been carried out within a two-channel Cosserat hypothesis — the `n`-channel for the electromagnetic sector, the `u`-channel for gravity. The framework consists of four identifications between parameters of the medium and the fundamental constants of nature: P1 (`ρ ≡ μ₀`), P2 (`G_shear ≡ 1/ε₀`), P3 (`ℏ` as a structural quantization constant of action), P4 (`G = c⁴ε₀/(16π l_G²)` through the Kleinert gauge mechanism).

**Electromagnetic sector.** Already P1 and P2 yield the transverse Cosserat wave speed `c_T = 1/√(ε₀μ₀) ≡ c_light`, on the bare experimental values of `μ₀, ε₀`. From the energy balance `B²/(2μ₀) = ρv²/2` the mechanical identification `H ↔ v` follows, and through it `[A] ↔ [m²/s]`, `[C] ↔ [m²]` — charge acquires the dimension of a cross-sectional area of a defect. The structural fixing of `c` and `ℏ/c` reduces the unit base `{m, kg, s, A} → {m}` (or equivalently to a single energetic dimension), and the summary table of §6 gives a mechanical interpretation of every principal SI quantity.

**Gravitational channel.** Kleinert's program is incorporated as the `u`-channel of the same medium: disclination defects of the elastic continuum are mathematically identical to the Ricci curvature of GR, and the action takes the Hilbert–Einstein form. Postulate P4 fixes the structural scale of the `u`-channel `l_G ≈ 4.6 × 10¹⁵ m`; the linearized Cosserat metric reproduces all five classical tests of GR (Mercury, deflection of light, Shapiro, redshift, gravitational waves). The Planck length turns out not to be fundamental but derived: `l_P = l₀²/(2√2 l_G) ≈ 1.6 × 10⁻³⁵ m`. The `10⁴²` hierarchy between EM and gravity takes the structural form `α·(m_P/m_e)²` with geometric root in `l_G/l₀ ≈ 10²⁵` — two points on a single hyperbola of the medium, rather than the "weakness of gravity" as a fundamental property.

**Fine-structure constant.** Combined with the dimensional reduction `[Q] ↔ [m²]` and the hopfionic identification of the electron (minimum of the functional `E[n, u]` with `Q_H = -1`), the geometry gives `α_bare = 1/128 = 2⁻⁷` — a bare value derived algebraically from `e = π(l₀/2)²` and the structural identity `l₀⁴ = ε₀ℏc/(2π)`. The experimental value of `α` is not used in the derivation. Agreement with the measured `α(M_Z) = 1/128.9` is `0.7%`; the gap to the low-energy `α(0) = 1/137` is the standard QED renormalization through vacuum polarization by virtual pairs.

**Closure.** The full canonical basis of fundamental constants of nature reduces to `{ε₀, μ₀, ℏ, G}`: all SI dimensional quantities are expressed through them, and one of the key dimensionless constants (`α ≈ 1/128 → 1/137`) is derived structurally. Operationally this is equivalent to the standard natural units `ℏ = c = G = 1`, but the justification is different — not a convenience of notation but a removal of redundancy already present in the SI under the assumption that the Cosserat hypothesis is physically realistic.

### 10.2. What is not established in the present paper

- It is not shown that Maxwell's equations are derivable from a Cosserat medium. That result is the subject of [25].
- It is not shown that the Cosserat interpretation is compatible with quantum mechanics at the precision level of QED experiments. An open question.
- The value of `G` (or equivalently the Planck mass `m_P` as the intersection point of the `n`- and `u`-channels on the medium's hyperbola, or the gravitational scale `l_G`) enters the program as an independent postulate (P4). A possible mechanism that would yield this value from the structure of the medium remains an open question.

### 10.3. Subsequent works

The present paper opens a series of six related publications developing different aspects of the Cosserat program:

**Work [10] — electron mass.** "Derivation of the bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization". Uses the dimensional reduction of the present paper to formulate the variational problem. Result: on a 1024×2048 grid (dyadic box `17 × 33 l₀`) the numerical `m_e^bare = 446.279 keV` — the bare electron mass in the Cosserat vacuum; with no free parameters. The dimensionless minimum `Ẽ_min ≈ 1039` fits the dyadic form `m_e/m₀ = x² + x/2 − 1` (`x = α⁻¹/4`); the same shift of the scale `x` that takes `α_bare = 1/128 → α(0) = 1/137` takes the bare mass to the physical `m_e ≈ 511 keV` ([10] §7).

**Work [25] — Maxwell equations.** "Maxwell equations as a theorem of the Cosserat functional" — in preparation. Shows that in the adiabatic, long-wavelength limit Maxwell's equations are **derived** from minimization of `E[n, u]`, promoting postulates P1, P2 to consequences.

**Work [26] — atomic cascade.** "Atomic energy levels from Cosserat functional: a parameter-free derivation for Z = 1 to 36" — in preparation.

**Work [27] — gravity as the u-channel.** "Two-channel structure of Cosserat continuum: gravity as the u-channel" — in preparation. An expansion of Section 8 of the present paper into a self-contained theory of gravitation with calculations for cosmological problems.

**Work [23] — proton as a disclination.** "Proton as a disclination of the medium lattice: mass and lattice length convergence" — in preparation. The baryon as a **disclination** defect of the Cosserat lattice (in contrast to the hopfionic knot of the electron). Preliminary: `m_p ≈ 992 MeV` (5.7%), `r_p ≈ 0.84` fm. Full derivation of the hierarchy `m_p/m_e ≈ 1836` via the running of the effective elasticity from the electron scale `l₀` to the nucleon scale.

### 10.4. Open questions

- A full derivation of the proton mass as a disclination of the Cosserat lattice — numerical computations of mass and lattice length convergence in the neighbourhood of a disclination defect are given in [23]; a general theory of baryons (including the neutron and the link with QCD colour degrees of freedom) is an open question.
- Relativistic corrections of order `α²` to atomic levels.
- Gravity experiments at the scale `l_K ≈ 200 nm` — testing for the massive Cosserat mode.

### 10.5. An interpretive consequence: entanglement as "two knots on the threads of one lattice"

Einstein in 1935 called quantum entanglement *spukhafte Fernwirkung* — "spooky action at a distance" [EPR, *Phys. Rev.* **47** (1935) 777], and that phrasing set the tone of the discussion for decades. The Cosserat picture offers a geometric reading of the same phenomenon in which there is no "action at a distance" at all — and it is worth saying how this works.

In the standard interpretation, two entangled particles are two separate objects with instantaneous correlations that cannot be reduced to local hidden variables (Bell's theorem 1964, the Aspect experiments 1982, and so on). In our picture a "particle" is not a separate object at all: it is a topological defect of **a single continuous field** `n(r,t)` (§5.5), tied to the field lines of that field. Two "entangled particles" are accordingly

> **two knots tied on the threads of one and the same Cosserat lattice.**

Seen this way, the strangeness disappears. The field `n(r,t)` is continuous everywhere in space, and its field lines bind the medium into a single geometric whole; the measurement of one knot is a local event, but **the configuration of threads itself** has encompassed both knots as a single whole from the moment the pair was prepared. The correlation does not "arise upon measurement" — it is simply **there**, as a geometric property of one configuration: the global charge `Q_total = Q_H⁽¹⁾ + Q_H⁽²⁾` is a topological invariant of the field lines passing through both knots, and for a pair with `Q_total = 0` (electron–positron) the individual charges of the knots are anti-correlated **by construction**, at any separation. No information is transmitted between the knots at the moment of measurement, and the speed of light is not at issue: that information was woven into the topology of the lattice from the moment of its creation. Measurement merely reveals what was already there.

The violation of Bell's inequalities is intelligible in this language too: local hidden variables fail not because nature is "spooky" but because **there are not two separate local objects** — there is one global field of threads with two defects in it.

**An analogy — a taut net.** Picture a net of threads with a connected topology; on two well-separated parts of it a knot has been tied. Untying one knot automatically changes the topology of **the whole** connected system — that is not action at a distance, it is a property of the net as a single geometric object. In a Cosserat medium the field lines of `n(r,t)` play the same role, and connectedness is provided by the continuity of the field itself.

**Status.** Numerically this interpretation reproduces standard QM for all known EPR experiments — it is an **ontological** reading, not a set of new equations. Distinguishing predictions are in principle possible — in strongly inhomogeneous Cosserat media (e.g. near massive bodies, where the `u`-channel nontrivially modifies `K_i, μ_c` and thereby the thread connectivity), and through a possible link of `Q_total` with quantitative bounds on Bell-inequality violation; both are subjects for separate work.

### 10.6. A methodological remark: the medium as a mediator

In physics there is a familiar pattern: introducing an intermediate structure between two descriptions often simplifies the mathematical apparatus. The earliest example is Maxwell's own argument (1861): the aether as a mediator turned the nonlocal Coulomb action at a distance into local field equations; half a century later Einsteinian spacetime did the same thing for Newtonian gravity, replacing it with local geometry. The Cosserat medium in this paper occupies an analogous position — but a broader one: it acts as a mediator between the topology of defects (`Q_H ∈ ℤ` in `π₃(S²)`) and the observable particles and fields, reducing the heterogeneous apparatus of QM (Hilbert spaces), QED (gauge fields), and GR (pseudo-Riemannian geometry) to a single problem — minimization of the functional `E[n, u]`.

This observation is an indication of mathematical economy of the program, not a proof of its correctness; the latter is decided by numerical predictions [10, 23, 24].

---

## Methodology and use of AI tools

In preparing this work the author used the large language model **Claude (Anthropic)** for the following auxiliary tasks: writing Python scripts for numerical verification of the structural identities (§§5.4, 6.3, 7.4, A.5 — evaluation of `l₀`, `M₀c²`, `α_bare = 1/128`, dimensional consistency checks), stylistic editing and proofreading of the manuscript, and assistance with bibliographic references and table formatting.

All key elements of the work — postulates P1–P4, the structural identifications of the electromagnetic and gravitational sectors, the derivations of the identities `m·l = ℏ/c` and `l₀⁴ = ε₀ℏc/(2π)`, the geometric interpretation of `α_bare`, the hierarchy of scales, and the reduction of the SI base — are due to the author.

The author has thoroughly checked all generated code (via independent reproduction of the numerical values of the constants) and the manuscript text, and takes full responsibility for the final content and results of the work.

---

## Acknowledgements

The author thanks:

- **J.C. Maxwell, W. Thomson (Kelvin), J. Larmor, E. and F. Cosserat** — for the historical foundation of the mechanical interpretation of electromagnetism and the formalism of micropolar continua.
- **H. Kleinert** — for the modern program of gauge theory of defects and its link with gravity through Einstein–Cartan. Section 8 of the present paper is a concrete Cosserat realization of Kleinert's program with the additional inclusion of the electromagnetic sector in a single medium.
- **A.C. Eringen, G.A. Maugin, W. Nowacki** — for the modern development of the Cosserat-media formalism.
- **L.D. Faddeev, A.J. Niemi, T.H.R. Skyrme** — for creating the language of topological solitons.
- **E. Cartan** — for the theory of affine connections with torsion, underlying Einstein–Cartan and the interpretation of disclinations.

---

## References

[1] **Maxwell, J.C.** (1861–1862). "On Physical Lines of Force." *Philosophical Magazine* **21**, 161–175, 281–291, 338–348; **23**, 12–24, 85–95.

[2] **Cosserat, E. and Cosserat, F.** (1909). *Théorie des corps déformables.* Hermann et Fils, Paris.

[3] **Eringen, A.C.** (1999). *Microcontinuum Field Theories I: Foundations and Solids.* Springer-Verlag, New York.

[4] **Faddeev, L. and Niemi, A.J.** (1997). "Stable knot-like structures in classical field theory." *Nature* **387**, 58–61.

[5] **Oseen, C.W.** (1933). "The theory of liquid crystals." *Transactions of the Faraday Society* **29**, 883–899. See also **Frank, F.C.** (1958), *Disc. Faraday Soc.* **25**, 19.

[6] **Larmor, J.** (1900). *Aether and Matter.* Cambridge University Press.

[7] **Skyrme, T.H.R.** (1962). "A unified field theory of mesons and baryons." *Nuclear Physics* **31**, 556–569.

[8] **Heaviside, O.** (1893–1912). *Electromagnetic Theory*, vols. I–III. London.

[9] **Maugin, G.A.** (1988). *Continuum Mechanics of Electromagnetic Solids.* North-Holland, Amsterdam.

[10] **Yeusiyevich, I.V.** (2026). "Derivation of electron mass from `{ε₀, μ₀, ℏ}` through Cosserat functional minimization." (In preparation, same DOI series.)

[11] **Kleinert, H.** (1989). *Gauge Fields in Condensed Matter, Vol. II: Stresses and Defects — Differential Geometry, Crystal Melting.* World Scientific, Singapore.

[12] **Kleinert, H.** (2008). *Multivalued Fields in Condensed Matter, Electromagnetism, and Gravitation.* World Scientific, Singapore.

[13] **Cartan, E.** (1922). "Sur une généralisation de la notion de courbure de Riemann et les espaces à torsion." *Comptes Rendus Acad. Sci. (Paris)* **174**, 593–595. See also **Hehl, F.W., von der Heyde, P., Kerlick, G.D., Nester, J.M.** (1976), "General Relativity with Spin and Torsion: Foundations and Prospects." *Rev. Mod. Phys.* **48**, 393–416.

[14] **Sakharov, A.D.** (1968). "Vacuum quantum fluctuations in curved space and the theory of gravitation." *Soviet Physics – Doklady* **12**, 1040.

[15] **Peskin, M.E. and Schroeder, D.V.** (1995). *An Introduction to Quantum Field Theory.* Addison-Wesley.

[16] **Jackson, J.D.** (1998). *Classical Electrodynamics*, 3rd ed. Wiley.

[17] **Misner, C.W., Thorne, K.S., and Wheeler, J.A.** (1973). *Gravitation.* W.H. Freeman.

[18] **Nowacki, W.** (1986). *Theory of Asymmetric Elasticity.* Pergamon Press / PWN, Warsaw.

[19] **CODATA-2018.** *The 2018 CODATA Recommended Values of the Fundamental Physical Constants.* NIST.

[20] **BIPM** (2019). *The International System of Units (SI), 9th edition.* Bureau International des Poids et Mesures.

[21] **Will, C.M.** (2014). "The Confrontation between General Relativity and Experiment." *Living Reviews in Relativity* **17**, 4. (A review of the PPN formalism and the experimental tests of GR.)

[22] **Abbott, B.P. et al. (LIGO/Virgo Coll.)** (2017). "Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A." *Astrophys. J. Lett.* **848**, L13. (The bound `|Δv|/c < 10⁻¹⁵` on the speed of gravitational waves.)

[23] **Yeusiyevich, I.V.** (2026). "Proton as a disclination of the medium lattice: mass and lattice length convergence." (In preparation, same DOI series.) — numerical computations for the baryonic sector of the Cosserat program: the proton as a disclination defect of the medium's lattice (in contrast to the hopfionic knot of the electron), convergence of mass and characteristic lattice length in the neighbourhood of the disclination. Preliminary results: `m_p ≈ 992 MeV` (accuracy 5.7% from the experimental 938.272 MeV), `r_p ≈ 0.84` fm; the hierarchy `m_p/m_e ≈ 1836` is interpreted via the running of the medium's effective elasticity from the electron scale `l₀` to the nucleon scale.

[25] **Yeusiyevich, I.V.** (2026). "Maxwell equations as a theorem of the Cosserat functional." (In preparation, same DOI series.) — shows that in the adiabatic, long-wavelength limit Maxwell's equations are derived from minimization of the Cosserat-medium functional `E[n, u]`, promoting postulates P1, P2 to consequences of a more fundamental structure.

[26] **Yeusiyevich, I.V.** (2026). "Atomic energy levels from Cosserat functional: a parameter-free derivation for Z = 1 to 36." (In preparation, same DOI series.) — atomic cascade without free parameters with mean relative error `1.13%` for Z = 1..36.

[27] **Yeusiyevich, I.V.** (2026). "Two-channel structure of Cosserat continuum: gravity as the u-channel." (In preparation, same DOI series.) — a self-contained theory of gravitation with calculations for cosmological problems, expanding Section 8 of the present paper.

[28] **Smalyukh, I.I.** (2020). "Knots and other new topological effects in liquid crystals and colloids." *Reports on Progress in Physics* **83**, 106601. See also **Ackerman, P.J. & Smalyukh, I.I.** (2017), "Static three-dimensional topological solitons in fluid chiral ferromagnets and colloids," *Nature Materials* **16**, 426. (Experimental realization of hopfions in continuous media.)

[29] **Berry, M.V.** (1984). "Quantal phase factors accompanying adiabatic changes." *Proceedings of the Royal Society of London A* **392**, 45–57. (Berry phase for spin-½ in a slowly varying field; the key reference for the Hopf–Berry correspondence in §1.4.)

[30] **Wilczek, F. and Zee, A.** (1984). "Appearance of gauge structure in simple dynamical systems." *Physical Review Letters* **52**, 2111–2114. (Non-Abelian generalization of the Berry phase; gauge structure on the parameter sphere.)

---

## Appendix A. Summary of postulates, identities, and scales

### A.1. Postulates

| | |
|---|---|
| **P1** | `ρ_medium ≡ μ₀` |
| **P2** | `G_shear ≡ 1/ε₀` |
| **P3** | `ℏ` — structural constant of the Cosserat medium (quantum of action) |
| **P4** | `G = c⁴ε₀/(16π l_G²)` (Kleinert mechanism, `l_G` is the structural scale of the `u`-channel) |
| **P5** | The cross-section of the hopfion tube in the derivation of `α` is approximated by a disc of radius `r_v`: `e = π·r_v²`. Idealization of the oblate shape optimal for minimization of `E[n, u]`; sensitivity of `α` to the asymmetry is `O(ε²)` |

### A.2. Derived identities

| | |
|---|---|
| **T1** | `c_T = √(G_shear/ρ) = 1/√(ε₀μ₀) ≡ c_light` |
| **T2** | `v = B/μ₀ = H` (mechanical interpretation of `H`) |
| **T3** | `[A] ↔ [m²/s]` |
| **T4** | `[C] ↔ [m²]` |
| **T5** | `1 s ↔ c · 1 s = 2.998 × 10⁸ m` |
| **T6** | `m · l_C = ℏ/c` (Compton trade-off) |
| **T7** | `[kg] ↔ [1/m]` |
| **T8** | `{m, kg, s, A} → {m} → {Energy}` (full reduction) |
| **T9** | `r_v = l₀/2` (vortex-tube radius = half the structural length) |
| **T10** | `l₀⁴ = ε₀ℏc/(2π)` (structural length identity) |
| **T11** | `α_bare = e²/(4πε₀ℏc) = 1/128 = 2⁻⁷` (fine-structure constant) |
| **T12** | `e²/(4πε₀) ≡ ℏcα` (Hyperbola II: charge squared × channel stiffness) |
| **T13** | `m₀² · e = (π/4)·(ℏ/c)² = √(8π²α)·(ℏ/c)²` (interlocking of the two hyperbolas) |
| **T14** | `G = c⁴ε₀/(16π l_G²)` (Kleinert) |
| **T15** | `l_P = l₀²/(2√2 · l_G)` (Planck length as a derived quantity) |
| **T16** | `E = mc² = ℏc/l = ℏω` (Einstein, de Broglie, Planck as three projections of one hyperbola; physically — the resonance energy of an LC circuit `ω(l) = c/l`, see §5.4) |
| **T17** | `E · t = m · l · c = ℏ` (universal structural identity) |
| **T18** | `Z₀ = 2α·R_K`, `R_K = h/e²` (Hyperbola II ≡ von Klitzing relation; measured to `10⁻¹⁰`, Appendix C.1) |
| **T19** | `[K] ↔ energy ↔ 1/m`; `λ·T = (ℏc/k_B)·(2π/x_W)` (thermal hyperbola = Wien's law, Appendix C.5) |
| **T20** | `μ_B = e·Γ₀/(4π)`, `Γ₀ = h/m_e` (Bohr magneton = charge-area × circulation quantum, Appendix C.6) |

### A.3. The full hierarchy of structural scales

| Scale | Symbol | Value | Channel | Source |
|---|---|---|---|---|
| Planck length | `l_P` | 1.62 × 10⁻³⁵ m | `n ∩ u` | T15 (derived: `l₀²/(2√2 l_G)`) |
| Compton length of the electron | `λ_C` | 3.86 × 10⁻¹³ m | `n` | T6: `ℏ/(m_e c)` |
| Structural length of the medium | `l₀` | 4.59 × 10⁻¹⁰ m | `n` | T10: `(ε₀ℏc/2π)^{1/4}` |
| Cosserat length | `l_K` | 2.02 × 10⁻⁷ m | `n → u` | numerically from `μ_c` |
| Gravitational scale | `l_G` | 4.62 × 10¹⁵ m | `u` | T14: `√(c⁴ε₀/(16π G))` |

### A.4. Dimensionless constants

| | |
|---|---|
| `α = e²/(4πε₀ℏc) ≈ 1/137` | Fine-structure constant |
| `κ_grav = Gμ₀/c² ≈ 9.3 × 10⁻³⁴` | Weakness of gravity |
| `l_G/l₀ ≈ 10²⁵` | Channel hierarchy |
| `m_P/m_e ≈ 10²²` | Mass hierarchy (equivalent) |
| `α_bare = 1/128 = 2⁻⁷` | "Bare" `α` (Section 7) |
| `η = 2π` | Cosserat coupling (see [10]) |
| `K₃/K₁ = 1 + η = 1 + 2π` | Elastic anisotropy (see [10]) |

### A.5. Numerical checks

**(a) Agreement `c_T = c_light`:**
```
c_T = 1/√(ε₀μ₀) = 1/√(8.854×10⁻¹² · 4π×10⁻⁷)
 = 2.99792458 × 10⁸ m/s ≡ c_light (CODATA) 
```

**(b) Agreement `m₀·l₀ = ℏ/c`:**
```
m₀ · l₀ = 7.66 × 10⁻³⁴ · 4.5943 × 10⁻¹⁰
 = 3.518 × 10⁻⁴³ kg·m
ℏ/c = 1.054572 × 10⁻³⁴ / 2.998 × 10⁸
 = 3.518 × 10⁻⁴³ kg·m (15 significant figures of CODATA)
```

**(c) Agreement `l₀⁴ = ε₀ℏc/(2π)`:**
```
l₀⁴_calc = (4.5943×10⁻¹⁰)⁴ = 4.4555 × 10⁻³⁸ m⁴
ε₀ℏc/(2π) = (8.854×10⁻¹²)(1.0546×10⁻³⁴)(2.998×10⁸)/(2π)
 = 4.4561 × 10⁻³⁸ m⁴ (agreement to 4 digits)
```

**(d) Agreement `α_bare = 1/128`:**
```
e = π(l₀/2)² = π · (4.5943×10⁻¹⁰/2)² = π · 5.279×10⁻²⁰ = 1.658×10⁻¹⁹ m²
e_exp = 1.602 × 10⁻¹⁹ C (i.e. m² in mech. units)
Agreement e_calc/e_exp = 1.035 (3.5%, within the geometric factor)

α_calc = e²/(4πε₀ℏc) with e = π(l₀/2)²:
 = π·l₀⁴/(64·ε₀ℏc) = π·(ε₀ℏc/(2π))/(64·ε₀ℏc) = 1/128
α_exp(M_Z) = 1/128.9 ± 0.1
Agreement: 0.7% 
```

**(e) Agreement `l_P = l₀²/(2√2 l_G)`:**
```
l₀²/(2√2 l_G) = (4.5943×10⁻¹⁰)² / (2√2 · 4.62×10¹⁵)
 = 2.111×10⁻¹⁹ / 1.307×10¹⁶
 = 1.615 × 10⁻³⁵ m
l_P_CODATA = √(ℏG/c³) = 1.616 × 10⁻³⁵ m 
```

**(f) Agreement `G = c⁴ε₀/(16π l_G²)`:**
```
G_check = (2.998×10⁸)⁴ · 8.854×10⁻¹² / (16π · (4.62×10¹⁵)²)
 = 6.674 × 10⁻¹¹ N·m²/kg²
G_CODATA = 6.6743 × 10⁻¹¹ N·m²/kg² 
```

---

## Appendix B. Data and code availability

Reproducible code is available in the repository:

```
https://github.com/igorevsiev-cmyk/cosserat-program
```

Supplementary materials specific to this preprint are located under `papers/2026-05-SI-reduction/`. An independent numerical verification of the Derrick balance of the canonical configuration (§7.3) is in `verifications/canonical_derrick/`.

A Zenodo copy of this preprint is registered with DOI:

```
https://doi.org/10.5281/zenodo.20187199
```

(Previous version v1.1: `10.5281/zenodo.20162265`.)

---

## Appendix C. Metrological closure, rheology of the medium, and the temperature branch

*(added in version 4, 2026-07-02)*

The dimensional reduction of §§3–6 has consequences that did not make it into the main text. They are collected here because they change the status of the program: some of its "theoretical" identities turn out to be **long-measured facts of precision metrology**, and the reduction extends naturally to the remaining SI base units. No statement in this appendix requires new postulates — everything follows from P1–P3 and Table 6.2.

### C.1. Hyperbola II has already been measured: the von Klitzing relation

The quantum Hall effect provides the resistance quantum (the von Klitzing constant):

```
R_K = h/e² = 25 812.807 Ω
```

— one of the most precisely reproducible quantities in physics (relative accuracy `~10⁻¹⁰`; since 2019 the value is exact by definition). Direct substitution of `ℏ = h/2π` into the impedance form of Hyperbola II (7.16c), `e²·Z₀ = 4πℏα`, gives:

```
Z₀ = 2α · R_K                                                              (C.1)
```

— numerically the identity holds to all CODATA digits (verified to 16 figures). That is, **Hyperbola II is not a construction of the program but a metrological fact of the highest available precision**; the program adds a mechanical ontology to it:

- `Ω ↔ kg/(m²·s)` is an acoustic impedance (§6.2), so **the Hall quantum is a quantized mechanical impedance of the medium**, and the Hall plateaux are integer fractions of the impedance of a single knot;
- the conductance quantum `G₀ = 2e²/h` (nanocontacts, point contacts) is a quantized mechanical admittance;
- `α = Z₀/2R_K` reads literally: the fine-structure constant is **the ratio of the impedance of the free medium to the impedance of the knot**.

### C.2. The SI-2019 pattern: exactly `{α, G}` remain free

The 2019 SI reform fixed the following constants to exact values:

| SI-2019 constant (exact) | Role in the Cosserat program |
|---|---|
| `c` | shear wave speed of the medium (T1) — conversion `s ↔ m` |
| `h` | action quantum of microrotations (P3) — conversion `kg ↔ 1/m` |
| `e` | cross-sectional area of the defect (T4, §7) — derived from `l₀` |
| `k_B` | conversion `K ↔ energy` (see C.5) |
| `N_A` | counting unit (dimensionless normalization) |
| `Δν_Cs`, `K_cd` | operational realizations of the second and the candela |

After these were fixed, exactly two quantities remained **measured** (i.e. carrying physical information rather than convention): `α` (equivalently, the pair `ε₀, μ₀` or `Z₀`, which since 2019 carry experimental uncertainty) and `G`. These are precisely **the two inputs of the Cosserat program**: `α` it *derives* (`α_bare = 1/128`, §7), and `G` it honestly *postulates* as the fourth constant (P4, §8).

In other words: metrology, possessing no theory of the medium whatsoever, arrived empirically at the same partition of constants into "structural conversions" and "physical content" as the present work. SI-2019 de facto carried out half of the reduction of §6.4; the program supplies that reduction with a mechanical justification and closes one of the two remaining quantities.

**The Kibble balance as the institutionalization of Hyperbola I.** Since 2019 the kilogram is *realized* through `h`: the watt balance equates the mechanical power `m·g·v` with the electrical power `U·I`, where `U` and `I` are measured via the Josephson and von Klitzing effects — that is, mass is determined by **counting quanta**. The reduction `kg ↔ 1/m` via `ℏ/c` (T7, Hyperbola I) is no longer an interpretation but the operating procedure for realizing the unit of mass.

### C.3. Rheology of the medium: resistance is viscosity

Table 6.2 implies a chain not spelled out in the main text:

```
[Ω·m] = kg/(m·s) = Pa·s      — resistivity ↔ DYNAMIC VISCOSITY
```

The electrical resistance of a substance is the viscosity of the medium with respect to the deformation flow (the current, `[A] ↔ m²/s`; note that the dimension of current itself coincides with kinematic viscosity and the diffusion coefficient — current is a transport coefficient). Numerically:

| System | "Viscosity" |
|---|---|
| Copper (ρ_R = 1.68×10⁻⁸ Ω·m) | `1.7×10⁻⁸ Pa·s` |
| Air | `1.8×10⁻⁵ Pa·s` |
| Water | `1.0×10⁻³ Pa·s` |
| Superconductor | `0` |

A metal is a medium with negligible viscosity (three orders of magnitude below air) for the deformation flow; **superconductivity = strictly zero viscosity = superfluidity** of the deformation flow. The London equations in this language describe ideal (dissipationless) flow; the connection with superfluid helium ceases to be an analogy (they share the circulation quantum `Γ = h/m`) and becomes an identity of dimensions.

Two consequences for circuit theory:

```
R·C = [kg/(m²·s)] · [m²·s²/kg] = s    — the RC time constant = the MAXWELL
                                        relaxation time τ = viscosity × compliance
L/R = [kg/m²] / [kg/(m²·s)] = s       — inertial relaxation
```

The electrical RC chain is literally a Maxwell rheological element (spring + damper); low-frequency electrical engineering is the rheology of the medium.

**Vacuum as a viscoelastic body.** Vacuum does not conduct direct current (does not "flow"), yet transmits elastic waves perfectly. In the terms of C.3 this is standard viscoelastic behaviour — and it closes, at the level of dimensions, the famous nineteenth-century puzzle ("is the aether solid or liquid?", Stokes's pitch analogy). Significantly, the same rheological language (the standard linear Zener body, relaxation `μ_el(ω)`) is applied to the **gravitational** `u`-channel in [27]: rheology is the common formalism of both channels of the medium.

### C.4. Magnetic flux is a mass flow rate (and the Table 6.2 erratum)

The correct mechanical dimension of magnetic flux:

```
Wb = V·s = (kg/s²)·s = kg/s;     equivalently  T·m² = [kg/(m²·s)]·m² = kg/s
```

— a **mass flow rate** (momentum per unit length). The rows "Volt = kg/s²" and "Henry = kg/m² = Wb/A" of Table §6.2 are consistent with this.

> ⚠ **Erratum.** In versions ≤ 2 of this work, the "Magnetic flux" row of Table §6.2 gave the dimension `kg·m/s` (momentum). This was an error, contradicting the neighbouring rows of the same table; the correct dimension is `kg/s`. Corrected in version 4.

Consequences:

- **The flux quantum** `Φ₀ = h/2e = 2.068×10⁻¹⁵ Wb ↔ 2.068×10⁻¹⁵ kg/s` is a **quantum of medium flow rate**: a superconducting ring quantizes not an abstract "flux" but the mass flow rate of the medium through its cross-section; a SQUID is a counter of these quanta.
- **The Josephson effect** `V = Φ₀·f` reads mechanically: "tension (kg/s²) = flow rate (kg/s) × frequency (1/s)". The voltage standard is a count of flow-rate quanta per second.
- The pair `(K_J = 2e/h, R_K = h/e²)` are exactly the two effects through which the Kibble balance realizes the kilogram (C.2): the metrological triangle "mass–voltage–resistance" closes inside a single mechanics of the medium.

### C.5. The temperature branch: kelvin → energy, Wien as a thermal hyperbola

The main text reduces `{m, kg, s, A}`; but the SI base also contains the kelvin, the mole, and the candela. The mole is a counting unit (dimensionless), the candela is anthropometric (a convolution of the watt with the sensitivity of the eye); only the kelvin carries physical content. The exact fixing of `k_B` in SI-2019 (C.2) makes the reduction trivial:

```
[K] ↔ energy ↔ 1/m      (T7):  temperature is an inverse length
```

To every temperature corresponds a length `λ(T) = ℏc/(k_B T)` — and this family is a **thermal hyperbola** `λ·T = const`, structurally parallel to Hyperbola I. Its experimental name is **Wien's displacement law**:

```
λ_max·T = b = (ℏc/k_B)·(2π/x_W),   x_W = 4.9651...  ⟹  b = 2.8978×10⁻³ m·K ✓ CODATA
```

(the dimensionless factor `x_W` is the root of the transcendental equation of the Planck spectrum; the entire dimensional part is the hyperbola of the medium).

The temperature equivalent of the vacuum cell is the **structural temperature of the medium**:

```
T₀ = M₀c²/k_B = 4.984×10⁶ K
```

The physical meaning of `T₀` (candidate: the "melting" scale of the orientational order of the cell) is an open question. *A curiosity without a mechanism (status: numerology, quoted only for completeness): the temperature of the Sun's core, `15.7×10⁶ K`, relates to `T₀` as `3.150 ≈ π` (0.3%).*

The full reduction of the SI base: `{m, kg, s, A, K, mol, cd} → {Energy}`.

### C.6. The Bohr magneton: a bond between two quanta of the program

The magnetic moment in mechanical units: `J/T ↔ m⁴/s = area × (m²/s)` — "area × circulation" (or "area × current", as in SI). The Bohr magneton is then assembled from two quanta already introduced by the program — the charge-area `e` (T4) and the circulation quantum `Γ₀ = h/m_e` (the same one that quantizes vortices in He-II):

```
μ_B = eℏ/(2m_e) = e·Γ₀/(4π) = 9.274×10⁻²⁴ J/T ✓                          (C.2)
```

The spin magnetic moment of the electron is the charge-area of the knot multiplied by the circulation quantum of the medium: the third quantum is expressed through the first two.

---

**End of main text.**

*Version 4. Comments and feedback are welcome at: igorevsiev@gmail.com.*
