#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : wish.py
# @Software: PyCharm
from app.web import web


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
# @login_required
def save_to_wish(isbn):
    pass


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
# @login_required
def redraw_from_wish(isbn):
    pass


def satifiy_with_limited():
    pass
