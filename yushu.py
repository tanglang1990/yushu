import json

from flask import Flask, make_response, jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


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
    # restful api 难点在于url设计，怎样很好的代表资源，而不是技术上面如何返回
    return jsonify(result)
    # json
    # return json.dumps(result), 200, {'content-type': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
