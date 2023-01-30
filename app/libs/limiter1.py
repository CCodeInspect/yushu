#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: limiter1.py
@time: 2023/1/30 23:44

"""
from flask import current_app


class ApiLimter:

    def __init__(self):
        self.total = 0

    @classmethod
    def limiter(cls, func):
        def func(f):
            if f.total >= current_app.config['API_LIMITED']:
                f.__exit__()
            else:
                f
            return True

        return func
