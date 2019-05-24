"""
author songjie
"""
import json

from flask import Response

from tool.lib.function import debug


class Reply(object):
    def __init__(self, **kwargs):
        self._result = kwargs.setdefault("result", "")
        self._status = kwargs.setdefault("status", 0)
        self._msg = kwargs.setdefault("msg", "")

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def json(self):
        """
        :return:
        """
        data = {
            "result": self._result,
            "status": self._status,
            "msg": self._msg
        }
        debug(data)
        data = json.dumps(data)
        debug(data)
        return Response(data, mimetype="application/json;charset=utf-8")

    def success(self, result=""):
        """
        :param result:
        :return:
        """
        if result == "":
            result = self._result
        self._status = 0
        self._result = result
        return self.json()

    def error(self, msg=""):
        """
        :param msg:
        :return:
        """
        self._status = 1
        self._msg = msg
        return self.json()
