from flask import Flask, render_template, jsonify

app = Flask(__name__)

students = [
    {'id': 1, 'username': 'zs', 'age': 18},
    {'id': 2, 'username': 'ls', 'age': 18},
    {'id': 3, 'username': 'ww', 'age': 18}
]


@app.route('/')
def index():
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>首页</title>
        </head>
        <body>
          <h1>单页与网站的区别</h1>
          <a href="/static/index.html">单页</a><br/>
          <a href="/template/index">网站</a>
        </body>
        </html>
    """
    return html


@app.route('/student/list', methods=['POST'])
def student_list():
    return jsonify({'ok': True, 'students': students})
    # return jsonify({'ok': False, 'msg': '你的请求url有问题'})


@app.route('/template/index')
def template_index():
    return render_template('template_index.html', objs=students)


if __name__ == '__main__':
    app.run(debug=True)
