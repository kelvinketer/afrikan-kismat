"""
Django settings for config project.
"""

import os
import sys
import django
import dj_database_url
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dl)5blh(x9o$fp_jo3(0wktx(hm)u$7^u#eg+kyfc!n#(w(*xy')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

# Apps
INSTALLED_APPS = [
    'cloudinary_storage',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- STATIC FILES CONFIG (DIAGNOSTIC MODE) ---

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 1. Define Local Static
CORE_STATIC_DIR = os.path.join(BASE_DIR, 'core', 'static')
if not os.path.exists(CORE_STATIC_DIR):
    os.makedirs(CORE_STATIC_DIR)

# 2. Define Admin Static Manually
DJANGO_ROOT = os.path.dirname(django.__file__)
ADMIN_STATIC_PATH = os.path.join(DJANGO_ROOT, 'contrib', 'admin', 'static')

# 3. PRINT DEBUG INFO TO LOGS (Look for these lines in Render!)
print(f"--- DEBUG: BASE_DIR is {BASE_DIR}")
print(f"--- DEBUG: STATIC_ROOT is {STATIC_ROOT}")
print(f"--- DEBUG: CORE_STATIC_DIR is {CORE_STATIC_DIR}")
print(f"--- DEBUG: ADMIN_STATIC_PATH is {ADMIN_STATIC_PATH}")
print(f"--- DEBUG: Does Admin Path exist? {os.path.exists(ADMIN_STATIC_PATH)}")

# 4. Use Both Paths Explicitly
STATICFILES_DIRS = [
    CORE_STATIC_DIR,
    ADMIN_STATIC_PATH, 
]

# 5. Use Standard Finders (This caused duplicates before, but we need to see if it works now)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# --- CLOUDINARY CONFIG ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'