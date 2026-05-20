# Cosserat Program

A research program reconstructing fundamental physics — electromagnetism, gravitation, atomic structure, and elementary particles — as phenomena of a single two-channel Cosserat continuum (an elastic medium with both translational and microrotational degrees of freedom). The program proceeds from four identifications of medium parameters with the fundamental constants of nature

- **P1:** `ρ ≡ μ₀` (medium density = magnetic permeability),
- **P2:** `G_shear ≡ 1/ε₀` (shear modulus = inverse electric permittivity),
- **P3:** `ℏ` as the action quantum of microrotations,
- **P4:** `G = c⁴ε₀/(16π l_G²)` via the Kleinert gauge mechanism,

and proceeds by deriving observed quantities — `c`, `α`, the electron mass, atomic spectra, the proton mass, the hierarchy of EM vs. gravitational forces — as theorems about this medium rather than as independent empirical inputs.

This repository hosts the preprints, supplementary data, and code accompanying the program.

## Papers in this repository

| # | Topic | Folder | Status |
|---|---|---|---|
| 1 | **SI reduction & fine-structure constant** | [`papers/2026-05-SI-reduction/`](papers/2026-05-SI-reduction/) | preprint v2 |
| 2 | **Bare electron mass from `{ε₀, μ₀, ℏ}` via Cosserat-functional minimization** | [`papers/2026-05-electron-mass/`](papers/2026-05-electron-mass/) | preprint |

Forthcoming papers in the same series (in preparation, will appear here as they are released):

- **[23]** Proton as a disclination of the medium lattice
- **[24]** Topological charge and the fine-structure constant
- **[25]** Maxwell equations as a theorem of the Cosserat functional
- **[26]** Atomic energy levels from the Cosserat functional (Z = 1..36)
- **[27]** Two-channel structure: gravity as the `u`-channel

## Supplementary verifications

- [`verifications/canonical_derrick/`](verifications/canonical_derrick/) — independent Derrick scan of the full canonical functional (§7.3 of paper 1): confirms that the canonical Hopf configuration is a true minimum under spatial dilation, with the bare electron mass `m_e^bare = 446.279 keV` (dyadic box `17 × 33 l₀`, `1024 × 2048` grid) and topology preserved across the scan.
- [`verifications/electron_mass_minimization/`](verifications/electron_mass_minimization/) — independent Nelder–Mead minimization (§5 of paper 2): reproduces the canonical Hopf optimum on a `1024 × 2048` grid (dyadic box `17 × 33`) from a generic initial guess, yielding the bare electron mass `m_e^bare = 446.279 keV` with no fitted parameters.

## Status

All works in this repository are preprints, not yet peer-reviewed. Each paper's folder contains its own README with citation, DOI, and supplementary materials.

## License

Creative Commons Attribution 4.0 International (CC-BY 4.0).

## Contact

Ihar Yeusiyevich — igorevsiev@gmail.com
