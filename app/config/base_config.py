"""
This has a base class for the Flask configuration.
Extend this class in the file `env_config` to create multiple required
configurations based on the environment.
"""

import os


class BaseConfig:
    # App Secret Key. Use below code to generate a random key
    # ''.join(random.choice(string.printable) for _ in range(32))
    SECRET_KEY = None

    # Absolute path for `app` and Project Base Directory
    APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    PROJECT_ROOT = os.path.dirname(APP_DIR)

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
    LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')
    ...

    # Static url and directory configurations
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(APP_DIR, 'static')

    # Turn on/off debugging mode
    DEBUG = True

    # Time Zone
    TIME_ZONE = 'UTC'

