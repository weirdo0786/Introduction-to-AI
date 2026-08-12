import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

row_r1 = a[1, :] #it shows that take row 1 and whole column that is 5,6,7,8 and for the shape Because NumPy removes the row dimension when you use a single integer 1.
row_r2 = a[1:2, :] #But there is an important difference. You’re saying: Give me a range of rows, from 1 to 2 Therefore NumPy keeps the row dimension.
row_r3 = a[[2], :] #Select the rows whose indices are in this list.  Select row(s) using a list
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
print(row_r3, row_r3.shape)


# learn or practice with these questions how it works.


# what you deliver in next week
# how you're going or define no of week to complete


a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1, 2], [0, 1, 0]])
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(a)
# np.arange(4) --- [0 1 2 3]
# a[np.arange(4), b] --- a[[0,1,2,3], b]
b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b])

a[np.arange(4), b] += 10
print('check')
print(a)

a = np.array([[1, 2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)

print(a[bool_idx])
print(a[a > 2])

x = np.array([1, 2])
print(x)
y = np.array([1.0, 2.0])
z = np.array([1, 2], dtype=np.int64)
print(x.dtype, y.dtype, z.dtype)

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))

