"""
author songjie
"""
import json
from sqlalchemy import Column, String
from sqlalchemy import Integer

from app.models.base import Base


class Book(Base):
    """
    一些属性定义重复性比较大，元类可以解决这个问题
    id: 唯一主键id
    title: 书籍标题(名称)
    _author: 作者
    binding: 书籍的装帧(平装或者精装)
    publisher: 出版社
    price: 价格
    pages: 总页数
    pubdate: 出版日期
    isbn: 国际书籍标号
    summary: 简介
    image: 图片路径
    """
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    @property
    def author(self):
        return self._author if not self._author else json.loads(self._author)

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            self._author = json.dumps(value, ensure_ascii=False)
        else:
            self._author = value

    @property
    def author_str(self):
        return '' if not self._author else '、'.join(self.author)
