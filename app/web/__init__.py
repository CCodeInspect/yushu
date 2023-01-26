#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 13:42
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish