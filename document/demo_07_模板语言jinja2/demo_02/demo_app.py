from flask import Flask, render_template, flash

from demo_class import Teacher

app = Flask(__name__)
app.secret_key = '\xefa\xc6\xf9\xa4-\xf8X\xd3\xb4c4\xefr\x1b\xbd\x9b\xc9\xa1ua%Nn'
# 可以通过以下方法得到一个secret_key
# import os
# s =os.urandom(24)
# print(s)


@app.route('/demo01')
def demo01():
    result = {'content': 'Hello,Ten'}
    title = "变量取值"
    return render_template('demo01.html', result=result, title=title)


@app.route('/demo02')
def demo02():
    t_list = ['Gavin', 'Anny', 'Ben', 'Ten']

    t_list2 = [
        {'name': 'gavin', 'students': ['stu1', 'stu2', 'stu3']},
        {'name': 'ben', 'students': [4, 5, 6]}
    ]

    return render_template('demo02.html', teachers1=t_list, teachers2=t_list2)


@app.route('/demo03')
def demo03():
    user = {'name': 'Ten', 'age': 18}
    return render_template('demo03.html', user=user)


@app.route('/demo04')
def demo04():
    ben = Teacher('ben', ['stu4', 'stu5', 'stu6'])
    return render_template('demo04.html', teacher=ben)


@app.route('/demo05')
def demo05():
    return render_template('demo05.html')


@app.route('/demo06')
def demo06():
    user = {'name': 'ten', 'info': '<h3>Ten老师你好帅</h3>'}
    return render_template('demo06.html', user=user)


@app.route('/demo07')
def demo07():
    return render_template('demo07.html')


@app.route('/demo08')
def demo08():
    # 消息闪现  Message flash
    # 详见：http://docs.jinkan.org/docs/flask/patterns/flashing.html
    flash('Hello,Ten', category='info')
    flash('input is error', category='error')
    return render_template('demo08.html')


if __name__ == '__main__':
    app.run(debug=True)
    # 开启调试模式之后，在修改完模板页面之后能立即生效
    # 如果不开启调试模式，模板页面会缓存，而可能不会从文件中直接读取
