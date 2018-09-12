from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    '''
        q:普通关键字, isbn
        page:页码
    '''
    # 判断是isbn还是关键字
    # isbn13 由13个0-9的数字组成
    # isbn10 由10个0-9的数字组成，可能含有'-'
    q = q.strip()  # 去除左右的空格
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
