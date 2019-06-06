"""
author songjie
"""
from flask import request, current_app
from flask_login import current_user, login_required

from app import db
from app.api import api
from app.libs.reply import Reply
from app.models.gift import Gift


@api.route("/gifts/my_gift")
def my_gift():
    pass


@api.route("/gifts/book", methods=['POST'])
@login_required
def save_to_gifts():
    isbn = request.values.get("isbn")
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
        return Reply.success()
    else:
        return Reply.error("该书籍已存在心愿清单或赠送清单，无法赠送")
