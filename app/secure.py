#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 00:00
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : secure.py
# @Software: PyCharm

DEBUG = True
PER_PAGE = 15
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:12345678@localhost:3306/ihuanshu'
SECRET_KEY = ''
BEANS_UPLOAD_ONE_BOOK = 0.5
BEANS_DOWNLOAD_ONE_BOOK = 1
RECENT_BOOK_COUNT = 30
API_LIMITED = 60

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
# MAIL_USERNAME = ''


# Token
TOKEN_ISS = ''
TOKEN_EXPIRE = 30
TOKEN_ALGORITHM = 'HS256'
