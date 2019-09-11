import logging

from app.generics.resources import BaseResource
from .controllers import LandingController

LOGGER = logging.getLogger(__name__)


class LandingResource(BaseResource):
    controller = LandingController()

    def get(self, *args, **kwargs):
        response_data = self.controller.get_response()
        return self.marshal_response(
            response_data, self.controller.marshal_fields), 200
