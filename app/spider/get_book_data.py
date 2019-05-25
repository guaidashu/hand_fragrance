"""
author songjie
"""
from flask import current_app

from app.libs.helper import Helper


class GetBookData:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        """
        search book according to isbn
        :param isbn:
        :return:
        """
        url = cls.isbn_url.format(isbn)
        result = Helper.get_book_api_data(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        """
        search book according to keyword
        :param page:
        :param keyword:
        :return:
        """
        url = cls.keyword_url.format(keyword, current_app.config['RECENT_BOOK_PER_PAGE'], cls.calculate_start(page))
        result = Helper.get_book_api_data(url)
        return result

    @staticmethod
    def calculate_start(page):
        return current_app.config['RECENT_BOOK_PER_PAGE'] * page
