#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 17:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : auth.py
# @Software: PyCharm
from app.web import web
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.user import User
from app.models.base import db


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        with db.auto_commit():
            """
            在这里调用auto_commit时，
            不需要重新示例化 app/models/base/类SQLAlchemy,
            因为在 app/models/base/类SQLAlchemy 已经被实例化成db了。
            """
            user = User()
            user.set_attrs(form.data)
            db.session().add(user)
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('用户不存在或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST' and form.validate():
        account_email = form.email.data
        user = User.query.filter_by(email=account_email).first_or_404()
        from app.libs.email import send_mail
        send_mail(to=form.email.data, subject='重置你的密码', template='email/reset_password.html', user=user,
                  token=user.generate_token())
    return render_template('auth/forget_password_request.html', form=form)


# 单元测试
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method and form == 'POST':
        pass
    return render_template('auth/forget_password.html')


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(endpoint='web.index'))
