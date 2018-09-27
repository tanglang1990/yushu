from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user

from app.forms.auth import RegisterForm, LoginForm
from app.models.base import db
from app.models.user import User
from . import web


@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        # user.password = generate_password_hash(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        # if user and user.password == generate_password_hash(form.password.data)
        if user and user.check_password(form.password.data):
            # 在此处需要写入票据(cookie)信息
            # 整个管理我们可以依赖于已有的插件flask-login
            # 官方文档 http://www.pythondoc.com/flask-login/
            # login_user中可以通过 关键字参数 remember=True 设定记住密码，
            # 配置 REMEMBER_COOKIE_DURATION 可以设置时长（默认365天）
            # 此外 login_user还可以通过 关键字参数 duration 设定指定时长
            # import datetime
            # duration = datetime.timedelta(seconds=30) # 30秒
            # duration = duration
            # login_user(user, remember=True, duration=duration)
            login_user(user, remember=True)
        else:
            flash('用户名或密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass


@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass


@web.route('/logout')
def logout():
    pass
