from dataclasses import dataclass


@dataclass
class Voiture:
    essence: int = 100

    def afficher_reservoir(self) -> None:
        print(f"La voiture contient {self.essence} litres d'essence")

    def roule(self, km: int) -> None:
        self.essence -= (km * 5) // 100
        print(f"self.essence : {self.essence}")
        if self.essence <= 0:
            return print("Vous n'avez plus d'essence, faites le plein !")
        elif self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
        print(f"La voiture a avancé de {km} kilomètres")

    def faire_le_plein(self) -> None:
        self.essence = 100
        print("Vous pouvez repartir !")


bumbo = Voiture()
bumbo.afficher_reservoir()
bumbo.roule(1200)
bumbo.roule(750)
bumbo.roule(250)
bumbo.faire_le_plein()
