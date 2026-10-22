import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

with open("person.json", "r") as file:
    person = json.load(file)
    print(person)