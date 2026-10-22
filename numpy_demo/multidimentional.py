from numpy_demo import *

a1 = array([1,2,3,4,5,6,7,8])
a2 = array([[1,2,3,4],[5,6,7,8]])
a3 = array([[[1,2], [3, 4]], [[5, 6], [7, 8]]])

print(a1, a1.ndim)
print(a2, ndim(a2))
print(a3)

print(a1.shape)
print(a2.shape)
print(a3.shape)

a2.shape = (4,2)
print(a2)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.dtype, a1.itemsize, a1.nbytes)