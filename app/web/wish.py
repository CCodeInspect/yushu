#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : wish.py
# @Software: PyCharm
from flask import current_app, flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.wish import Wish
from app.web import web
from app.models.base import db


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn=isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加到心愿清单或赠送清单，请不要重复添加')
    return redirect(url_for(endpoint='web.book_detail'), isbn=isbn)


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
# @login_required
def redraw_from_wish(isbn):
    pass


def satifiy_with_limited():
    pass
