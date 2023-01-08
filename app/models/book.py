#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/8 19:21
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm


from sqlalchemy import column, Integer, String
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = column(Integer, primary_key=True, autoIncrement=True)
    title = column(String(50), nullable=False)
    author = column(String(30), default='未名')
    binding = column(String(20))
    publisher = column(String(50))
    price = column(String(20))
    pages = column(Integer)
    pubdate = column(String(20))
    isbn = column(String(15), nullable=False, unique=True)
    summary = column(String(1000))
    image = column(String(50))
