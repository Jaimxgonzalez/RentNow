from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UsuarioViewSet,
    login_usuario,
    registro,
    listar_categorias,
    productos,
    publicar_producto,
)

from .views import (
    UsuarioViewSet,
    login_usuario,
    registro,
    listar_categorias,
    productos,
    publicar_producto,
    logout_usuario,
)
from core import views
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', registro, name='registro'),
    path('login/', login_usuario, name='login'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('productos/', productos, name='productos'),
    path('publicar-producto/', publicar_producto, name='publicar_producto'),
    path('logout/', logout_usuario, name='logout'),
    path('alquilar-producto/<int:id_publicacion>/',views.alquilar_producto, name='alquilar_producto'),
    path('alquilar-producto/<int:id_publicacion>/', views.alquilar_producto, name='alquilar_producto'),
    
]


