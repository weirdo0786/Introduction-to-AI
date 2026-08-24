"""
Vapour-Liquid Dome Using van der Waals Equation
with Maxwell Equal-Area Construction

Reduced van der Waals EOS:

    P_r = 8*T_r / (3*v_r - 1) - 3/v_r^2

Maxwell equal-area condition:

    P_sat * (v_g - v_f)
        = integral(P_vdW dv) from v_f to v_g

The code:
1. Finds the spinodal points.
2. Finds the saturation pressure using Maxwell's rule.
3. Finds saturated liquid and vapour volumes.
4. Repeats this for many temperatures.
5. Plots the vapour-liquid dome.
"""

import os

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq


# ============================================================
# 1. REDUCED VAN DER WAALS EQUATION
# ============================================================

def P_r(v_r, T_r):
    """
    Reduced van der Waals pressure.

    P_r = 8*T_r/(3*v_r - 1) - 3/v_r^2
    """
    return (
        8.0 * T_r / (3.0 * v_r - 1.0)
        - 3.0 / v_r**2
    )


# ============================================================
# 2. INTEGRAL OF THE VAN DER WAALS EQUATION
# ============================================================

def integral_P(v, T_r):
    """
    Antiderivative of P_r with respect to v_r.

    Integral(P_r dv_r)
        = (8*T_r/3)*ln(3*v_r - 1) + 3/v_r
    """

    return (
        (8.0 * T_r / 3.0)
        * np.log(3.0 * v - 1.0)
        + 3.0 / v
    )


# ============================================================
# 3. SPINODAL POINTS
# ============================================================

def spinodal(T_r):
    """
    Find the two spinodal volumes.

    Spinodal points occur where:

        dP_r/dv_r = 0

    For the reduced van der Waals EOS:

        dP_r/dv_r =
            -24*T_r/(3*v_r - 1)^2
            + 6/v_r^3
    """

    if T_r >= 1.0:
        return None

    def dPdv(v):
        return (
            -24.0 * T_r / (3.0 * v - 1.0)**2
            + 6.0 / v**3
        )

    # Left spinodal point
    v_lo = brentq(
        dPdv,
        1.0 / 3.0 + 1e-10,
        1.0
    )

    # Right spinodal point
    v_hi = brentq(
        dPdv,
        1.0,
        100.0
    )

    return v_lo, v_hi


# ============================================================
# 4. MAXWELL EQUAL-AREA CONSTRUCTION
# ============================================================

def maxwell(T_r):
    """
    Find:

        P_sat
        v_f  = saturated liquid volume
        v_g  = saturated vapour volume

    at a specified subcritical temperature T_r.

    Conditions:

        P(v_f) = P_sat

        P(v_g) = P_sat

        Integral(P dv, vf -> vg)
            = P_sat * (vg - vf)
    """

    # Maxwell construction only applies below the
    # critical temperature.
    if T_r >= 1.0:
        return None

    # --------------------------------------------------------
    # Step 1: Find spinodal points
    # --------------------------------------------------------

    v_lo, v_hi = spinodal(T_r)

    # Pressures at the spinodal points
    P_lo = P_r(v_lo, T_r)
    P_hi = P_r(v_hi, T_r)

    # --------------------------------------------------------
    # Step 2: Establish pressure bracket
    # --------------------------------------------------------

    # Saturation pressure must be positive.
    P_bottom = max(P_lo, 1e-8)

    # Stay slightly below the upper spinodal pressure.
    P_top = P_hi - 1e-12

    if P_bottom >= P_top:
        return None

    # --------------------------------------------------------
    # Step 3: For a trial pressure, find vf and vg
    # --------------------------------------------------------

    def find_roots(P_s):
        """
        Find the liquid and vapour roots for a given
        trial saturation pressure P_s.
        """

        # -------------------------
        # Liquid root
        # -------------------------

        vf = brentq(
            lambda v: P_r(v, T_r) - P_s,
            1.0 / 3.0 + 1e-10,
            v_lo
        )

        # -------------------------
        # Vapour root
        # -------------------------

        # Start with an upper volume.
        upper = max(2.0 * v_hi, 2.0)

        # Increase upper limit until the function
        # changes sign.
        while P_r(upper, T_r) - P_s > 0.0:

            upper *= 2.0

            if upper > 1e12:
                raise RuntimeError(
                    "Could not bracket vapour root."
                )

        vg = brentq(
            lambda v: P_r(v, T_r) - P_s,
            v_hi,
            upper
        )

        return vf, vg

    # --------------------------------------------------------
    # Step 4: Maxwell area residual
    # --------------------------------------------------------

    def area_residual(P_s):

        vf, vg = find_roots(P_s)

        # Integral of P_vdW from vf to vg
        integral_area = (
            integral_P(vg, T_r)
            - integral_P(vf, T_r)
        )

        # Area of rectangle under Psat
        rectangle_area = P_s * (vg - vf)

        # Maxwell condition:
        #
        # integral_area - rectangle_area = 0
        #
        return integral_area - rectangle_area

    # --------------------------------------------------------
    # Step 5: Find Psat
    # --------------------------------------------------------

    P_sat = brentq(
        area_residual,
        P_bottom,
        P_top,
        xtol=1e-12,
        rtol=1e-12
    )

    # --------------------------------------------------------
    # Step 6: Find final vf and vg using correct Psat
    # --------------------------------------------------------

    v_f, v_g = find_roots(P_sat)

    return P_sat, v_f, v_g


