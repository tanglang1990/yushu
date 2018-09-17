from flask import jsonify
from flask import request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

from . import web


@web.route('/test')
def test1():
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('.................')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('.................')
    return ''


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
