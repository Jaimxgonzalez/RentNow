from django.db import models


class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey('rentals.Alquileres', models.DO_NOTHING, db_column='id_alquiler')
    id_usuario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario')
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=13)
    referencia_transaccion = models.CharField(unique=True, max_length=100, blank=True, null=True)
    estado_pago = models.CharField(max_length=11)
    fecha_pago = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pagos'

class Resenas(models.Model):
    id_resena = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey('rentals.Alquileres', models.DO_NOTHING, db_column='id_alquiler')
    id_usuario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario')
    calificacion = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resenas'
        unique_together = (('id_alquiler', 'id_usuario'),)

class Reportes(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_reportante = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_reportante')
    id_usuario_reportado = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario_reportado', related_name='reportes_id_usuario_reportado_set', blank=True, null=True)
    id_publicacion = models.ForeignKey('catalog.Publicaciones', models.DO_NOTHING, db_column='id_publicacion', blank=True, null=True)
    motivo = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado_reporte = models.CharField(max_length=11)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reportes'
