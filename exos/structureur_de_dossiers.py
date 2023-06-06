from pathlib import Path

chemin = Path(r"D:\DEV\Python\udemy\assets\structureur_de_dossiers")

d = {
    "Films": ["Le seigneur des anneaux", "Harry Potter", "Moon", "Forrest Gump"],
    "Employes": ["Paul", "Pierre", "Marie"],
    "Exercices": ["les_variables", "les_fichiers", "les_boucles"],
}

for key, values in d.items():
    (chemin / key).mkdir()
    for v in values:
        (chemin / key / v).mkdir()
    