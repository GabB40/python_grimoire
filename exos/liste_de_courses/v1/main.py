import fonctions as cartFunctions

shopping_list = []

input_choices = {
    1: "ajouter",
    2: "retirer",
    3: "afficher",
    4: "vider",
    5: "quitter",
}

descriptions = {
    "ajouter": "ajouter un élément à la liste de courses",
    "retirer": "retirer un élément de la liste de courses",
    "afficher": "afficher la liste de courses",
    "vider": "vider la liste de courses",
    "quitter": "quitter le programme",
}

functions = {
    "ajouter": cartFunctions.addItem,
    "retirer": cartFunctions.removeItem,
    "afficher": cartFunctions.displayList,
    "vider": cartFunctions.clearList,
}

input_choice = ""

print("Bienvenue dans votre gestionnaire de liste de courses :)")

while input_choice != "quitter":
    print("----------------------------------------------------")
    for k, v in input_choices.items():
        print(f"{k} -> {v} ({descriptions[v]})")
    print("----------------------------------------------------")
    input_choice = input("\nQuel est votre choix ? (Saisir numéro ou mot clé) : ")

    if input_choice.startswith("-"):
        print("\nLa saisie ne doit pas commencer par un tiret\n")
        continue

    if input_choice.isdigit():
        if int(input_choice) in input_choices:
            input_choice = input_choices[int(input_choice)]
        else:
            print(f"\nLe numéro {input_choice} n'est pas valide\n")
            continue

    input_choice = input_choice.lower()
    if input_choice == "quitter":
        print("\nÀ bientôt :)")
        break

    if input_choice in functions:
        functions[input_choice](shopping_list)
    else:
        print(
            f"\n/!\ Une erreur s'est produite : la fonction functions[{input_choice}] n'existe pas !\n"
        )
        continue
