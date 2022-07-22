import os
import datetime
from dotenv import load_dotenv
from pathlib import Path
from celery.schedules import crontab
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = [s.strip() for s in os.getenv('ALLOWED_HOSTS', '').split(',')]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'todoapp.apps.cardlist',
    'todoapp.apps.person',
    'todoapp.apps.user',
    'todoapp.apps.utils'
]
MIDDLEWARE = [
    'todoapp.apps.utils.middleware.DisableCSRF',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'todoapp.apps.utils.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}

JWT_ALGORITHM = 'HS256'
JWT_ACCESS_TOKEN_LIFETIME = datetime.timedelta(seconds=int(os.getenv('JWT_ACCESS_TOKEN_LIFETIME')))
JWT_REFRESH_TOKEN_LIFETIME = datetime.timedelta(seconds=int(os.getenv('JWT_REFRESH_TOKEN_LIFETIME')))
JWT_RESET_TOKEN_LIFETIME = datetime.timedelta(seconds=int(os.getenv('JWT_RESET_TOKEN_LIFETIME')))

# Настройка Celery
REDIS_HOST = os.getenv('REDIS_HOST', '')
REDIS_PORT = os.getenv('REDIS_PORT', '')
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/1'
CELERY_TIMEZONE = 'Asia/Almaty'
# BROKER_TRANSPORT_OPTIONS = {
#     'visibility_timeout': 3600,
#     'socket_keepalive': True,
#     'health_check_interval': 4
# }
# CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/1'
# CELERYD_CONCURRENCY = 2
# CELERY_RESULT_PERSISTENT = True
# CELERY_ACCEPT_CONTENT = ['pickle', 'json']
#
# CELERY_BEAT_SCHEDULE = {
#     "send_notifications": {
#         "task": "send_notifications",
#         "schedule": datetime.timedelta(seconds=10)
#     },
# }