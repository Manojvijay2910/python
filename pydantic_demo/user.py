from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

user = User(id = 1, name = "John", age = 30)
print(user)
try:
    user2 = User(id = 1, name = "John", age = "T")
except Exception as e:
    print(e)