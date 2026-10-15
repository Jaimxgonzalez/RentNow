from django.contrib import admin
from .models import Alquileres, Entregas

for modelo in [Alquileres, Entregas]:
    try:
        admin.site.register(modelo)
    except admin.sites.AlreadyRegistered:
        pass
