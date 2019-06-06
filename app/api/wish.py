"""
author songjie
"""
from flask import request
from flask_login import login_required

from app.api import api


@api.route
@login_required
def save_to_wish():
    isbn = request.values.get("isbn")
