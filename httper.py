#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 02:22
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : httper.py
# @Software: PyCharm
import requests
from return_normal import return_json, return_text


class HTTP(object):
    @staticmethod
    def get(url, return_json1=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {'errrrr': '123'} if return_json1 else ''
        return r.json() if return_json1 else r.text
