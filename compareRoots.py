"""
Experiment 5: Comparison of the methods
f(x) = e^(-x) - x
Initial values: a = 0, b = 1 (for Bisection, Regular Falsi, Secant)
Stopping Criteria <= 1 * 10^-5

Plots True percent relative error (log scale) vs Iterations
for Bisection, False Position, Secant, and Newton-Raphson.
"""

import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Function and its derivative:  f(x) = e^(-x) - x
# ---------------------------------------------------------
def f(x):
    return math.exp(-x) - x

def df(x):
    return -math.exp(-x) - 1

# The "true" root (known to high precision), used to compute TRUE percent
# relative error, exactly like the textbook/slide plot.
TRUE_ROOT = 0.5671432904097838
TOLERANCE = 1e-5   # Stopping criteria <= 1 * 10^-5


def true_error(x):
    return abs((TRUE_ROOT - x) / TRUE_ROOT) * 100


# ---------------------------------------------------------
# 1. Bisection Method
# ---------------------------------------------------------
def bisection(a, b, tol=TOLERANCE, max_iter=20):
    fa = f(a)
    fb = f(b)
    errors = []

    if fa * fb > 0:
        raise ValueError("Root does not lie between a and b.")

    iteration = 1
    x = (a + b) / 2
    while true_error(x) >= tol and iteration <= max_iter:
        x = (a + b) / 2
        fx = f(x)
        errors.append(true_error(x))

        if fa * fx < 0:
            b = x
            fb = fx
        elif fx * fb < 0:
            a = x
            fa = fx
        else:
            break
        iteration += 1

    return errors


# ---------------------------------------------------------
# 2. False Position (Regula Falsi) Method
# ---------------------------------------------------------
def false_position(a, b, tol=TOLERANCE, max_iter=20):
    fa = f(a)
    fb = f(b)
    errors = []

    if fa * fb > 0:
        raise ValueError("Root does not lie between a and b.")

    iteration = 1
    while iteration <= max_iter:
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        errors.append(true_error(x))

        if true_error(x) < tol:
            break

        if fa * fx < 0:
            b = x
            fb = fx
        elif fx * fb < 0:
            a = x
            fa = fx
        else:
            break
        iteration += 1

    return errors


# ---------------------------------------------------------
# 3. Newton-Raphson Method
# ---------------------------------------------------------
def newton_raphson(x0, tol=TOLERANCE, max_iter=20):
    x = x0
    errors = []
    iteration = 1

    while iteration <= max_iter:
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        errors.append(true_error(x_new))

        if true_error(x_new) < tol:
            x = x_new
            break

        x = x_new
        iteration += 1

    return errors


# ---------------------------------------------------------
# 4. Secant Method
# ---------------------------------------------------------
def secant(x0, x1, tol=TOLERANCE, max_iter=20):
    errors = []
    iteration = 1

    while iteration <= max_iter:
        f0 = f(x0)
        f1 = f(x1)
        x_new = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        errors.append(true_error(x_new))

        if true_error(x_new) < tol:
            break

        x0 = x1
        x1 = x_new
        iteration += 1

    return errors


# ---------------------------------------------------------
# Run all methods with the given initial values
# Initial values: a = 0, b = 1 (Bisection, False Position, Secant)
# Newton-Raphson needs a single starting guess -> using x0 = 1 (same as b)
# ---------------------------------------------------------
bisection_errors      = bisection(0, 1)
false_position_errors = false_position(0, 1)
secant_errors         = secant(0, 1)
newton_errors         = newton_raphson(1)

print("Bisection iterations:", len(bisection_errors))
print("False position iterations:", len(false_position_errors))
print("Secant iterations:", len(secant_errors))
print("Newton-Raphson iterations:", len(newton_errors))

# ---------------------------------------------------------
# Plot (matches the style of the slide)
# ---------------------------------------------------------
plt.figure(figsize=(8, 6))

plt.semilogy(range(1, len(newton_errors) + 1), newton_errors,
             'k-', linewidth=2)
plt.semilogy(range(1, len(secant_errors) + 1), secant_errors,
             'k-', linewidth=2)
plt.semilogy(range(1, len(false_position_errors) + 1), false_position_errors,
             'k-', linewidth=2)
plt.semilogy(range(1, len(bisection_errors) + 1), bisection_errors,
             'k-', linewidth=2)

plt.xlabel("Iterations")
plt.ylabel("True percent relative error")
plt.title("Comparison of root-finding methods for f(x) = e^(-x) - x")
plt.ylim(1e-6, 20)
plt.xlim(0, 20)
plt.grid(True, which="both", linestyle="--", alpha=0.4)


def label_curve(errors, text, target_y=0.05, rotation=-70, ha="left", dx=0.15):
    """Place label near the point on the curve closest to target_y (in log space),
    so labels land inside the plot area instead of overlapping the title."""
    target_log = math.log10(target_y)
    best_idx = min(range(len(errors)), key=lambda i: abs(math.log10(errors[i]) - target_log))
    x_pos = best_idx + 1
    y_pos = errors[best_idx]
    x_text = x_pos + dx if ha == "left" else x_pos - dx
    plt.text(x_text, y_pos, text, rotation=rotation, va="center", ha=ha, fontsize=9)

label_curve(newton_errors, "Newton-Raphson", target_y=0.03, ha="right", dx=0.1)
label_curve(secant_errors, "Secant", target_y=0.005, ha="left", dx=0.2)
label_curve(false_position_errors, "False position", target_y=0.3)
label_curve(bisection_errors, "Bisection", target_y=0.003)

plt.tight_layout()
plt.savefig("root_methods_comparison.png", dpi=150)
plt.show()termi