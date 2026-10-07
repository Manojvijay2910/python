#Open the file for writing
f = open("myfile.txt", "w")
print("Enter text (Type # when you are done)")
s = ''
while s != '#':
    s = input()
    if s != '#':
        f.write(s + '\n')
f.close()