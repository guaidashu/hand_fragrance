"""
author songjie
"""
from flask import request

from app.api import api


@api.route("/login", methods=['GET', 'POST'])
def login():
    """
    :return:
    """
    if request.method == 'GET':
        return show_login_page()
    else:
        return handle_login()


def handle_login():
    """
    :return:
    """
    return "handle_login"


def show_login_page():
    """
    :return:
    """
    return "show_login_page"
