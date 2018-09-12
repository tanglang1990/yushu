from flask import Flask

from config import DEBUG

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'hello,ten!'


app.run(host='0.0.0.0', debug=DEBUG, port=81)
