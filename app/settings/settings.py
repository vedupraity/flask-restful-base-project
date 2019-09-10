"""
This file contains a base class for the Flask App Configuration.
Extend this class in the file `env_config.py` to create multiple environment
configurations.
"""

import os

import pytz
from decouple import config

app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get environment from the environment variable
# environment = os.environ.get('FLASK_ENV', None)
# Get environment from the decouple settings file (settings.ini)
environment = config('ENV', default='production')


class BaseConfig(object):
    # Absolute path for Project Base Directory
    BASE_DIR = os.path.dirname(app_dir)

    # File logs path
    LOGS_DIR = os.path.join(BASE_DIR, 'logs')

    # What environment the app is running in. Flask and extensions may enable
    # behaviors based on the environment, such as enabling debug mode. The
    # env attribute maps to this settings key. This is set by the FLASK_ENV
    # environment variable and may not behave as expected if set in code.
    #
    # **Do not enable development when deploying in production.**
    #
    # Default: `production`

    ENV = environment

    # App Secret Key. Below Example to create a 32 character hex string
    #
    #   >>> import uuid
    #   >>> uuid.uuid4().hex
    #   'c6caf210ce2d4973a1126c5bc3aeb2aa'

    # SECRET_KEY = settings('SECRET_KEY')

    # Whether debug mode is enabled. When using flask run to start the
    # development server, an interactive debugger will be shown for unhandled
    # exceptions, and the server will be reloaded when code changes. The
    # debug attribute maps to this settings key. This is enabled when ENV is
    # `development` and is overridden by the FLASK_DEBUG environment
    # variable. It may not behave as expected if set in code.
    #
    # **Do not enable debug mode when deploying in production.**
    #
    # Default: True if ENV is `development`, or False otherwise.

    # DEBUG = settings('DEBUG', default=True, cast=bool)

    # Database connection settings

    # DATABASE = {
    #     'HOST': settings('db_HOST'),
    #     'PORT': settings('db_PORT'),
    #     'NAME': settings('db_NAME'),
    #     'USERNAME': settings('db_USERNAME'),
    #     'PASSWORD': settings('db_PASSWORD')
    # }

    # Allow hosts to access the APIs

    # ALLOWED_HOSTS = ['*']

    # CORS Configuration

    # ...

    # Logging Configurations

    # LOGS_DIR = os.path.join(BASE_DIR, 'logs')

    # Logging levels: NOTSET, DEBUG, INFO, WARNING, WARN, ERROR, FATAL, CRITICAL
    # LOGGING_LEVEL = settings('LOGGING_LEVEL')

    # LOGGING_CONFIG = {
    #     'version': 1,
    #     'formatters': {
    #         'default': {
    #             'format': '[%(asctime)s] %(levelname)s in %(module)s: '
    #                       '%(message)s',
    #         },
    #         'extended': {
    #             'format': '[%(asctime)s] %(levelname)s [%(name)s: '
    #                       '%(funcName)s: %(lineno)s] %(message)s'
    #         }
    #     },
    #     'handlers': {
    #         'wsgi': {
    #             'class': 'logging.StreamHandler',
    #             'stream': 'ext://flask.logging.wsgi_errors_stream',
    #             'formatter': 'extended'
    #         },
    #         'rotating_file_handler': {
    #             'level': LOGGING_LEVEL,
    #             'class': 'logging.handlers.RotatingFileHandler',
    #             'filename': os.path.join(BaseConfig.LOGS_DIR, 'app.log'),
    #             'maxBytes': 1024 * 1024 * 5,  # 5 MB
    #             'backupCount': 30,
    #             'formatter': 'extended',
    #         }
    #     },
    #     'root': {
    #         'level': LOGGING_LEVEL,
    #         'handlers': ['wsgi', 'rotating_file_handler']
    #     }
    # }

    # Static url and directory configurations

    STATIC_URL = '/static'
    STATIC_ROOT = os.path.join(app_dir, 'static')

    # Default Time Zone used for the Python DateTime objects will be `UTC`
    #
    # A different timezone can be set as:
    #
    #   >>> pytz.timezone('Asia/Kolkata')
    #   <DstTzInfo 'Asia/Kolkata' LMT+5:53:00 STD>

    TIME_ZONE = pytz.UTC


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = 'c6caf210ce2d4973a1126c5bc3aeb2aa'

    # Do not enable debug mode when deploying in production
    DEBUG = True

    # Allow hosts to access the APIs
    ALLOWED_HOSTS = ['*']

    # Database connection settings

    # DATABASE = {
    #     'HOST': settings('db_HOST'),
    #     'PORT': settings('db_PORT'),
    #     'NAME': settings('db_NAME'),
    #     'USERNAME': settings('db_USERNAME'),
    #     'PASSWORD': settings('db_PASSWORD')
    # }

    # Logging Configurations

    LOGGING_LEVEL = 'DEBUG'

    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: '
                          '%(message)s',
            },
            'extended': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s: '
                          '%(funcName)s: %(lineno)s] %(message)s'
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'extended'
            },
            'rotating_file_handler': {
                'level': LOGGING_LEVEL,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BaseConfig.LOGS_DIR, 'app.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 30,
                'formatter': 'extended',
            }
        },
        'root': {
            'level': LOGGING_LEVEL,
            'handlers': ['wsgi', 'rotating_file_handler']
        }
    }


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'c6caf210ce2d4973a1126c5bc3aeb2aa'

    # Do not enable debug mode when deploying in production
    DEBUG = False

    # Allow hosts to access the APIs
    ALLOWED_HOSTS = ['*']

    # Database connection settings

    # DATABASE = {
    #     'HOST': settings('db_HOST'),
    #     'PORT': settings('db_PORT'),
    #     'NAME': settings('db_NAME'),
    #     'USERNAME': settings('db_USERNAME'),
    #     'PASSWORD': settings('db_PASSWORD')
    # }

    # Logging Configurations

    LOGGING_LEVEL = 'ERROR'

    LOGGING_CONFIG = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: '
                          '%(message)s',
            },
            'extended': {
                'format': '[%(asctime)s] %(levelname)s [%(name)s: '
                          '%(funcName)s: %(lineno)s] %(message)s'
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'extended'
            },
            'rotating_file_handler': {
                'level': LOGGING_LEVEL,
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(BaseConfig.LOGS_DIR, 'app.log'),
                'maxBytes': 1024 * 1024 * 5,  # 5 MB
                'backupCount': 30,
                'formatter': 'extended',
            }
        },
        'root': {
            'level': LOGGING_LEVEL,
            'handlers': ['wsgi', 'rotating_file_handler']
        }
    }
