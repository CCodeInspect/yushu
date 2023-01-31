#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: wish.py
@time: 2023/1/27 18:37

"""
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')  # 关联到User模型
    uid = Column(Integer, ForeignKey('user.id'))  # 关联到user变量下的id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wish_list(cls, uid):
        wish = cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()
        return wish

    @classmethod
    def get_gifts_count(cls, isbn_list):
        """使用in在wishes表中查询isbn列表中的心愿，计算数量"""
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(
            Gift.isbn).all()

        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]

        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first
