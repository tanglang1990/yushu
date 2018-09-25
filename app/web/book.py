from flask import jsonify, render_template, flash
from flask import request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel

from . import web


@web.route('/book/search')
def search():
    form = SearchForm(request.args)
    result = {}
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            data = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(data, q)
        else:
            data = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(data, q)
        # return jsonify(result)
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字')
    return render_template('search_result.html', books=result)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    data = YuShuBook.search_by_isbn(isbn)
    book = BookViewModel.handle_book_data(data)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


@web.route('/test')
def test():
    r = {'name': 'Ten', 'age': 18}
    # 模板
    return render_template('test.html', data=r)
    # return jsonify(r)


@web.route('/test1')
def test1():
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('.................')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('.................')
    return ''
