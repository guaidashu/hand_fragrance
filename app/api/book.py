"""
author songjie
"""
from app.api import api
from app.libs.helper import Helper
from app.spider.get_book_data import GetBookData


@api.route("/book/search/<q>/<page>")
def search(q, page):
    """
    q: 普通的关键字 或者 isbn
    page: 分页
    :return:
    """
    isbn_or_key = Helper.is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = GetBookData.search_by_isbn(q)
    else:
        result = GetBookData.search_by_keyword(q)
    return "search book"
