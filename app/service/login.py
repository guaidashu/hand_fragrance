"""
author songjie
"""
from flask import request

from app.libs.reply import Reply
from tool.lib.function import debug


def handle_login():
    """
    :return:
    """
    user_name = request.values.get("userName")
    password = request.values.get("password")
    reply = Reply()
    if str(user_name) == '13739497421':
        if password == 'wyysdsa!':
            reply.result = "ok"
        else:
            reply.status = 1
    else:
        reply.status = 1
    return reply.json()