# ============================================================
# 5. BUILD THE COMPLETE VAPOUR-LIQUID DOME
# ============================================================

def build_dome(
    n=400,
    T_min=0.60
):
    """
    Calculate saturated liquid and saturated vapour
    curves for many reduced temperatures.
    """

    # Temperatures from T_min to just below the critical point
    T_values = np.linspace(
        T_min,
        0.99995,
        n
    )

    # Lists for storing results
    vf_all = []
    vg_all = []
    P_all = []

    # --------------------------------------------------------
    # Calculate Maxwell construction for every temperature
    # --------------------------------------------------------

    for T_r in T_values:

        try:

            result = maxwell(T_r)

            if result is None:
                continue

            P_sat, v_f, v_g = result

            # Basic validity check
            if (
                P_sat <= 0
                or v_f <= 1.0 / 3.0
                or v_f >= v_g
            ):
                continue

            vf_all.append(v_f)
            vg_all.append(v_g)
            P_all.append(P_sat)

        except Exception as error:

            print(
                f"Warning: calculation failed "
                f"at T_r = {T_r:.5f}: {error}"
            )

    # --------------------------------------------------------
    # Add exact critical point
    # --------------------------------------------------------

    vf_all.append(1.0)
    vg_all.append(1.0)
    P_all.append(1.0)

    return (
        np.array(vf_all),
        np.array(vg_all),
        np.array(P_all)
    )


# ============================================================
# 6. MAIN PLOTTING FUNCTION
# ============================================================

