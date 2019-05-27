"""
author songjie
"""
from flask import request

from app.api import api
from app.forms.book import SearchForm
from app.libs.helper import Helper
from app.libs.reply import Reply
from app.spider.get_book_data import GetBookData
from app.view_models.book import BookCollection


@api.route("/book/search")
def search():
    """
    q: 普通的关键字 或者 isbn
    page: 分页
    :return:
    """
    form = SearchForm(request.args)
    if not form.validate():
        return Reply.error("参数错误")

    q = form.q.data.strip()
    page = form.page.data
    isbn_or_key = Helper.is_isbn_or_key(q)
    book_collection = BookCollection()
    get_book_data = GetBookData()

    if isbn_or_key == 'isbn':
        get_book_data.search_by_isbn(q)
    else:
        get_book_data.search_by_keyword(q, page)

    book_collection.fill(get_book_data, q)
    return Reply.success(book_collection)
