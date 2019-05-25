"""
author songjie
"""
from flask import request

from app.libs.conversion_data_type import ConversionDataType
from app.libs.reply import Reply


def handle_login():
    """
    handle login event
    :return:
    """
    user_name = request.values.get("userName")
    password = request.values.get("password")
    if str(user_name) == '13739497421':
        if password == 'wyysdsa!':
            return Reply.success("ok")
    return Reply.error("用户名或密码错误")


def handle_register():
    """
    handle register event
    :return:
    """
    form = request.values
    form = ConversionDataType.combined_multi_dict_to_dict(form)
    del form['rePassword']
    return Reply.success(form)
