from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    # 除了函数视图外还有基于类的视图（即插视图）
    return 'hello,ten!'


# app.add_url_rule('/hello', view_func=hello)
app.run(debug=True)
