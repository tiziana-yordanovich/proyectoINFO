from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        #engine = motor de base de datos
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_info',
        'USER': 'root',
        'PASSWORD': 'Nami1510!',
        'HOST': 'localhost',
        'PORT': '',
    }
}
