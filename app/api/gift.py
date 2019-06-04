"""
author songjie
"""
from flask import request

from app.api import api


@api.route("/gifts/my_gift")
def my_gift():
    pass


@api.route("/gifts/book")
def save_to_gifts():
    isbn = request.values.get("isbn")
