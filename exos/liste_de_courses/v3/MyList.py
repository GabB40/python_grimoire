import json
import os
from dataclasses import dataclass

from constants import FILES_DIR

# RMQ : la correction fait un héritage de la classe list (mais pas encore vu à ce stage du cours O_o)


@dataclass
class MyList:
    list_name: str
    _is_file_check_done: bool = False

    def __post_init__(self) -> None:
        self.shopping_list_file_path: str = f"{FILES_DIR}/{self.list_name}.json"

    def get_shopping_list(self) -> list[str]:
        if not (
            self._is_file_check_done or os.path.exists(self.shopping_list_file_path)
        ):
            print("(liste.json n'existe pas ==> création du fichier)")
            with open(self.shopping_list_file_path, "w") as f:
                json.dump([], f)
            self._is_file_check_done = True

        with open(self.shopping_list_file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _update_list(self, shopping_list):
        with open(self.shopping_list_file_path, "w", encoding="utf-8") as f:
            json.dump(shopping_list, f, indent=4)

    def add_item(self):
        item: str = input("\nQue souhaitez-vous ajouter ? : ")
        shopping_list: list[str] = self.get_shopping_list()
        shopping_list.append(item)
        self._update_list(shopping_list)
        print(f"'{item}' a bien été ajouté à la liste")
        self.display_shopping_list()

    def remove_item(self):
        shopping_list = self.get_shopping_list()
        if not shopping_list:
            print("\nVotre liste est vide\n")
            return
        item: str = input("\nQue souhaitez-vous enlever ? : ")
        if item in shopping_list:
            shopping_list.remove(item)
            self._update_list(shopping_list)
            print(f"'{item}' a bien retiré la liste\n")
        else:
            print(f"\n'{item}' n'appartient pas à la liste\n")
            self.display_shopping_list()

    def display_shopping_list(self):
        shopping_list: list[str] = self.get_shopping_list()
        if shopping_list:
            print(f"\nVoici votre liste : ")
            for item in shopping_list:
                print(f"  - {item}")
            print()
        else:
            print("\nVotre liste est vide\n")

    def clear_shopping_list(self):
        confirm: str = input("Êtes-vous sûr de vouloir supprimer la liste ? (o/n)")
        if confirm == "o":
            shopping_list: list[str] = self.get_shopping_list()
            shopping_list.clear()
            self._update_list(shopping_list)
            print(f"\nVotre liste a bien été vidée")
        print("\n")
