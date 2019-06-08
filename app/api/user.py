"""
Created by yy on 2019-04-15
"""
from flask_login import current_user, login_required, logout_user

from app.api import api
from app.libs.reply import Reply
from app.service.login import handle_login, handle_register


@api.route('/user/getUserInfo', methods=['POST'])
def get_user_info():
    if current_user.id:
        return Reply.success(current_user, data_type=2)
    else:
        return Reply.success(current_user)


@api.route("/user/login", methods=['POST'])
def login():
    """
    :return:
    """
    return handle_login()


@api.route("/user/register", methods=['POST'])
def register():
    """
    :return:
    """
    return handle_register()


@api.route("/user/logout", methods=["POST"])
@login_required
def logout():
    """
    登出
    :return:
    """
    logout_user()
    return Reply.success()
