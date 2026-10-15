
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Publicaciones
from pathlib import Path
from decimal import Decimal, InvalidOperation
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import default_storage
from django.db import transaction
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import viewsets

from .models import (
    Usuarios,
    Categorias,
    Productos,
    Publicaciones,
    ImagenesPublicacion,
)
from .serializers import UsuarioSerializer


# ==========================================
# PÁGINA DE INICIO
# ==========================================

def home(request):
    return render(request, 'core/inicio.html')


# ==========================================
# REGISTRO DE USUARIOS
# ==========================================

def registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        correo = request.POST.get('correo', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        tipo_documento = request.POST.get('tipo_documento', '').strip()
        numero_documento = request.POST.get(
            'numero_documento', ''
        ).strip()
        contrasena = request.POST.get('contrasena', '')
        confirmar_contrasena = request.POST.get(
            'confirmar_contrasena', ''
        )

        if not all([
            nombre, correo, tipo_documento,
            numero_documento, contrasena, confirmar_contrasena
        ]):
            return render(request, 'core/registro.html', {
                'error': 'Completa todos los campos obligatorios.'
            })

        if contrasena != confirmar_contrasena:
            return render(request, 'core/registro.html', {
                'error': 'Las contraseñas no coinciden.'
            })

        if Usuarios.objects.filter(correo=correo).exists():
            return render(request, 'core/registro.html', {
                'error': 'El correo electrónico ya está registrado.'
            })

        if Usuarios.objects.filter(
            numero_documento=numero_documento
        ).exists():
            return render(request, 'core/registro.html', {
                'error': 'El número de documento ya está registrado.'
            })

        Usuarios.objects.create(
            id_rol_id=4,
            nombre=nombre,
            correo=correo,
            telefono=telefono or None,
            contrasena=make_password(contrasena),
            tipo_documento=tipo_documento,
            numero_documento=numero_documento,
            estado='activo'
        )

        return redirect('/api/login/')

    return render(request, 'core/registro.html')


# ==========================================
# INICIO DE SESIÓN
# ==========================================

def login_usuario(request):
    if request.method == 'POST':
        correo = request.POST.get('correo', '').strip()
        contrasena = request.POST.get('contrasena', '')

        usuario = Usuarios.objects.filter(
            correo=correo,
            estado='activo',
            fecha_eliminacion__isnull=True
        ).first()

        if usuario and check_password(
            contrasena, usuario.contrasena
        ):
            request.session['id_usuario'] = usuario.id_usuario
            request.session['nombre_usuario'] = usuario.nombre
            request.session['primer_nombre'] = (
                usuario.nombre.strip().split()[0]
            )
            request.session['id_rol'] = usuario.id_rol_id

            return redirect('/api/productos/')

        return render(request, 'core/login.html', {
            'error': 'Correo o contraseña incorrectos.'
        })

    return render(request, 'core/login.html')


# ==========================================
# LISTAR CATEGORÍAS
# ==========================================

def listar_categorias(request):
    categorias = Categorias.objects.filter(
        estado='activo',
        fecha_eliminacion__isnull=True
    ).order_by('nombre')

    datos = [
        {
            'id_categoria': categoria.id_categoria,
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
        }
        for categoria in categorias
    ]

    return JsonResponse(datos, safe=False)


# ==========================================
# CATÁLOGO DE PRODUCTOS
# ==========================================

def productos(request):
    publicaciones = Publicaciones.objects.filter(
        estado='activo',
        disponibilidad='disponible',
        fecha_eliminacion__isnull=True
    ).select_related(
        'id_usuario',
        'id_categoria'
    ).order_by('-fecha_creacion')

    datos_publicaciones = []

    print("USUARIO EN SESIÓN:", request.session.get('id_usuario'))

    for publicacion in publicaciones:
        imagen = ImagenesPublicacion.objects.filter(
            id_publicacion_id=publicacion.id_publicacion,
            estado='activo',
            fecha_eliminacion__isnull=True
        ).order_by('-es_principal', 'id_imagen').first()

        datos_publicaciones.append({
            'id_publicacion': publicacion.id_publicacion,
            'titulo': publicacion.titulo,
            'descripcion': publicacion.descripcion,
            'precio_alquiler': publicacion.precio_alquiler,
            'ubicacion': publicacion.ubicacion,
            'categoria': publicacion.id_categoria.nombre,
            'propietario': publicacion.id_usuario.nombre,
            'imagen': imagen.url_imagen if imagen else None,
            'disponibilidad': publicacion.disponibilidad,
        })

    return render(
        request,
        'core/productos.html',
        {'publicaciones': datos_publicaciones}
    )


# ==========================================
# PUBLICAR PRODUCTO
# ==========================================

def publicar_producto(request):
    id_usuario = request.session.get('id_usuario')

    # Verificar sesión
    if not id_usuario:
        return redirect('/api/login/')

    # Verificar que el usuario siga activo
    usuario = Usuarios.objects.filter(
        id_usuario=id_usuario,
        estado='activo',
        fecha_eliminacion__isnull=True
    ).first()

    if not usuario:
        request.session.flush()
        return redirect('/api/login/')

    categorias = Categorias.objects.filter(
        estado='activo',
        fecha_eliminacion__isnull=True
    ).order_by('nombre')

    contexto = {'categorias': categorias}

    if request.method != 'POST':
        return render(
            request,
            'core/publicar_producto.html',
            contexto
        )

    # Obtener datos del formulario
    titulo = request.POST.get('titulo', '').strip()
    descripcion = request.POST.get('descripcion', '').strip()
    ubicacion = request.POST.get('ubicacion', '').strip()
    id_categoria = request.POST.get('id_categoria', '').strip()
    precio_texto = request.POST.get('precio_alquiler', '').strip()
    imagen = request.FILES.get('imagen')

    # Validar campos obligatorios
    if not all([
        titulo, descripcion, ubicacion,
        id_categoria, precio_texto
    ]):
        contexto['error'] = 'Completa todos los campos obligatorios.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    if len(titulo) > 150 or len(ubicacion) > 255:
        contexto['error'] = 'El nombre o la ubicación son demasiado largos.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    # Validar precio
    try:
        precio = Decimal(precio_texto)

        if (
            not precio.is_finite()
            or precio <= 0
            or precio >= Decimal('10000000000')
        ):
            raise InvalidOperation

        precio = precio.quantize(Decimal('0.01'))

    except (InvalidOperation, ValueError):
        contexto['error'] = 'Introduce un precio válido mayor que cero.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    # Validar categoría
    categoria = Categorias.objects.filter(
        id_categoria=id_categoria,
        estado='activo',
        fecha_eliminacion__isnull=True
    ).first()

    if not categoria:
        contexto['error'] = 'Selecciona una categoría válida.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    # Validar imagen
    if not imagen:
        contexto['error'] = 'Debes seleccionar una imagen.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    extensiones_permitidas = {'.jpg', '.jpeg', '.png', '.webp'}
    extension = Path(imagen.name).suffix.lower()

    if extension not in extensiones_permitidas:
        contexto['error'] = 'La imagen debe ser JPG, PNG o WEBP.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    if imagen.size > 5 * 1024 * 1024:
        contexto['error'] = 'La imagen no puede superar los 5 MB.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    if imagen.content_type not in {
        'image/jpeg', 'image/png', 'image/webp'
    }:
        contexto['error'] = 'El archivo seleccionado no es válido.'
        return render(
            request, 'core/publicar_producto.html', contexto
        )

    # Guardar imagen y registros en MySQL
    ruta_imagen = None

    try:
        with transaction.atomic():
            ahora = timezone.now()

            # Guardar la fotografía
            ruta_imagen = default_storage.save(
                f'publicaciones/{imagen.name}',
                imagen
            )

            # TABLA 1: PRODUCTOS
            producto = Productos.objects.create(
                id_usuario_id=usuario.id_usuario,
                id_categoria_id=categoria.id_categoria,
                nombre=titulo,
                descripcion=descripcion,
                estado='disponible',
                fecha_creacion=ahora,
                fecha_actualizacion=ahora
            )

            # TABLA 2: PUBLICACIONES
            # Estado activo y disponibilidad disponible al publicar.
            publicacion = Publicaciones.objects.create(
                id_usuario_id=usuario.id_usuario,
                id_categoria_id=categoria.id_categoria,
                titulo=titulo,
                descripcion=descripcion,
                precio_alquiler=precio,
                ubicacion=ubicacion,
                disponibilidad='disponible',
                estado='activo',
                fecha_creacion=ahora,
                fecha_actualizacion=ahora
            )

            # TABLA 3: IMAGENES_PUBLICACION
            ImagenesPublicacion.objects.create(
                id_publicacion_id=publicacion.id_publicacion,
                url_imagen=ruta_imagen,
                es_principal=1,
                estado='activo',
                fecha_creacion=ahora,
                fecha_actualizacion=ahora
            )

    except Exception:
        if ruta_imagen and default_storage.exists(ruta_imagen):
            default_storage.delete(ruta_imagen)
        raise

    return redirect('/api/productos/')


