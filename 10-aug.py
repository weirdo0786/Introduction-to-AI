import numpy as np

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
for x in [-1, 0, 1]:
    print(sign(x))


    def hello(name, loud=False):

        if loud:

            print(f'Hello {name.upper()}')

        else:

            print(f'Hello, {name}!')


    hello('Bob')

    hello('Fred', loud=True)

a = np.array([1, 2, 3])
print(a)
print(type(a), a.shape,a[0],a[1],a[2])
a[0] = 5
print(a)

print('2d array')

a = np.array([[1, 2, 3],[4, 5, 6]])
print(a)

print(type(a), a.shape,a[0],a[1])
a[0][0] = 5
print('check')
print(a)



a = np.array([[1, 2, 3],[4, 5, 6]])
for i in range(2):
    for j in range(3):
        a[i][j] +=1
print(a)


# Numpy is support element wise operations as we see when we did for a[0] = 5 then it will change the whole 1st row in 5 elements.
a = np.array([[1, 2, 3],[4, 5, 6]])
a[0] = a[0] + 1
print(a)

a = np.array([[1, 2, 3],[4, 5, 6]])
a = a + 1
print(a)


print('Array to print with single loop')
a = np.array([[1, 2, 3],[4, 5, 6]])
# for i in range(a.size):
#     print(a[i]+1)


a = np.zeros((2, 2))
print(a)

print('printing 1')
b = np.ones((1, 2))
print(b)

c = np.ones((3,4))
print(c)


c = np.full((2,2), 7)
print(c)
print(c.dtype)  #check this working or not why here '.' is not there.

d = np.eye(2)
print(d)
print(d.dtype)

# practice this - How to print [1.00 0.00],[0.00 1.00]
#using a single for loop , add +1 and print that array

rng = np.random.default_rng()
e = rng.random((2,2))
print(e)
print(e.dtype)

rng = np.random.default_rng()
e = rng.random((2, 2))
e = e.astype(int)
print(e)
print(e.dtype)


# A 3d array: shape (2,3,4)
# (height, width< channels)
a = np.ones((2,3,4))
print(a)
print(a.dtype)
print(f'Shape: {a.shape}')
print(f'Sum over axis 0: {np.sum(a, axis=0).shape}')
print(f'Sum over axis 2: {np.sum(a, axis=2).shape}')
print(f'Sum over axis (0,2): {np.sum(a, axis=(0,2)).shape}')

a = a/2
print(a)
print(a[0][0][0])


a = np.array([[1, 2, 3, 4],[5, 6, 7,8],[9,10,11,12]])
b = a[:2, 1:3]
print(b)

# a[0][0] = 1
# a[0][1] = 2

print(a[0,1])
b[0,0] = 77
print(a[0,1])
print(a)

# practice that why b taking the values of a without linking of a . think about it.











