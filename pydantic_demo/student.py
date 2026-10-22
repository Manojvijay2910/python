from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing_extensions import Annotated

class Student(BaseModel):
    name: Annotated[str, Field(min_length = 3, max_length = 30)]
    age: Annotated[int, Field(ge = 18, le = 60)]
    gpa: Annotated[float, Field(ge = 0, le = 10)]
    email: EmailStr
    website: AnyUrl

s1 = Student(
    name = "John",
    age = 20,
    gpa = 7.4,
    email = "bob@bob.com",
    website = "http://www.john.com"
)
print(s1)

try:
    s2 = Student(
        name = "Alice",
        age = 16,
        gpa = 12.3,
        email = "abc",
        website = "abc"
    )
    print(s2)
except Exception as e:
    print(e)