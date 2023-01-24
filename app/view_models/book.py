#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: book.py
@time: 2023/1/12 17:43

"""


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = book['author']
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    def intro_1(self):
        """intro_1() == intro(),intro()使用了filter()"""
        if self.title:
            pass
        if self.publisher:
            pass
        if self.author:
            pass

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [str(self.author), self.publisher, self.price])
        return '/'.join(intros)


class BookCollections:
    def __init__(self):
        self.total = 0
        self.keyword = ''
        self.books = []

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class __BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['books'] = [cls.__cut_data(data)]
            returned['total'] = 1
        else:
            print("total表达式返回False且total== " + data['total'])
        return returned

    @classmethod
    def package_collections(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['books'] = [cls.__cut_data(data=book) for book in data['books']]
            returned['total'] = data['total']
        else:
            print("返回的data有问题，请自查")
        return returned

    @classmethod
    def __cut_data(cls, data):
        data = {
            'title': data['title'] or '',
            'publisher': data['publisher'] or '',
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']) or '',
            'price': data['price'] or '',
            'summary': data['summary'] or '',
            'image': data['image'] or ''
        }
        return data
