from pymongo import MongoClient
from Scraper import quotes_data

client = MongoClient("mongodb://localhost:27017/")
db = client["ScrapedData"]
collection = db["ScrapedData"]

collection.delete_many({})
collection.insert_many(quotes_data)

print("Documents inseres :", collection.count_documents({}))