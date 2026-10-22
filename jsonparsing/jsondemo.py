import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(person, indent=4)
print(json_data)

person_data = json.loads(json_data)
print(person_data)
print(person_data.get("age"))