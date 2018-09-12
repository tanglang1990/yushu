from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    # headers: content-type(text/html、text/plain、application/json)
    # status code: 200 404 301
    # body

    # Response

    headers = {
        'content-type': 'text/plain',
        'location': 'http://www.bing.com'
    }
    # response = make_response('<html></html>', 302)
    # response.headers = headers
    # return response

    return '<html></html>', 302, headers

    # return '<html></html>'


def hello_func():
    return 'hello,ten'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
