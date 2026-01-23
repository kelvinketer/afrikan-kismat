"""
Django settings for config project.
"""
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

# ... existing code ...

# Add these at the bottom of settings.py
MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')

import os
import dj_database_url
from pathlib import Path
from dotenv import load_dotenv # <--- IMPORT THIS

# Load environment variables from .env file
load_dotenv() 

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-dl)5blh(x9o$fp_jo3(0wktx(hm)u$7^u#eg+kyfc!n#(w(*xy')

# We keep DEBUG=True for now to help with errors.
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    # 1. Jazzmin must be ABOVE 'django.contrib.admin'
    'jazzmin',

    'cloudinary_storage',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom Apps
    'core',
    'payments', # <--- NEW APP REGISTERED HERE
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Keep Middleware active
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

# --- STATIC FILES CONFIG ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Ensure core/static exists (Created by our build_assets.py script)
CORE_STATIC_DIR = os.path.join(BASE_DIR, 'core', 'static')
if not os.path.exists(CORE_STATIC_DIR):
    os.makedirs(CORE_STATIC_DIR)

STATICFILES_DIRS = [
    CORE_STATIC_DIR,
]

# [CRITICAL FIX] DISABLE COMPRESSION
# We use the standard Django storage. This prevents the "FileNotFound" crash
# when Whitenoise tries to compress a file that was skipped due to duplicates.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# --- CLOUDINARY CONFIG ---
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- JAZZMIN DASHBOARD CONFIG (Blue/Teal Professional Theme) ---
JAZZMIN_SETTINGS = {
    "site_title": "Afrikan Kismat Admin",
    "site_header": "Afrikan Kismat",
    "site_brand": "Afrikan Kismat",
    "welcome_sign": "Welcome to the Staff Portal",
    "copyright": "Afrikan Kismat Expeditions",
    "search_model": "core.SafariPackage",
    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Site", "url": "/", "new_window": True},
    ],
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "core.SafariPackage": "fas fa-paw",
        "core.Destination": "fas fa-map-marked-alt",
        "core.Inquiry": "fas fa-envelope",
        "core.Testimonial": "fas fa-star",
        "core.Partner": "fas fa-handshake",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",   
    "navbar": "navbar-dark", 
    "sidebar": "sidebar-dark-primary",
    "button_classes": {
        "primary": "btn-primary", 
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# --- M-PESA CONFIGURATION ---
MPESA_ENVIRONMENT = os.environ.get('MPESA_ENVIRONMENT', 'sandbox')
MPESA_CONSUMER_KEY = os.environ.get('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.environ.get('MPESA_CONSUMER_SECRET')
MPESA_PASSKEY = os.environ.get('MPESA_PASSKEY')
MPESA_SHORTCODE = os.environ.get('MPESA_SHORTCODE')
MPESA_INITIATOR_PASSWORD = os.environ.get('MPESA_INITIATOR_PASSWORD')