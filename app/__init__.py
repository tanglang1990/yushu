from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    # print(__name__) # 打印显示app
    # 为什么找到了app下的static这个目录就是因为__name__的缘故
    # 通过参数 static_folder 指定静态文件的目录, 如：static_folder='test/static'
    # 通过参数 static_url_path 指定静态文件的访问url前缀, 如: static_url_path='/statics'
    # 实际上蓝图的方法和Flask的方法基本相同，所以其实也可以通过蓝图实现类似效果
    # 通过参数 template_folder 指定模板文件的目录，默认是templates
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    registe_blueprint(app)
    db.init_app(app)
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
