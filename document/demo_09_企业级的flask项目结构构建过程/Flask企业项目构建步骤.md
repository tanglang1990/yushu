## Flask企业级项目构建

1. 新建入口文件 main.py 作为一个项目的入口模块

1. 新建python包app作为项目的主目录

1. 在app目录下新建web包，在在app/web/__init__.py中实例化蓝图
    ```python
    from flask import Blueprint
    
    # 实例化蓝图对象 
    web = Blueprint('web', __name__)
    ```

1. 在app/web新建网站的视图函数模块文件，如我们新建app/web/user.py,代码如下
    ```python
    from . import web
    
    
    @web.route('/hello')  # 使用蓝图注册路由
    def hello():
        # 视图函数
        return 'hello,world!'
    ```

1. 修改app/web/__init__.py, 导入我们需要使用的视图函数模块，代码如下
    ```python
    from flask import Blueprint
    
    # 实例化蓝图对象 
    web = Blueprint('web', __name__)
    
    # 导入我们需要使用的视图函数模块(如果有的话)
    from app.web import user
    ...
    ```

1. 在app包下新建普通配置文件setting.py和机密配置文件secure.py，可以在里面对flask核心对象进行设置。
    如我们修改 app/secure.py 如下
    ```python
    DEBUG = True
    ```

1. 在app/__init__中定义创建flask核心对象的函数、使用配置文件、实例和注册插件、注册蓝图等，代码如下
    ```python
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
    ```

1. 修改main.py，使用创建核心对象函数创建flask核心对象，并允许。
    ```python
    from app import create_app
    
    app = create_app()
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
    
    ```

1. 运行main.py,然后访问http://127.0.0.1:81/hello，响应hello,world!，项目构建完成。







