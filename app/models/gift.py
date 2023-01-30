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
from sqlalchemy import Column, String, Integer, Float, Boolean, desc, func
from app.models.base import Base, db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')  # 关联到User模型
    uid = Column(Integer, ForeignKey('user.id'))  # 关联到user变量下的id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gift(cls, uid):
        gifts = cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        """wish_counts和get_user_gift的gifts一样，都是查询对象，无数据"""
        wish_counts = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()

        count_list = [{'count': wish[0], 'isbn': wish[1]} for wish in wish_counts]

        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]

        return count_list

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
