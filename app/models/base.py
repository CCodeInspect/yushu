#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: base.py
@time: 2023/1/26 14:58

"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, Float, Boolean, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)

    # create_time = Column()

    def set_attrs(self, attr_dict):
        for k, v in attr_dict.items():
            if hasattr(self, k) and k != 'id':
                setattr(self, k, v)
