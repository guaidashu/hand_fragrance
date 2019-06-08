"""
author songjie
"""
import json

from flask import Response


class Reply(object):
    _result = None
    _code = None
    _msg = None
    _data_type = 1

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

    @property
    def data_type(self):
        return Reply._data_type

    @data_type.setter
    def data_type(self, value):
        Reply._data_type = value

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

    @classmethod
    def object_to_dict(cls, value):
        data = {}
        if Reply._data_type == 1:
            return value.__dict__
        try:
            for column in value.__table__.columns:
                data[column.name] = getattr(value, column.name)
        except:
            data = value.__dict__
        return data

    @classmethod
    def success(cls, result="", code=0, data_type=1):
        """
        :param data_type:
        :param code:
        :param result:
        :return:
        """
        cls._data_type = data_type
        if not result:
            result = cls._result
        cls._code = code
        cls._result = result
        cls._msg = ""
        return cls.json()

    @classmethod
    def error(cls, msg="", code=1, data_type=1):
        """
        :param data_type:
        :param code:
        :param msg:
        :return:
        """
        cls._data_type = data_type
        cls._code = code
        cls._msg = msg
        cls._result = ""
        return cls.json()
