#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : main.py
# @Software: PyCharm
from flask import render_template

from app.view_models.book import BookViewModel
from app.web import web
from app.models.gift import Gift


@web.route('/')
def index():
    recent_gifts = Gift.get_recent_gifts()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent1=books)


@web.route('/personal')
# @login_required
def personal_center():
    pass

