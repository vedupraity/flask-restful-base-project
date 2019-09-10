"""
Flask App initialization
Ref: https://flask.palletsprojects.com/en/1.1.x/
"""

from logging.config import dictConfig

from flask import Flask

from app.apis import ApiRoutes
from app.apis.blueprint import api_blueprint
from app.settings.settings import (
    BaseConfig, DevelopmentConfig, ProductionConfig,
)

if BaseConfig.ENV == 'development':
    config = DevelopmentConfig()
else:
    config = ProductionConfig()

# Configure logger before initiating flask app
dictConfig(config.LOGGING_CONFIG)

# Initiate Flask App and Api
APP = Flask(__name__, static_url_path=config.STATIC_URL)

# Initiate app configuration
APP.config.from_object(config)

# Register all routes with the app
ApiRoutes()

# Register blueprints here
APP.register_blueprint(api_blueprint)
