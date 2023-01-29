#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: base.py
@time: 2023/1/26 14:58

"""
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, String, Integer, Float, Boolean, SmallInteger
from contextlib import contextmanager
from datetime import datetime


class SQLAlchemy(_SQLAlchemy):
    """
    1.给flask_sqlalchemy 原生的SQLAlchemy 给别名 '_SQLAlchemy'
    2.使用contextmanager包装了业务中需要提交之前的所有代码
    3.业务可直接调用auto_commit()
    """

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    create_time = Column('create_time', Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attr_dict):
        for k, v in attr_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)

    @property
    def create_date_time(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
