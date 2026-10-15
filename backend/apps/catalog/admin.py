from django.contrib import admin
from .models import Categorias, Productos, Publicaciones, ImagenesPublicacion

for modelo in [Categorias, Productos, Publicaciones, ImagenesPublicacion]:
    try:
        admin.site.register(modelo)
    except admin.sites.AlreadyRegistered:
        pass
