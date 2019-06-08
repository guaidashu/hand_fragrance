"""
author songjie
"""

# -*- coding: utf-8 -*-

from enum import Enum


class PendingStatus(Enum):
    """交易状态"""
    waiting = 1
    success = 2
    reject = 3
    redraw = 4

    # gifter_redraw = 5

    @classmethod
    def pending_str(cls, status, key):
        key_map = {
            cls.waiting: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.reject: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.redraw: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            cls.success: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }
        return key_map[status][key]

    @classmethod
    def pending_status(cls, status):
        key_map = {
            cls.waiting: {
                'status': 1,
                'value': '等待发货'
            },
            cls.reject: {
                'status': 3,
                'value': '撤销'
            },
            cls.redraw: {
                'status': 4,
                'value': '对方已撤销'
            },
            cls.success: {
                'status': 2,
                'value': '你已邮寄，交易完成'
            }
        }
        return key_map[status]


class GiftStatus(Enum):
    waiting = 0
    success = 1
    redraw = 2
