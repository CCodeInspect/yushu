#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 00:00
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : secure.py
# @Software: PyCharm

DEBUG = True
PER_PAGE = 15
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:12345678@localhost:3306/yushu'
SECRET_KEY = '1234567'
BEANS_UPLOAD_ONE_BOOK = 0.5
BEANS_DOWNLOAD_ONE_BOOK = 1
RECENT_BOOK_COUNT = 30
API_LIMITED = 60

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '302869907@qq.com'
MAIL_PASSWORD = 'otuwarezykupbigj'
MAIL_SUBJECT_PREFIX = '[鱼书]邮件'
MAIL_SENDER = '鱼书<hello@pauline>'
