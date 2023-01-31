#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: trade.py
@time: 2023/1/28 16:45

"""
from app.view_models.book import BookViewModel


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
            time = good.create_date_time.strftime('%Y-%m-%d')
        else:
            time = '未知'
        return dict(
            user_name=good.user.nickname,  # 这里dict返回的字段要和渲染模版取的字段一致，否则渲染的模版取不到该字段
            time=time,
            id=good.id
        )


class MyTrades:
    def __init__(self, trades_of_mine, trade_count_list):
        self.trades = []

        self.__trades_of_mine = trades_of_mine
        self.__trade_count_list = trade_count_list

        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self.__trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0
        for trade_count in self.__trade_count_list:
            if trade.isbn == trade_count['isbn']:
                count = trade_count['count']
        r = {
            'count': count,
            'book': BookViewModel(trade.book),
            'id': trade.id
        }
        return r