def main():

    # --------------------------------------------------------
    # Create figure
    # --------------------------------------------------------

    fig, ax = plt.subplots(
        figsize=(11, 7.5)
    )

    # --------------------------------------------------------
    # Temperatures for van der Waals isotherms
    # --------------------------------------------------------

    T_isotherms = [
        0.75,
        0.85,
        0.95,
        1.00,
        1.10
    ]

    # Different dashed patterns
    dash_styles = [
        (0, (4, 2)),
        (0, (6, 2, 1, 2)),
        (0, (2, 2)),
        (0, (5, 2)),
        (0, (1, 1.6))
    ]

    # Volume range
    v_grid = np.linspace(
        0.3401,
        8.0,
        4000
    )

    # --------------------------------------------------------
    # Plot van der Waals isotherms
    # --------------------------------------------------------

    for T_r, dash_style in zip(
        T_isotherms,
        dash_styles
    ):

        ax.plot(
            v_grid,
            P_r(v_grid, T_r),
            linestyle=dash_style,
            color='0.35',
            linewidth=1.0,
            label=fr'$T_r$ = {T_r:.2f}',
            zorder=2
        )

    # --------------------------------------------------------
    # Calculate vapour-liquid dome
    # --------------------------------------------------------

    vf, vg, Ps = build_dome(
        n=400,
        T_min=0.60
    )

    # --------------------------------------------------------
    # Plot saturated liquid line
    # --------------------------------------------------------

    ax.plot(
        vf,
        Ps,
        color='#1f6fb4',
        linewidth=2.4,
        label='Saturated liquid line',
        zorder=4
    )

    # --------------------------------------------------------
    # Plot saturated vapour line
    # --------------------------------------------------------

    ax.plot(
        vg,
        Ps,
        color='#d9622b',
        linewidth=2.4,
        label='Saturated vapour line',
        zorder=4
    )

    # --------------------------------------------------------
    # Shade two-phase region
    # --------------------------------------------------------

    v_fill = np.concatenate([
        vf,
        vg[::-1]
    ])

    P_fill = np.concatenate([
        Ps,
        Ps[::-1]
    ])

    ax.fill(
        v_fill,
        P_fill,
        color='#c9a227',
        alpha=0.13,
        label='Liquid + Vapour region',
        zorder=1
    )

    # --------------------------------------------------------
    # Critical point
    # --------------------------------------------------------

    ax.plot(
        1.0,
        1.0,
        'o',
        color='#e07b39',
        markersize=10,
        markeredgecolor='white',
        markeredgewidth=1.2,
        label='Critical point',
        zorder=6
    )

    ax.annotate(
        'Critical Point\n'
        r'$(P_r = 1,\ v_r = 1)$',
        xy=(1.0, 1.0),
        xytext=(1.30, 1.045),
        fontsize=10,
        color='0.25'
    )

    # --------------------------------------------------------
    # Axis limits
    # --------------------------------------------------------

    ax.set_xlim(
        0,
        8
    )

    ax.set_ylim(
        0,
        1.45
    )

    # --------------------------------------------------------
    # Axis labels
    # --------------------------------------------------------

    ax.set_xlabel(
        r'Reduced Volume, $v_r = v/v_c$',
        fontsize=12
    )

    ax.set_ylabel(
        r'Reduced Pressure, $P_r = P/P_c$',
        fontsize=12
    )

    # --------------------------------------------------------
    # Title
    # --------------------------------------------------------

    ax.set_title(
        'Vapour-Liquid Dome Using van der Waals Equation\n'
        'with Maxwell Equal-Area Construction',
        fontsize=13,
        color='0.2',
        pad=14
    )

    # --------------------------------------------------------
    # Reorder legend
    # --------------------------------------------------------

    handles, labels = (
        ax.get_legend_handles_labels()
    )

    dome_indices = [
        i for i, label in enumerate(labels)
        if not label.startswith('$T_r$')
    ]

    isotherm_indices = [
        i for i, label in enumerate(labels)
        if label.startswith('$T_r$')
    ]

    order = (
        dome_indices
        + isotherm_indices
    )

    ax.legend(
        [handles[i] for i in order],
        [labels[i] for i in order],
        loc='upper right',
        fontsize=8.5,
        frameon=False
    )

    # --------------------------------------------------------
    # Remove top and right borders
    # --------------------------------------------------------

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.tick_params(
        labelsize=10,
        colors='0.3'
    )

    # --------------------------------------------------------
    # Improve layout
    # --------------------------------------------------------

    fig.tight_layout()

    # --------------------------------------------------------
    # Save figure
    # --------------------------------------------------------

    out_path = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'vdw_dome.png'
    )

    fig.savefig(
        out_path,
        dpi=200,
        bbox_inches='tight'
    )

    print(
        f"\nFigure saved to:\n{out_path}"
    )

    # ========================================================
    # 7. SANITY CHECK
    # ========================================================

    print(
        "\nMaxwell construction results:"
    )

    print(
        "-" * 55
    )

    print(
        f"{'T_r':>8}"
        f"{'P_sat':>12}"
        f"{'v_f':>12}"
        f"{'v_g':>12}"
    )

    print(
        "-" * 55
    )

    for T_r in [
        0.75,
        0.85,
        0.95
    ]:

        result = maxwell(T_r)

        if result is None:
            print(
                f"{T_r:8.2f}"
                "   Calculation failed"
            )
            continue

        P_sat, v_f, v_g = result

        print(
            f"{T_r:8.2f}"
            f"{P_sat:12.4f}"
            f"{v_f:12.4f}"
            f"{v_g:12.4f}"
        )

    print(
        "-" * 55
    )

    # --------------------------------------------------------
    # Display plot
    # --------------------------------------------------------

    plt.show()


# ============================================================
# 8. RUN PROGRAM
# ============================================================

if __name__ == "__main__":
    main()