#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : main.py
# @Software: PyCharm
from app.web import web


# from flask_login import login_required, current_user


@web.route('/')
def index():
    return "i am index"


@web.route('/personal')
# @login_required
def personal_center():
    pass
