class Programmr:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies

p1 = Programmr()
p1.setName("John")
p1.setSalary(10000)
p1.setTechnologies(["Java", "Spring", "Hibernate", "Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())