#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: wish.py
@time: 2023/1/27 18:37

"""
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')  # 关联到User模型
    uid = Column(Integer, ForeignKey('user.id'))  # 关联到user变量下的id
    isbn = Column(String(15), nullable=False)
    # book = relationship('Book')
    # book_id = Column(Integer, ForeignKey('book.id'))
    launched = Column(Boolean, default=False)
