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
from flask import current_app


class YuShu:
    url_search_by_isbn = 'http://t.talelin.com/v2/book/isbn/{}'
    url_search_by_keyword = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        r = HTTP.get(cls.url_search_by_isbn.format(isbn))
        return r

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        r = HTTP.get(
            cls.url_search_by_keyword.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page)))
        return r

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
