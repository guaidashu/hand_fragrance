"""
author songjie
"""
from flask import request, Flask

# app = Flask(__name__)
# 单元测试用例
# with app.test_request_context('/hello', method="POST"):
#     assert request.path == '/hello'
#     assert request.method == 'POST', '请求方式出错'
from flask_mail import Mail


def send_email():
    mail = Mail()
