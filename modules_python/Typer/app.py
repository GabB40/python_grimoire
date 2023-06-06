from pathlib import Path
import typer
from typing import Optional

app = typer.Typer()

@app.command("run")
def main(
    extension: str,
    directory: Optional[str] = typer.Argument(
        None, help="Dossier dans lequel chercher."
    ),
    delete: bool = typer.Option(False, help="Supprime les fichiers trouvés."),
) -> None:
    """
    Affiche les fichiers trouvés avec l'extension donnée.
    """
    directory_path: Path = Path(directory) if directory else Path.cwd()

    if not directory_path.exists():
        typer.secho(f"Le dossier '{directory_path}' n'existe pas", fg=typer.colors.RED)

    files = directory_path.rglob(f"*.{extension}")
    if delete:
        msg: str = typer.style(
            "Voulez-vous vraiment supprimer tous les fichiers trouvés ?",
            bg=typer.colors.BRIGHT_RED,
        )
        typer.confirm(f"\n{msg}", abort=True)
        for file in files:
            file.unlink()
            typer.secho(f"Suppression du fichier {file}.", fg=typer.colors.RED)
    else:
        typer.secho(
            f"\nFichiers trouvés avec l'extension {extension}:",
            bg=typer.colors.YELLOW,
        )
        for file in files:
            typer.secho(file, fg=typer.colors.YELLOW)

@app.command()
def search(extension: str):
    """
    Chercher les fichiers avec l'extension donnée. 
    """
    main(extension=extension, directory=None, delete=False)
    
@app.command()
def delete(extension: str):
    """
    Supprimer les fichiers avec l'extension donnée. 
    """
    main(extension=extension, directory=None, delete=True)
    
if __name__ == "__main__":
    app()
