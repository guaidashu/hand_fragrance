"""
author songjie
"""
from tool.lib.function import get_date_time


class TradeInfo(object):
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        return dict(
            nickname=single.user.nickname,
            time=get_date_time(single.create_time, '%Y-%m-%d'),
            id=single.id
        )

    @staticmethod
    def map_to_trade(single):
        return dict(
            user=single.user,
            time=get_date_time(single.create_time, '%Y-%m-%d'),
            id=single.id
        )
