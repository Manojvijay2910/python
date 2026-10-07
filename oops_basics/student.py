class Student:
    major = "CSE"

    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

s1 = Student(1, "John")
s2 = Student(2, "Bill")
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)