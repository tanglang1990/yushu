from flask import Flask

from app.models.book import db
from flask_login import LoginManager

login_manager = LoginManager()


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
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
