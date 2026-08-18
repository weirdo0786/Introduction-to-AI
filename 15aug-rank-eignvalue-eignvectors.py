import numpy as np
a = np.array([[4, 2, 0],[0, 3, 2],[0, 0, 2]])
b = np.array([5, 4, 6])
print(a)
print(b)
print('Shape of A : {}'.format(a.shape))
print('Rank of A: {}'.format(np.linalg.matrix_rank(a)))
eigenvalues, eigenvectors = np.linalg.eig(a)
print("\nEigenvalues:")
print(eigenvalues.real.astype(int))
print("\nEigenvectors:")
print(eigenvectors.real.astype(float))







