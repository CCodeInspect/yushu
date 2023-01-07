#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm
from helper import is_isbn_or_key
from yushu_book import YuShu
from app.web import web
from flask import request, jsonify
from app.forms.book import SearchForms


@web.route(rule='/book/search')  # 路由注册到蓝图
def search():
    """

    :param q: 查询条件为：（1）纯13位isbn数字；（2）纯10位isbn数字,并且包含'-'；（3）普通的字符
    :param page:
    :return:
    """
    form = SearchForms(request.args)  # 这里要传入request.args,否则q会为none
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            res = YuShu.search_by_isbn(q)
        else:
            res = YuShu.search_by_keyword(q, page)
        return jsonify(res)
    else:
        return jsonify(form.errors)
