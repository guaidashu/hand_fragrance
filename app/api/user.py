"""
Created by yy on 2019-04-15
"""
from flask import request

from app.api import api


@api.route('/user/getUserInfo')
def get_user_info():
    return 'get user info'
