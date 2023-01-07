#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 03:02
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : yushu_book.py
# @Software: PyCharm

import requests, json
from flask import jsonify

from httper import HTTP


class YuShu:
    url_search_by_isbn = 'http://t.talelin.com/v2/book/isbn/{}'
    url_search_by_keyword = 'http://yushu.talelin.com/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        r = HTTP.get(cls.url_search_by_isbn.format(isbn))
        return r

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        r = HTTP.get(cls.url_search_by_keyword.format(keyword, count, start))
        return r
