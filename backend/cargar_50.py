from decimal import Decimal
from django.db import transaction
from django.utils import timezone

from apps.users.models import Usuarios
from apps.catalog.models import Categorias, Productos, Publicaciones

modelos = [
    Usuarios, Categorias, Productos, Publicaciones
]

with transaction.atomic():
    usuario = Usuarios.objects.first()
    categoria = Categorias.objects.first()
    producto_base = Productos.objects.first()
    publicacion_base = Publicaciones.objects.first()

    if not all([usuario, categoria, producto_base, publicacion_base]):
        raise RuntimeError("Faltan registros base. No se insertaron datos.")

    ahora = timezone.now()

    Productos.objects.bulk_create([
        Productos(
            id_usuario=usuario,
            id_categoria=categoria,
            nombre=f"ExtraProd{i:03}",
            descripcion=f"Producto ficticio adicional {i} para pruebas de RentNow.",
            estado=producto_base.estado,
            fecha_creacion=ahora,
            fecha_actualizacion=ahora,
        )
        for i in range(1, 26)
    ])

    Publicaciones.objects.bulk_create([
        Publicaciones(
            id_usuario=usuario,
            id_categoria=categoria,
            titulo=f"ExtraPub{i:03}",
            descripcion=f"Publicación ficticia adicional {i} para pruebas de RentNow.",
            precio_alquiler=Decimal("25000.00"),
            ubicacion="Riohacha, La Guajira",
            disponibilidad=publicacion_base.disponibilidad,
            estado=publicacion_base.estado,
            fecha_creacion=ahora,
            fecha_actualizacion=ahora,
        )
        for i in range(1, 26)
    ])

    print("Productos adicionales:", 25)
    print("Publicaciones adicionales:", 25)
    print("Productos totales:", Productos.objects.count())
    print("Publicaciones totales:", Publicaciones.objects.count())
    print("Registros agregados:", 50)
