"""
author songjie
"""
from flask import request
from flask_login import current_user, login_required

from app.api import api
from app.forms.book import SearchForm, IsbnForm
from app.libs.helper import Helper
from app.libs.reply import Reply
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.get_book_data import GetBookData
from app.view_models.book import BookCollection, BookViewModel
from app.view_models.trade import TradeInfo


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
    is_in_gift = False
    is_in_wish = False

    # 如果用户已登录，则查询 此书籍是否已经被添加到赠送清单或者心愿清单
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            is_in_gift = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            is_in_wish = True

    # 查询所有此书的赠送信息 和 心愿信息(用作显示)
    gift = Gift.query.filter_by(isbn=isbn, launched=False).all()
    wish = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gift = TradeInfo(gift)
    trade_wish = TradeInfo(wish)

    book.gift = trade_gift
    book.wish = trade_wish
    book.is_in_gift = is_in_gift
    book.is_in_wish = is_in_wish
    return Reply.success(book)
