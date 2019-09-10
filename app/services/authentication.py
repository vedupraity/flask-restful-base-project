import logging

LOGGER = logging.getLogger(__name__)

# def authenticate(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if not getattr(func, 'authenticated', True):
#             return func(*args, **kwargs)
#
#         acct = basic_authentication()  # custom account lookup function
#
#         if acct:
#             return func(*args, **kwargs)
#
#         restful.abort(401)
#     return wrapper
