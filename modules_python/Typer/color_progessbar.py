# sur windows nécessite l'installation du package colorama (pip install colorama)
import time
import typer

def main():
    prenom: str = typer.style("Patrick", bold=True, fg=typer.colors.CYAN)
    nom: str = typer.style("DUPOND", italic=True, bg=typer.colors.BLUE)
    typer.echo(f"Bonjour {prenom} {nom}")
    typer.secho("Bienvenue :)", bg=typer.colors.BRIGHT_YELLOW)
    
    taches: list[str] = ["plop", "blop", "bloup", "gloup", "plip"]
    with  typer.progressbar(taches) as progress:
        for tache in progress:
            time.sleep(1)
        
    typer.echo("Fin de la boucle")
    
if __name__ == "__main__":
    typer.run(main)