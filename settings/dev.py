"""
Dev.py: - This is the settings used in development (DUBUG = True)
"""
from settings.base import *


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

PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'  # for testing only
PAYPAL_RECEIVER_EMAIL = 'admin@gamershub.uk'

SITE_URL = 'http://127.0.0.1:8000'
ALLOWED_HOSTS.append(u'0.0.0.0',)

# A nifty Django feature that allows the sending of emails to be displayed in
# the console, a bit like a fake SMTP server

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
