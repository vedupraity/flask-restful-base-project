"""
Define Constants here to be used App wide
"""

API_ERRORS = {
    'BadRequest': {
        'status': 400,
        'error_code': 'BAD_REQUEST',
        'message': "The request could not be understood by the server due to"
                   " malformed syntax.",
    },

    'Unauthorized': {
        'status': 401,
        'error_code': 'UNAUTHORIZED',
        'message': "The request requires user authentication."
    },

    'Forbidden': {
        'status': 403,
        'error_code': 'FORBIDDEN',
        'message': "You don\'t have the permission to access the requested"
                   " resource."
    },

    'NotFound': {
        'status': 404,
        'error_code': 'NOT_FOUND',
        'message': "The requested resource was not found on the server."
    },

    'MethodNotAllowed': {
        'status': 405,
        'error_code': 'METHOD_NOT_ALLOWED',
        'message': "The method is not allowed for the requested URL."
    },

    'NotAcceptable': {
        'status': 406,
        'error_code': 'NOT_ACCEPTABLE',
        'message': "The resource identified by the request is only capable of"
                   " generating response entities which have content"
                   " characteristics not acceptable according to the accept"
                   " headers sent in the request."
    },

    'RequestTimeout': {
        'status': 408,
        'error_code': 'REQUEST_TIMEOUT',
        'message': "The server closed the network connection because the"
                   " browser didn't finish the request within the specified"
                   " time."
    },

    'Conflict': {
        'status': 409,
        'error_code': 'CONFLICT',
        'message': "The request could not be completed due to a conflict with"
                   " the current state of the resource."
    },

    'Gone': {
        'status': 410,
        'error_code': 'GONE',
        'message': "The requested URL is no longer available on this server and"
                   " there is no forwarding address."
    },

    'LengthRequired': {
        'status': 411,
        'error_code': 'LENGTH_REQUIRED',
        'message': "A request with this method requires a valid <code>Content-"
                   "Length</code> header."
    },

    'PreconditionFailed': {
        'status': 412,
        'error_code': 'PRECONDITION_FAILED',
        'message': "The precondition on the request for the URL failed"
                   " positive evaluation."
    },

    'RequestEntityTooLarge': {
        'status': 413,
        'error_code': 'REQUEST_ENTITY_TOO_LARGE',
        'message': "The data value transmitted exceeds the capacity limit."
    },

    'RequestURITooLarge': {
        'status': 414,
        'error_code': 'REQUEST_URI_TOO_LARGE',
        'message': "The length of the requested URL exceeds the capacity"
                   " limit for this server. The request cannot be processed."
    },

    'UnsupportedMediaType': {
        'status': 415,
        'error_code': 'UNSUPPORTED_MEDIA_TYPE',
        'message': "The server does not support the media type transmitted in"
                   " the request."
    },

    'RequestedRangeNotSatisfiable': {
        'status': 416,
        'error_code': 'REQUESTED_RANGE_NOT_SATISFIABLE',
        'message': "The server cannot provide the requested range."
    },

    'ExpectationFailed': {
        'status': 417,
        'error_code': 'EXPECTATION_FAILED',
        'message': "The server could not meet the requirements of the Expect"
                   " header"
    },

    'ImATeapot': {
        'status': 418,
        'error_code': 'IM_A_TEAPOT',
        'message': "This server is a teapot, not a coffee machine"
    },

    'UnprocessableEntity': {
        'status': 422,
        'error_code': 'UNPROCESSABLE_ENTITY',
        'message': "The request was well-formed but was unable to be followed"
                   " due to semantic errors."
    },

    'Locked': {
        'status': 423,
        'error_code': 'LOCKED',
        'message': "The resource that is being accessed is locked."
    },

    'FailedDependency': {
        'status': 424,
        'error_code': 'FAILED_DEPENDENCY',
        'message': "The method could not be performed on the resource because"
                   " the requested action depended on another action and that"
                   " action failed."
    },

    'PreconditionRequired': {
        'status': 428,
        'error_code': 'PRECONDITION_REQUIRED',
        'message': "This request is required to be conditional; try using"
                   " 'If-Match' or 'If-Unmodified-Since'."
    },

    'TooManyRequests': {
        'status': 429,
        'error_code': 'TOO_MANY_REQUESTS',
        'message': "This user has exceeded an allotted request count. Try again"
                   " later."
    },

    'RequestHeaderFieldsTooLarge': {
        'status': 431,
        'error_code': 'REQUEST_HEADER_FIELDS_TOO_LARGE',
        'message': "One or more header fields exceeds the maximum size."
    },

    'UnavailableForLegalReasons': {
        'status': 451,
        'error_code': 'UNAVAILABLE_FOR_LEGAL_REASONS',
        'message': "Unavailable for legal reasons."
    },

    'InternalServerError': {
        'status': 500,
        'error_code': 'INTERNAL_SERVER_ERROR',
        'message': "The server encountered an internal error and was unable to"
                   " complete your request. Either the server is overloaded or"
                   " there is an error in the application."
    },

    'NotImplemented': {
        'status': 501,
        'error_code': 'NOT_IMPLEMENTED',
        'message': "The server does not support the action requested by the"
                   " browser."
    },

    'BadGateway': {
        'status': 502,
        'error_code': 'BAD_GATEWAY',
        'message': "The proxy server received an invalid response from an"
                   " upstream server."
    },

    'ServiceUnavailable': {
        'status': 503,
        'error_code': 'SERVICE_UNAVAILABLE',
        'message': "The server is temporarily unable to service your request"
                   " due to maintenance downtime or capacity problems. Please"
                   " try again later."
    },

    'GatewayTimeout': {
        'status': 504,
        'error_code': 'GATEWAY_TIMEOUT',
        'message': "The connection to an upstream server timed out."
    },

    'HTTPVersionNotSupported': {
        'status': 505,
        'error_code': 'HTTPVERSION_NOT_SUPPORTED',
        'message': "The server does not support the HTTP protocol version used"
                   " in the request."
    }

}
