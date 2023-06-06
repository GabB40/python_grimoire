import random

my_hero = {
    "health": 50,
    "attack_strength": (5, 10),
    "potions_count": 3,
    "potions_strength": (15, 50),
}

bad_guy = {
    "health": 50,
    "attack_strength": (5, 15),
}


def getRandom(strength):
    if len(strength) != 2:
        print("Bad argument, baaad !")
        exit()
    return random.randint(strength[0], strength[1])


def addS(num):
    return "s" if num == 1 else ""


while bad_guy["health"] > 0 or my_hero["health"] > 0:
    print("\n")
    choix = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    if choix not in ["1", "2"]:
        print("Choix invalide !")
        continue

    if choix == "2":
        if my_hero["potions_count"] == 0:
            print("Il ne vous reste plus de potion :(")
            continue
        my_hero["potions_count"] -= 1
        potion_strength = getRandom(my_hero["potions_strength"])
        my_hero["health"] += potion_strength
        print(f"La potion vous a fait gagné {potion_strength}")
        print(f"Vous avez {my_hero['health']} point{addS(my_hero['health'])}")

    else:
        my_attack_strength = getRandom(my_hero["attack_strength"])
        bad_guy["health"] -= my_attack_strength
        print(f"Vous avez porté un coup de {my_attack_strength} de puissance")
        if bad_guy["health"] <= 0:
            print(
                "*** L'ennemi n'a plus de point de vie : bravo, vous avez triomphé du mal :D"
            )
            break
        print(f"Il reste {bad_guy['health']} points de vie à votre ennemi")

    # tour de l'ennemi
    print("\nL'ennemi attaque !!!")
    bad_guy_attack_strength = getRandom(bad_guy["attack_strength"])
    my_hero["health"] -= bad_guy_attack_strength
    print(f"L'ennemi vous a porté un coup de {bad_guy_attack_strength} points de dégat")

    if my_hero["health"] <= 0:  # RIP
        print("*** -_- Il ne vous reste plus de point de vie : vous avez perdu :'(")
        break
    print(f"Il vous reste {my_hero['health']} point{addS(my_hero['health'])} de vie")
