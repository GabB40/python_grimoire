from pprint import pprint
import sys
import utils
# import ext_utils

print(utils.add(3, 5))

# affiche les dossiers connu de python pour l'import de module
pprint(sys.path)
# le dossier parent de ce fichier n'y figurant pas, on ne peut pas utiliser tel quel le module ext_utils
# le pprint ci-dessous affiche une erreur si on le décommente et lance le code
# print(ext_utils.sub(5, 3))

# il faut au préalable ajouter le chemin de ce module dans le path de python
sys.path.append(r"D:\DEV\Python\udemy\modules")
print()
pprint(sys.path)
import ext_utils # bien-sûr, ne devrait pas se trouver ici : besoin pour la démo
print(ext_utils.sub(5, 3))

# cette méthode implique de devoir ajouter au sys.path tous les chemins des différents dossiers de nos modules
# et de RÉPÉTER CETTE OPÉRATION POUR CHACUN DES FICHIERS UTILISANT CES MODULES EXTERNES

# une autre méthode consiste à créer une variable d'environnement pour les chemins des modules externes
# pour cela, créer une var d'env avec comme nom PYTHONPATH et comme valeur la liste des chemins des modules désirées séparés par des ;

# lors de modif dans le module externe, il peut être nécessaire de 'recharger' le module pour que ces modifs soient prises en compte
# pour cela, dans les v de python > 3.4 on peut utiliser importlib
# > import importlib
# > importlib.reload(nom_du_module)