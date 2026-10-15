from django.contrib import admin
from .models import Pagos, Resenas, Reportes

for modelo in [Pagos, Resenas, Reportes]:
    try:
        admin.site.register(modelo)
    except admin.sites.AlreadyRegistered:
        pass
