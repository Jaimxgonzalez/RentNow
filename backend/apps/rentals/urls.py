
from django.urls import path
from .views import (listar_alquileres,detalle_alquiler,listar_entregas,)

urlpatterns = [
    path("", listar_alquileres, name="listar_alquileres"),
    path(
        "<int:id_alquiler>/",
        detalle_alquiler,
        name="detalle_alquiler",
    ),
    path(
    "entregas/",
    listar_entregas,
    name="listar_entregas",
),
]
