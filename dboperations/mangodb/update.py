from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
collection = database['product']

filter = {"name": "Dell"}
collection.update_one(filter, {"$set":{"price":1800}})

cursor = collection.find({"name": "Dell"})
for item in cursor:
    print(item)

filter = {"name": "IPhone"}
result = collection.update_many(filter, {"$set":{"price":1500}})
print(result.modified_count)
cursor = collection.find({"name": "IPhone"})
for item in cursor:
    print(item)

