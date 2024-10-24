# Proyecto Bodegas

## Descripción

**Bodegas Web** es una aplicación web desarrollada con **Django** y **PostgreSQL** para solicitar cotizaciones de bodegas con una pagina principal de noticias.

### Funcionalidades Principales

- **Registro de Usuarios**: Autenticación con roles de arrendador o arrendatario.
- **Dar like a noticias**
- **Solicitudes de Cotizaciones**: Los arrendatarios envían solicitudes que los arrendadores pueden aprobar o rechazar.
- **Ver resumen de Cotización solicitada**

## Instalación

Sigue estos pasos para configurar el proyecto localmente.

### Prerrequisitos

- **Python 3.8+**
- **Django 4.1+**
- **PostgreSQL 12+**
- **pip** y **virtualenv** instalados


### Paso 2: Crear y Activar un Entorno Virtual

```bash
virtualenv venv
source venv/Scripts/activate  # En diferentes a Windows: venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Configurar Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con tus credenciales de base de datos:

```bash
ENGINE=django.db.backends.postgresql
NAME=tu_bd
USER=tu_usuario
HOST=127.0.0.1
PORT=5432
PASSWORD=tu_contraseña

DEBUG='True'
TEST_ENV= test-.env
DJANGO_SETTINGS_MODULE=bodegas.settings
SECRET_KEY='tu_secret_key'
```

### Paso 5: Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## Ejecutar el Proyecto

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre el navegador en `http://127.0.0.1:8000/`.

## Cargar Datos Iniciales

El proyecto incluye datos de ejemplo. Para cargarlos, ejecuta:

```bash
python manage.py loaddata web/data/users.json
python manage.py loaddata web/data/noticias.json
python manage.py loaddata web/data/tipo_bodegas.json
python manage.py loaddata web/data/bodegas.json
```

## Generar Dump de la Base de Datos
Un "dump" es una copia de seguridad completa de la base de datos.

Aquí pueden **indicar el `nombre_de_archivo.json` (o archivos) donde se encuentra nuestro dump** (volcado de datos), como también podemos indicar de como pueden crear su propio **dump**. Ejemplo:

- En este proyecto se debe encontrar en el archivo `all_data.json` y se ha creado mediante el siguiente comando para volcar todos los datos de tu base de datos en un archivo JSON y SAQL:

```bash
python manage.py dumpdata --indent 4 > all_data.json
```
Así se pueden exportar los datos de tu base de datos a un archivo JSON


```bash
pg_dump -u postgres -h localhost nombre_db >> nombre_db.sql
```
Así se pueden exportar los datos de tu base de datos a un archivo SQL

## Comandos Principales


- **Crear entorno virtual**: `virtualenv venv`
- **Activar entorno virtual (Windows)**: `source venv/Scripts/activate`
- **Instalar dependencias**: `pip install -r requirements.txt`
- **Crear migraciones**: `python manage.py makemigrations`
- **Aplicar migraciones**: `python manage.py migrate`
- **Ejecutar servidor de desarrollo**: `python manage.py runserver`
- **Crear superusuario**: `python manage.py createsuperuser`
- **Ejecutar pruebas**: `python manage.py test`

## Credenciales de Prueba

### Administrador
- **Usuario**: admin  
- **Email**: admin@mail.com  
- **Contraseña**: 1234

### Usuarios Generados
Se han creado usuarios de prueba, todos con la contraseña `1234`.

### Subir el Archivo Comprimido
- A modo de entrega se sube el archivo `.zip` a la plataforma designada en la opción “Entrega prueba de certificación”.


- **Verifica la Configuración:** Asegúrate de que todas las rutas y configuraciones en `settings.py` sean correctas.
- **Pruebas de Funcionamiento:** Ejecuta el servidor y prueba todas las funcionalidades antes de la entrega.
- **Documentación Completa:** Completa el README con toda la información necesaria para que otros puedan entender y ejecutar el proyecto sin inconvenientes.
- **Buenas Prácticas:** Implementa y sigue buenas prácticas de desarrollo, como el uso de variables de entorno y la modularización del código.

### Rutas

- "/data"
- "/migrations"
- "/templates"
- "/static"
- "/management
- "/registration

### Integrantes

- Gonzalo Parodi 
  - [GitHub](<https://github.com/gonzaloparod1>)

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE.md).

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de [gonzalo.parodi@gmail.com].