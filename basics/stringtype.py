s = " You are awesome. "
print(s, type(s))

s1 = """You are 
the developer
of this project."""
print(s1, type(s1))

print(s[0], type(s[0]))

print(s*2)

print(len(s1))

print(s[0:5])
print(s[1:])
print(s[:8])
print(s[-3:-1])

print(s[0:9:2]) #this will print every second element in string since step is 2
print(s[15::-1]) #reverse the string, need to give starting index as len(s) - 1 and step as -1
print(s[::-1]) # we can use this for reversing the string

print(s.strip()) # we can use lstrip or rstrip to only remove spaces from left or right side
print(s.lstrip())
print(s.rstrip())

print(s.find("awe"), 0, 8)
print(s.count("a"))
print(s.replace("awesome","super"))

print(s.upper())
print(s.lower())
print(s.title())