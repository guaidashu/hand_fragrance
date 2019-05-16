"""
author songjie
"""
import json

from flask import Response


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
        data = {
            "result": self._result,
            "status": self.status,
            "msg": self.msg
        }
        return Response(json.dumps(data), mimetype="application/json;charset=utf-8")
