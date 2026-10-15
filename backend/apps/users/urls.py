
from django.urls import path
from .views import listar_roles, listar_usuarios, detalle_usuario

urlpatterns = [
    path("", listar_usuarios, name="listar_usuarios"),
    path("roles/", listar_roles, name="listar_roles"),
    path("<int:id_usuario>/", detalle_usuario,name="detalle_usuario",),
    
]
