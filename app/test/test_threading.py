#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: test_threading.py
@time: 2023/1/9 23:40

"""
import threading
import time


def operate_func():
    print("123")
    t = threading.current_thread()
    print(t.getName())


# main_thread = threading.main_thread()
# print(main_thread.getName())

# another_thread = threading.Thread(target=operate_func, name='aaaaa')
# print(another_thread.getName())
thread_4 = threading.Thread()  # Thread-1
print(thread_4.getName())
time.sleep(60)
thread_4.start()

thread_3 = threading.current_thread()  # MainThread
print(thread_3.getName())

thread_5 = threading.Thread()  # Thread-2
print(thread_5.getName())
