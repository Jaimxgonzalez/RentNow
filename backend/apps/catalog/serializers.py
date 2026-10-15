
from rest_framework import serializers
from .models import Publicaciones, Categorias, Productos


class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
        fields = "__all__"


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = "__all__"


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = "__all__"
