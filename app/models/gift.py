#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: gift.py
@time: 2023/1/26 14:58

"""
from flask import current_app
from sqlalchemy import Column, String, Integer, Float, Boolean, desc
from app.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')  # 关联到User模型
    uid = Column(Integer, ForeignKey('user.id'))  # 关联到user变量下的id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_recent_gifts(cls):
        """
        链式调用
        1：主体 Query
        2：子函数
        3.first()  all()
        """
        recent_gifts = cls.query.filter_by(launched=False).group_by(cls.isbn).order_by(desc(cls.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()
        return recent_gifts