# ==========================================
# CERRAR SESIÓN
# ==========================================

def logout_usuario(request):
    request.session.flush()
    return redirect('/')





# ==========================================
# ALQUILAR PRODUCTO
# ==========================================

def alquilar_producto(request, id_publicacion):
    id_usuario = request.session.get('id_usuario')

    # Verificar sesión activa
    if not id_usuario:
        return redirect('/api/login/')

    # Obtener información del usuario logueado
    usuario = Usuarios.objects.filter(
        id_usuario=id_usuario,
        estado='activo',
        fecha_eliminacion__isnull=True
    ).first()

    if not usuario:
        request.session.flush()
        return redirect('/api/login/')

    # Obtener información del producto a alquilar
    publicacion = Publicaciones.objects.filter(
        id_publicacion=id_publicacion,
        estado='activo',
        disponibilidad='disponible',
        fecha_eliminacion__isnull=True
    ).select_related('id_categoria', 'id_usuario').first()

    # Si el producto no existe o ya no está disponible
    if not publicacion:
        return redirect('/api/productos/')

    # Obtener la imagen principal del producto
    imagen = ImagenesPublicacion.objects.filter(
        id_publicacion_id=publicacion.id_publicacion,
        estado='activo',
        fecha_eliminacion__isnull=True
    ).order_by('-es_principal', 'id_imagen').first()

    contexto = {
        'usuario': usuario,
        'publicacion': publicacion,
        'imagen': imagen.url_imagen if imagen else None,
    }

    if request.method == 'POST':
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        comentarios = request.POST.get('comentarios', '').strip()

        if not fecha_inicio or not fecha_fin:
            contexto['error'] = 'Por favor selecciona las fechas de alquiler.'
            # ⬇️ Apunta a alquilar.html
            return render(request, 'core/alquilar.html', contexto)

     

        return redirect('/api/productos/')

    # ⬇️ Apunta a alquilar.html
    return render(request, 'core/alquilar.html', contexto)
# ==========================================
# API DE USUARIOS
# ==========================================

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
