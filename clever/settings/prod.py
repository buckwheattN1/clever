from .base import *
import os

SECRET_KEY = DJANGO_SECRET_KEY
DEBUG = False
ALLOWED_HOSTS = ['nestingpolska.usermd.net']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'p1472_nesting',
        'USER': 'p1472_nesting',
        'PASSWORD': 'Cleverspace2022',
        'HOST': 'pgsql52.mydevil.net',
        'PORT': '5432',
    },
}

