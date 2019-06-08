"""
author songjie
"""
from flask import request, current_app
from flask_login import login_required, current_user

from app import db
from app.api import api
from app.libs.reply import Reply
from app.models.wish import Wish


@api.route("/wish/book", methods=['POST'])
@login_required
def save_to_wish():
    """
    添加到心愿清单
    :return:
    """
    isbn = request.values.get("isbn")
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
        return Reply.success()
    else:
        return Reply.error("该书籍已存在心愿清单或赠送清单，无法添加到心愿清单")
