from flask import Flask


# 创建核心对象
def create_app():
    app = Flask(__name__)
    # 使用配置文件对核心对象进行配置
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    registe_blueprint(app)
    return app


# 注册蓝图
def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)