from pprint import pprint
import random

# afficher les fonctions disponibles dans random
print(f"dir(random) : {dir(random)}")

# affiche l'aide sur random.randint
help(random.randint)

# affichage plus propre des fonctions disponibles dans random
pprint(dir(random))

# --------------------------------------------------------------------
# pprint n'est pas callable, d'où la synthaxe différente pour l'import
print(f'Est-ce que pprint est callable ? {callable(pprint)}')