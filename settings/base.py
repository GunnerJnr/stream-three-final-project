import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['GAMERSHUB_SECRET_KEY']

ALLOWED_HOSTS = []

# Site ID
SITE_ID = 2

# Application definition

INSTALLED_APPS = [
    'accounts',
    'home',
    'gamersblog',
    'disqus',
    'paypal.standard.ipn',
    'gamershub_store',
    'gamershub_products',
    'django_forms_bootstrap',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Login, Logout and Profile Handling
LOGIN_REDIRECT_URL = reverse_lazy('user_profile')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gamershub.urls'

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

WSGI_APPLICATION = 'gamershub.wsgi.application'

# Authentication Backends for our custom user authentication
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#other-authentication-sources

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth',
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'GB'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# SMTP Email Settings
# https://docs.djangoproject.com/en/1.11/topics/email/#django.core.mail.backends.smtp.EmailBackend

# EMAIL_HOST = 'GAMERSHUB_MAIL_HOST'
# EMAIL_HOST_USER = 'GAMERSHUB_EMAIL_ADDRESS'
# EMAIL_HOST_PASSWORD = 'GAMERSHUB_EMAIL_PASSWORD'
# EMAIL_PORT = 465  # default SMTP port 587
# EMAIL_USE_TLS = True  # Whether to use a TLS (secure) connection when
# talking to the SMTP server

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Media Root - serve the media files uploaded by users

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
