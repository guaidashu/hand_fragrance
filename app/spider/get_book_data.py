"""
author songjie
"""
from flask import current_app

from app.libs.helper import Helper


class GetBookData(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.books = []
        self.total = 0

    def search_by_isbn(self, isbn):
        """
        search book according to isbn
        :param isbn:
        :return:
        """
        url = self.isbn_url.format(isbn)
        result = Helper.get_book_api_data(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        """
        search book according to keyword
        :param page:
        :param keyword:
        :return:
        """
        url = self.keyword_url.format(keyword, current_app.config['SEARCH_BOOK_PER_PAGE'], self.calculate_start(page))
        result = Helper.get_book_api_data(url)
        self.__fill_collection(result)

    def __fill_single(self, data):
        """
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """
        :param data:
        :return:
        """
        self.total = data['total']
        self.books = data['books']

    @staticmethod
    def calculate_start(page):
        return current_app.config['RECENT_BOOK_PER_PAGE'] * page

    @property
    def first(self):
        return self.books[0] if self.total > 0 else None
