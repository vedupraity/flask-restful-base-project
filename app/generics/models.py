"""Base model classes"""


class Context(object):
    def __init__(self, resource_instance, request_instance, *args, **kwargs):
        self.resource = resource_instance
        self.request = request_instance
        self.args = args
        self.kwargs = kwargs
