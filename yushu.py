from flask import Flask

app = Flask(__name__)
print(f"id为{id(app)}的app实例化")

app.config.from_object('config')

# 同一个模块在一次执行里只会导入一次
from app.web import book

if __name__ == '__main__':
    print(f"id为{id(app)}的app启动")
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
