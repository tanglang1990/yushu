from flask import Blueprint

# 实例化蓝图对象
web = Blueprint('web', __name__)

# 导入我们需要使用的视图函数模块(如果有的话)
from app.web import user
