import json
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
shopping_list_file_path = f"{script_dir}/liste.json"
is_file_check_done = False


def get_shopping_list():
    global is_file_check_done
    if not (is_file_check_done or os.path.exists(shopping_list_file_path)):
        print("(liste.json n'existe pas ==> création du fichier)")
        with open(shopping_list_file_path, "w") as f:
            json.dump([], f)
        is_file_check_done = True

    with open(shopping_list_file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def update_list(shopping_list):
    with open(shopping_list_file_path, "w", encoding="utf-8") as f:
        json.dump(shopping_list, f, indent=4)


def add_item():
    item = input("\nQue souhaitez-vous ajouter ? : ")
    shopping_list = get_shopping_list()
    shopping_list.append(item)
    update_list(shopping_list)
    print(f"'{item}' a bien été ajouté à la liste")
    display_shopping_list()


def remove_item():
    shopping_list = get_shopping_list()
    if not shopping_list:
        print("\nVotre liste est vide\n")
        return
    item = input("\nQue souhaitez-vous enlever ? : ")
    if item in shopping_list:
        shopping_list.remove(item)
        update_list(shopping_list)
        print(f"'{item}' a bien retiré la liste\n")
    else:
        print(f"\n'{item}' n'appartient pas à la liste\n")
        display_shopping_list()


def display_shopping_list():
    shopping_list = get_shopping_list()
    if shopping_list:
        print(f"\nVoici votre liste : ")
        for item in shopping_list:
            print(f"  - {item}")
        print()
    else:
        print("\nVotre liste est vide\n")


def clear_shopping_list():
    confirm = input("Êtes-vous sûr de vouloir supprimer la liste ? (o/n)")
    if confirm == "o":
        shopping_list = get_shopping_list()
        shopping_list.clear()
        update_list(shopping_list)
        print(f"\nVotre liste a bien été vidée")
    print("\n")
