from dataclasses import dataclass
from typing import ClassVar


@dataclass
class SecondVoiture:
    marque: str
    couleur: str = "blanche"
    voitures_crees: ClassVar[int] = 0 # attribut de classe et non d'instance - cf ClassVar

    def __post_init__(self):
        SecondVoiture.voitures_crees += 1
        
    def afficher_marque_couleur(self) -> None:
        print(f"La voiture est une {self.marque} de couleur {self.couleur}")


voiture_02 = SecondVoiture("Renault", "rouge")
voiture_03 = SecondVoiture("OSEF")
print(SecondVoiture.voitures_crees)
print(voiture_02.marque)
voiture_02.afficher_marque_couleur()
# voiture_04 = SecondVoiture() # ERREUR car attribut marque est obligatoire

print(voiture_02.__dict__) # ne contient pas l'attribut de classe 'voiture_crees'
