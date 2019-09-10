from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint('apis', __name__, url_prefix='/api')
API = Api(api_blueprint, catch_all_404s=True, errors=None)
