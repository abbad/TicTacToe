from decimal import Decimal
import json
import os
import sys
import logging

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", '7c3^c=$noeh#3_=v-@w8jvno^$s&-jo2^lf==fuhjpq3s6rx_^')

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

# Email lists
# For Django errors
ADMINS = (
    ('Ahmad Abbad', 'ahm.abbad@gmail.com')
)

DJANGO_ROOT_PATH = os.environ.get("DJANGO_ROOT_PATH", "")

# URL prefix for static files - heavily used in templates and also used for the static files app when running locally
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Settings used to serve static files.
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = 'static/'

# Additional locations of static files
STATICFILES_DIRS = (
    DJANGO_ROOT_PATH + 'staticfiles/',
)

STATICFILES_TEMPLATE_DIR = os.path.join(SETTINGS_PATH, 'staticfiles/templates')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'mysite.urls'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'debug_toolbar',
    'django.contrib.staticfiles',
    'mysite.tictactoe',
    'mysite.account',
    'south',
)



DEBUG = True

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

# DB connection.

DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'HOST': 'localhost',
            'PORT': '3306',  # Set to empty string for default.
            'NAME': 'TICTACTOE',  # Or path to database file if using sqlite3.
            'USER': 'root',
            'PASSWORD': '', # these configuration needs to be envirnement variables.
        },
}