import logging
logging.basicConfig(filename = "log.log", level=logging.DEBUG)

try:
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers:").split()]
    logging.info("Division in progress")
    c = a / b
    f.write(f"Writing {c} to file")
    print(c)
except ZeroDivisionError:
    print("You can't divide by zero")
    print("Try again")
    logging.error("Division by Zero")
else:
    print("You have entered a non-zero number")
finally:
    f.close()
    print("File closed")

print("code after exception")