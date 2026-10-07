n = int(input("Enter the number of rows: "))
# right angled triangle
for i in range(n):
    print("* " *i)

for i in range(1, n + 1):
    print(" "*(n - i), end = "")
    print("* " *i)