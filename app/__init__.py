from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    registe_blueprint(app)

    '''
        db.create_all()
        此处会抛出 No application found的异常
        这是困扰大多数flask新手的问题
        实际上flask会去一个叫栈的地方取出flask的核心对象
        欲知详情，请听下会讲解
    '''
    db.init_app(app)
    db.create_all()
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
