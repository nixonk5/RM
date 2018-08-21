from .base import *


SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
	default='wqxq670vlj6=9t^mtqyas%0e5t+)tag75!t*19yrrz9qno6=!v')

DEBUG = env.bool('DJANGO_DEBUG', True)

CORS_ORIGIN_ALLOW_ALL 	= True
SESSION_COOKIE_SECURE 	= False
CSRF_COOKIE_SECURE 		= False
SECURE_SSL_REDIRECT 	= False