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
        数据校验:
            q 至少一个字符
            page 正整数
        数据校验演变（从比较差到比较好）：
            1 在视图函数中写if else判断
            2 将if else判断封装成函数
            3 使用wtforms
    '''
    q = request.args['q']
    page = request.args['page']

    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
