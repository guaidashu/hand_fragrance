"""
author songjie
"""
from flask import request
from flask_login import login_user

from app.forms.user import RegisterForm, LoginForm
from app.models.base import db
from app.libs.reply import Reply
from app.models.user import User


def handle_login():
    """
    handle login event
    :return:
    """
    form = LoginForm(request.values)
    if not form.validate():
        return Reply.error(form.errors)
    user = User.query.filter_by(email=form.email.data).first()
    if user:
        if not user.check_password(form.password.data):
            return Reply.error("用户名或密码错误")
    else:
        return Reply.error("用户名或密码错误")
    # 保存用户信息(票据)
    login_user(user, remember=True)
    return Reply.success(user, data_type=2)


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
    with db.auto_commit():
        user = User()
        user.set_attrs(form)
        db.session.add(user)
    return Reply.success()
