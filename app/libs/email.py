#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: email.py
@time: 2023/2/1 12:46

"""
from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_mail(to, subject, template, **kwargs):
    # msg = Message(subject='测试邮件', sender='302869907@qq.com', body='123', recipients=['302869907@qq.com'])
    msg = Message('[鱼书]' + '' + subject, sender=current_app.config['MAIL_USERNAME'], recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(message=msg)
