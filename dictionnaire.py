from collections import defaultdict


films = {
    "Le Seigneur Des Anneaux": 12,
    "Harry Potter": 9,
    "Blade Runner": 7.5,
}

print(f"\n1ere méthode : keys in film")
for key in films:
    print(f"  key : {key} | value : {films[key]}")

print(f"\n2eme méthode : key, values in films.item()")
for key, value in films.items():
    print(f"  key : {key} | value : {value}")
    
print("\n calcul du prix total en tuilisant films.values()")
prix = 0
for value in films.values():
    prix += value
print(f"prix : {prix}")

# récup un élément
print(f"\nfilms['Harry Potter'] : {films['Harry Potter']}")
print(f"\nfilms.get('Harry Potter') : {films.get('Harry Potter')}")
# avantage de la méthode .get()
# print(f"\nfilms['Existe pas'] : {films['Existe pas']}") # lève une erreur
print(f"\nfilms.get('Existe pas') : {films.get('Existe pas')}") # pas d'erreur : retourne 'None'
print(f"\nfilms.get('Existe pas', 'pas de correspondance') : {films.get('Existe pas', 'pas de correspondance')}") # passage d'une valeur par défaut

# ajout/suppr de clé
films["Forrest Gump"] = 1_000_000
films["Avatar"] = 10
print(f"\nFilms : {films}")
del films["Forrest Gump"]
deleted = films.pop('Avatare', 'plop')
print(f"\deleted : {deleted}")
print(f"\nFilms : {films}")

# sorte d'optional chaining operator
print()
print(films.get("Forrest Gump", {}).get("prix")) # ne provoque pas d'erreur

# différents types de clé d'un dictionnaire = tous types de clés immuables
my_dict = {
    1 : '1',
    "2": "2",
    (3, 4): "(3, 4)",
    5.5: "5.5"
}
for k in my_dict:
    print(f"my_dict[k] : {my_dict[k]}")
    
# les defaultdic : permet de définir une valeur par défaut au cas où clé non existante
defDic = defaultdict(lambda: "plop")
defDic = defDic | {
    "chose": "une chose",
    "truc": "un truc"
}
print(type(defDic))
print((defDic))
# defDic["chose"] = "une chose"
# defDic["truc"] = "un truc"
# print(f"\n'machin' in defDic : {'machin' in defDic}")
# print(defDic["chose"], defDic["truc"], defDic["machin"])
