#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: drift.py
@time: 2023/2/2 09:24

"""
from app.models.base import Base
from sqlalchemy import Column, String, Integer, Boolean, SmallInteger


class Drift(Base):
    """
    1.一次具体交易信息
    2.具有记录性质的模型不要做模型关联
    3.如果模型中有关联，修改a模型的数据必然会影响到被关联模型的数据
    4.不关联会有数据冗余，是违反了数据库的设计原则
    5.利用合理冗余，减少数据库的查询次数
    """
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    mobile = Column(String(20), nullable=False)
    message = Column(String(200))

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    pending = Column(SmallInteger, default=1)



