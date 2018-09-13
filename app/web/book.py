from flask import jsonify

from yushu import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook

print(f"id为{id(app)}的app注册路由")
@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
        q:普通关键字, isbn
        page:页码
    '''
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
