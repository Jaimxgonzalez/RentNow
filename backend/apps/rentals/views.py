
from django.http import JsonResponse
from .models import Alquileres
from .models import Alquileres, Entregas

def listar_alquileres(request):
    alquileres = Alquileres.objects.all()
    datos = []

    for alquiler in alquileres:
        registro = {}

        for campo in Alquileres._meta.fields:
            valor = getattr(alquiler, campo.name)

            # Convertir claves foráneas en sus identificadores
            if campo.is_relation and valor is not None:
                valor = getattr(alquiler, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def detalle_alquiler(request, id_alquiler):
    try:
        alquiler = Alquileres.objects.get(pk=id_alquiler)
    except Alquileres.DoesNotExist:
        return JsonResponse(
            {"error": "Alquiler no encontrado"},
            status=404
        )

    datos = {}

    for campo in Alquileres._meta.fields:
        valor = getattr(alquiler, campo.name)

        if campo.is_relation and valor is not None:
            valor = getattr(alquiler, campo.attname)

        datos[campo.name] = valor

    return JsonResponse(datos)


def listar_entregas(request):
    entregas = Entregas.objects.all()
    datos = []

    for entrega in entregas:
        registro = {}

        for campo in Entregas._meta.fields:
            valor = getattr(entrega, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(entrega, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)
