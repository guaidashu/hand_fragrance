"""
author songjie
"""
from flask import request

from app.api import api
from app.forms.book import SearchForm, IsbnForm
from app.libs.helper import Helper
from app.libs.reply import Reply
from app.spider.get_book_data import GetBookData
from app.view_models.book import BookCollection, BookViewModel


@api.route("/book/search", methods=['POST', 'GET'])
def search():
    """
    q: 普通的关键字 或者 isbn
    page: 分页
    :return:
    """
    form = SearchForm(request.values)
    if not form.validate():
        return Reply.error(form.errors)

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


@api.route("/book/detail", methods=['POST'])
def detail():
    """
    单个书籍详情数据获取
    isbn: 书籍isbn，必传参数
    :return:
    """
    form = IsbnForm(request.values)
    if not form.validate():
        return Reply.error(form.errors)
    isbn = form.isbn.data
    get_book_data = GetBookData()
    get_book_data.search_by_isbn(isbn)
    book = BookViewModel(get_book_data.first)
    return Reply.success(book)
