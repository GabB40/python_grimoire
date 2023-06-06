from pathlib import Path
import shutil
import time

file_path = Path(r"D:\DEV\Python\udemy\modules\pathlib_module.py")
print(f"file_path : {file_path}")

# propriétés intéressantes
print("\n*** propriétés intéressantes")
print(f"file_path.parent : {file_path.parent}")
print(f"file_path.suffix : {file_path.suffix}")
print(f"file_path.suffixes : {file_path.suffixes}")
print(f"file_path.stem : {file_path.stem}")
print(f"file_path.parts : {file_path.parts}")

# méthodes intéressantes
print("\n*** méthodes intéressantes")
print(f"file_path.home() : {file_path.home()}")
print(f"file_path.cwd() (Current Working Directory): {file_path.cwd()}")
print(f"file_path.exists() : {file_path.exists()}")
print(f"file_path.is_dir() : {file_path.is_dir()}")
print(f"file_path.is_file() : {file_path.is_file()}")

# concaténation / join
print("\n*** concaténation / join")
join_path_1 = Path.cwd() / "modules" / "pathlib_module.py"  # 1ere méthode
print(f"join_path_1 : {join_path_1}")
join_path_2 = Path.cwd().joinpath("modules", "pathlib_module.py")  # 2eme méthode
print(f"join_path_2 : {join_path_2}")

# création
dossier_test = file_path.parent / "dossier_test"
if not dossier_test.exists():
    dossier_test.mkdir()
# (Path.cwd() / "dossier_test").mkdir() # le dossier existe déjà : va produire une erreur
dossier_test.mkdir(exist_ok=True)  # pas d'erreur grâce à cet argument
(dossier_test / "1" / "2").mkdir(
    parents=True, exist_ok=True
)  # créer une hiérarchie de dossiers

# création/suppression de fichier
(dossier_test / "test.txt").touch()
(dossier_test / "test.txt").unlink()

# suppression de dossier
(dossier_test / "to_delete").mkdir()  # créa dossier à supprimer
(dossier_test / "to_delete").rmdir()  # suppression SI DOSSIER VIDE
# pour supprimer plusieurs dossiers non vides, utiliser plutôt shutil.rmtree(path)
(dossier_test / "to_delete_parent" / "to_delete_child").mkdir(
    parents=True
)  # créa hiérarchie dossiers à supprimer
(dossier_test / "to_delete_parent" / "to_delete_child" / "file.txt").touch()
sleep_time = 1
print(f"pause de {sleep_time} secondes")
time.sleep(sleep_time)
shutil.rmtree(dossier_test / "to_delete_parent")

# écriture et lecture
file = dossier_test / "file.txt"
file.touch() # créa fichier file.txt
file.write_text('plop') # écriture dedans
content = file.read_text() # lecture
print(f"file content : {content}")

# scanner des dossiers et fichiers
folders_and_files = [f for f in dossier_test.iterdir()]
print(f"folders_and_files : {folders_and_files}")
folders_only = [f for f in dossier_test.iterdir()  if f.is_dir()] # avec condition pour ne récupérer que les dossiers
print(f"folders_only : {folders_only}")
# avec glob (non (récurssif) et rglob (récurssif)
glob_scan_txt = [f for f in dossier_test.glob('*.txt')]
print(f"glob_scan_txt : {glob_scan_txt}")
rglob_scan_txt = [f for f in dossier_test.rglob('*.txt')]
print(f"rglob_scan_txt : {rglob_scan_txt}")

# autre exemple : création d'un fichier de svg
file_svg = file.parent / (file.stem + "-svg" + file.suffix)
file_svg.touch()

# déplacer un fichier
shutil.rmtree(file_svg.parent / "svg") # suppression si dossier précédemment crée par lancement du script
time.sleep(1)
(file_svg.parent / "svg").mkdir()
file_svg.rename(file_svg.parent / "svg" / file_svg.name) 

# SUPER EXEMPLE POUR TRIER UN DOSSIER : rangement, par extension, dans dossiers spécifiques
# ==> voir chapitre 228 de la section 36 du cours python udemy