#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:42
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    """把蓝图web注册到app"""
    app.register_blueprint(web)
