from flask import Blueprint

from app.generics.constants import API_ERRORS
from app.generics.flask_restful_api import ExtendedApi

api_blueprint = Blueprint('apis', __name__, url_prefix='/api')
API = ExtendedApi(api_blueprint, catch_all_404s=True, errors=API_ERRORS)
