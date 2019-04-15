"""
Created by yy on 2019-04-15
"""

from app.api import api


@api.route("/user/login")
def login():
    return 'login'
