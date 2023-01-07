#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/6 23:36
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : fisher.py
# @Software: PyCharm


from app import create_app

app = create_app()

# app.add_url_rule('/hello/', view_func=hello)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=50014)
