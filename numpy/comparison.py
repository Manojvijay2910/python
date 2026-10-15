from numpy import *

a1 = array([10,30,50,70,90])
a2 = array([20,30,50,70,90])

print(a1 > a2)
print(a1 < a2)

print(all(a1 > a2))
print(logical_and(a1 > 10, a2 < 100))
print(where(a1 < 50, a1, 0))