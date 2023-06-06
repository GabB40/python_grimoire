def addItem(shopping_list):
    item = input("\nQue souhaitez-vous ajouter ? : ")
    shopping_list.append(item)
    print(f"'{item}' a bien été ajouté à la liste")
    displayList(shopping_list)


def removeItem(shopping_list):
    if not shopping_list:
        print("\nVotre liste est vide\n")
        return
    item = input("\nQue souhaitez-vous enlever ? : ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' a bien retiré la liste\n")
    else:
        print(f"\n'{item}' n'appartient pas à la liste\n")
        displayList(shopping_list)


def displayList(shopping_list):
    if shopping_list:
        print(f"\nVoici votre liste : ")
        for item in shopping_list:
            print(f"  - {item}")
        print("\n")
    else:
        print("\nVotre liste est vide\n")


def clearList(shopping_list):
    confirm = input("Êtes-vous sûr de vouloir supprimer la liste ? (o/n)")
    if confirm == "o":
        shopping_list.clear()
        print(f"\nVotre liste a bien été vidée")
    print("\n")
