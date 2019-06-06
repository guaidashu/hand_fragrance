"""
Created by yy on 2019-04-15
"""
from flask_login import current_user

from app.api import api
from app.libs.reply import Reply
from app.service.login import handle_login, handle_register


@api.route('/user/getUserInfo', methods=['POST'])
def get_user_info():
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
