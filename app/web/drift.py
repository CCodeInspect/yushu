#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2023/1/7 17:43
# @Author  : paulinelee
# @Site    : https://github.com/llaichiyu/
# @File    : drift.py
# @Software: PyCharm
from app.web import web


@web.route('/drift/<int:gid>', methods=['GET', 'POST'])
def send_drift(gid):
    pass


@web.route('/pending')
def pending():
    pass


@web.route('/drift/<int:did>/reject')
def reject_drift(did):
    pass


@web.route('/drift/<int:did>/redraw')
def redraw_drift(did):
    pass


@web.route('/drift/<int:did>/mailed')
def mailed_drift(did):
    pass


def save_drift(drift_form, current_gift):
    pass
