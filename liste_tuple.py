my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
my_list.remove(11)
print(f"my_list :                   {my_list}")
print(
    f"my_list[1:-1] :             {my_list[1:-1]}"
)  # on exclue le premier et le dernier élément
print(f"my_list[2:] :               {my_list[2:]}")  # on exclue les 2 premiers éléments
print(f"my_list[-4] :               {my_list[-4]}")  # 4eme élément en partant de la fin
print(f"my_list[-4:] :              {my_list[-4:]}")  # 4 derniers éléments
print(
    f"my_list[1:9:2] :            {my_list[1:9:2]}"
)  # récupère élément à l'index 1 jusqu'à l'index 9 (exclusif!) avec un pas de 2
print(f"my_list[::-1] :             {my_list[::-1]}")  # tableau inversé
print(
    f"my_list[::len(my_list)-1] : {my_list[::len(my_list)-1]}"
)  # récupère le premier et le dernier élément

print("-------------------------------")

employes = ["Carlos", "Paul", "Claire", "Pierre", "Jean", "Alex", "Pierre", "Carole"]
print(f"employes : {employes}")
print(f"employes.index('Alex') : {employes.index('Alex')}")
print(f"count(Pierre) : {employes.count('Pierre')}")
sorted_employes = sorted(employes)
print(f"sorted_employes : {sorted_employes}")
# RMQ : il existe la méthode liste.sort() qui permet de trier une liste mais ne retourne rien = modif liste originale
# la méthode reverse marche de la même manière :
employes.reverse()
print(f"employes après .reverse() : {employes}")
print(f"employes.reverse() retourne 'None' : {employes.reverse()}")
print(f"employes.pop(-1) : {employes.pop(-1)}")
print(f"employes : {employes}")
employes.clear()
print(f"employes apres employes.clear(): {employes}")

print("-------------------------------------------------")

liste = ["Ceci", "est", "un", "exemple"]
join = " ".join(liste)
print(f"liste : {liste}")
print(f"join : {join}")
print(f"split du join : {join.split()}")
print(f"'Ceci' in liste : {'Ceci' in liste}")
print(f"'Plop' not in liste : {'Plop' not in liste}")

print("-------------------------------------------------")

# compréhensions de liste
liste = [-5, -2, -1, 0, 2, 5, 8, 10, 12]
nb_positifs = [i for i in liste if i > 0]
print(f"nb_positifs_x2 : {nb_positifs}")
nb_positifs_x2 = [i * 2 for i in liste if i > 0]
print(f"nb_positifs_x2 : {nb_positifs_x2}")

# Any et All
print(f"any([False, False, True, False]) : {any([False, False, True, False])}")
print(f"all([False, False, True, False]) : {all([False, False, True, False])}")
print(f"any([i > 11 for i in liste]) : {any([i > 11 for i in liste])}")
print(f"any([i > 11 for i in liste]) : {any([i for i in liste if i > 11])}")

nb1 = input("Entrez un premier nombre : ")
nb2 = input("Entrez un deuxième nombre : ")
if (not nb1.isdigit() or not nb2.isdigit()):
  print(f"Saisie incorrecte : {nb1 if not nb1.isdigit() else nb2} n'est pas un nombre")
else :
  print(f"Le résultat de l'addition de {nb1} avec {nb2} est égal à {int(nb1) + int(nb2)}")  
