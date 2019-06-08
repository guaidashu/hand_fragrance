"""
author songjie
"""
from math import floor

from flask_login import UserMixin
from app import login_manager
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from app.libs.enums import PendingStatus
from app.libs.helper import Helper
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Base
from app.models.drift import Drift
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.get_book_data import GetBookData


class User(UserMixin, Base):
    """
    id:
    nickname: 昵称、用户名
    phone_number: 电话号码
    email: 邮箱
    confirmed: 确认
    beans:
    send_counter
    receive_counter
    gifts
    """
    # __tablename__ 用以指定表名
    __tablename__ = 'user'
    # __bind_key__ = 'fisher'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(11), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    # gifts = relationship('Gift')

    _password = Column('password', String(255))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if Helper.is_isbn_or_key(isbn) != 'isbn':
            return False
        get_book_data = GetBookData()
        get_book_data.search_by_isbn(isbn)
        if not get_book_data.first:
            return False
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

    def can_send_drift(self):
        if self.beans < 1:
            return False
        success_gifts = Drift.query.filter(Drift.pending == PendingStatus.success,
                                           Drift.gifter_id == self.id).count()
        success_receive = Drift.query.filter(Drift.pending == PendingStatus.success,
                                             Drift.requester_id == self.id).count()
        return True if floor(success_gifts) >= floor(success_receive / 2) else False


@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))
