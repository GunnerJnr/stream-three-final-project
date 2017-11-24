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
DISQUS_WEBSITE_SHORTNAME='gunnerjnr'

# PayPal Settings

PAYPAL_NOTIFY_URL='gamershub.herokuapp.com'
PAYPAL_RECEIVER_EMAIL='admin@gamershub.uk'

SITE_URL="https://gamershub.herokuapp.com"
ALLOWED_HOSTS.append('gamershub.herokuapp.com')

# SMTP Email Settings
# https://docs.djangoproject.com/en/1.11/topics/email/#django.core.mail.backends.smtp.EmailBackend

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['GAMERSHUB_MAIL_HOST']
EMAIL_HOST_USER = os.environ['GAMERSHUB_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['GAMERSHUB_EMAIL_PASSWORD']
DEFAULT_FROM_EMAIL = os.environ['GAMERSHUB_DEFAULT_FROM_EMAIL']
EMAIL_PORT = 587  # default SMTP port 587
EMAIL_USE_TLS = True  # Whether to use a TLS (secure) connection when talking to the SMTP server
ACCOUNT_EMAIL_VERIFICATION = 'none'

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