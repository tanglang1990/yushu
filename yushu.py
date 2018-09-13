from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
