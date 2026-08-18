import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# AUTOMATIC PRESSURE CALCULATION
# ==========================================

# Inputs
rho = float(input("Enter fluid density (kg/m^3): "))
P0 = float(input("Enter reference pressure P0 (Pa): "))
z0 = float(input("Enter reference elevation z0 (m): "))
L = float(input("Enter pipe length (m): "))
theta = float(input("Enter inclination angle (degrees): "))

g = 9.81

# ------------------------------------------
# Distance along inclined pipe
# ------------------------------------------
s = np.linspace(0, L, 100)

# Convert angle to radians
theta_rad = np.radians(theta)

# ------------------------------------------
# Automatically calculate elevation z
# z = z0 + s sin(theta)
# ------------------------------------------
z = z0 + s * np.sin(theta_rad)

# ------------------------------------------
# Automatically calculate height difference
# h = z - z0
# ------------------------------------------
h = z - z0

# ------------------------------------------
# Pressure change
# ΔP = rho * g * h
# ------------------------------------------
delta_P = rho * g * h

# ------------------------------------------
# Pressure at every point
# P = P0 - rho*g*h
# ------------------------------------------
P = P0 - delta_P

# Convert to kPa
P_kPa = P / 1000


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n==========================================")
print("       AUTOMATIC PRESSURE CALCULATION")
print("==========================================")

print(f"Fluid density       = {rho:.2f} kg/m^3")
print(f"Reference pressure  = {P0:.2f} Pa")
print(f"Reference elevation = {z0:.2f} m")
print(f"Pipe length         = {L:.2f} m")
print(f"Inclination angle   = {theta:.2f}°")

print("\n------------------------------------------")
print("Calculated Values")
print("------------------------------------------")

print(f"Final elevation z   = {z[-1]:.3f} m")
print(f"Height difference h = {h[-1]:.3f} m")
print(f"Pressure change     = {delta_P[-1]:.2f} Pa")
print(f"Final pressure      = {P[-1]:.2f} Pa")
print(f"Final pressure      = {P_kPa[-1]:.2f} kPa")


# ==========================================
# PLOT PRESSURE VS ELEVATION
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(z, P_kPa, linewidth=2)

plt.xlabel("Elevation, z (m)")
plt.ylabel("Pressure, P (kPa)")
plt.title("Pressure Distribution in an Inclined Pipe")

plt.grid(True)
plt.show()