import os, sys
if os.path.isfile("myfile.txt"):
    #Open the file for writing
    f = open("myfile.txt", "r")
    s = f.read()
    print(s)
    f.close()
else:
    print("File not found")
    sys.exit()