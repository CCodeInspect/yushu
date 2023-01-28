#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: trade.py
@time: 2023/1/28 16:45

"""


class Trade:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self._parse_goods(goods)

    def _parse_goods(self, goods):
        self.total = len(goods)
        self.trades = [self._map_to_trade(good) for good in goods]

    def _map_to_trade(self, good):
        if good.create_date_time:
            time = good.create_date_time.strftime('%Y-%m-d%')
        else:
            time = '未知'
        return dict(
            username=good.user.nickname,
            create_time=time,
            trade_id=good.id
        )
