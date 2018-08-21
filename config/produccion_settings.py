from .base import *
import os, dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY', '1@3#46YhGf6&(iJkJhYt6&6$3@&8(hJhG')

DEBUG = env.bool('DJANGO_DEBUG', False)

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY 				= True