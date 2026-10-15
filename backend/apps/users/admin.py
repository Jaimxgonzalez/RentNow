from django.contrib import admin
from .models import Roles, Usuarios

for modelo in [Roles, Usuarios]:
    try:
        admin.site.register(modelo)
    except admin.sites.AlreadyRegistered:
        pass
