from decimal import Decimal
from django.db import transaction
from django.utils import timezone

from apps.users.models import Usuarios, Roles
from apps.catalog.models import Categorias, Productos, Publicaciones, ImagenesPublicacion
from apps.rentals.models import Alquileres, Entregas
from apps.transactions.models import Pagos, Resenas, Reportes

modelos = [
    Roles, Usuarios, Categorias, Productos, Publicaciones,
    ImagenesPublicacion, Alquileres, Entregas, Pagos, Resenas, Reportes
]

def contar():
    return sum(m.objects.count() for m in modelos)

with transaction.atomic():
    inicial = contar()

    if inicial != 27:
        raise RuntimeError(
            f"Se esperaban 27 registros iniciales, pero hay {inicial}. "
            "No se insertaron datos."
        )

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
            nombre=f"PruebaProd{i:03}",
            descripcion=f"Producto ficticio de prueba {i} para RentNow.",
            estado=producto_base.estado,
            fecha_creacion=ahora,
            fecha_actualizacion=ahora,
        )
        for i in range(1, 37)
    ])

    Publicaciones.objects.bulk_create([
        Publicaciones(
            id_usuario=usuario,
            id_categoria=categoria,
            titulo=f"PruebaPub{i:03}",
            descripcion=f"Publicación ficticia de prueba {i} para RentNow.",
            precio_alquiler=Decimal("25000.00"),
            ubicacion="Riohacha, La Guajira",
            disponibilidad=publicacion_base.disponibilidad,
            estado=publicacion_base.estado,
            fecha_creacion=ahora,
            fecha_actualizacion=ahora,
        )
        for i in range(1, 38)
    ])

    final = contar()

    if final != 100:
        raise RuntimeError(
            f"El total resultó {final}, no 100. Se cancelará la transacción."
        )

print(f"Correcto: total inicial = {inicial}")
print("Productos de prueba agregados: 36")
print("Publicaciones de prueba agregadas: 37")
print(f"TOTAL FINAL: {final}")
