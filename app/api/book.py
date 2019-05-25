"""
author songjie
"""
from flask import request

from app.api import api
from app.forms.book import SearchForm
from app.libs.helper import Helper
from app.libs.reply import Reply
from app.spider.get_book_data import GetBookData


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
    if isbn_or_key == 'isbn':
        result = GetBookData.search_by_isbn(q)
    else:
        result = GetBookData.search_by_keyword(q)
    return Reply.success(result)
