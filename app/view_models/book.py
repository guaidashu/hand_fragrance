"""
author songjie
"""


class BookViewModel(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.pubdate = book['pubdate']
        self.author = book['author']
        self.price = book['price']
        self.binding = book['binding']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.isbn = book['isbn']


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        """
        构造最终数据
        :param books:
        :param keyword:
        :return:
        """
        self.total = books.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in books.books]


class _BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        """
        根据isbn处理，只可能会有0个或者1个结果
        :param data:
        :param keyword:
        :return:
        """
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = 1
            result['books'] = [cls.__cut_book_data(data)]

    @classmethod
    def package_collection(cls, data, keyword):
        """
        根据关键词查询，由于查询到的会是多个书籍数据，所以这里单独循环处理
        :param data:
        :param keyword:
        :return:
        """
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = data['total']
            result['books'] = [cls.__cut_book_data(book) for book in data['books']]

    @classmethod
    def __cut_book_data(cls, data):
        """
        书籍数据裁剪(单个)
        :param data:
        :return:
        """
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            # 'author': '、'.join(data['author']),
            'author': data['author'],
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
