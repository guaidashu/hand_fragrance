"""
author songjie
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import Base


class User(Base):
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
    phone_number = Column(String(18), unique=True)
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
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)
