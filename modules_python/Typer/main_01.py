import typer

# lancement avec python {chemin_correcte}/main_01.py + les éventuels agruments/options
# lancer la cmde help pour savoir comment lancer correctement :
# > python {chemin_correcte}/main_01.py --help


# def main(extension: str = typer.Argument(..., help = "Extension à chercher")): # ... = required
def main(
    delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"),
    extension: str = typer.Argument("txt", help="Extension à chercher"),
):
    """
    Affiche les fichiers trouvés avec l'extension donnée.
    """
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    extension = typer.prompt("Quelle extension souhaitez-vous chercher ?")

    if delete:
        do_delete: bool = typer.confirm("Confirmer la suppression ?", abort=True)
        # condition évitée grâce au 2nd param 'abort=True'
        """ if not do_delete:
            typer.echo("Suppression annulé")
            raise typer.Abort() """


if __name__ == "__main__":
    typer.run(main)
