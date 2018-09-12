from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'hello,ten!'


if __name__ == '__main__':
    # 生产环境是nginx+uwsgi，并不需要执行下段代码
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
