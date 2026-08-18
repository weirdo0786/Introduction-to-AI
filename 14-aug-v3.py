import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A @ B)


result = np.dot(A, B)
print("a.b =", result)





# A = np.array([[1, 2],
#               [3, 4]])
#
# B = np.array([[5, 6],
#               [7, 8]])

# Create a 2x2 matrix of zeros
result = np.zeros((2, 2), dtype=int)
print(result)

# Matrix multiplication using for loops
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]

print(result)
print('all done')




