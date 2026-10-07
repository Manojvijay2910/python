s = "Python is cool"
temp = s.split()
reverse = []
for i in range(0, len(temp)):
    reverse.append(temp[i][::-1])
print(' '.join(reverse))