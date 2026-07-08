# -*- coding: utf-8 -*-
"""
verify_g0_and_identity_3d.py — check of g₀ ↔ e (normalization audit) +
the Leibniz identity on the CANONICAL 3D hopfion.

Parts:
  A. Analytic audit (pure SI, printed numbers):
     - g₀ from the energy normalization (Skyrme = Maxwell): γ² = 4μ₀C₄
     - charge of the w-quantum q_w = ℏ/γ, its α_w = q_w²/(4πε₀ℏc)
     - comparison with the geometric e = π(l₀/2)², α_bare = 1/128
  B. Numerical part (canonical hopfion from
     verifications/electron_mass_minimization, NM optimum):
     - field n on a 3D Cartesian grid (frame rule: n1,n2 in the r̂,φ̂ basis)
     - identity: ∂_i F_ij = n·(∇²n × ∂_j n) + n·(∂_i n × ∂_i∂_j n)
     - E_Sk(3D) and E_OF(3D) against the canonical 2D values
     - ‖term1‖/‖term2‖

Canonical optimum (result.json, DOI 10.5281/zenodo.20477123):
  R_r = 0.6408160149362525, R_z = 0.8072875518184682, w = 0.7019955806536682
  E_OF = 221.88762 keV, E_Sk = 220.63364 keV, M0c² = 429.50679 eV
"""

import numpy as np
import math

try:
    import torch
    HAS_TORCH = torch.cuda.is_available()
except ImportError:
    HAS_TORCH = False

# ============================================================
# PART A: normalization audit g₀ ↔ e (pure SI)
# ============================================================
print("=" * 72)
print("PART A. Normalization audit g0 <-> e (SI, no sim-units)")
print("=" * 72)

EPS0 = 8.854187817e-12      # F/m
HBAR = 1.054571817e-34      # J·s
C    = 299792458.0          # m/s
MU0  = 1.0 / (EPS0 * C * C) # kg/m³ (mechanical)
Z0   = MU0 * C              # 376.73

l0   = (EPS0 * HBAR * C / (2 * np.pi)) ** 0.25
M0C2 = HBAR * C / l0

print(f"l0        = {l0:.6e} m = {l0*1e9:.4f} nm")
print(f"M0 c^2    = {M0C2/1.602176634e-19:.4f} eV")

# --- Coefficient convention ----------------------------------------
# Code (compute_skyrme_stretched): E_Sk = c4 * ∫ Σ_pairs F_ab² dV, c4 = 1.
# In the Lorentz form L = (C4/4) F_μν F^μν this is C4 = 2·c4_code:
#   (C4/4) F_μν F^μν = (C4/2) Σ_pairs F² = c4_code Σ_pairs F²  ⟹ C4 = 2.
# Sim units: energy M0c², length l0 ⟹ C4_SI = 2 · M0c² · l0 = 2ℏc.
# σ-model coefficient: E_OF(isotropic) = (K1/2)|∇n|², K1 = 2
#   ⟹ c2 = K1 = 2 sim = 2 · M0c²/l0 = 2ℏc/l0².
C4_SI = 2.0 * M0C2 * l0          # = 2 ℏ c
c2_SI = 2.0 * M0C2 / l0          # = 2 ℏ c / l0²
print(f"C4 (Lorentz convention, code c4=1) = {C4_SI:.6e} J·m = 2ℏc: "
      f"{C4_SI/(2*HBAR*C):.15f}")
print(f"c2 (K1=2)                        = {c2_SI:.6e} J/m")

# --- Energy normalization g0 ----------------------------------------
# F = n·(∂n×∂n) = 2(∂A−∂A) = 2G.  Skyrme: (C4/4)F² = C4·G².
# Maxwell: (1/4μ0)F_phys², F_phys = γG (A_phys = γA).
# Matching the terms: C4 = γ²/(4μ0) ⟹ γ = 2√(μ0 C4);  F_phys = g0·F,
# g0 = γ/2 = √(μ0 C4).
gamma = 2.0 * math.sqrt(MU0 * C4_SI)
g0    = math.sqrt(MU0 * C4_SI)
print(f"\nγ = 2√(μ0 C4) = {gamma:.6e};  g0 = √(μ0 C4) = {g0:.6e}")

# --- Charge of the w-quantum ----------------------------------------
# D = ∂ − iA = ∂ − i(A_phys/γ);  SI coupling D = ∂ − i(q/ℏ)A_phys
#   ⟹ q_w = ℏ/γ = ℏ/(2√(μ0 C4)) = ℏ/(2√(2 μ0 ℏ c))
q_w  = HBAR / gamma
q_w2 = q_w * q_w
print(f"q_w = ℏ/γ = {q_w:.6e}  (units m² — charge-as-area)")
print(f"q_w² = {q_w2:.6e} m⁴")
print(f"q_w² / (ℏ ε0 c / 8) = {q_w2/(HBAR*EPS0*C/8):.15f}   (analytic = 1)")
print(f"q_w² / (π l0⁴ / 4)  = {q_w2/(np.pi*l0**4/4):.15f}   (analytic = 1)")

