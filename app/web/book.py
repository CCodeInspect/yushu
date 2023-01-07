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


@web.route(rule='/book/search/<q>/<page>')  # 路由注册到蓝图
def search(q, page):
    """

    :param q: 查询条件为：（1）纯13位isbn数字；（2）纯10位isbn数字,并且包含'-'；（3）普通的字符
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        res = YuShu.search_by_isbn(q)
        print(res)
    else:
        res = YuShu.search_by_keyword(q)
    return res
