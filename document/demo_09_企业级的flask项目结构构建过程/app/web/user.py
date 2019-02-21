from . import web


@web.route('/hello')  # 使用蓝图注册路由
def hello():
    # 视图函数
    return 'hello,world!'
