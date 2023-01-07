#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/6 23:36
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : fisher.py
# @Software: PyCharm


from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')
print(app.config)
from helper import is_isbn_or_key
from yushu_book import YuShu


@app.route(rule='/book/search/<q>/<page>')  # 路由注册
def search(q, page):
    """

    :param q: 查询条件为：（1）纯13位isbn数字；（2）纯10位isbn数字,并且包含'-'；（3）普通的字符
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        res = YuShu.search_by_isbn(q)
        print(res)
    else:
        res = YuShu.search_by_keyword(q)
    return res


# app.add_url_rule('/hello/', view_func=hello)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=50007)
