from base import *
import dj_database_url


DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Django Disqus Settings
DISQUS_WEBSITE_SHORTNAME = 'gunnerjnr'

# PayPal Settings

SITE_URL = "GAMERSHUB_SITE_URL"
PAYPAL_NOTIFY_URL = 'GAMERSHUB_HARD_TO_GUESS_URL'
PAYPAL_RECEIVER_EMAIL = os.environ['GAMERSHUB_PAYPAL_RECEIVER_EMAIL']

ALLOWED_HOSTS.append('gamershub.herokuapp.com')

# SMTP Email Settings
# https://docs.djangoproject.com/en/1.11/topics/email/#django.core.mail.backends.smtp.EmailBackend

EMAIL_HOST = 'GAMERSHUB_MAIL_HOST'
EMAIL_HOST_USER = 'GAMERSHUB_EMAIL_ADDRESS'
EMAIL_HOST_PASSWORD = 'GAMERSHUB_EMAIL_PASSWORD'
DEFAULT_FROM_EMAIL = 'GAMERSHUB_DEFAULT_FROM_EMAIL'
EMAIL_PORT = 'GAMERSHUB_EMAIL_PORT'  # default SMTP port 587
EMAIL_USE_TLS = True  # Whether to use a TLS (secure) connection when talking to the SMTP server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Log DEBUG information to the console
LOGGING = {
    'version': 1.0,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}