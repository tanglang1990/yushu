from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    registe_blueprint(app)
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
