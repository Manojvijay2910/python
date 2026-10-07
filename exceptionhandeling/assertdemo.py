try:
    num = int(input("Enter a even number: "))
    assert num % 2 == 0, "You have entered an odd number"
except AssertionError as e:
    print(e)
print("After the assertion")