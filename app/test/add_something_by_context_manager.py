#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: add_something_by_context_manager.py
@time: 2023/1/27 21:00

"""

from contextlib import contextmanager


@contextmanager
def print_total():
    print("《", end='')
    yield
    print("》", end='')


with print_total():
    print("格列佛游记", end='')
