import numpy as np


# code start for LU Decomposition
X = np.array([[1, 3],[2, 6]], dtype=float)
print("X:")
print(X)

U = X.copy()
L21 = U[1, 0] / U[0, 0]
U[1] = U[1] - L21 * U[0]
L = np.array([[1, 0],[L21, 1]], dtype=float)
print("\nL:")
print(L)
print("\nU:")
print(U)
print("\nCheck X = L @ U:")
print(np.allclose(X, L @ U))


# ============================================================
# LU DECOMPOSITION
# ============================================================
#
# We want:
#
# X = L @ U
#
# X =
# [[1, 3],
#  [2, 6]]
#
# ------------------------------------------------------------
# Step 1: Find U
# ------------------------------------------------------------
#
# First pivot = X[0][0] = 1
#
# Element below pivot = X[1][0] = 2
#
# Find L21:
#
# L21 = X[1][0] / X[0][0]
#     = 2 / 1
#     = 2
#
# Eliminate the element below the pivot:
#
# R2 = R2 - L21 * R1
#
# R2 = [2, 6] - 2[1, 3]
#    = [0, 0]
#
# Therefore:
#
# U =
# [[1, 3],
#  [0, 0]]



# ------------------------------------------------------------
# Step 2: Find L
# ------------------------------------------------------------
#
# Doolittle form:
#
# L =
# [[1,  0],
#  [L21, 1]]
#
# We already calculated:
#
# L21 = 2



# ------------------------------------------------------------
# Print L and U
# ------------------------------------------------------------
# ------------------------------------------------------------
# Check whether X = L @ U
# ------------------------------------------------------------



# Rank
print("\nRank of X:")
print(np.linalg.matrix_rank(X))




# For your matrix:
#
# A =
# [[4, 2, 0],
#  [0, 3, 2],
#  [0, 0, 2]]
#
# LU decomposition means finding:
#
# A = L @ U
#
# where:
# L = Lower Triangular Matrix
# U = Upper Triangular Matrix
#
# Since A is already an upper triangular matrix,
# the LU decomposition is simple:
#
# L =
# [[1, 0, 0],
#  [0, 1, 0],
#  [0, 0, 1]]
#
# U =
# [[4, 2, 0],
#  [0, 3, 2],
#  [0, 0, 2]]
#
# Therefore:
#
# A = L @ U
# NumPy does not have a direct LU decomposition function.
# We can use scipy.linalg.lu().
# First install SciPy if required:
# pip install scipy

# ============================================================

# LU DECOMPOSITION

# ============================================================

#

# LU decomposition means writing a matrix A as:

#

#                 A = L @ U

#

# L = Lower Triangular Matrix

# U = Upper Triangular Matrix

#

# In Doolittle LU decomposition:

# - The diagonal elements of L are 1.

# - The values below the diagonal of L are the elimination multipliers.

# - U is obtained after Gaussian elimination.

#

# ------------------------------------------------------------

# EXAMPLE

# ------------------------------------------------------------

#

# Let:

#

# A =

# [[1, 3],

#  [2, 6]]

#

# Step 1: Find U using Gaussian elimination.

#

# The first pivot is:

# a11 = 1

#

# The element below the pivot is:

# a21 = 2

#

# We want to make a21 = 0.
# To find the elimination multiplier:
# L21 = a21 / a11

#

# Therefore:

#

# L21 = 2 / 1

#     = 2

#

# So the row operation is:

#

# R2 = R2 - L21 * R1

# R2 = R2 - 2 * R1

#

# R2 = [2, 6] - 2[1, 3]

#    = [2, 6] - [2, 6]

#    = [0, 0]

#

# Therefore:

#

# U =

# [[1, 3],

#  [0, 0]]

#

# ------------------------------------------------------------

# Step 2: Find L

# ------------------------------------------------------------

#

# In Doolittle decomposition, L has 1 on its diagonal:

#

# L =

# [[1, 0],

#  [L21, 1]]

#

# We already calculated:

#

# L21 = 2

#

# Therefore:

#

# L =

# [[1, 0],

#  [2, 1]]

#

# ------------------------------------------------------------

# HOW TO CALCULATE VALUES OF L

# ------------------------------------------------------------

#

# The values of L come from the multipliers used during

# Gaussian elimination.

#

# For a general matrix, when eliminating A[i][j], calculate:

#

# L[i][j] = A[i][j] / U[j][j]

#

# Here:

# - A[i][j] is the value that we want to eliminate.

# - U[j][j] is the current pivot.

# - The result is stored in L[i][j].

#

# For our example:

#

# L21 = A21 / U11

#     = 2 / 1

#     = 2

#

# ------------------------------------------------------------

# FINAL ANSWER

# ------------------------------------------------------------

#

# L =

# [[1, 0],

#  [2, 1]]

#

# U =

# [[1, 3],

#  [0, 0]]

#

# Verification:

#

# L @ U =

# [[1, 0],      [[1, 3],      [[1, 3],

#  [2, 1]]   @   [0, 0]]   =   [2, 6]]

#

# Therefore:

#

#                  A = L @ U

#

# ============================================================

