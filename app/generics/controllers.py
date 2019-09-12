"""Base controller classes"""

import logging

from flask_restful import reqparse
from werkzeug.exceptions import InternalServerError

LOGGER = logging.getLogger(__name__)


class BaseController(object):
    # flask-restful: request parsing
    # ref: https://flask-restful.readthedocs.io/en/0.3.5/reqparse.html
    request_parser = reqparse.RequestParser(bundle_errors=True)
    validated_json = None
    context = None

    # flask-restful: output fields (response marshalling)
    # ref: https://flask-restful.readthedocs.io/en/0.3.5/fields.html
    marshal_fields = {}

    def set_context(self, context):
        self.context = context

    def get_context(self):
        if self.context is None:
            LOGGER.error('Context Not set')
            raise InternalServerError
        return self.context

    def validate_request(self):
        # Add arguments to parser here
        return self.request_parser.parse_args()
