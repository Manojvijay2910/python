from numpy_demo import *

a1 = arange(12)
print(a1)

a2 = a1.reshape(4,3)  # a2 = reshape(a1, (4,3)) will also give same output
print(a2)

a3 = reshape(a1, (2,2,3))
print(a3)

print(a3.flatten())

print(eye(3))