d = {1: 'Jacky', 2: 'John', 3: 'Smith'}
print(d, type(d))

print(d.items())

k = d.keys()
for i in k: print(i)

v = d.values()
for i in v: print(i)

print(d[3])

del d[2]
print(d)