x = 123 # this is a global variable

def display():
    print(globals()['x']) # this is another way to difference b/w local and global variable
    y = 678 # this is a local variable
    print(y)

print(x)
z = display # a function can be assigned to a variable
z()
#print(y) this is error since y is not available outside of function display