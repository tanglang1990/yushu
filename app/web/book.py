from flask import jsonify
from flask import request

from helper import is_isbn_or_key
from yushu_book import YuShuBook

from . import web


@web.route('/book/search')
def search():
    '''
        q:普通关键字, isbn
        page:页码
        /book/search?q=9787806737842&page=1
    '''
    # Request
    # HTTP请求信息：请求方式、参数、remote ip等等，可以看成对WSGI中environ的封装
    q = request.args['q']
    page = request.args['page']
    # d = request.args.to_dict()
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
