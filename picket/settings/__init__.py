from .dist import *
try:
    from .local import *
except ImportError:
    from .local_sample import *
    from warnings import warn
    warn('Cannot import local settings. Using local_sample instead.')
