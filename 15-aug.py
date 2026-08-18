import numpy as np
a = np.array([[1, 0, 3],[10, 1, 7],[-5, 0, -3]])
b = np.array([5, 4, 6])
print('Shape of A : {}'.format(a.shape))
print('Rank of A: {}'.format(np.linalg.matrix_rank(a)))
x = np.linalg.inv(a) @ b
print('Solution: {}'.format(x))


# Matrix A
A = np.array([[4, 2, 0],[0, 3, 2],[0, 0, 2]], dtype=float)
print("Matrix A:")
print(A)
# Find eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvalues:")
print(eigenvalues.real.astype(int))
print("\nEigenvectors:")
print(eigenvectors)
# V = matrix of eigenvectors
V = eigenvectors
# Lambda = diagonal matrix of eigenvalues
Lambda = np.diag(eigenvalues)
# V inverse
V_inverse = np.linalg.inv(V)
print("\nV:")
print(V)
print("\nLambda:")
print(Lambda)
print("\nV inverse:")
print(V_inverse)
# Eigendecomposition formula
A_reconstructed = V @ Lambda @ V_inverse
print("\nV @ Lambda @ V^-1:")
print(A_reconstructed)

# Check

print("\nIs A = V @ Lambda @ V^-1?")

print(np.allclose(A, A_reconstructed))


print("Spectral Decomposition")

A = np.array([
    [4, 2, 0],
    [0, 3, 2],
    [0, 0, 2]
], dtype=float)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Remove unnecessary imaginary part
eigenvalues = eigenvalues.real
eigenvectors = eigenvectors.real

# V = matrix of eigenvectors
V = eigenvectors
print("\nV:")
print(V)

# Lambda = diagonal matrix of eigenvalues
Lambda = np.diag(eigenvalues)

# V inverse
V_inverse = np.linalg.inv(V)

# A^42 = V Lambda^42 V^-1
Lambda_42 = np.linalg.matrix_power(Lambda.astype(int), 42)

A_42 = V @ Lambda_42 @ V_inverse

print("\nA^42:")
print(np.round(A_42))