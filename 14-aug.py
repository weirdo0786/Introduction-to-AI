import math
import matplotlib.pyplot as plt

A = 1 / (10 ** 13)
Ea = 75000
R = 8.314

T_values = []
K_values = []

# 20 temperature points from 300 K to 1000 K
for i in range(20):
    T = 300 + i * (1000 - 300) / 19

    # Arrhenius equation
    K = A * math.exp(-Ea / (R * T))

    T_values.append(T)
    K_values.append(K)

# Print values
for T, K in zip(T_values, K_values):
    print(f"T = {T:.2f} K, K = {K:.4e}")

# Plot K vs T
plt.plot(T_values, K_values, marker='o')

plt.xlabel("Temperature (K)")
plt.ylabel("K")
plt.title("Arrhenius Equation: K vs Temperature")
plt.grid(True)

plt.show()


