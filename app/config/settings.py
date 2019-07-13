"""
This file contains a base class for the Flask App Configuration.
Extend this class in the file `env_config.py` to create multiple environment
configurations.
"""

import logging
import os

from decouple import config
import pytz


class AppConfig:
    # App Secret Key. Below Example to create a 32 character hex string
    #
    #   >>> import uuid
    #   >>> uuid.uuid4().hex
    #   'c6caf210ce2d4973a1126c5bc3aeb2aa'

    SECRET_KEY = config('SECRET_KEY')

    # What environment the app is running in. Flask and extensions may enable
    # behaviors based on the environment, such as enabling debug mode. The
    # env attribute maps to this config key. This is set by the FLASK_ENV
    # environment variable and may not behave as expected if set in code.
    #
    # **Do not enable development when deploying in production.**
    #
    # Default: `production`

    ENV = config('ENV', default='production')

    # Database connection

    DATABASE = {
        'HOST': config('db_HOST'),
        'PORT': config('db_PORT', cast=int),
        'NAME': config('db_NAME'),
        'USERNAME': config('db_USERNAME'),
        'PASSWORD': config('db_PASSWORD')
    }

    # Allow hosts to access the APIs

    ALLOWED_HOSTS = ['*']

    # CORS Configuration

    # ...

    # Absolute path for `app` and Project Base Directory

    APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.dirname(APP_DIR)

    # Logging Configurations

    LOGS_DIR = os.path.join(BASE_DIR, 'logs')
    LOGGING_LEVEL = logging.DEBUG

    # Static url and directory configurations

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(APP_DIR, 'static')

    # Whether debug mode is enabled. When using flask run to start the
    # development server, an interactive debugger will be shown for unhandled
    # exceptions, and the server will be reloaded when code changes. The
    # debug attribute maps to this config key. This is enabled when ENV is
    # `development` and is overridden by the FLASK_DEBUG environment
    # variable. It may not behave as expected if set in code.
    #
    # **Do not enable debug mode when deploying in production.**
    #
    # Default: True if ENV is `development`, or False otherwise.

    DEBUG = config('DEBUG', default=True, cast=bool)

    # Default Time Zone used for the Python DateTime objects will be `UTC`
    #
    # A different timezone can be set as:
    #
    #   >>> pytz.timezone('Asia/Kolkata')
    #   <DstTzInfo 'Asia/Kolkata' LMT+5:53:00 STD>

    TIME_ZONE = pytz.UTC
