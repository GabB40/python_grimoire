import typer

app = typer.Typer()


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
        typer.echo(f"Suppression des fichiers {extension}")
        # condition évitée grâce au 2nd param 'abort=True'
        """ if not do_delete:
            typer.echo("Suppression annulé")
            raise typer.Abort() """

@app.command("search")
def search_py():
    main(delete=False, extension="py")

@app.command("delete")
def delete_py():
    main(delete=True, extension="py")

if __name__ == "__main__":
    app()
