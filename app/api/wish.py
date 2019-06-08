"""
author songjie
"""
from flask import request, current_app
from flask_login import login_required, current_user

from app import db
from app.api import api
from app.libs.reply import Reply
from app.models.gift import Gift
from app.models.wish import Wish
from app.service.wish import WishService
from app.view_models.wish import MyWishes
from app.libs.email import send_email


@api.route("/wish/getMyWishes", methods=['POST'])
@login_required
def my_wish():
    """
    获取我的心愿清单
    :return:
    """
    uid = current_user.id
    wishes = Wish.get_user_wishes(uid)
    counter_list = WishService.get_gifts_count(wishes)
    my_wishes = MyWishes(wishes, counter_list)
    wishes = my_wishes.package()
    return Reply.success(wishes)


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


@api.route("/wish/redraw", methods=["POST"])
@login_required
def redraw_from_wishes():
    """
    从心愿清单移除
    :return:
    """
    wish_id = request.values.get("id")
    wish = Wish.query.filter_by(id=wish_id, launched=False).first_or_404()
    with db.auto_commit():
        current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
        wish.delete()
    return Reply.success()


@api.route("/wish/satisfy", methods=["POST"])
@login_required
def satisfy():
    # 赠送别人书籍
    wish_id = request.values.get("wish_id")
    # 首先查询gift
    wish = Wish.query.get_or_404(wish_id)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        return Reply.error("你没有上传此书，请点击赠送此书后再进行此操作")
    else:
        # 发送邮件
        send_email(wish.user.email, "有人想送你一本书", 'email/satisfy_wish', wish=wish, gift=gift)
        return Reply.success()
