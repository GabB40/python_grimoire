import os

path = "D:\\DEV\\Python"
dossier = os.path.join(path, "test", "created_from_code")
os.makedirs(dossier, exist_ok=True)
print("dossier créé")

if os.path.exists(dossier):
    os.removedirs(dossier)
print("dossier supprimé")

