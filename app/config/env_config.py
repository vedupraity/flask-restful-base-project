"""
This file contains multiple environment configurations extended by class
`BaseConfig` from the `base_config.py` file.
"""
from app.config.base_config import BaseConfig


class Development(BaseConfig):
    SECRET_KEY = None

    # Database connection configurations
    DEFAULT_DATABASE = {
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
    ...

    # Turn on/off debugging mode
    DEBUG = True


class Production(BaseConfig):
    SECRET_KEY = None

    # Database connection configurations
    DEFAULT_DATABASE = {
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
    ...

    # Turn on/off debugging mode
    DEBUG = False
