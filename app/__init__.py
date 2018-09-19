from flask import Flask

from app.models.book import db


def create_app():
    app = Flask(__name__)
    # print(__name__) # 打印显示app
    # 为什么找到了app下的static这个目录就是因为__name__的缘故
    # 通过参数 static_folder 指定静态文件的目录, 如：static_folder='test/static'
    # 通过参数 static_url_path 关键字参数指定静态文件的访问url前缀, 如: static_url_path='/statics'
    # 实际上蓝图的方法和Flask的方法基本相同，所以其实也可以通过蓝图实现类似效果
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
    # db.create_all(app=app)
    with app.app_context():
        db.create_all()
    return app


def registe_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
