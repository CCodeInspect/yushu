#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: user.py
@time: 2023/1/26 14:58

"""
import datetime
import json

import jwt
from flask import current_app
from flask_login import UserMixin, current_user
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    """面向对象不仅可以继承，继承之后如果想改写父类的方法的话，可以通过定义同名的函数来覆盖原来父类的函数"""
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True)
    confirmed = Column(Boolean, default=True)
    beans = Column(Float, default=0)
    send_counters = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return 'isbn不符合规范'
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            """
            1.不允许一个用户同时赠送多本相同的书
            2.一个用户不能同时成为赠送人和索要人
            3.当前赠送的图书既不在赠送清单，也不在心愿清单中才能赠送
            """
            return "当前isbn对应的书不存在"
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()

        if not gifting and not wishing:
            return True
        else:
            return False

    @staticmethod
    def reset_password(token, new_password):
        tk_decoder = User.token_decoder(token=token)
        if tk_decoder:
            user_id = tk_decoder['data']['user_id']
            if user_id:
                user = User.query.get(user_id)
                user.password = new_password
        return True

    def token_generator(self):
        """
        https://pyjwt.readthedocs.io/en/latest/usage.html
        :param user_id:
        :return:
        """
        dic = {
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=current_app.config['TOKEN_EXPIRE']),  # 过期时间
            'iat': datetime.datetime.now(),  # 发行时间
            'iss': current_app.config['TOKEN_ISS'],  # token签发者
            'data': {  # 内容，一般存放该用户id和开始时间
                'user_id': self.id
            }
        }
        s = jwt.encode(payload=dic, key=current_app.config['SECRET_KEY'],
                       algorithm=current_app.config['TOKEN_ALGORITHM'])  # 加密生成字符串
        return s

    @staticmethod
    def token_decoder(token):
        decoded = jwt.decode(jwt=token, key=current_app.config['SECRET_KEY'],
                             algorithms=current_app.config['TOKEN_ALGORITHM'])
        return decoded


@login_manager.user_loader
# 这里的loglogin_manager指的是在create_app时，LoginManager()的实例化对象loglogin_manager，而不是flask_login中的loglogin_manager(无user_loader属性)
def get_user(uid):
    return User.query.get(int(uid))
