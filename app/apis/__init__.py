"""
Import and register all the routes here
"""


class ApiRoutes:
    def __init__(self):
        # Import all routes here
        from app.apis.landing import routes
