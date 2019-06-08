"""
author songjie
"""
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc
from sqlalchemy.orm import relationship

from app.models import Base
from app.spider.get_book_data import GetBookData


class Gift(Base):
    __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        # 用于判断是否是自己的礼物
        if self.uid == uid:
            return True

    @property
    def book(self):
        """
        所有模型都只返回原始数据
        :return:
        """
        get_book_data = GetBookData()
        get_book_data.search_by_isbn(self.isbn)
        return get_book_data.first

    # @classmethod
    # @cache.memoize(timeout=600)
    # def recent(cls):
    #     gift_list = cls.query.filter_by(launched=False).order_by(
    #         desc(Gift.create_time)).group_by(Gift.book_id).limit(
    #         current_app.config['RECENT_BOOK_PER_PAGE']).all()
    # view_model = GiftsViewModel.recent(gift_list)
    # return view_model

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(
            uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts
