import sys

from flask import current_app
from flask.signals import got_request_exception
from flask_restful import Api
from flask_restful.utils import http_status_message
from werkzeug.datastructures import Headers
from werkzeug.exceptions import HTTPException


class ExtendedApi(Api):
    def handle_error(self, e):
        """Error handler for the API transforms a raised exception into a Flask
        response, with the appropriate HTTP status code and body.

        :param e: the raised Exception object
        :type e: Exception

        """
        got_request_exception.send(current_app._get_current_object(),
                                   exception=e)

        # if not isinstance(e,
        #                   HTTPException) and current_app.propagate_exceptions:
        #     exc_type, exc_value, tb = sys.exc_info()
        #     if exc_value is e:
        #         raise
        #     else:
        #         raise e

        headers = Headers()
        if isinstance(e, HTTPException):
            code = e.code
            default_data = {
                'message': getattr(e, 'description', http_status_message(code))
            }
            headers = e.get_response().headers
        else:
            code = 500
            # default_data = {
            #     'message': http_status_message(code),
            # }
            default_data = self.errors.get('InternalServerError', {})

        # Werkzeug exceptions generate a content-length header which is added
        # to the response in addition to the actual content-length header
        # https://github.com/flask-restful/flask-restful/issues/534
        remove_headers = ('Content-Length',)

        for header in remove_headers:
            headers.pop(header, None)

        data = getattr(e, 'data', default_data)

        if code and code >= 500:
            exc_info = sys.exc_info()
            if exc_info[1] is None:
                exc_info = None
            current_app.log_exception(exc_info)

        error_cls_name = type(e).__name__
        if error_cls_name in self.errors:
            custom_data = self.errors.get(error_cls_name, {}).copy()
            code = custom_data.get('status', 500)

            # Avoid overwriting of message in response body
            if 'message' in data and 'message' in custom_data:
                custom_data.pop('message')

            data.update(custom_data)

        if code == 406 and self.default_mediatype is None:
            # if we are handling NotAcceptable (406), make sure that
            # make_response uses a representation we support as the
            # default mediatype (so that make_response doesn't throw
            # another NotAcceptable error).
            supported_mediatypes = list(self.representations.keys())
            fallback_mediatype = supported_mediatypes[
                0] if supported_mediatypes else "text/plain"
            resp = self.make_response(
                data,
                code,
                headers,
                fallback_mediatype=fallback_mediatype
            )
        else:
            resp = self.make_response(data, code, headers)

        if code == 401:
            resp = self.unauthorized(resp)
        return resp
