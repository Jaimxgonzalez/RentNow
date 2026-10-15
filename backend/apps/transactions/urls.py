
from django.urls import path
from .views import listar_pagos, detalle_pago
from .views import listar_pagos, detalle_pago, listar_resenas
from .models import Pagos, Resenas, Reportes
from .views import (listar_reportes,)

urlpatterns = [
    path("pagos/", listar_pagos, name="listar_pagos"),
    path(
        "pagos/<int:id_pago>/",
        detalle_pago,
        name="detalle_pago",
    ),
    path(
    "resenas/",
    listar_resenas,
    name="listar_resenas",
),
path(
    "reportes/",
    listar_reportes,
    name="listar_reportes",
),
]
