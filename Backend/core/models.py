# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alquileres(models.Model):
    id_alquiler = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey('Publicaciones', models.DO_NOTHING, db_column='id_publicacion')
    id_arrendatario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_arrendatario')
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entregas(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey(Alquileres, models.DO_NOTHING, db_column='id_alquiler')
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


class ImagenesPublicacion(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey('Publicaciones', models.DO_NOTHING, db_column='id_publicacion')
    url_imagen = models.CharField(max_length=500)
    es_principal = models.IntegerField()
    estado = models.CharField(max_length=8)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_eliminacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes_publicacion'


class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey(Alquileres, models.DO_NOTHING, db_column='id_alquiler')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
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


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
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
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
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


class Reportes(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_reportante = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_reportante')
    id_usuario_reportado = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_reportado', related_name='reportes_id_usuario_reportado_set', blank=True, null=True)
    id_publicacion = models.ForeignKey(Publicaciones, models.DO_NOTHING, db_column='id_publicacion', blank=True, null=True)
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


class Resenas(models.Model):
    id_resena = models.AutoField(primary_key=True)
    id_alquiler = models.ForeignKey(Alquileres, models.DO_NOTHING, db_column='id_alquiler')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
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
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol')
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
