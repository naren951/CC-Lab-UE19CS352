from pymongo import MongoClient

# host = MongoClient("172.17.0.2")
host = MongoClient("mongodb")

db = host["sample_db"]
collection = db["sample_collection"]

sample_data = {"Name:":"A Narendiran","SRN":"PES1UG19CS001"}
collection.insert_one(sample_data)
print('Inserted into the MongoDB database!')

rec_data = collection.find_one({"SRN":"PES1UG19CS001"})
print("Fecthed from MongoDB: ",rec_data)