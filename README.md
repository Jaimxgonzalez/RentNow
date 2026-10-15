# RentNow

Alquiler de productos por horas entre usuarios, con garantía y pagos retenidos.

## Contexto académico

- Universidad: Universidad de La Guajira, Facultad de Ingeniería
- Curso: Ingeniería de Software I
- Grupo: B1
- Docente: Ing. Robert Damián Quintero Laverde
- Integrantes:
  Cristian David Muñoz Hernández
  Maria Camila Hernandez Valencia
  Jaime Rafael Gonzalez Ballesta

## Descripción del problema y la solución

Mucha gente necesita un producto solo por unas horas y comprarlo no tiene sentido, mientras que otros tienen objetos que casi no usan. RentNow es un "marketplace" entre usuarios: el propietario publica un producto con su precio por hora, el interesado lo busca en el catálogo y lo alquila por el tiempo que necesita. El pago queda retenido y se respalda con una garantía hasta que el producto se devuelve en buen estado.

## Stack tecnológico

- Django
- Django REST Framework
- MySQL (driver `mysqlclient`)
- Pillow (subida de imágenes)
- python-dotenv (variables de entorno)
- Autenticación por sesión de Django, con contraseñas hasheadas

## Estructura del proyecto

 ```bash
.gitignore              # Archivos y carpetas ignorados por Git
README.md               # Documentación principal del proyecto
requirements.txt        # Dependencias de Python necesarias
Base de datos rentnow.sql  # Script SQL con la estructura de la base de datos

Backend/
  manage.py             # Script principal para comandos de Django
  .env.example          # Variables de entorno de ejemplo
  config/               # Configuración global del proyecto (settings, urls, wsgi)
  core/                 # Lógica central, apps base y utilidades
                        
 ```                              


## Instalación y puesta en marcha

Los comandos de Django se ejecutan desde la carpeta `Backend/`.

1. Clonar el repositorio:

   ```bash
   git clone [URL del repositorio]
   cd RentNow
   ```

2. Crear y activar el entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:

   ```bash
   cd Backend
   cp .env.example .env          # Windows: copy .env.example .env
   ```

   Edita `.env` con tus valores (ver la sección siguiente).

5. Crear la base de datos en MySQL e importar el esquema:

   ```bash
   mysql -u <usuario> -p -e "CREATE DATABASE rentnow CHARACTER SET utf8mb4;"
   mysql -u <usuario> -p rentnow < "../Base de datos rentnow.sql"
   ```

6. Correr las migraciones:

   ```bash
   python manage.py migrate
   ```

   Los modelos de `core` usan `managed = False`, por lo que Django no crea las tablas de negocio: el esquema sale del `.sql` del paso anterior. `migrate` solo crea las tablas internas de Django (auth, sessions, admin, etc.).

7. Crear el superusuario:

   ```bash
   python manage.py createsuperuser
   ```

8. Levantar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

## Variables de entorno

`Backend/config/settings.py` lee estas variables desde `Backend/.env`.

| Variable | Descripción | Ejemplo |
|---|---|---|
| `SECRET_KEY` | Clave secreta de Django (obligatoria) | `cambia-esta-clave-por-una-larga-y-aleatoria` |
| `DEBUG` | Modo depuración (`True` o `False`; por defecto `False`) | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos, separados por coma | `localhost,127.0.0.1` |
| `DB_NAME` | Nombre de la base de datos (por defecto `rentnow`) | `rentnow` |
| `DB_USER` | Usuario de MySQL (por defecto `root`) | `usuario_mysql` |
| `DB_PASSWORD` | Contraseña de MySQL (obligatoria) | `contrasena_mysql` |
| `DB_HOST` | Host de MySQL (por defecto `127.0.0.1`) | `127.0.0.1` |
| `DB_PORT` | Puerto de MySQL (por defecto `3306`) | `3306` |

El repositorio incluye `Backend/.env.example` con estos nombres y valores ficticios. `.env` está en `.gitignore`: nunca se suben credenciales reales.

## Documentación de la API

Todas las rutas cuelgan del prefijo `/api/`, salvo `/` y `/admin/`.

| Método | Ruta | Descripción | Requiere autenticación |
|---|---|---|---|
| GET | `/` | Página de inicio | No |
| GET, POST | `/api/registro/` | Formulario y registro de usuario | No |
| GET, POST | `/api/login/` | Formulario e inicio de sesión | No |
| GET, POST | `/api/usuarios/` | Listar y crear usuarios (ViewSet de DRF) | [Por definir] |
| GET, PUT, PATCH, DELETE | `/api/usuarios/{id}/` | Detalle, actualización y eliminación de un usuario | [Por definir] |
| GET | `/api/categorias/` | Lista de categorías activas en JSON | No |
| GET | `/api/productos/` | Catálogo de publicaciones disponibles | No |
| GET, POST | `/api/publicar-producto/` | Formulario y publicación de un producto con imagen | Sí (sesión) |
| — | `/admin/` | Panel de administración de Django | Sí (staff) |


## Metodología de desarrollo

El proyecto se gestiona con Scrumban.

## Diagramas y documentación adicional

- Diagrama entidad-relación: [ruta o enlace][RentNow.png.pdf](https://github.com/user-attachments/files/33233714/RentNow.png.pdf)

- Diagrama de casos de uso: [ruta o enlace][diagrama de casos de usos.pdf](https://github.com/user-attachments/files/33233655/diagrama.de.casos.de.usos.pdf)

- Entregables : [ruta o enlace]<img width="1756" height="414" alt="diagrama de componentes" src="https://github.com/user-attachments/assets/89fa7d3f-03d6-4f7c-8e8d-aeb303b0ea2b" />



- 
- 


## Pruebas

```bash
cd Backend
python manage.py test
python manage.py test core    # solo la app core
```

`core/tests.py` está vacío por ahora.
