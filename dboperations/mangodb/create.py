from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
print("Database Created")
collection = database['product']
print("Collection Created")

product = {"name": "IPhone", "price": 1000}
result = collection.insert_one(product)
print(result.inserted_id)

products = [{"name": "Mac Book", "price": 2000},
            {"name": "Dell", "price": 1500}]
result = collection.insert_many(products)
print(result.inserted_ids)


