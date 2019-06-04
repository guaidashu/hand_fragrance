"""
author songjie
"""
from flask import request

from app.forms.user import RegisterForm, LoginForm
from app.models.base import db
from app.libs.conversion_data_type import ConversionDataType
from app.libs.reply import Reply
from app.models.user import User


def handle_login():
    """
    handle login event
    :return:
    """
    form = LoginForm(request.values)
    # user_name = request.values.get("userName")
    # password = request.values.get("password")
    if not form.validate():
        return Reply.error(form.errors)
    user = User.query.filter_by(email=form.email.data).first()
    if user:
        if not user.check_password(form.password.data):
            return Reply.error("用户名或密码错误")
    else:
        return Reply.error("用户名或密码错误")
    return Reply.success()


def handle_register():
    """
    handle register event
    :return:
    """
    # form = request.values
    # form = ConversionDataType.combined_multi_dict_to_dict(form)
    # del form['rePassword']
    form = RegisterForm(request.values)
    if not form.validate():
        return Reply.error(form.errors)
    user = User()
    user.set_attrs(form)
    db.session.add(user)
    db.session.commit()
    return Reply.success(user)
