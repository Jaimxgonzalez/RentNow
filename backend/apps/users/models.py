from django.db import models


class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_rol = models.ForeignKey('users.Roles', models.DO_NOTHING, db_column='id_rol')
    nombre = models.CharField(max_length=150)
    correo = models.CharField(unique=True, max_length=150)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    contrasena = models.CharField(max_length=255)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.CharField(unique=True, max_length=30)
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
