"""
Flask App initialization
"""

from flask import Flask
from flask_restful import Api

from app.routes_config import RoutesConfig

# Initiate Flask App and Api
flask_app = Flask(__name__, static_url_path='/static')
rest_api = Api(flask_app, catch_all_404s=True)

# Initiate app configuration
flask_app.config.from_object('app.config.settings')

# Initiate the logger
logger = flask_app.logger
logger.setLevel(flask_app.config['LOGGING_LEVEL'])

# Initiate all the routes
RoutesConfig()
