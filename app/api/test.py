"""
author songjie
"""
from flask import render_template

from app.api import api
from app.libs.email import send_test
from app.libs.reply import Reply
from tool.lib.function import curl_data, debug


@api.route('/test')
def test():
    data = {"title": "测试页"}
    return render_template("test/test.html", data=data)


@api.route('/test/testCurl')
def test_curl():
    data, res = curl_data("https://blog.tan90.club", return_response=True)
    return data


@api.route("/test/sendEmail")
def send_mail():
    # send_test("这是一封测试邮件")
    return Reply.success("send successful")
