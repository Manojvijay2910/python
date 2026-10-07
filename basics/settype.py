s = {10, 20, 30, 'xyz', 10}
print(s, type(s))
s.update([88, 90]) # or we can use s.update({88, 90})
print(s)
s.remove(30)
print(s)

f = frozenset(s) # it converts our set to immutable set