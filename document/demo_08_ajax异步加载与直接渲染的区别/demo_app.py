from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

STUDENTS = [
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
          <h1>ajax异步加载与直接渲染的区别</h1>
          <a href="/static/index.html">单页</a><br/>
          <a href="/template/index">网站</a>
        </body>
        </html>
    """
    return html


@app.route('/student/list', methods=['POST'])
def student_list():
    # request.form
    try:
        keyword = request.form['keyword']
        students = student_search(keyword)
        return jsonify({'ok': True, 'students': students})
    except KeyError:
        return jsonify({'ok': False, 'msg': '你传入的请求参数有问题'})


@app.route('/template/index')
def template_index():
    try:
        keyword = request.args['keyword']
    except KeyError:
        keyword = ''
    students = student_search(keyword)
    return render_template('template_index.html', students=students)


def student_search(keyword):
    keyword = keyword.strip()
    student_filter = filter(lambda x: keyword in x['username'], STUDENTS)
    return list(student_filter)


if __name__ == '__main__':
    app.run(debug=True)
