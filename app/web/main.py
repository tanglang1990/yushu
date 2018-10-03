from flask import render_template
from flask_login import login_required, current_user

from app.models.gift import Gift
from . import web


@web.route('/')
def index():
    # 此处由于书本信息本身会去调用豆瓣的api，加上频繁的访问
    # 可以考虑将将api的结果缓存起来，可以使用 Flask-Cache
    # 官方文档: http://www.pythondoc.com/flask-cache/index.html
    recent_gifts = Gift.recent()
    books = [gift.book for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)
