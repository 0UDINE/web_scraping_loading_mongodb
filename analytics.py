from load2Mongodb import collection

pipeline = [
    {"$group": {"_id": "$author", "count": {"$sum": 1}}},
    {"$sort": {"count": 1}},
]

results = collection.aggregate(pipeline)
for doc in results:
    print(doc)