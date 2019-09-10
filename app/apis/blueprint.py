from flask import Blueprint
from flask_restful import Api

from app.generics.constants import API_ERRORS

api_blueprint = Blueprint('apis', __name__, url_prefix='/api')
API = Api(api_blueprint, catch_all_404s=True, errors=API_ERRORS)
