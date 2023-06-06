from typing import Any
from urllib import request


obj = {
    1: "Ajouter",
    2: "Enlever",
    3: "Afficher",
    4: "Vider",
    5: "Quitter",
}

for key in obj:
    print(key)
    print(obj[key])

for key, value in obj.items():
    print(f"key : {key} | item : {value}")

for value in obj.values():
    print(value)

div = [1, 2]
div.extend([3, 4])
print(div)

obj = {
    0: "plop",
    (3, 4): {"prenom": "Julie", "nom": "Dupuit", "age": 25},
}

print(obj.get((3, 4), "marche po !!!"))

a, b, r = 5, "2", 0
try:
    r = a / b # type: ignore
except Exception as e:
    print(f"ERROR : {e}")
print(f"r : {r}")

# passage par référence


def append_to_param(param: list[Any]) -> None:
    print(f"into append_to_param() : {id(param)}")
    param.append(4)


attr: list[int] = [1, 2, 3]
print(f"attr id : {id(attr)}")
append_to_param(attr)

attr2: list[int] = [1, 2, 3]
print(f"attr2 id : {id(attr2)}")
append_to_param(attr2)


def create_list(a: int | float = 1, b: int | float = 2) -> list[int | float]:
    """create_list fonction bidon ne servant pas à grand chose

    Args:
        a (int | float, optional): un int ou float. Defaults to 1.
        b (int | float, optional): un deuxième int ou float. Defaults to 2.

    Returns:
        list[int | float]: une liste de int ou float
    """
    return [a, b]


print(create_list(2, 5.5))

liste: list[int] = [1, 2]

print(True + False)
