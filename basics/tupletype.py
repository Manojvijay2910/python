tpl = (20, 30, 40, 20, 50, 'xyz')
# tpl[3] = 20 is not allowed, we can't modify a tuple after assignment
print(tpl, type(tpl))
print(tpl.count(20))
print(tpl.index(20))

lst = [67, 30, 'abc']
print(lst)
tpl1 = tuple(lst)
print(tpl1)