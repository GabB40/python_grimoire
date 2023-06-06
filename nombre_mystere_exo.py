import random

min = 0
max = 100
nombre_mystere = random.randint(min, max)
essais_restant = chances = 5

while essais_restant != 0:
    essais_restant -= 1
    nombre_saisi = int(input(f"Saisissez un nombre entre {min} et {max} : "))
    if nombre_saisi == nombre_mystere:
        nombre_coups = chances - essais_restant
        if nombre_coups == 1:
            print(f"\nExtraordinaire !!! Vous avez trouvé le nombre mystère du premier coup :D")
        else:
            print(f"\nBravo ! Vous avez trouvé le nombre mystère en {chances - essais_restant} coups :)")
        break
    if nombre_saisi > nombre_mystere:
        print(f"\nle nombre mystère est plus petit que {nombre_saisi}")
    else:
        print(f"\nle nombre mystère est plus grand que {nombre_saisi}")

if essais_restant == 0:
    print(f"\nVous avez perdu: le nombre mystère était {nombre_mystere} ! Mais retentez votre chance :)")
