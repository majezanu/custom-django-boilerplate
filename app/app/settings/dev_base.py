from .base import *             # NOQA
import logging.config

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATES[0]['OPTIONS'].update({'debug': True})

# Django Debug Toolbar
INSTALLED_APPS += (
    'debug_toolbar',)

# Additional middleware introduced by debug toolbar
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# Allow internal IPs for debugging
INTERNAL_IPS = [
    '127.0.0.1',
    '0.0.0.1',
]

# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)

LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'django_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': str(LOGFILE_ROOT / 'django.log'),
            'formatter': 'verbose'
        },
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': str(LOGFILE_ROOT / 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['django_log_file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)
