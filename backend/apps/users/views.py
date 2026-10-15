
from django.http import JsonResponse
from .models import Roles, Usuarios


def listar_roles(request):
    roles = Roles.objects.all()
    datos = []

    for rol in roles:
        registro = {}

        for campo in Roles._meta.fields:
            valor = getattr(rol, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(rol, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def listar_usuarios(request):
    usuarios = Usuarios.objects.all()
    datos = []

    # Campos permitidos para mostrar en la API
    campos_publicos = [
        campo.name
        for campo in Usuarios._meta.fields
        if campo.name not in {
            "password",
            "contrasena",
            "contrasena_hash",
            "token",
        }
    ]

    for usuario in usuarios:
        registro = {}

        for nombre in campos_publicos:
            campo = Usuarios._meta.get_field(nombre)
            valor = getattr(usuario, nombre)

            if campo.is_relation and valor is not None:
                valor = getattr(usuario, campo.attname)

            registro[nombre] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


from django.shortcuts import get_object_or_404


def detalle_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuarios, pk=id_usuario)

    # Solo exponer campos permitidos
    campos_excluidos = {
        "password",
        "contrasena",
        "contrasena_hash",
        "token",
    }

    datos = {}

    for campo in Usuarios._meta.fields:
        if campo.name in campos_excluidos:
            continue

        valor = getattr(usuario, campo.name)

        if campo.is_relation and valor is not None:
            valor = getattr(usuario, campo.attname)

        datos[campo.name] = valor

    return JsonResponse(datos)
