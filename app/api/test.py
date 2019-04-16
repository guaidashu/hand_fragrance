"""
author songjie
"""
from flask import render_template

from app.api import api


@api.route('/test')
def test():
    data = {"title": "测试页"}
    return render_template("test/test.html", data=data)
