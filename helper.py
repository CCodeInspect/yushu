#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 01:45
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : helper.py
# @Software: PyCharm

def is_isbn_or_key(word):
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
        short = word.replace('-', '')
    if '-' in word and len(short) == 10 and short.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
