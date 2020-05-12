from . import *
import os


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'sampledb'),
        'USER': os.environ.get('DB_USERNAME', 'sampleuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'samplesecret'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432')
    }
}