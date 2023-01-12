#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.web import web
from flask import request, jsonify
from app.forms.book import SearchForms
from app.view_models.book import BookCollections, BookViewModel
import json


@web.route(rule='/book/search')  # 路由注册到蓝图
def search():
    """

    :param q: 查询条件为：（1）纯13位isbn数字；（2）纯10位isbn数字,并且包含'-'；（3）普通的字符
    :param page:
    :return:
    """
    form = SearchForms(request.args)  # 这里要传入request.args,否则q会为none
    books = BookCollections()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        # __dict__
        books.fill(yushu_book=yushu_book, keyword=q)
        return json.dumps(books, default=lambda x: x.__dict__)
    else:
        return json.dumps(form.errors)
