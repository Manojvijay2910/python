from random import *

for i in range(10):
    print(random())

for i in range(10):
    print(randint(1, 50))

for i in range(10):
    print(uniform(1, 50))

for i in range(10):
    print(randrange(10))

lst = ["java", "python", "aws", "devops"]

for i in range(10):
    print(choice(lst))