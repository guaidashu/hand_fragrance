"""
author songjie
"""
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
    def search_by_keyword(cls, keyword, count=15, start=0):
        """
        search book according to keyword
        :param start:
        :param count:
        :param keyword:
        :return:
        """
        url = cls.keyword_url.format(keyword, count, start)
        result = Helper.get_book_api_data(url)
        return result
