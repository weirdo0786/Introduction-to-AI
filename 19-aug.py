import numpy as np

# Original matrix
X = np.array([
    [1, 1, 0],
    [2, 3, 1],
    [4, 5, 1],
    [3, 7, 5]
], dtype=float)

print("Original Matrix X:")
print(X)

XXT = X @ X.T

print("\nX @ X.T:")

print(XXT)

# Check eigenvalues and eigenvectors of X @ X.T

eigenvalues, eigenvectors = np.linalg.eigh(XXT)

print("\nEigenvalues of X @ X.T:")

print(eigenvalues)

print("\nEigenvectors of X @ X.T:")

print(eigenvectors)



# Singular Value Decomposition
U, S, VT = np.linalg.svd(X)

# print(S)

# Create Sigma matrix of size 4 x 3
Sigma = np.zeros((X.shape[0], X.shape[1]))
np.fill_diagonal(Sigma, S)

print("\nU:")
print(U)

print("\nSingular Values:")
print(S)

print("\nSigma:")
print(Sigma)

print("\nV.T:")
print(VT)

# Reconstruct X
X_reconstructed = U @ Sigma @ VT

print("\nU @ Sigma @ V.T:")
print(X_reconstructed)

# Check
print("\nSVD is correct:")
print(np.allclose(X, X_reconstructed))