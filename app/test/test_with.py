#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: test_with.py
@time: 2023/1/9 15:09

"""


# todo:见 '/app/test/test_context_manager.py'


class A:
    def __enter__(self):
        print('进行占用资源')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print("process exception")
        else:
            print("no exception")
        print("释放资源")
        return False

    def query(self):
        print("进行查询")


try:
    with A() as qqq:
        # 1 / 0  # 异常
        qqq.query()
except Exception as ex:
    pass
