#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:42
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    """把蓝图web注册到app"""
    app.register_blueprint(web)
