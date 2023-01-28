#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm
from flask_login import current_user

from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.trade import Trade
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
    """
    1.当前isbn既不是gift也不是wish
    2.
    """
    has_in_gift = False
    has_in_wish = False

    # 拿到书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn=isbn)
    book = BookViewModel(yushu_book.get_first_element)

    # 判断当前用户是否登陆
    if current_user.is_authenticated:
        user_gift = Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False, status=1).first
        if user_gift:
            has_in_gift = True
        user_wish = Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False, status=1).first
        if user_wish:
            has_in_wish = True
    # 这里查到的是gift及wish的对象
    trade_gift = Gift().query.filter_by(isbn=isbn, launched=False).all()
    trade_wish = Wish().query.filter_by(isbn=isbn, launched=False).all()

    # 把gift及wish的对象传给Trade()
    gift_trade_models = Trade(trade_gift)
    wish_trade_models = Trade(trade_wish)

    return render_template('book_detail.html', book=book, wishes=wish_trade_models, gifts=gift_trade_models,
                           has_in_gift=has_in_gift, has_in_wish=has_in_wish)
