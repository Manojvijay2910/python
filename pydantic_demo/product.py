from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id : int
    name: str
    price: float
    description: Optional[str] = "No description provided"

p1 = Product(id = 1, name = "John", price = 3.14)
print(p1)
print(p1.model_dump())
print(p1.model_dump_json(indent = 2))