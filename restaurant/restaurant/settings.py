"""
Django settings for restaurant project.
Generated by 'django-admin startproject' using Django 2.2.4.
For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import django_heroku
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h4453v_%-b8*4ne33j5r4n+@@3sgz&4t#f5mgn3e@_0ygqus-k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Access Apps
    'apps.access_apps.access',

    # Backend Apps
    'apps.backend_apps.food',
    'apps.backend_apps.order',
    'apps.backend_apps.report',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'restaurant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates',
            os.path.join(BASE_DIR,'apps/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'restaurant.wsgi.application'

DATABASES = {  
    'default'                   : {  
        'ENGINE'                : 'djongo',  
        'NAME'                  : 'restaurant_db',  
        'USER'                  : 'nibedika',  
        'PASSWORD'              : 'cbst6semester',  
        'HOST'                  : 'mongodb://nibedika:<password>@cbstcluster-shard-00-00-sxkqx.mongodb.net:27017,cbstcluster-shard-00-01-sxkqx.mongodb.net:27017,cbstcluster-shard-00-02-sxkqx.mongodb.net:27017/test?ssl=true&replicaSet=cbstCluster-shard-0&authSource=admin&retryWrites=true&w=majority',  
        'PORT'                  : 27017,  
        'SUPPORTS_TRANSACTIONS' : False,  
    }  
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATETIME_FORMAT = 'Y-m-d H:i:s'
DURATIONFIELD_ALLOW_YEARS = True
DURATIONFIELD_ALLOW_MONTHS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# For Static File Include From Static Folder
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


#For Media File [Uploaded File, Image, Video] Setting
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# Activate Django-Heroku.
django_heroku.settings(locals())