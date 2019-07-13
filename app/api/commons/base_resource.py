"""
This file contains `BaseResource` class extended from Flask-Restful - `Resource`
class for defining additional variables and methods.
"""

from flask import request
from flask_restful import Resource

from app import flask_app


class BaseResource(Resource):
    LOGGER = flask_app.logger

    def get_context(self, *args, **kwargs):
        """
        """
        return {
            'resource_instance': self,
            'resource_args': args,
            'resource_kwargs': kwargs,
            'request': request,
            'request_user': kwargs.get('request_user'),
        }
