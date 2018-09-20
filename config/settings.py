

try:
	from .local_settings import *
except ImportError:
	from .produccion_settings import *