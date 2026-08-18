import math
from scipy.stats import norm

# Given values
# mu = 500          # Population mean
# sigma = 20        # Population standard deviation
# n = 36            # Sample size
# x_bar = 506       # Sample mean
# alpha = 0.05      # Significance level

mu = 3.5
sigma = 0.8
n = 49
x_bar = 3.2
alpha = 0.05

# Calculate Z-statistic
z = (x_bar - mu) / (sigma / math.sqrt(n))

# Critical value for two-tailed test
z_critical = norm.ppf(1 - alpha / 2)

# Calculate p-value
p_value = 2 * (1 - norm.cdf(abs(z)))

# Display results
print("Z-test for Population Mean")
print("--------------------------")
print(f"Population Mean (μ)       = {mu} MPa")
print(f"Population Std. Dev. (σ)  = {sigma} MPa")
print(f"Sample Size (n)            = {n}")
print(f"Sample Mean (x̄)           = {x_bar} MPa")
print(f"Significance Level (α)     = {alpha}")

print(f"\nZ-statistic                = {z:.2f}")
print(f"Critical Z-value           = ±{z_critical:.2f}")
print(f"P-value                    = {p_value:.4f}")

# Decision
if abs(z) > z_critical:
    print("\nDecision: Reject H0")
    print("Conclusion: The mean tensile strength is significantly different from 500 MPa.")
else:
    print("\nDecision: Fail to Reject H0")
    print("Conclusion: There is insufficient evidence that the mean tensile strength")
    print("is different from 500 MPa.")