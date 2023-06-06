# UNITTEST
Via l'installation *(de préférence dans un venv)* du package `coverage`, possibilité d'obtenir le code coverage
`$ coverage run -m unittest (+ éventuellement nom fichier de test)`

la cmde précédente va créer un *.coverage* à la racine du dossier où a été exécutée la cmde

lancer un :
`$ coverage html`

--> génère le dossier **htmlcov** dans lequel se trouve un `index.html` représentant le code coverage

# PYTEST
installer au préalable le package `pytest-html`

ensuite lancer un:
`$ pytest (+ éventuellement nom fichier de test) --html=chemin_ou_generer.html`

(lien_doc)[https://pytest-html.readthedocs.io/en/latest/user_guide.html]