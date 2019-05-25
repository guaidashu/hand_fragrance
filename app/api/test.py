"""
author songjie
"""
from flask import render_template

from app.api import api
from tool.lib.function import curl_data, debug


@api.route('/test')
def test():
    data = {"title": "测试页"}
    return render_template("test/test.html", data=data)


@api.route('/test/testCurl')
def test_curl():
    data, res = curl_data("https://blog.tan90.club", return_response=True)
    return data
