"""
author songjie
"""
from tool.lib.function import curl_data


class Helper(object):
    @staticmethod
    def is_isbn_or_key(word):
        """
        This function is used to judge the var is a isbn or a keyword
        As all we know, isbn is composed of 13 integer or 10 integer and some '-'
        :param word:
        :return:
        """
        # set a default value
        isbn_or_key = 'key'
        # if length of word is 13 and it's composed of 13 integer, then we can be sure it's a isbn
        if len(word) == 13 and word.isdigit():
            isbn_or_key = 'isbn'
        short_key = word.replace("-", "")
        # if there are some '-' and the length of short_key is 10, and also it's all composed of integer
        if '-' in word and len(short_key) == 10 and short_key.isdigit():
            isbn_or_key = 'isbn'
        return isbn_or_key

    @staticmethod
    def get_book_api_data(url, return_json=True):
        """
        This function is used to get book data and decide to data format which will return
        :param url:
        :param return_json:
        :return:
        """
        data, res = curl_data(url, return_response=True)
        if res.status_code != 200:
            return {} if return_json else ''
        else:
            return res.json() if return_json else res.text
