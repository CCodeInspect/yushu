#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: test_localstack.py
@time: 2023/1/10 17:15

"""
import threading
import time

from werkzeug.local import LocalStack

main_thread = threading.currentThread()
my_stack = LocalStack()
print("i 'm" + str(main_thread.getName()) + "。 stack.top ==  " + str(my_stack.top))  # 1


#
def get_a_new_stack():
    stack = LocalStack()
    stack = stack.top
    print(stack.top)
    return stack.top


thread2 = threading.Thread(name='thread2', target=get_a_new_stack)
thread2.start()
time.sleep(10)
print("i 'm" + str(main_thread.getName()) + "。 stack.top ==  " + str(my_stack.top))  # 1
