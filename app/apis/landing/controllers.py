import logging
from datetime import datetime

from flask_restful import fields, HTTPException

from app.generics.controllers import BaseController
from app.generics.custom_marshal_fields import TimestampField

LOGGER = logging.getLogger(__name__)


class LandingController(BaseController):
    marshal_fields = {
        'id': fields.Integer,
        'url': fields.Url(absolute=True),
        'http_method': fields.String(attribute='request_method'),
        'datetime': fields.DateTime,
        'timestamp': TimestampField
    }

    def _get_response_data(self):
        return {
            'id': self.context.request.view_args.get('id', None),
            'url': self.context.request.url,
            'request_method': self.context.request.method,
            'datetime': datetime.now(),
            'timestamp': datetime.now(),
        }

    def get_response(self):
        response_data = self._get_response_data()

        # Logging examples
        LOGGER.debug('debug log statement')
        LOGGER.info('info log statement')
        LOGGER.warn('warn log statement')
        LOGGER.error('error log statement')
        LOGGER.critical('critical log statement')

        # flask abort example
        try:
            d = {}
            value = d['nek']
        except KeyError:
            raise HTTPException()

        return response_data
