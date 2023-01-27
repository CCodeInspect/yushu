#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: base.py
@time: 2023/1/26 14:58

"""
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, String, Integer, Float, Boolean, SmallInteger
from contextlib import contextmanager


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


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    # create_time = Column()

    def set_attrs(self, attr_dict):
        for k, v in attr_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
