class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.clinical = []

    def add_clinical(self, clinical):
        self.clinical.append(clinical)

class Clinical:
    def __init__(self, componentName, componentValue):
        self.componentName = componentName
        self.componentValue = componentValue

p = Patient("John", 40)
c1 = Clinical("bp", "80/120")
p.add_clinical(c1)

c2 = Clinical("heartRate", 80)
p.add_clinical(c2)

print(p.name)
print(p.age)
for clinical in p.clinical:
    print(clinical.componentName)
    print(clinical.componentValue)