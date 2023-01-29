#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:42
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : __init__.py.py
# @Software: PyCharm

from flask import Flask
from app.models.base import db
from flask_login import LoginManager

login_manager = LoginManager()


def create_app():
    app = Flask(__name__)  # __name__决定了项目的根目录是app而不是app上一级fisher_flask
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'  # login_view知道了web.login是登陆视图函数
    login_manager.login_message = '请先登录或注册'

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    from app.web.book import web
    """把蓝图web注册到app"""
    app.register_blueprint(web)
