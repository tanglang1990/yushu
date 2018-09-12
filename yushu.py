from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello,ten!'


app.run(host='0.0.0.0', debug=True, port=81)
