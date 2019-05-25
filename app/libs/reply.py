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
        Reply._result = kwargs.setdefault("result", "")
        Reply._code = kwargs.setdefault("code", 0)
        Reply._msg = kwargs.setdefault("msg", "")

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
        data = json.dumps(data)
        return Response(data, mimetype="application/json;charset=utf-8")

    @classmethod
    def success(cls, result=""):
        """
        :param result:
        :return:
        """
        if result == "":
            result = cls._result
        cls._code = 0
        cls._result = result
        return cls.json()

    @classmethod
    def error(cls, msg=""):
        """
        :param msg:
        :return:
        """
        cls._code = 1
        cls._msg = msg
        return cls.json()