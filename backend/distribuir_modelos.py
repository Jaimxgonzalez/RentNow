from pathlib import Path
import re

source = Path("modelos_inspeccionados.py").read_text(encoding="utf-16")

# Extraer cada modelo generado por inspectdb.
matches = list(re.finditer(r"^class (\w+)\(models\.Model\):", source, re.M))
models = {}

for i, match in enumerate(matches):
    end = matches[i + 1].start() if i + 1 < len(matches) else len(source)
    models[match.group(1)] = source[match.start():end].rstrip() + "\n"

groups = {
    "apps/users/models.py": ["Roles", "Usuarios"],
    "apps/catalog/models.py": ["Categorias", "Productos", "Publicaciones", "ImagenesPublicacion"],
    "apps/rentals/models.py": ["Alquileres", "Entregas"],
    "apps/transactions/models.py": ["Pagos", "Resenas", "Reportes"],
}

# Referencias entre aplicaciones.
refs = {
    "'Publicaciones'": "'catalog.Publicaciones'",
    "'Usuarios'": "'users.Usuarios'",
    "ForeignKey(Alquileres,": "ForeignKey('rentals.Alquileres',",
    "ForeignKey(Categorias,": "ForeignKey('catalog.Categorias',",
    "ForeignKey(Publicaciones,": "ForeignKey('catalog.Publicaciones',",
    "ForeignKey(Roles,": "ForeignKey('users.Roles',",
    "ForeignKey(Alquileres,": "ForeignKey('rentals.Alquileres',",
}

for filename, names in groups.items():
    blocks = []
    for name in names:
        if name not in models:
            raise SystemExit(f"No se encontró el modelo: {name}")
        block = models[name]
        for old, new in refs.items():
            block = block.replace(old, new)
        blocks.append(block)

    output = (
        "from django.db import models\n\n\n"
        + "\n\n".join(blocks)
    )
    Path(filename).write_text(output, encoding="utf-16")
    print(f"Actualizado: {filename}")

print("Modelos distribuidos. No se ejecutaron migraciones.")


