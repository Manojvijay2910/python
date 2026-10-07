lst = [10, 20, 30, 40, 234]
print(lst, type(lst))

b = bytes(lst)
print(type(b)) # we can't modify this bytes so b[3] = 22 will be error

b1 = bytearray(lst)
print(type(b1))
b1[3] = 22 # bytearray can be modified