from base import *


DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# PayPal Settings

# SITE_URL = "GAMERSHUB_SITE_URL"
# PAYPAL_NOTIFY_URL = 'GAMERSHUB_HARD_TO_GUESS_URL'
#  PAYPAL_RECEIVER_EMAIL = os.environ['GAMERSHUB_PAYPAL_RECEIVER_EMAIL']

SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'  # for testing only
PAYPAL_RECEIVER_EMAIL = 'admin@gamershub.uk'
