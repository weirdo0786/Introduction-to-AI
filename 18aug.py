import numpy as np
# Matrix
X = np.array([
    [2, 1],
    [1, 1]
], dtype=float)
print("X:")
print(X)
# Eigenvalues and normalized eigenvectors
eigenvalues, eigenvectors = np.linalg.eigh(X)
print("\nEigenvalues:")
print(eigenvalues)
print("\nNormalized Eigenvectors:")
print(eigenvectors)
# Q = eigenvector matrix
Q = eigenvectors
# Lambda = diagonal matrix of eigenvalues
Lambda = np.diag(eigenvalues)
print("\nQ:")
print(Q)
print("\nLambda:")
print(Lambda)
# Since X is symmetric, Q is orthogonal
print("\nQ.T:")
print(Q.T)
print("\nQ inverse:")
print(np.linalg.inv(Q))
print("\nQ.T @ Q:")
print(np.round(Q.T @ Q, 10))
# Spectral decomposition
# X = Q @ Lambda @ Q.T
X_new = Q @ Lambda @ Q.T
print("\nQ @ Lambda @ Q.T:")
print(np.round(X_new, 10))
print("\nOriginal X:")
print(X)
print("\nSpectral Decomposition is correct:")
print(np.allclose(X, X_new))




