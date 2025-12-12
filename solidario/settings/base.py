
from pathlib import Path
import sys
import os
import dj_database_url # <--- IMPORTANTE: Agregamos esto

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# --- SEGURIDAD: CLAVE SECRETA ---
# En producción, Render nos dará una clave segura. En local usamos una por defecto.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-clave-por-defecto-para-local')

# --- SEGURIDAD: DEBUG ---
# En Render (Producción) DEBUG debe ser False.
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = [
    'infosolidario.onrender.com',
    'localhost',
    '127.0.0.1' 
]

# Permitir automáticamente la URL interna de Render
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Tus apps
    'apps.articulos',
    'apps.usuarios',
    # Librerías extra
    'ckeditor', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # --- IMPORTANTE: WhiteNoise va AQUÍ (justo después de Security) ---
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'solidario.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'solidario.wsgi.application'


# --- BASE DE DATOS (Configuración Híbrida) ---
# Si estamos en Render, usa PostgreSQL. Si estamos en PC, usa SQLite.
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# -----------------------
# INTERNACIONALIZACIÓN
# -----------------------
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -----------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# -----------------------

STATIC_URL = '/static/'

# Render necesita una carpeta donde juntar todos los estilos.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Esto permite que Render sirva los archivos comprimidos y eficientes
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/articulos/' 
LOGOUT_REDIRECT_URL = '/'