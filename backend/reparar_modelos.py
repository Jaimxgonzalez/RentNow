from pathlib import Path
import re

source_path = Path("modelos_inspeccionados_backup.py")
source = source_path.read_text(encoding="utf-16")

matches = list(re.finditer(r"^class (\w+)\(models\.Model\):", source, re.M))
models = {}

for i, match in enumerate(matches):
    end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
    models[match.group(1)] = source[match.start():end].rstrip()

groups = {
    "apps/users/models.py": ["Roles", "Usuarios"],
    "apps/catalog/models.py": ["Categorias", "Productos", "Publicaciones", "ImagenesPublicacion"],
    "apps/rentals/models.py": ["Alquileres", "Entregas"],
    "apps/transactions/models.py": ["Pagos", "Resenas", "Reportes"],
}

for filename, names in groups.items():
    blocks = []
    for name in names:
        block = models[name]
        block = block.replace("'Publicaciones'", "'catalog.Publicaciones'")
        block = block.replace("'Usuarios'", "'users.Usuarios'")
        block = block.replace("ForeignKey(Alquileres,", "ForeignKey('rentals.Alquileres',")
        block = block.replace("ForeignKey(Categorias,", "ForeignKey('catalog.Categorias',")
        block = block.replace("ForeignKey(Publicaciones,", "ForeignKey('catalog.Publicaciones',")
        block = block.replace("ForeignKey(Roles,", "ForeignKey('users.Roles',")
        blocks.append(block)

    text = "from django.db import models\n\n\n" + "\n\n".join(blocks) + "\n"
    Path(filename).write_text(text, encoding="utf-8")

print("Modelos regenerados en UTF-8.")
