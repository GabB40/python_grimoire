# RMQ : depuis python 3.7, préférer l'utilisation du décorateur @dataclass qui sipmlifie la création de classe
# --> voir fichier ./data_classes.py


class FirstVoiture:
    marque: str = "Lamborghini"
    couleur: str = "rouge"


print(FirstVoiture.marque)
print(FirstVoiture.couleur)

voiture_01 = FirstVoiture()
print(voiture_01.marque)
voiture_01.marque = "Porsche"
print(voiture_01.marque)


class SecondVoiture:
    voitures_crees: int = 0
    couleur: str = "blanche"

    def __init__(self, marque, couleur="blanche") -> None:
        SecondVoiture.voitures_crees += 1
        self.marque: str = marque
        self.couleur: str = couleur

    def afficher_marque_couleur(self) -> None:
        print(f"La voiture est une {self.marque} de couleur {self.couleur}")
        
    @classmethod
    def methode_de_classe(cls):
        return cls(marque="Lamborghini", couleur="noire")
    
    @staticmethod
    def static_method() -> None:
        print(SecondVoiture.voitures_crees)
        
    # permet de définir l'afficahge lors d'un print
    def __str__(self):
        return f"Voiture de marque {self.marque} avec une couleur {self.couleur}"


voiture_02 = SecondVoiture("Renault", "rouge")
voiture_03 = SecondVoiture("OSEF")
print(SecondVoiture.voitures_crees)
print(voiture_02.marque)
voiture_02.afficher_marque_couleur()

lambo = SecondVoiture.methode_de_classe()
print(lambo) # affiche ce qui est défini dans __str__ au lieu de <__main__.SecondVoiture object at xxx>
