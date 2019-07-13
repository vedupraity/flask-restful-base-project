"""
Flask App initialization
"""

from flask import Flask
from flask_restful import Api

# Initiate Flask App and Api
app = Flask(__name__, static_url_path='/static')
api = Api(app, catch_all_404s=True)

# Initiate app configuration
app.config.from_object('app.config.settings')

# Initiate the logger
logger = app.logger
logger.setLevel(app.config['LOGGING_LEVEL'])
