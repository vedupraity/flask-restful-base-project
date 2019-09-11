from datetime import datetime

from flask_restful import fields


class TimestampField(fields.Raw):
    def format(self, value):
        return value.timestamp() if isinstance(value, datetime) else None
