#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: test.py
@time: 2023/1/9 12:42

"""
from flask import Flask, current_app, request

app = Flask(__name__)
ctx_app = app.app_context()
ctx_app.push()
print(current_app)
ctx_app.pop()

ctx_request = app.request_context(environ=xxx) #这段是伪代码
ctx_request.push()
print(request)
ctx_request.pop()
