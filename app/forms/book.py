#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 16:39
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : book.py
# @Software: PyCharm

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForms(Form):
    """DataRequired去除了q为单个空字符但page有值的情况"""
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
