#!/usr/bin/env python3
"""
hopfion_visualize.py — approximate visualization of the canonical electron
hopfion using its closed-form Hopf ansatz. Pure numpy + matplotlib.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Canonical electron parameters (from NM optimization of the bare
# Cosserat functional with m^2 = 0 on the dyadic box L = 17 x 33,
# see ../electron_mass_minimization/)
R_R = 0.64082
R_Z = 0.80729
W   = 0.70200


def hopf_field(rr, zz, R_r=R_R, R_z=R_Z, w=W):
    """Three-parameter Hopf ansatz, returns (n1, n2, n3) on (rr, zz) grid."""
    r = rr / R_r
    z = zz / R_z
    Y = r * r + z * z - 1.0
    D = (2.0 * z)**2 + Y * Y
    w2 = w * w
    P = D + 4.0 * r * r * w2
    P = np.maximum(P, 1e-30)
    n3 = (D - 4.0 * r * r * w2) / P
    n1 = 8.0 * r * z * w / P
    n2 = -4.0 * r * Y * w / P
    # Normalize (safety; should already be on S^2)
    norm = np.sqrt(n1*n1 + n2*n2 + n3*n3)
    norm = np.maximum(norm, 1e-30)
    return n1 / norm, n2 / norm, n3 / norm


def hopf_charge_density(n1, n2, n3, dr, dz):
    """rho_Q = n . (dn/dr x dn/dz)."""
    n1_r = np.gradient(n1, dr, axis=0)
    n2_r = np.gradient(n2, dr, axis=0)
    n3_r = np.gradient(n3, dr, axis=0)
    n1_z = np.gradient(n1, dz, axis=1)
    n2_z = np.gradient(n2, dz, axis=1)
    n3_z = np.gradient(n3, dz, axis=1)
    cx = n2_r * n3_z - n3_r * n2_z
    cy = n3_r * n1_z - n1_r * n3_z
    cz = n1_r * n2_z - n2_r * n1_z
    return n1 * cx + n2 * cy + n3 * cz


def make_2d_grid(L=2.5, N=400):
    r = np.linspace(0.001, L, N)
    z = np.linspace(-L, L, N)
    rr, zz = np.meshgrid(r, z, indexing='ij')
    dr = r[1] - r[0]
    dz = z[1] - z[0]
    return rr, zz, dr, dz


def panel_n3(ax, rr, zz, n3):
    im = ax.pcolormesh(zz, rr, n3, cmap='RdBu_r', vmin=-1, vmax=1, shading='auto')
    cs = ax.contour(zz, rr, n3, levels=[-0.5, 0.0, 0.5],
                    colors='black', linewidths=0.6, alpha=0.6)
    ax.clabel(cs, fontsize=7, fmt='%.1f')
    ax.set_xlabel(r'$z\ /\ \ell_0$')
    ax.set_ylabel(r'$r\ /\ \ell_0$')
    ax.set_title(r'$n_z(r, z)$  —  director $z$-component')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label=r'$n_z$', shrink=0.8)


def panel_nperp(ax, rr, zz, n1, n2):
    n_perp = np.sqrt(n1*n1 + n2*n2)
    im = ax.pcolormesh(zz, rr, n_perp, cmap='magma', vmin=0, vmax=1, shading='auto')
    # Locate vortex tube center: where n_perp is maximum at z=0
    iz0 = n_perp.shape[1] // 2
    r_v_idx = int(np.argmax(n_perp[:, iz0]))
    r_v = rr[r_v_idx, iz0]
    ax.axhline(r_v, color='cyan', ls='--', lw=0.8, alpha=0.6)
    ax.text(0.02, r_v + 0.05, f'  tube core $r_v \\approx {r_v:.2f}\\,\\ell_0$',
            color='cyan', fontsize=8, transform=ax.transData)
    ax.set_xlabel(r'$z\ /\ \ell_0$')
    ax.set_ylabel(r'$r\ /\ \ell_0$')
    ax.set_title(r'$|n_\perp(r, z)|$  —  vortex tube')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label=r'$|n_\perp|$', shrink=0.8)


def panel_charge_density(ax, rr, zz, rho_q):
    vmax = np.abs(rho_q).max()
    im = ax.pcolormesh(zz, rr, rho_q, cmap='seismic',
                       vmin=-vmax, vmax=vmax, shading='auto')
    ax.set_xlabel(r'$z\ /\ \ell_0$')
    ax.set_ylabel(r'$r\ /\ \ell_0$')
    ax.set_title(r'Hopf-charge density  $\rho_Q = n\cdot(\partial_r n \times \partial_z n)$')
    ax.set_aspect('equal')
    plt.colorbar(im, ax=ax, label=r'$\rho_Q$', shrink=0.8)


def _contour_paths(rr, zz, field, level):
    """Extract iso-contours at the given level as a list of (N, 2) arrays."""
    fig_tmp, ax_tmp = plt.subplots()
    cs = ax_tmp.contour(rr, zz, field, levels=[level])
    paths = [seg for seg in cs.allsegs[0]] if cs.allsegs else []
    plt.close(fig_tmp)
    return paths


def _revolve(r_path, z_path, n_theta=64, theta_max=2 * np.pi):
    """Revolve a planar (r, z) curve around the z-axis to a 3D surface.

    Set theta_max < 2*pi to cut the surface (e.g., theta_max=pi shows
    only the front half y > 0).
    """
    theta = np.linspace(0, theta_max, n_theta)
    R, T = np.meshgrid(r_path, theta, indexing='ij')
    Z, _ = np.meshgrid(z_path, theta, indexing='ij')
    X = R * np.cos(T)
    Y = R * np.sin(T)
    return X, Y, Z


def panel_3d_isosurfaces(ax, R_r=R_R, R_z=R_Z, w=W):
    """3D rendering of the canonical hopfion shape, with a small wedge cut out.

    Computes n_z(r, z) on a 2D grid from the analytic Hopf ansatz,
    extracts the iso-contour n_z = -0.5 (the "body" of the soliton),
    and revolves over theta in [0, 1.5*pi] -- this carves out a 90-degree
    pie-slice so the donut shape is clearly visible AND the inside (tube
    core) is exposed on the cut faces.
    """
    # Fine 2D grid in (r, z)
    L_r_local = 1.5
    L_z_local = 1.0
    N = 300
    r1d = np.linspace(0.005, L_r_local, N)
    z1d = np.linspace(-L_z_local, L_z_local, N)
    rr_local, zz_local = np.meshgrid(r1d, z1d, indexing='ij')

    n1, n2, n3 = hopf_field(rr_local, zz_local, R_r=R_r, R_z=R_z, w=w)

    # Cut a 90-degree wedge: revolve over 270 degrees only.
    theta_start = 0.0
    theta_end = 1.5 * np.pi  # 270 degrees -> a 90-degree wedge removed

    for seg in _contour_paths(rr_local, zz_local, n3, level=-0.5):
        if len(seg) < 6:
            continue
        seg_r = seg[:, 0]
        seg_z = seg[:, 1]

        # Outer surface (revolved 3/4 turn)
        theta = np.linspace(theta_start, theta_end, 96)
        R_grid, T_grid = np.meshgrid(seg_r, theta, indexing='ij')
        Z_grid, _ = np.meshgrid(seg_z, theta, indexing='ij')
        X = R_grid * np.cos(T_grid)
        Y = R_grid * np.sin(T_grid)
        ax.plot_surface(X, Y, Z_grid, color='tab:red', alpha=0.95,
                        linewidth=0, rstride=1, cstride=1,
                        antialiased=True, shade=True)

        # Two cut faces (at theta = theta_start and theta = theta_end):
        for theta_cut in (theta_start, theta_end):
            cx = seg_r * np.cos(theta_cut)
            cy = seg_r * np.sin(theta_cut)
            cz = seg_z
            ax.plot(cx, cy, cz, color='darkred', lw=1.5)

    # The vortex tube axis: a closed circle of radius R_r in the z=0 plane.
    # Draw the 3/4-arc that remains after the wedge cut.
    t_arc = np.linspace(theta_start, theta_end, 200)
    ax.plot(R_r * np.cos(t_arc), R_r * np.sin(t_arc), np.zeros_like(t_arc),
            color='black', lw=2.2)
    # Mark the two endpoints on the cut faces:
    for theta_cut in (theta_start, theta_end):
        ax.scatter([R_r * np.cos(theta_cut)], [R_r * np.sin(theta_cut)], [0],
                   color='black', s=55, zorder=10)

    ax.set_xlabel(r'$x\ /\ \ell_0$')
    ax.set_ylabel(r'$y\ /\ \ell_0$')
    ax.set_zlabel(r'$z\ /\ \ell_0$')
    ax.set_title(r'3D shape with a wedge cut: body (red) + tube axis (black)')
    lim = 1.0
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.view_init(elev=22, azim=35)
    ax.set_box_aspect((1, 1, 1))


def main():
    print(f"Canonical Hopf ansatz: R_r={R_R}, R_z={R_Z}, w={W}")
    rr, zz, dr, dz = make_2d_grid(L=2.5, N=400)
    n1, n2, n3 = hopf_field(rr, zz)
    rho_q = hopf_charge_density(n1, n2, n3, dr, dz)

    fig = plt.figure(figsize=(15, 10))

    ax1 = fig.add_subplot(2, 2, 1)
    panel_n3(ax1, rr, zz, n3)

    ax2 = fig.add_subplot(2, 2, 2)
    panel_nperp(ax2, rr, zz, n1, n2)

    ax3 = fig.add_subplot(2, 2, 3)
    panel_charge_density(ax3, rr, zz, rho_q)

    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    panel_3d_isosurfaces(ax4)

    fig.suptitle(
        rf'Canonical electron hopfion (approximate). '
        rf'$R_r={R_R}$, $R_z={R_Z}$, $w={W}$  —  $Q_H = -1$',
        fontsize=12, y=0.99,
    )
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    out = '/tmp/hopfion_visualize.png'
    plt.savefig(out, dpi=140, bbox_inches='tight')
    print(f'Saved: {out}')


if __name__ == '__main__':
    main()
