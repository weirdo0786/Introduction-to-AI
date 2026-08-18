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

    K = A * math.exp(-Ea / (R * T))

    T_values.append(T)
    K_values.append(K)

# Calculate -1/T and ln(K)
minus_1_T = []
ln_K = []

for T, K in zip(T_values, K_values):
    minus_1_T.append(-1 / T)
    ln_K.append(math.log(K))

# Plot ln(K) vs -1/T
plt.plot(minus_1_T, ln_K, marker='o')

plt.xlabel("-1/T (K⁻¹)")
plt.ylabel("ln(K)")
plt.title("Arrhenius Plot")
plt.grid(True)

plt.show()