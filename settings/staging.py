from base import * 


DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Django Disqus Settings
DISQUS_WEBSITE_SHORTNAME = 'gunnerjnr'

# PayPal Settings

# SITE_URL = "GAMERSHUB_SITE_URL"
# PAYPAL_NOTIFY_URL = 'GAMERSHUB_HARD_TO_GUESS_URL'
#  PAYPAL_RECEIVER_EMAIL = os.environ['GAMERSHUB_PAYPAL_RECEIVER_EMAIL']

PAYPAL_NOTIFY_URL = 'https://gamershub.herokuapp.com/a-very-hard-to-guess-url/'  # for testing only
PAYPAL_RECEIVER_EMAIL = 'admin@gamershub.uk'

SITE_URL = 'https://gamershub.herokuapp.com'
ALLOWED_HOSTS.append('gamershub.herokuapp.com')

# SMTP Email Settings
# https://docs.djangoproject.com/en/1.11/topics/email/#django.core.mail.backends.smtp.EmailBackend

EMAIL_HOST = 'GAMERSHUB_MAIL_HOST'
EMAIL_HOST_USER = 'GAMERSHUB_EMAIL_ADDRESS'
EMAIL_HOST_PASSWORD = 'GAMERSHUB_EMAIL_PASSWORD'
EMAIL_PORT = 'GAMERSHUB_EMAIL_PORT'  # default SMTP port 587
EMAIL_USE_TLS = True  # Whether to use a TLS (secure) connection when talking to the SMTP server

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