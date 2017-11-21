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

# PAYPAL_NOTIFY_URL = 'GAMERSHUB_HARD_TO_GUESS_URL'
#  PAYPAL_RECEIVER_EMAIL = os.environ['GAMERSHUB_PAYPAL_RECEIVER_EMAIL']

PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'  # for testing only
PAYPAL_RECEIVER_EMAIL = 'admin@gamershub.uk'

SITE_URL = 'https://your-heroku-app.herokuapp.com'
ALLOWED_HOSTS.append('your-heroku-app.herokuapp.com')

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