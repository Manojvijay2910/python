import pickle, stuent

f = open("student.dat", "wb")
s = stuent.Student(123, "John", 90)
pickle.dump(s, f)
f.close()