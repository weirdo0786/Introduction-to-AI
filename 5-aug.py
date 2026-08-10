print('Hello Class')

x = 3
print(x, type(x))
print(x+1)
print(x-1)
print(x*2)
print(x**2)

x +=1
print(x)
x *=2
print(x)

y = 2.5
print(type(y))
print(y,y+1,y*2,y**2)

t,f = True, False
print(type(t))

print(t and f)
print(t or f)
print(not t)


hello = 'hello'
wolrd = 'wolrd'
print(hello, len(hello))

xs = [3,1,2]
print(xs, xs[2])
print(xs[-1])

xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)


nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:1])
print(nums[:])
print(nums[:-1])
nums[2:4] = [8,9]
print(nums)

animals = ['dog', 'cat', 'bird']
print(animals)

for animal in animals:
    print(animal)

for idex, animal in enumerate(animals):
    print(f' index {idex} : {animal}')
print('next code')
nums = [0,1,2,3,4]
print(nums)
squares=[]
for x in nums:
    squares.append(x**2)
    print(squares)

print(squares)

nums = [0,1,2,3,4]
squares = [x**2 for x in nums]
print(squares)

nums = [0,1,2,3,4]
even_squares = [x**2 for x in nums if x % 2 == 0]
print(even_squares)



# Dictinaories - (key, value) pairs
d = {'cat':'cute', 'dog':'furry'}
print(d['cat'])
print('cat' in d)
print(d)

animals = {'cat', 'dog', 'monkey'}
for idx, animal in enumerate(animals):
    print(f'#{idx+1}: {animal}')

    from math import sqrt
    print({int(sqrt(x)) for x in range(30)})
    print('check')
    print({float(sqrt(x)) for x in range(30)})

#Tuples : it can't be change, ordered list of values. tuples can be used as a dictonaries.

d = {(x,x+1): x for x in range(10)}
t = (5,6)
print(type(t))
print(d[t])
print(d[(1,2)])
print(d)


def sign(x):
    if x > 0:
        return '+ve'
    elif x < 0:
        return '-ve'

    sign(1)




