"""
Dev.py: - This is the settings used in development (DUBUG = True)
"""
import logging
from settings.base import *  # pylint: disable=W0401, W0614

logging.basicConfig(filename='debug.log',\
format='%(asctime)s:%(levelname)s:%(message)s',\
level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p ', filemode='w')
logging.debug('You are now using the Development Debug Settings')
logging.info('Settings.Dev')
logging.warning('You are in Development Mode, Debug is set to True!')

SECRET_KEY = 'gh^jqtpb1@e3^ks@y2i4@xuxo9r(xqf6v8-$$5e6ak*v6-g8$f5idag' # dummy key for development

DEBUG = True

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

PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'  # for testing only
PAYPAL_RECEIVER_EMAIL = 'admin@gamershub.uk'

SITE_URL = 'http://127.0.0.1:8000'
ALLOWED_HOSTS.append(u'0.0.0.0',)

# A nifty Django feature that allows the sending of emails to be displayed in
# the console, a bit like a fake SMTP server

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'
