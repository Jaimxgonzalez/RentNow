from rest_framework import serializers
from .models import Usuarios


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = [
            'id_usuario',
            'id_rol',
            'nombre',
            'correo',
            'telefono',
            'tipo_documento',
            'numero_documento',
            'estado',
            'fecha_creacion',
            'fecha_actualizacion',
            'fecha_eliminacion',
        ]