"""
Flask App initialization
"""

from flask import Flask
from flask_restful import Api

# Initialize Flask App and Api
app = Flask(__name__)
api = Api(app, catch_all_404s=True)

app.config.from_object('app.config.settings.AppConfig')
