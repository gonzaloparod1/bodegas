# PROYECTO - GENERIC-APP

**En las pruebas tècnicas no se menciona ni solicita el uso de `.env` (variables de entorno), pero cabe aclarar que es una buena práctica el implementarlas**

1. Iniciar Proyecto
2. Implementar postgres SQL 
3. Crear los modelos 
4. Crear DB en postgres SQL
**.env**
```bash
ENGINE=django.db.backends.postgresql
NAME=MISMO-NOMBRE-DE-LA-BASE-DE-DATOS-QUE-DEBEMOS-CREAR
USER=postgres
HOST=127.0.0.1
PORT=5432
PASSWORD=1234
DEBUG=True
TEST_ENV= test-.env
DJANGO_SETTINGS_MODULE=mysite.settings
DJANGO_SETTINGS_TEST=hola-mundo-temp
```
5. Poblar de datos nuestra DB (data semilla - load-data)
6. MIGRAR
7. Crear servicios en nuestro services.py
8. Testeo de nuestra DB desde el temp.py, o desde el services usando la SHELL
9. Ver Vistas Básicas
    - ● Vista Presentación `"/"` - Tipo LandingPage o Vista tipo Lista simple de inicio para no registrados
        - O en `"/"` solo una función de lógica que re-direcciona a "/login" || "/aaaaa"  ||  "/bbbbb"
    - ● Login 
    - ● Register 
    - ● Register_tipo_usuario (si la requiere) 
    - ● Vista Lista de Productos
    - ● Vista Ver Perfil
    - ● Vista Editar Perfil

 
10. Revisar nuestras estructuras Html (templates)
    - base.html 
    - navBar.html
    - footer.html
    - about.html
- Formularios
    - Registro
    - Inicio sesión 
    - Alguna vista simple 

11. Revisar la urls
```py
urlpatterns = [
    path('', index, name='home'),
    path('accounts/register', register, name='register'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    
    path('profile', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
#███████████████████████████████████████████████████████████████████████████████████████████████████
    # PATH (routes) SIMPLES 
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

#███████████████████████████████████████████████████████████████████████████████████████████████████
    # TODO__ PATH (urls - ROUTES) - AAAAA
    path('index_a', index_a, name='aaaaa'),
#███████████████████████████████████████████████████████████████████████████████████████████████████
    # TODO__ PATH (urls - ROUTES) - BBBBB
    path('index_b', index_b, name="bbbbb"),
]
```
12. Revisar los FORMS ya iniciados
13. Crear el superuser (admin)
14. Levantar la app
15. Testear y corregir
16. Dejar funcinal el PROJECT BASE
17. Subir a GIT y hacer primer COMMIT

¡Felicidades!!!
