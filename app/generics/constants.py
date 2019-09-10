"""
Define Constants here to be used App wide
"""

# Default Success HTTP Response JSON
DEFAULT_SUCCESS_HTTP_RESPONSE = {
    'success': True
}

# API Error Codes and Response JSON
HTTP_ERRORS = {
    # Generic HTTP Error Codes Definition
    'BAD_REQUEST': {
        'status_code': 400,
        'response_body': {
            'error_code': 'BAD_REQUEST',
            'message': 'Bad Request',
        }
    },
    'UNAUTHORIZED': {
        'status_code': 401,
        'response_body': {
            'error_code': 'UNAUTHORIZED',
            'message': 'Unauthorized'
        }
    },
    'FORBIDDEN': {
        'status_code': 403,
        'response_body': {
            'error_code': 'FORBIDDEN',
            'message': 'Forbidden'
        }
    },
    'NOT_FOUND': {
        'status_code': 404,
        'response_body': {
            'error_code': 'NOT_FOUND',
            'message': 'Not Found'
        }
    },
    'METHOD_NOT_ALLOWED': {
        'status_code': 405,
        'response_body': {
            'error_code': 'METHOD_NOT_ALLOWED',
            'message': 'Method Not Allowed'
        }
    },
    'CONFLICT': {
        'status_code': 409,
        'response_body': {
            'error_code': 'CONFLICT',
            'message': 'Conflict'
        }
    },
    'TOO_MANY_REQUESTS': {
        'status_code': 429,
        'response_body': {
            'error_code': 'TOO_MANY_REQUESTS',
            'message': 'Too Many Requests'
        }
    },
    'INTERNAL_SERVER_ERROR': {
        'status_code': 500,
        'response_body': {
            'error_code': 'INTERNAL_SERVER_ERROR',
            'message': 'Internal Server Error'
        }
    },

    # Custom Error Codes Definitions goes here
}
