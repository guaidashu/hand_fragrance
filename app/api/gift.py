"""
author songjie
"""
from flask import request, current_app
from flask_login import current_user, login_required

from app import db
from app.api import api
from app.libs.reply import Reply
from app.models.gift import Gift
from app.service.gift import GiftService
from app.view_models.gift import MyGifts


@api.route("/gifts/my_gift", methods=["POST"])
@login_required
def my_gift():
    """
    我的赠送清单
    :return:
    """
    uid = current_user.id
    gifts = Gift.get_user_gifts(uid)
    counter_list = GiftService.get_wish_counts(gifts)
    my_gifts = MyGifts(gifts, counter_list)
    gifts = my_gifts.package()
    return Reply.success(gifts)


@api.route("/gifts/book", methods=['POST'])
@login_required
def save_to_gifts():
    """
    点击赠送书籍后触发此接口进行 赠送存储
    :return:
    """
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


@api.route("/gifts/getRecentBooks", methods=['POST'])
def get_recent_books():
    """
    获取最近点击赠送的书籍
    :return:
    """
    books = GiftService.recent()
    return Reply.success(books)


@api.route("/gifts/redraw", methods=["POST"])
@login_required
def redraw_from_gifts():
    """
    从赠送清单移除
    :return:
    """
    gift_id = request.values.get("id")
    gift = Gift.query.filter_by(id=gift_id, launched=False).first_or_404()
    with db.auto_commit():
        current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
        gift.delete()
    return Reply.success()
