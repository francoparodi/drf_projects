# Project setup
## Linux

### Django Rest Framework

```sh
python3 -m venv .venv

source .venv/bin/activate

pip install django djangorestframework

pip install psycopg2-binary

django-admin startproject <project_name>

cd <project_name>

python manage.py startapp <app_name>

```

Create admin user:
```sh
python manage.py createsuperuser
```

### DB connection configuration

Add to 'settings.py' file the 'rest_framework' app and all other apps (es. <app_name>)

```sh
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    <app_name>,
]
```

Create/run docker postgres container (need docker installed on system):

```sh
docker pull postgres
docker run --name file_provider_db -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

Be sure to start container automatically:

```sh
docker update --restart unless-stopped $(docker ps -aq)
```

Configure DB parameters:

```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres', 
        'PASSWORD': 'postgres', 
        'HOST': 'localhost',  
        'PORT': '5432',           
    }
}
```

If prod context, remember to set:

```sh
DEBUG = False
```

Migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

Run app:

```sh
python manage.py runserver
```

App served on http://127.0.0.1:8000/ 

Admin page http://localhost:8000/admin