
from django.urls import path
from .views import detalle_producto
from .views import (
    api_status,
    listar_publicaciones,
    detalle_publicacion,
    listar_categorias,
    listar_productos,
)
from .views import PublicacionesAPI, CategoriasAPI, ProductosAPI

urlpatterns = [
    path("status/", api_status, name="api_status"),
    path(
        "publicaciones/",
        listar_publicaciones,
        name="listar_publicaciones",
    ),
    path(
        "publicaciones/<int:id_publicacion>/",
        detalle_publicacion,
        name="detalle_publicacion",
    ),

    path(
    "categorias/",
    listar_categorias,
    name="listar_categorias",
),

path(
    "productos/",
    listar_productos,
    name="listar_productos",
),
path(
    "productos/<int:id_producto>/",
    detalle_producto,
    name="detalle_producto",
),
path(
    "publicaciones-rest/",
    PublicacionesAPI.as_view(),
    name="publicaciones_rest",
),

path("publicaciones-rest/", PublicacionesAPI.as_view(), name="publicaciones_rest"),
path("categorias-rest/", CategoriasAPI.as_view(), name="categorias_rest"),
path("productos-rest/", ProductosAPI.as_view(), name="productos_rest"),
]
