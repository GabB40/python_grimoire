# pip install tinydb
from tinydb import TinyDB, Query, where
# from tinydb.storages import MemoryStorage # possibilité de créer une db en mémoire : db = TinyDB(storage=MemoryStorage)

db = TinyDB('./database/data.json', indent=2)

# db.insert({"name": "Patrick", "score": 0})
# db.insert_multiple([
#     {"name": "Julie", "score": 50},
#     {"name": "Paul", "score": 20},
#     {"name": "Nathalie", "score": 40}
# ])

User = Query()
patricks = db.search(User.name == "Patrick") # multiple
print(f"patricks : {patricks}")
patrick = db.get(User.name == "Patrick") # unique
print(f"patrick : {patrick}")

# sans Query avec where
julie = db.search(where("name") == "Julie")
high_scores = db.search(where("score") > 20)
print(f"julie : {julie}")
print(f"high_scores : {high_scores}")

print(f"len(db) : {len(db)}")
print(f"db.contains(where('name') == 'Patrick') : {db.contains(where('name') == 'Patrick')}")
print(f"db.count(where('name') == 'Patrick') : {db.count(where('name') == 'Patrick')}")

db.update({"score": 10}, where("name") == "Patrick")
db.update({"roles": ["Junior"]})

# mettre à jour (si existe) ou insérer = upsert
db.upsert({"name": "Pierre", "score": 240, "roles": ["Senior"]}, where("name") == "Pierre")

db.insert({"name": "Pierre", "score": 0, "roles": ["Junior"]})
db.remove(where('score') == 0)

""" # possibilité de créer plusieurs tables dans un même fichier eg:
users = db.table("Users")
cars = db.table("Cars")
users.insert_multiple([
    {"name": "Julie", "score": 50},
    {"name": "Paul", "score": 20},
    {"name": "Nathalie", "score": 40}
])
cars.insert_multiple([
    {"marque": "Renault"},
    {"marque": "Citroën"}
]) """