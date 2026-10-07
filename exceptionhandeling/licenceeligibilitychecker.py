class TooYoungException(Exception):
    def __init__(self, message):
        self.message = message

class TooOldException(Exception):
    def __init__(self, message):
        self.message = message

age = int(input("Enter the age:"))

if age < 18:
    raise TooYoungException("You have to be 18 or older to apply")
elif age > 90:
    raise TooOldException("You have to be younger than 90 to apply")
else:
    print("You are eligible")