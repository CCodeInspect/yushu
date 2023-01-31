#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: auth.py
@time: 2023/1/26 15:44

"""

from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError

from app.models.user import User


class RegisterForm(Form):
    nickname = StringField(validators=[Length(min=2, max=10), DataRequired('昵称至少需要2个字符，最多10个字符')])
    email = StringField(validators=[Length(min=8, max=64), DataRequired(), Email('电子邮箱不符合规范')])
    password = PasswordField(validators=[Length(min=6, max=32), DataRequired('密码不能为空，请输入你的密码')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('用户名重复')


class LoginForm(Form):
    email = StringField(validators=[Length(min=8, max=64), DataRequired(), Email('电子邮箱不符合规范')])
    password = PasswordField(validators=[Length(min=6, max=32), DataRequired('密码不能为空，请输入你的密码')])


class EmailForm(Form):
    email = StringField(validators=[Length(min=8, max=64), DataRequired(), Email('电子邮箱不符合规范')])
