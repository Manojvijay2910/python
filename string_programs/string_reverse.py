s = input("Enter the string: ")
#print(s[::-1])
print(''.join(reversed(s)))

w = "All the power is with in you"
t = w.split()
print(t)
reverse = []
for i in range(len(t) - 1, -1, -1):
    reverse.append(t[i])

print(' '.join(reverse))