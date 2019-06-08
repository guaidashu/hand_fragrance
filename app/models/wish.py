"""
author songjie
"""

from app.spider.get_book_data import GetBookData
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base


class Wish(Base):
    __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        get_book_data = GetBookData()
        get_book_data.search_by_isbn(self.isbn)
        return get_book_data.first