# --- α of the two routes ---------------------------------------------
alpha_w    = q_w2 / (4 * np.pi * EPS0 * HBAR * C)
e_geom     = np.pi * (l0 / 2) ** 2
alpha_geom = e_geom**2 / (4 * np.pi * EPS0 * HBAR * C)
print(f"\nα_w    = q_w²/(4πε0ℏc) = {alpha_w:.8f} = 1/{1/alpha_w:.4f}")
print(f"          analytically 1/(32π) = {1/(32*np.pi):.8f} "
      f"(ratio {alpha_w*32*np.pi:.15f})")
print(f"α_geom = e²/(4πε0ℏc)   = {alpha_geom:.8f} = 1/{1/alpha_geom:.4f} "
      f"(= 1/128: {alpha_geom*128:.15f})")
print(f"α_w / α_geom = {alpha_w/alpha_geom:.10f};  4/π = {4/np.pi:.10f}")
print(f"q_w² / (e·l0²) = {q_w2/(e_geom*l0**2):.15f}   (analytic = 1: "
      "q_w = geometric mean of defect area and cell area)")

# effective radius if q_w is a disk area
r_q = math.sqrt(q_w / np.pi)
print(f"r_q = √(q_w/π) = {r_q/l0:.4f} l0   (compare: r_v = 0.498 l0)")

print("""
SUMMARY OF PART A:
  1) The energy normalization is UNIQUE and free:
     g0 = √(μ0 C4); at C4 = 2ℏc (canonical c4=1 in the code convention)
     the Skyrme term is IDENTICALLY equal to the Maxwell (1/4μ0)F_phys².
  2) Dynamical charge (w-quantum, CP¹): q_w² = ℏε0c/8 = (π/4)·l0⁴.
     STRUCTURAL MATCH with the geometric route: charge² ∝ l0⁴,
     i.e. charge = area, Hyperbola II is reproduced dynamically.
  3) α_w = 1/(32π) ≈ 1/100.5 — EXACT and universal (independent of
     the medium: ℏ and Z0 cancel). α_geom = 1/128.
     Gap: α_w/α_geom = 4/π ≈ 1.273 — an OPEN coefficient.
  4) The identity q_w² = e·l0² is exact (an observation, not a derivation).
  5) The formula g0 = √(2c2/(μ0 c4)) from derivation.md is DIMENSIONALLY
     inconsistent with the energy normalization (it mixes rescaling of the
     field and of the current) — to be replaced by g0 = √(μ0 C4),
     q_w = ℏ/(2√(μ0 C4)).
""")

# ============================================================
# PART B: Leibniz identity on the canonical 3D hopfion
# ============================================================
print("=" * 72)
print("PART B. Canonical hopfion: identity ∂F = j in full 3D")
print("=" * 72)

# Canonical NM optimum (result.json)
R_R, R_Z, W = 0.6408160149362525, 0.8072875518184682, 0.7019955806536682
M0C2_keV = 0.42950679467240735
E_OF_2D = 221.88762383285322 / M0C2_keV     # sim units
E_SK_2D = 220.6336421747573 / M0C2_keV
print(f"Canonical 2D (sim): E_OF = {E_OF_2D:.3f}, E_Sk = {E_SK_2D:.3f}")

N   = 256          # points per side
LBOX = 8.0         # box [-L, L]^3 (l0)
dev = 'cuda' if HAS_TORCH else 'cpu'
if not HAS_TORCH:
    import torch
dtype = torch.float64
print(f"Grid {N}³, box ±{LBOX} l0, dx = {2*LBOX/N:.4f} l0, "
      f"device = {dev}, float64")

ax = torch.linspace(-LBOX, LBOX, N, dtype=dtype, device=dev)
dx = float(ax[1] - ax[0])
X = ax.view(N, 1, 1)
Y = ax.view(1, N, 1)
Z = ax.view(1, 1, N)

# --- Ansatz (hopf_variational from nm_minimization.py), frame rule ----
rho2 = X * X + Y * Y
r_ = torch.sqrt(rho2) / R_R          # r = ρ/R_r
z_ = Z / R_Z
Yv = r_ * r_ + z_ * z_ - 1.0
Dv = (2.0 * z_) ** 2 + Yv * Yv
w2 = W * W
P  = (Dv + 4.0 * r_ * r_ * w2).clamp(min=1e-30)
n3 = (Dv - 4.0 * r_ * r_ * w2) / P
# n1 = 8 r z w / P, n2 = -4 r Y w / P  in the (r̂, φ̂, ẑ) basis;
# smooth Cartesian assembly: n1/ρ, n2/ρ are finite on the axis
n1_over_rho = 8.0 * z_ * W / (P * R_R)
n2_over_rho = -4.0 * Yv * W / (P * R_R)
nx = X * n1_over_rho - Y * n2_over_rho
ny = Y * n1_over_rho + X * n2_over_rho
nz = n3
del rho2, r_, z_, Yv, Dv, P, n3, n1_over_rho, n2_over_rho

norm = torch.sqrt(nx * nx + ny * ny + nz * nz)
print(f"|n|: max|.|-1| = {(norm-1).abs().max().item():.2e} (ansatz exactly unit)")
del norm

n = torch.stack([nx, ny, nz])        # (3, N, N, N)
del nx, ny, nz

# --- Derivatives: 4th order, interior --------------------------------
def d_axis(f, axis):
    """4th-order central; edges (2 points each) — 2nd order / copy."""
    g = torch.zeros_like(f)
    sl = [slice(None)] * f.dim()
    def s(a, b):
        t = list(sl); t[axis] = slice(a, b if b != 0 else None); return tuple(t)
    g[s(2, -2)] = (-f[s(4, 0)] + 8 * f[s(3, -1)] - 8 * f[s(1, -3)] + f[s(0, -4)]) / (12 * dx)
    return g

M = 4  # margin for norms/integrals (trim stencil edges)
def inner(f):
    return f[..., M:-M, M:-M, M:-M]

# first derivatives dn[i][c] = ∂_i n_c
dn = [torch.stack([d_axis(n[c], i) for c in range(3)]) for i in range(3)]

def cross(a, b):
    return torch.stack([a[1] * b[2] - a[2] * b[1],
                        a[2] * b[0] - a[0] * b[2],
                        a[0] * b[1] - a[1] * b[0]])

def dot3(a, b):
    return (a * b).sum(dim=0)

# --- F_ij ------------------------------------------------------------
F = {}
for (i, j) in [(0, 1), (1, 2), (2, 0)]:
    F[(i, j)] = dot3(n, cross(dn[i], dn[j]))
def Fij(i, j):
    if i == j:
        return None
    if (i, j) in F:
        return F[(i, j)]
    return -F[(j, i)]

# --- E_Sk, E_OF in 3D ------------------------------------------------
dV = dx ** 3
c4_code = 1.0
e_sk = (F[(0, 1)] ** 2 + F[(1, 2)] ** 2 + F[(2, 0)] ** 2)
E_SK_3D = c4_code * inner(e_sk).sum().item() * dV
del e_sk

K1, K2, K3 = 2.0, 2.0, 14.56
div_n = dn[0][0] + dn[1][1] + dn[2][2]
curl = torch.stack([dn[1][2] - dn[2][1],
                    dn[2][0] - dn[0][2],
                    dn[0][1] - dn[1][0]])
twist = dot3(n, curl)
bend2 = dot3(curl, curl) - twist ** 2
e_of = 0.5 * (K1 * div_n ** 2 + K2 * twist ** 2 + K3 * bend2)
E_OF_3D = inner(e_of).sum().item() * dV
del e_of, div_n, curl, twist, bend2

print(f"\nE_Sk(3D) = {E_SK_3D:9.3f}   vs 2D canon {E_SK_2D:9.3f}   "
      f"Δ = {100*(E_SK_3D/E_SK_2D-1):+.3f}%")
print(f"E_OF(3D) = {E_OF_3D:9.3f}   vs 2D canon {E_OF_2D:9.3f}   "
      f"Δ = {100*(E_OF_3D/E_OF_2D-1):+.3f}%")
print("(small Δ: finite box ±8 l0 vs 17×33 + grid interpolation)")

# --- Identity: LHS_j = Σ_i ∂_i F_ij;  RHS_j = term1_j + term2_j ------
lap_n = torch.stack([sum(d_axis(d_axis(n[c], i), i) for i in range(3))
                     for c in range(3)])
# Laplacian accuracy: applying the 1st derivative (4th order) twice is
# effectively 4th order with a wider stencil; consistent with LHS/term2,
# since the same d_axis operators are used everywhere.

res_num2 = 0.0
rhs_num2 = 0.0
t1_num2 = 0.0
t2_num2 = 0.0
for j in range(3):
    LHS_j = sum(d_axis(Fij(i, j), i) for i in range(3) if i != j)
    dnj = dn[j]
    term1_j = dot3(n, cross(lap_n, dnj))
    term2_j = torch.zeros_like(term1_j)
    for i in range(3):
        d2_ij = torch.stack([d_axis(dn[i][c], j) for c in range(3)])
        term2_j += dot3(n, cross(dn[i], d2_ij))
        del d2_ij
    RHS_j = term1_j + term2_j
    res = inner(LHS_j - RHS_j)
    res_num2 += (res ** 2).sum().item()
    rhs_num2 += (inner(RHS_j) ** 2).sum().item()
    t1_num2 += (inner(term1_j) ** 2).sum().item()
    t2_num2 += (inner(term2_j) ** 2).sum().item()
    del LHS_j, term1_j, term2_j, RHS_j, res

resid = math.sqrt(res_num2 / rhs_num2)
print(f"\nIDENTITY ∂_iF_ij = j_j on the canonical 3D hopfion:")
print(f"  ‖LHS − RHS‖ / ‖RHS‖ = {100*resid:.4f}%")
print(f"  ‖term1‖ / ‖term2‖   = {math.sqrt(t1_num2/t2_num2):.4f}")
print(f"  (term1 ≠ 0: the ansatz is NOT a harmonic map — Skyrme + "
      f"anisotropy K3/K1 tilt □n away from n; cf. §8 of the paper)")

print("\nDONE.")
