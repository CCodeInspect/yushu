#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : wish.py
# @Software: PyCharm
from flask import current_app, flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app.libs.email import send_mail
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.trade import MyTrades
from app.web import web
from app.models.base import db


def limit_key_prefix():
    pass


@web.route('/my/wish')
def my_wish():
    """
    1.查当前登陆用户的所有wish
    2.每个wish对应的gift
    :return:
    """
    uid = current_user.id
    my_wishes_list = Wish.get_user_wish_list(uid=uid)
    isbn_list = [w.isbn for w in my_wishes_list]
    gift_count = Wish.get_gifts_count(isbn_list=isbn_list)
    view_model_wishes = MyTrades(trades_of_mine=my_wishes_list, trade_count_list=gift_count)
    return render_template('my_wish.html', wishes=view_model_wishes.trades)


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn=isbn):
        with db.auto_commit():
            wish = Wish()
            wish.isbn = isbn
            wish.uid = current_user.id
            db.session.add(wish)
    else:
        flash('这本书已添加到心愿清单或赠送清单，请不要重复添加')
    return redirect(url_for(endpoint='web.book_detail', isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
@login_required
def satisfy_wish(wid):
    wish = Wish.query.filter_by(wid)
    gift = Gift.query.filter_by(uid=current_user.id, isbn=wish.isbn).first()
    if not gift:
        flash(message="你还没有上传此书，请点击'加入此赠送清单'添加此书。添加前，请确保自己可以赠送此书")
    else:
        send_mail(wish.user.email, "有人想送你一本书", 'email/satisfy_wish.html', wish=wish, gift=gift)
        flash(message="已向他/她发送了一封邮件，如果他/她愿意接受你的赠送，你将收到一个鱼漂")
    return redirect(url_for('web.book_detail', isbn=wish.isbn))


@web.route('/wish/book/<isbn>/redraw')
@login_required
def redraw_from_wish(isbn):
    wish = Wish.query.filter_by(isbn=isbn, launched=False).first_or_304()
    with db.auto_commit():
        wish.delete()
    return redirect(url_for('web.my_wish'))


def satifiy_with_limited():
    pass
