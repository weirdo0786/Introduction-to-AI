# ============================================================
# Spectral Decomposition
# ============================================================
#
# Spectral decomposition is a method of representing a matrix
# using its eigenvalues and eigenvectors.
#
# For a matrix A, spectral decomposition is written as:
#                 A = Q Λ Q^T
# where:
#
# Q     -> Matrix containing the normalized eigenvectors of A
# Λ     -> Diagonal matrix containing the eigenvalues of A
# Q^T   -> Transpose of Q
#
# Spectral decomposition is possible for a real symmetric matrix.
#
# A matrix is symmetric if:
#
#                 A = A^T
#
# For a symmetric matrix, the eigenvectors can be chosen to be
# orthonormal. Therefore:
#
#                 Q^T Q = I
#
# and:
#
#                 Q^(-1) = Q^T
#
# This is why we can write:
#
#                 A = Q Λ Q^T
#
# ------------------------------------------------------------
# How it works:
# ------------------------------------------------------------
#
# 1. Find the eigenvalues of A.
#
# 2. Find the corresponding eigenvectors.
#
# 3. Normalize the eigenvectors so that their length is 1.
#
# 4. Put the normalized eigenvectors as columns of Q.
#
# 5. Put the eigenvalues on the diagonal of Λ.
#
# 6. Calculate:
#
#                 A = Q @ Λ @ Q.T
#
# ------------------------------------------------------------
# Example:
# ------------------------------------------------------------
#
# Suppose:
#
#                 A = [[2, 1],
#                      [1, 2]]
#
# The eigenvalues are:
#
#                 λ1 = 3
#                 λ2 = 1
#
# After finding and normalizing the eigenvectors, we construct Q
# and Λ.
#
# Then:
#
#                 A = Q @ Λ @ Q.T
#
# ------------------------------------------------------------
# Important:
# ------------------------------------------------------------
#
# Spectral decomposition is mainly used for symmetric matrices.
#
# For a symmetric matrix:
#
#                 A = Q Λ Q^T
#
# Also, because Q is an orthogonal matrix:
#
#                 Q^(-1) = Q^T
#
# Therefore:
#
#                 A = Q Λ Q^(-1)


import numpy as np
a = np.array([[4, 2, 0],[0, 3, 2],[0, 0, 2]])
b = np.array([5, 4, 6])
print("a:")
print(a)
print("b:")
print(b)
print('Shape of A : {}'.format(a.shape))
print('Rank of A: {}'.format(np.linalg.matrix_rank(a)))
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues.real.astype(int))
print("\nEigenvectors:")
print(eigenvectors.real)

#                 A = Q Λ Q^T


# P = Eigenvector matrix
P = eigenvectors
# Lambda = Diagonal matrix of eigenvalues
Lambda = np.diag(eigenvalues)
# P inverse
P_inverse = np.linalg.inv(P)
print("\nP (Eigenvector Matrix):")
print(P.real)
print("\nLambda:")
print(Lambda.real)
print("\nP inverse:")
print(P_inverse.real)

A = P @ Lambda @ P_inverse
# A = P @ Lambda @ P.T
print("\nP @ Lambda @ P^-1:")
print(np.round(A.real).astype(int))
print("\nOriginal A:")
print(a)
print("\nDecomposition is correct:")
print(np.allclose(a, A.real))
# print(P)
# print(P.T.real)
# print(P @ P.T)

print('Here Transpose is now working because it is not Orthogonal matrix. So better to be work for A^-1 rather than A^T')

print('======================')
print('Now we have to calculate for A^K')
#              A^K = P @ Lambda^K @ P^-1
K = 42
# Calculate Lambda^K
Lambda_K = np.diag(eigenvalues ** K)
A_K = P @ Lambda_K @ P_inverse
print("\nA^42:")
print(np.round(A_K.real).astype(float))




# Calculating A^K:


# This is useful because calculating Lambda^K is very easy.
# Since Lambda is a diagonal matrix, we only need to raise
# each eigenvalue to the power K.
# ============================================================


# start code for transpose for an another example -- sachin
# A = np.array([
#     [2, 1],
#     [1, 2]
# ])
#
# eigenvalues, eigenvectors = np.linalg.eig(A)
#
# Q = eigenvectors
# Lambda = np.diag(eigenvalues)
#
# print("Q:")
# print(Q)
#
# print("\nQ.T:")
# print(Q.T)
#
# print("\nQ inverse:")
# print(np.linalg.inv(Q))
#
# print("\nQ.T @ Q:")
# print(np.round(Q.T @ Q))
#
# # Spectral decomposition
# A_new = Q @ Lambda @ Q.T
#
# print("\nOriginal A:")
# print(A)
#
# print("\nQ @ Lambda @ Q.T:")
# print(np.round(A_new).real)
#
# print("\nCorrect:")
# print(np.allclose(A, A_new))
# end of my other code




# A:
# [[4 2 0]
#  [0 3 2]
#  [0 0 2]]
#
# B:
# [5 4 6]
#
# Shape of A: (3, 3)
# Rank of A: 3
#
# Eigenvalues:
# [4 3 2]
#
# Eigenvectors (integer form):
# [[ 1 -2  2]
#  [ 0  1 -2]
#  [ 0  0  1]]

# for i in range(eigenvectors.shape[1]):
#     v = eigenvectors[:, i].real
#     v = v / np.min(np.abs(v[np.abs(v) > 1e-10]))
#     eigenvectors[:, i] = np.round(v)
# eigenvectors = eigenvectors.real.astype(int)
# print("\nEigenvectors:")
# print(eigenvectors)


