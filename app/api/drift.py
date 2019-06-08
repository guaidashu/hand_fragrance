"""
author songjie
"""
from flask import request
from flask_login import login_required

from app.api import api
from app.libs.reply import Reply
from app.models.gift import Gift
from app.view_models.trade import TradeInfo


@api.route("/drift/getGiftUserInfo", methods=['POST'])
@login_required
def get_gift_user_info():
    """
    根据礼物id获取 礼物的信息，包括
    {
        赠送者的所有用户信息
        赠送事件发布时间
    }
    :return:
    """
    gift_id = request.values.get("id")
    gift = Gift.query.filter_by(id=gift_id).first()
    gift = TradeInfo.map_to_trade(gift)
    return Reply.success(gift, data_type=2)
