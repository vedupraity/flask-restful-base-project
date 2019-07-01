"""
Define Constants here to be used App wide
"""

# Default HTTP Response JSON
DEFAULT_HTTP_RESPONSE = {
    'success': True
}

# API Error Codes and Response JSON
ERROR_CODES = {
    # Generic Error Codes Definition
    'BAD_REQUEST': {
        'status': 400,
        'response': {
            'error_code': 'BAD_REQUEST',
            'message': 'Bad Request',
        }
    },
    'UNAUTHORIZED': {
        'status': 401,
        'response': {
            'error_code': 'UNAUTHORIZED',
            'message': 'Unauthorized'
        }
    },
    'FORBIDDEN': {
        'status': 403,
        'response': {
            'error_code': 'FORBIDDEN',
            'message': 'Forbidden'
        }
    },
    'NOT_FOUND': {
        'status': 404,
        'response': {
            'error_code': 'NOT_FOUND',
            'message': 'Not Found'
        }
    },
    'METHOD_NOT_ALLOWED': {
        'status': 405,
        'response': {
            'error_code': 'METHOD_NOT_ALLOWED',
            'message': 'Method Not Allowed'
        }
    },
    'CONFLICT': {
        'status': 409,
        'response': {
            'error_code': 'CONFLICT',
            'message': 'Conflict'
        }
    },
    'TOO_MANY_REQUESTS': {
        'status': 429,
        'response': {
            'error_code': 'TOO_MANY_REQUESTS',
            'message': 'Too Many Requests'
        }
    },
    'INTERNAL_SERVER_ERROR': {
        'status': 500,
        'response': {
            'error_code': 'INTERNAL_SERVER_ERROR',
            'message': 'Internal Server Error'
        }
    },

    # Custom Error Codes Definition
}
