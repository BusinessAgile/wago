from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DEV_SECRET_KEY"),


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', 'businessagile.dev', 'batech.dev']


try:
    from .local import *
except ImportError:
    pass
