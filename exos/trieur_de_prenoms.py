from pathlib import Path
import re

file_path = Path(r"D:\DEV\Python\udemy\assets\prenoms.txt")
raw_first_names = file_path.read_text(encoding="utf-8").split()
first_names = [re.sub("[^A-zÀ-ú]", "", f) for f in raw_first_names]
print(first_names)


# pas de mode 'append' à pathlib ??!
# file_path.touch() # on clean le fichier au préalable
# for first_name in sorted(first_names):
#     file_path.write_text(first_name)

open(file_path, "w").close()  # on clean le fichier au préalable
with open(file_path, "a", encoding="utf-8") as f:
    for i, first_name in enumerate(sorted(first_names)):
        if i > 0:
            f.write("\n")
        f.write(first_name)
