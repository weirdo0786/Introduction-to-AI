import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Input parameters
# -----------------------------
rho = float(input("Enter fluid density (kg/m^3): "))
g = 9.81

h = float(input("Enter pressure head / height difference h (m): "))

P = rho * g * h

print("\nHydrostatic Pressure")
print("--------------------")
print(f"Density (rho) = {rho} kg/m^3")
print(f"Height (h)    = {h} m")
print(f"Pressure      = {P:.2f} Pa")
print(f"Pressure      = {P/1000:.2f} kPa")


# =====================================================
# GENERALIZED CASE FOR INCLINED PIPE
# =====================================================

P0 = float(input("\nEnter reference pressure P0 (Pa): "))
z0 = float(input("Enter reference elevation z0 (m): "))

L = float(input("Enter inclined pipe length (m): "))
theta = float(input("Enter inclination angle theta (degrees): "))

# Distance along the inclined pipe
s = np.linspace(0, L, 100)

# Convert angle to radians
theta_rad = np.radians(theta)

# Vertical elevation
z = z0 + s * np.sin(theta_rad)

# Height difference from reference point
h_z = z - z0

# Hydrostatic pressure:
# P = P0 - rho*g*h
P_z = P0 - rho * g * h_z

# Convert to kPa
P_z_kPa = P_z / 1000


# -----------------------------
# Print pressure distribution
# -----------------------------
print("\nPressure distribution:")
print("---------------------")

for i in range(0, len(z), 10):
    print(
        f"z = {z[i]:.3f} m, "
        f"h = {h_z[i]:.3f} m, "
        f"P = {P_z[i]:.3f} Pa"
    )


# -----------------------------
# Plot Pressure vs z
# -----------------------------
plt.figure(figsize=(8, 5))

plt.plot(z, P_z_kPa, linewidth=2)

plt.xlabel("Vertical elevation, z (m)")
plt.ylabel("Pressure, P (kPa)")
plt.title("Pressure Distribution in an Inclined Pipe")

plt.grid(True)
plt.show()