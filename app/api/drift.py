"""
author songjie
"""
from flask import request
from flask_login import login_required, current_user
from sqlalchemy import or_, desc

from app.api import api
from app.forms.book import DriftForm
from app.libs.reply import Reply
from app.models.drift import Drift
from app.models.gift import Gift
from app.service.drift import DriftService
from app.view_models.drift import DriftViewModel
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


@api.route("/drift/sendDrift", methods=['POST'])
@login_required
def send_drift():
    gift_id = request.values.get("gift_id")
    current_gift = Gift.query.get_or_404(gift_id)
    if current_gift.is_yourself_gift(current_user.id):
        return Reply.error("这本书是你自己的，不能向自己索取")
    can = current_user.can_send_drift()
    if not can:
        return Reply.error("你有条件不满足，无法发起索要书籍")
    form = DriftForm(request.values)
    if not form.validate():
        return Reply.error(form.errors)
    DriftService.save_a_drift(form, current_gift)
    return Reply.success()


@api.route("/drift/getDriftList", methods=["POST"])
@login_required
def get_drift_list():
    drifts = Drift.query.filter(
        or_(Drift.requester_id == current_user.id, Drift.gifter_id == current_user.id)).order_by(
        desc(Drift.create_time)).all()
    drifts = DriftViewModel.pending(drifts)
