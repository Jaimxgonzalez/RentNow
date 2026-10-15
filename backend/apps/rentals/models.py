from django.db import models


class Alquileres(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey('catalog.Publicaciones', models.DO_NOTHING, db_column='id_publicacion')
    id_arrendatario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_arrendatario')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    valor_garantia = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    estado_alquiler = models.CharField(max_length=10)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alquileres'

class Entregas(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey('rentals.Alquileres', models.DO_NOTHING, db_column='id_alquiler')
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=255)
    estado_entrega = models.CharField(max_length=9)
    condicion_entrega = models.CharField(max_length=255, blank=True, null=True)
    condicion_devolucion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entregas'
