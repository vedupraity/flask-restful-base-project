from app.apis.blueprint import API
from .resources import LandingResource

API.add_resource(LandingResource, '/landing/<int:id>')
