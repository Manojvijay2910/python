f = open("sample.txt", "a+")
print("Cursor at: ", f.tell())
f.write("Django is for web development.")
f.seek(0)
a = []
for line in f:
    a.append(line)
print(a)
f.close()