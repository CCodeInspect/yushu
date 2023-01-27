#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: test_context_manager.py
@time: 2023/1/27 20:47

"""

# todo:见 '/app/test/test_with.py'


from contextlib import contextmanager


class Cc():
    # def __enter__(self):
    #     print('i am enter')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('i am exit')

    def query(self):
        print('i am query in cc')


# with Cc() as r:
#     r.query()


@contextmanager
def make_my_cc():
    print('i am enter')
    yield Cc()
    print('i am exit')


with make_my_cc() as r:
    r.query()
