#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: pauline.lee
@contact: Pauline.Y.Li@outlook.com
@site: https://github.com/llaichiyu/
@file: gift.py
@time: 2023/1/31 11:48

"""
from app.view_models.book import BookViewModel


class MyGift:
    def __init__(self, id, book, wishes_count):
        self.id = id
        self.book = book
        self.wishes_count = wishes_count


class MyGifts:
    def __init__(self, my_gift_list, wishes_list):
        self.gifts = []

        self.__my_gift_list = my_gift_list
        self.__wishes_list = wishes_list

        self.gifts = self.__parse()

    def __parse(self):
        templates = []
        for gift in self.__my_gift_list:
            my_gifts = self.__matching(gift)
            templates.append(my_gifts)
        return templates

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wishes_list:
            if gift.isbn == wish_count['isbn']:
                count = wish_count['count']
        my_gifts = MyGift(id=gift.id, book=BookViewModel(gift.book), wishes_count=count)
        return my_gifts
