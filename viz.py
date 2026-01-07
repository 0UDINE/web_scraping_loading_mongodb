import matplotlib.pyplot as plt
from load2Mongodb import collection

pipeline = [
    {"$group": {"_id": "$author", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]

results = list(collection.aggregate(pipeline))

# Extraction des données pour le plot
auteurs = [doc["_id"] for doc in results]
nombres = [doc["count"] for doc in results]

if not auteurs:
    print("Attention : Aucune donnée trouvée dans MongoDB !")
else:
    plt.bar(auteurs, nombres)
    plt.xticks(rotation=45)
    plt.ylabel("Nombre de citations")
    plt.title("Nombre de citations par auteur")
    plt.show()