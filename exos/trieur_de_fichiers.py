from pathlib import Path

data_path = Path(r"D:\DEV\Python\udemy\assets\data_h")

associations = {
    (".flac", ".mp3", ".wav"): "Musique",
    (".avi", ".gif", ".mp4"): "Vidéos",
    (".bmp", ".jpeg", ".jpg", ".png"): "Images",
    (
        ".csv",
        ".doc",
        ".txt",
        ".odp",
        ".pages",
        ".pdf",
        ".pptx",
        ".xls",
        ".xlsm",
        ".xlsx",
    ): "Documents",
    "autre": "Divers",
}

excluded_folder_names = [v for v in associations.values()]
empty_folders_path = []

def get_folder_path(suffix):
    matches = [associations[k] for k in associations if suffix in k]
    folder_name = matches[0] if matches else associations["autre"]
    return data_path / folder_name


def classify(path, is_recursive=False, delete_empty_folder=False):
    if not path:
        print("[ERROR] dossier non trouvé !")
        return

    folders_and_files = path.iterdir()
    for f in folders_and_files:
        if f.is_file():
            folder_path = get_folder_path(f.suffix)
            folder_path.mkdir(exist_ok=True)
            f.rename(folder_path / f.name)
        elif is_recursive and f.name not in excluded_folder_names and f.is_dir():
            classify(f, is_recursive, delete_empty_folder)
            empty_folders_path.append(f)

    if delete_empty_folder and list(empty_folders_path):
        for p in empty_folders_path:
            p.rmdir()
        empty_folders_path.clear()


classify(data_path, True, True)
