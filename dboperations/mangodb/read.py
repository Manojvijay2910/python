from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
collection = database['product']

print(collection.find_one())

cursor = collection.find()   # we can use collection.find({"name": "Dell"}) to filter records
for item in cursor:
    print(item)

