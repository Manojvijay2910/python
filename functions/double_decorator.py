def decorfun(func):
    def inner():
        result = func()
        return result * 2
    return inner

@decorfun
def num():
    return 10

print(num())