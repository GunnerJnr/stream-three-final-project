"""
Staging.py: This is the settings used for deployment with heroku live on the web
"""
import dj_database_url
from settings.base import *  # pylint: disable=W0401, W0614

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['GAMERSHUB_SECRET_KEY']

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

PAYPAL_NOTIFY_URL = os.environ['GAMERSHUB_HARD_TO_GUESS_URL']
PAYPAL_RECEIVER_EMAIL = os.environ['GAMERSHUB_PAYPAL_RECEIVER_EMAIL']

SITE_URL = os.environ['GAMERSHUB_SITE_URL']
ALLOWED_HOSTS.append(os.environ['GAMERSHUB_ALLOWED_HOST'])

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

AWS_STORAGE_BUCKET_NAME = os.environ['GAMERSHUB_AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = os.environ['GAMERSHUB_AWS_S3_REGION_NAME'] # e.g. us-east-2
AWS_ACCESS_KEY_ID = os.environ['GAMERSHUB_AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['GAMERSHUB_AWS_SECRET_ACCESS_KEY']

# Tell django-storages the domain to use to refer to static files.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 3099 23:59:59 GMT',
    'CacheControl': 'max-age=94608000',
}

# Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

THUMBNAIL_FORCE_OVERWRITE = True

# Log the DEBUG information to the console
# https://docs.djangoproject.com/en/2.0/topics/logging/#topic-logging-parts-loggers
LOGGING = {
    'version': 1.0,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '../logs/django/debug.log',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
    },
}
