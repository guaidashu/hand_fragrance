"""
Created by yy on 2019-04-15
"""
from app.api import api
from app.service.login import handle_login


@api.route('/user/getUserInfo')
def get_user_info():
    return 'get user info'


@api.route("/user/login", methods=['POST'])
def login():
    """
    :return:
    """
    return handle_login()
