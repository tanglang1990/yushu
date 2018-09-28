from flask import render_template, flash
from flask import request
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from app.view_models.trade import TradeInfo

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
    has_in_gifts = False
    has_in_wishes = False
    # 联系到 User中 can_save_to_list 方法讲过的，及我们的产品设计，一个人不能同时既赠送此书又希望得到此书
    # 书本对应用户一共会存在三种关系：
    # 1、既不在赠送清单也不在心愿清单中 2、在赠送清单但不在心愿清单中 3、在心愿清单但不在赠送清单中

    # 获取书籍数据
    data = YuShuBook.search_by_isbn(isbn)
    book = BookViewModel.handle_book_data(data)

    # 判断用户是否登录
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                                launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()
    wishes = TradeInfo(trade_wishes)
    gifts = TradeInfo(trade_gifts)

    return render_template(
        'book_detail.html', book=book, wishes=wishes, gifts=gifts,
        has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)


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
