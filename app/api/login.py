"""
author songjie
"""
from flask import request

from app.api import api


@api.route("/login/index", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return show_login_page()
    else:
        return handle_login()


def handle_login():
    return "handle_login"


def show_login_page():
    return "show_login_page"
