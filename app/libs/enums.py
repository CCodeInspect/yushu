#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: enums.py
@time: 2023/2/2 10:17

"""
from enum import Enum


class PendingStatus(Enum):
    waiting = 1
    success = 2
    reject = 3
    redraw = 4
