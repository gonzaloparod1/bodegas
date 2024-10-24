
1. Comandos para iniciar un proyecto

```bash 
virtualenv venv 
source venv/Scripts/activate
pip install django 
pip install python-dotenv
pip install psycopg2

django-admin startproject base_project . 
python manage.py startapp web

pip freeze > requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

pip install -r requirements.txt
```
2. Estructura carpetas y archivos 
    - Crear .gitignore
    - Crear el .env 
    - Crear el doc. README 
    - Anexar la app en el settings.py 
    - Crear la carpeta templates en la app 
    - Crear la carpeta static en la app 
    - Modularizar el urls del project a la/s app/s (include)

3. Postgres SQL 

