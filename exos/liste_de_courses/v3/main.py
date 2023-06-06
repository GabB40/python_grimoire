import os
from MyList import MyList
from constants import FILES_DIR

incorrect_choice_msg = "Choix incorrect ! Fermeture de l'application..."

print("\n*** Bienvenue dans votre gestionnaire de liste :) ***\n")
create_or_update_list = input(
    """Que souhaitez-vous faire ? 
    (1) Créer une nouvelle liste 
    (2) Ouvrir une liste existante
    (3) Afficher et gérer les listes
    :"""
)

if create_or_update_list not in ["1", "2", "3"]:
    print(incorrect_choice_msg)
    exit()

if create_or_update_list == "1":
    list_name = input("Quel est le nom de la liste que vous souhaitez créer ? : ")
elif create_or_update_list == "2":
    list_name = input("Quel est le nom de la liste que vous souhaitez ouvrir ? : ")
    if not os.path.exists(f"{FILES_DIR}/{list_name}.json"):
        print(
            "Aucune correspondance pour le nom de liste renseigné ! Fermeture de l'application..."
        )
        exit()
else:
    print(
        "Voici vos listes (0 pour sortir - entrer le numéro d'une lsite pour la supprimer) : "
    )
    print("(0) sortir")
    for i, f in enumerate(os.listdir(FILES_DIR), 1):
        print(f"({i}) {os.path.splitext(f)[0]}")
    choice = input("Votre choix ?")
    if choice == "0" :
        print("À bientôt :)")
    elif choice == "0" or int(choice) not in range(len(os.listdir(FILES_DIR)) + 1):
        print(incorrect_choice_msg)
    else:
        os.remove(f"{FILES_DIR}/{os.listdir(FILES_DIR)[int(choice) - 1]}")
        print("Liste correctement supprimée")
    exit()

my_list = MyList(list_name)

input_choices: dict[int, str] = {
    1: "ajouter",
    2: "retirer",
    3: "afficher",
    4: "vider",
    5: "quitter",
}

descriptions: dict[str, str] = {
    "ajouter": "ajouter un élément à la liste",
    "retirer": "retirer un élément de la liste",
    "afficher": "afficher la liste",
    "vider": "vider la liste",
    "quitter": "quitter le programme",
}

functions = {
    "ajouter": my_list.add_item,
    "retirer": my_list.remove_item,
    "afficher": my_list.display_shopping_list,
    "vider": my_list.clear_shopping_list,
}

input_choice: str = ""
separator: str = "-" * 50


while input_choice != "quitter":
    print(separator)
    print(f"*** ma liste '{list_name}' ***")
    for k, v in input_choices.items():
        print(f"{k} -> {v} ({descriptions[v]})")
    print(separator)
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
        functions[input_choice]()
    else:
        print(
            f"\n/!\\ Une erreur s'est produite : la fonction functions[{input_choice}] n'existe pas !\n"
        )
        continue
