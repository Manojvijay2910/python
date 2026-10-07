lst = [10, 20, 'Jacky', -10, 30.5, True]
print(lst, type(lst))
print(lst[3])
print(lst[2:5])
print(lst*2)
print(len(lst))

lst.append(40)
lst.remove(20)
del(lst[1]) # or del lst[1]
print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 99)
print(lst)

lst.sort()
print(lst)
lst.reverse() # or lst.sort(reverse=True)
print(lst)

lst.clear()
print(lst)