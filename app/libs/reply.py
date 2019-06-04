"""
author songjie
"""
import json

from flask import Response


class Reply(object):
    _result = None
    _code = None
    _msg = None

    def __init__(self, **kwargs):
        pass

    @property
    def result(self):
        return Reply._result

    @result.setter
    def result(self, value):
        Reply._result = value

    @property
    def code(self):
        return Reply._code

    @code.setter
    def code(self, value):
        Reply._code = value

    @property
    def msg(self):
        return Reply._msg

    @msg.setter
    def msg(self, value):
        Reply._msg = value

    @classmethod
    def json(cls):
        """
        :return:
        """
        data = {
            "result": cls._result,
            "code": cls._code,
            "msg": cls._msg
        }
        data = json.dumps(data, default=cls.object_to_dict)
        return Response(data, mimetype="application/json;charset=utf-8")

    @staticmethod
    def object_to_dict(value):
        data = {}
        for column in value.__table__.columns:
            data[column.name] = getattr(value, column.name)
        return data

    @classmethod
    def success(cls, result="", code=0):
        """
        :param code:
        :param result:
        :return:
        """
        if not result:
            result = cls._result
        cls._code = code
        cls._result = result
        cls._msg = ""
        return cls.json()

    @classmethod
    def error(cls, msg="", code=1):
        """
        :param code:
        :param msg:
        :return:
        """
        cls._code = code
        cls._msg = msg
        cls._result = ""
        return cls.json()
