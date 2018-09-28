from flask import Flask
from flask_cache import Cache

from app.models.book import db
from flask_login import LoginManager

login_manager = LoginManager()
cache = Cache()

'''
引入Flask-Cache，并使用如果抛出下述异常
Traceback (most recent call last):
  File "D:/yushu/yushu.py", line 3, in <module>
    from flask.ext.cache import make_template_fragment_key
ModuleNotFoundError: No module named 'flask.ext'

可以找到 site-packages\flask_cache\jinja2ext.py把 
from flask.ext.cache import make_template_fragment_key
改成 下面的代码即可
from flask_cache import make_template_fragment_key
'''


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    registe_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    db.init_app(app)
    with app.app_context():
        db.create_all()

    cache.init_app(app)
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
