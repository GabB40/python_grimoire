import json

pathR = "D:/DEV/Python/udemy/assets/fichiers/read.txt"
pathW = "D:/DEV/Python/udemy/assets/fichiers/write.txt"
pathJ = "D:/DEV/Python/udemy/assets/fichiers/fichier.json"

# ( encoding='utf-8' prévinet d'éventuelles erreurs sur windows (...? j'en sais pas plus !) )

# MODE LECTURE
with open(
    pathR, "r", encoding="utf-8"
) as f:  # cette synthaxe avec **with** permet de se soustraire de l'utilisation du close()
    content = (
        f.read().splitlines()
    )  # le splitLines permet de se soustraire du retour à la ligne (cf \n)
    print(f"MODE LECTURE : {content}")

# MODE ECRITURE
with open(
    pathW, "a", encoding="utf-8"
) as f:  # 'w' écrase le contenu du fichier, 'a' ajoute au contenu du fichier
    f.write("plop\n")

# JSON - ECRITURE
with open(pathJ, "w", encoding="utf-8") as f:
    json.dump(list(range(4)), f, indent=4)

# JSON - LECTURE
with open(pathJ, "r", encoding="utf-8") as f:
    liste = json.load(f)

print(f"JSON - MODE LECTURE : {liste}")

# JSON - MODIFICATION (on se base sur le liste précédemment récupéré en 'w')
liste.append(4)
with open(pathJ, "w", encoding="utf-8") as f:
    json.dump(liste, f, indent=4)
