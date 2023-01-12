#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 03:02
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : yushu_book.py
# @Software: PyCharm

from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    url_search_by_isbn = 'http://t.talelin.com/v2/book/isbn/{}'
    url_search_by_keyword = 'http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collections(self, data):
        if data:
            self.books = data['books']
            self.total = data['total']

    def search_by_isbn(self, isbn):
        url = self.url_search_by_isbn.format(isbn)
        r = HTTP.get(url)
        self.__fill_single(r)

    def search_by_keyword(self, keyword, page=1):
        url = self.url_search_by_keyword.format(keyword, current_app.config['PER_PAGE'],
                                                self.calculate_start(page))
        r = HTTP.get(url)
        self.__fill_collections(r)

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']
