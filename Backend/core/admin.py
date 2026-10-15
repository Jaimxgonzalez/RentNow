
from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import (
    Alquileres,
    Categorias,
    Entregas,
    ImagenesPublicacion,
    Pagos,
    Productos,
    Publicaciones,
    Reportes,
    Resenas,
    Roles,
    Usuarios,
)

# Registrar los 11 modelos de RentNow
modelos_rentnow = [
    Alquileres,
    Categorias,
    Entregas,
    ImagenesPublicacion,
    Pagos,
    Productos,
    Publicaciones,
    Reportes,
    Resenas,
    Roles,
    Usuarios,
]

for modelo in modelos_rentnow:
    if modelo not in admin.site._registry:
        admin.site.register(modelo)

# Quitar los modelos predeterminados de Django Admin
for modelo in [Group, User]:
    if modelo in admin.site._registry:
        admin.site.unregister(modelo)
