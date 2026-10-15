
from django.http import JsonResponse
from .models import Pagos, Reportes
from .models import Pagos, Resenas

def listar_pagos(request):
    pagos = Pagos.objects.all()
    datos = []

    for pago in pagos:
        registro = {}

        for campo in Pagos._meta.fields:
            valor = getattr(pago, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(pago, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def detalle_pago(request, id_pago):
    try:
        pago = Pagos.objects.get(pk=id_pago)
    except Pagos.DoesNotExist:
        return JsonResponse(
            {"error": "Pago no encontrado"},
            status=404
        )

    datos = {}

    for campo in Pagos._meta.fields:
        valor = getattr(pago, campo.name)

        if campo.is_relation and valor is not None:
            valor = getattr(pago, campo.attname)

        datos[campo.name] = valor

    return JsonResponse(datos)


def listar_resenas(request):
    resenas = Resenas.objects.all()
    datos = []

    for resena in resenas:
        registro = {}

        for campo in Resenas._meta.fields:
            valor = getattr(resena, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(resena, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)


def listar_reportes(request):
    reportes = Reportes.objects.all()
    datos = []

    for reporte in reportes:
        registro = {}

        for campo in Reportes._meta.fields:
            valor = getattr(reporte, campo.name)

            if campo.is_relation and valor is not None:
                valor = getattr(reporte, campo.attname)

            registro[campo.name] = valor

        datos.append(registro)

    return JsonResponse(datos, safe=False)

