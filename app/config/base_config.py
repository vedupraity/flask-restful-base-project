"""
This file contains a base class for the Flask App Configuration.
Extend this class in the file `env_config.py` to create multiple environment
configurations.
"""

import os


class BaseConfig:
    # App Secret Key. Below Example to create a 32 character hex string
    #   >>> import uuid
    #   >>> uuid.uuid4().hex
    #   'c6caf210ce2d4973a1126c5bc3aeb2aa'
    SECRET_KEY = None

    # Absolute path for `app` and Project Base Directory
    APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BASE_DIR = os.path.dirname(APP_DIR)

    # Database connection configurations
    DATABASE = {
        'HOST': None,
        'PORT': None,
        'NAME': None,
        'USERNAME': None,
        'PASSWORD': None
    }

    # Allow hosts to access the APIs
    ALLOWED_HOSTS = ['*']

    # CORS Configuration
    ...

    # Logging Configurations
    LOGS_DIR = os.path.join(BASE_DIR, 'logs')
    ...

    # Static url and directory configurations
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(APP_DIR, 'static')

    # Turn on/off debugging mode
    DEBUG = True

    # Time Zone
    TIME_ZONE = 'UTC'
