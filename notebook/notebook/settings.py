import os
from pathlib import Path

from dotenv import load_dotenv

from .utilities import secret_key_validator

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = secret_key_validator()

DEBUG = os.getenv('DJANGO_DEBUG', False)

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', []).split(',')

CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', []).split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'note',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notebook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'notebook/templates'],
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

WSGI_APPLICATION = 'notebook.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django'
                '.contrib'
                '.auth'
                '.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django'
                '.contrib'
                '.auth'
                '.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django'
                '.contrib'
                '.auth'
                '.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django'
                '.contrib'
                '.auth'
                '.password_validation'
                '.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE', 'en')

TIME_ZONE = os.getenv('DJANGO_TIME_ZONE', 'UTC')

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'
