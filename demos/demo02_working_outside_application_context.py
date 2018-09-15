from flask import Flask, current_app, request

app = Flask(__name__)

# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 我们要取得对象，应该从上下文中去取
# 离线应用 单元测试

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = a.config['DEBUG']
# ctx.pop()


# 上下文管理器(不懂的同学要回顾基础中上下文管理器的内容)
with app.app_context():
    a = current_app
    d = a.config['DEBUG']
