from django.db import models


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey('catalog.Categorias', models.DO_NOTHING, db_column='id_categoria')
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=13)
    fecha_creacion = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'

class Publicaciones(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('users.Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey('catalog.Categorias', models.DO_NOTHING, db_column='id_categoria')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio_alquiler = models.DecimalField(max_digits=12, decimal_places=2)
    ubicacion = models.CharField(max_length=255)
    disponibilidad = models.CharField(max_length=10)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicaciones'

class ImagenesPublicacion(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey('catalog.Publicaciones', models.DO_NOTHING, db_column='id_publicacion')
    url_imagen = models.CharField(max_length=500)
    es_principal = models.IntegerField()
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes_publicacion'
