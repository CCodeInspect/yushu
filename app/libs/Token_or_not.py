#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: Token_or_not.py
@time: 2023/2/1 15:25

"""
import time

import jwt, datetime


def get_token():
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=30),  # 过期时间
        'iat': int(time.time()) + 1,  # 发行时间
        'iss': '123',  # token签发者
        'data': {  # 内容，一般存放该用户id和开始时间
            'user_id': '123'
        }
    }

    a = jwt.encode(payload=dic, key='212',
                   algorithm='HS256')
    print(a)
    return a


def decode(token):
    s = jwt.decode(jwt=token, key='212', algorithms='HS256')
    print(s)
    return s


d = get_token()

if __name__ == '__main__':
    get_token()
    decode(token=d)
