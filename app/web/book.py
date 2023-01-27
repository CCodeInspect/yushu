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
from flask import request, render_template, flash
from app.forms.book import SearchForms
from app.view_models.book import BookViewModel, BookCollections


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
            yushu_book.search_by_isbn(isbn=q)
        else:
            yushu_book.search_by_keyword(keyword=q, page=page)
        # __dict__
        books.fill(yushu_book=yushu_book, keyword=q)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template(template_name_or_list='search_result.html', books=books)


@web.route('/test')
def test():
    r = {
        'name': 'pauline',
        'age': 18
    }
    flash(message='i am message', category='warning')
    flash(message='message2', category='error')
    r1 = {
        'name': 'solotov.liu',
        'identified': 'husband'
    }
    return render_template(template_name_or_list='test.html', data=r, context2=r1)


@web.route('/test1')
def test2():
    r = {'sex': 'male'}
    return render_template(template_name_or_list='test2.html', data=r)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn=isbn)
    book = BookViewModel(yushu_book.get_first_element)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])
