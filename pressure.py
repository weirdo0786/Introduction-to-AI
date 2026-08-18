import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Input parameters
# -----------------------------
rho = float(input("Enter fluid density (kg/m^3): "))
g = 9.81

P0 = float(input("Enter reference pressure P0 (Pa): "))
z0 = float(input("Enter reference elevation z0 (m): "))

L = float(input("Enter inclined pipe length (m): "))
theta = float(input("Enter inclination angle theta (degrees): "))

# -----------------------------
# Generate distance along pipe
# -----------------------------
s = np.linspace(0, L, 100)

# Convert angle from degrees to radians
theta_rad = np.radians(theta)

# Vertical elevation
z = z0 + s * np.sin(theta_rad)

# -----------------------------
# Pressure distribution
# P(z) = P0 - rho*g*(z-z0)
# -----------------------------
P = P0 - rho * g * (z - z0)

# Convert pressure to kPa
P_kPa = P / 1000

# -----------------------------
# Display values
# -----------------------------
print("\nPressure distribution:")
for i in range(0, len(z), 10):
    print(f"z = {z[i]:.3f} m, P = {P[i]:.3f} Pa")

# -----------------------------
# Plot P versus z
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(z, P_kPa, linewidth=2)

plt.xlabel("Vertical elevation, z (m)")
plt.ylabel("Pressure, P (kPa)")
plt.title("Pressure Distribution in an Inclined Pipe")
plt.grid(True)

plt.show()