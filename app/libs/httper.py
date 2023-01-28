#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 02:22
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : httper.py
# @Software: PyCharm
import requests


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {'errrr': 'code不为200，你的请求有问题，自查哈'} if return_json else ''
        return r.json() if return_json else r.text
