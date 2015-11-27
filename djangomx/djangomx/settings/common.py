# coding: utf-8
import os
import json
from unipath import FSPath as Path

BASE_DIR = Path(__file__).absolute().parent.parent.parent

SECRETS_PATH = BASE_DIR.parent.child('conf').child('secrets.json')
try:
    with open(SECRETS_PATH) as handle:
        SECRETS = json.load(handle)
except IOError:
    SECRETS = {
        'secret_key': 'a',
    }

DEBUG = True


ADMINS = (
    ('netoxico', 'me@netoxico.com'),
    ('andyosuna', 'andyosuna@gmail.com'),
)

MANAGERS = ADMINS


ALLOWED_HOSTS = ['django.mx']

TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'es-mx'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djangomx.urls'

SECRET_KEY = str(SECRETS['secret_key'])

WSGI_APPLICATION = 'djangomx.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request'
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS.get('db_name', ''),
        'USER': SECRETS.get('db_user', ''),
        'PASSWORD': SECRETS.get('db_password', ''),
        'HOST': SECRETS.get('db_host', ''),
    }
}

INSTALLED_APPS = [
    'suit',
    'suit_redactor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'compressor',
    'django_gravatar',
    'sorl.thumbnail',
    'django_markdown',

    'blog',
    'contact',
    'core',
    'courses',
    'jobs',
    'newsletter',
    'accounts',
]

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {"format": "[%(name)s] %(levelname)s: %(message)s"},
        "full": {"format": "%(asctime)s [%(name)s] %(levelname)s: %(message)s"},
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "include_html": True,
            "filters": ['require_debug_false'],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
    }
}

DEFAULT_FROM_EMAIL = 'Django Mexico <no-reply@django.mx>'

# Sourl thumbnail settings
THUMBNAIL_DEBUG = True
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_QUALITY = 100

MARKDOWN_EXTENSIONS = ['codehilite']

# django_gravatar settings
GRAVATAR_DEFAULT_SIZE = 180
GRAVATAR_DEFAULT_IMAGE = 'retro'

# Django nose
INSTALLED_APPS.append('django_nose')
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--with-coverage',
    #'--verbosity=0',
    '--with-fixture-bundling',
    '--cover-package=accounts,blog'
]
