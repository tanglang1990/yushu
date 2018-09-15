from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    registe_blueprint(app)

    '''
        如果只是db.create_all()
        此处会抛出 No application found的异常
        这是困扰大多数flask新手的问题
        实际上flask会去一个叫栈的地方取出flask的核心对象
        接下来就是flask中最难理解的部分了，希望大家要有信心
    '''
    db.init_app(app)
    db.create_all(app=app)
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
