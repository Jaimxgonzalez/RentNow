
from django.http import JsonResponse
from rest_framework import generics
from .models import Publicaciones, Categorias, Productos
from .serializers import PublicacionesSerializer

from django.http import JsonResponse
from rest_framework import generics
from .models import Publicaciones, Categorias, Productos
from .serializers import (
    PublicacionesSerializer,
    CategoriasSerializer,
    ProductosSerializer,
)




def api_status(request):
    return JsonResponse({
        "proyecto": "RentNow",
        "estado": "correcto",
        "mensaje": "Backend funcionando correctamente"
    })


def api_status(request):
    return JsonResponse({
        "proyecto": "RentNow",
        "estado": "correcto",
        "mensaje": "Backend funcionando correctamente"
    })


def listar_publicaciones(request):
    publicaciones = Publicaciones.objects.all()

    datos = []

    for publicacion in publicaciones:
        registro = {}

        for campo in Publicaciones._meta.fields:
            valor = getattr(publicacion, campo.name)

            # Convertir las relaciones a sus identificadores
            if campo.is_relation and valor is not None:
                valor = getattr(
                    publicacion,
                    campo.attname
                )

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def detalle_publicacion(request, id_publicacion):
    try:
        publicacion = Publicaciones.objects.get(
            pk=id_publicacion
        )
    except Publicaciones.DoesNotExist:
        return JsonResponse(
            {"error": "Publicación no encontrada"},
            status=404
        )

    datos = {}

    for campo in Publicaciones._meta.fields:
        valor = getattr(publicacion, campo.name)

        if campo.is_relation and valor is not None:
            valor = getattr(publicacion, campo.attname)

        datos[campo.name] = valor

    return JsonResponse(datos)


def listar_categorias(request):
    categorias = Categorias.objects.all()
    datos = []

    for categoria in categorias:
        registro = {}

        for campo in Categorias._meta.fields:
            valor = getattr(categoria, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(categoria, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def listar_productos(request):
    productos = Productos.objects.all()
    datos = []

    for producto in productos:
        registro = {}

        for campo in Productos._meta.fields:
            valor = getattr(producto, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(producto, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def detalle_producto(request, id_producto):
    try:
        producto = Productos.objects.get(pk=id_producto)
    except Productos.DoesNotExist:
        return JsonResponse(
            {"error": "Producto no encontrado"},
            status=404
        )

    datos = {}

    for campo in Productos._meta.fields:
        valor = getattr(producto, campo.name)

        if campo.is_relation and valor is not None:
            valor = getattr(producto, campo.attname)

        datos[campo.name] = valor

    return JsonResponse(datos)

class PublicacionesAPI(generics.ListAPIView):
    queryset = Publicaciones.objects.all()
    serializer_class = PublicacionesSerializer

class PublicacionesAPI(generics.ListAPIView):
    queryset = Publicaciones.objects.all()
    serializer_class = PublicacionesSerializer


class CategoriasAPI(generics.ListAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProductosAPI(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer    