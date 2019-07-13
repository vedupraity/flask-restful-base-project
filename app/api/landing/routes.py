from app import rest_api
from app.api.landing import resources as landing_resources


rest_api.add_resource(landing_resources.Landing, '/')
