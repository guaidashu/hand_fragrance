"""
author songjie
"""
from flask import request

from app.admin import admin


@admin.route('/user/index')
def index():
    uuid = request.args.get("id", 'id')
    return uuid
