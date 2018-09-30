from flask_mail import Message

from app import mail


def send_mail():
    msg = Message('测试邮件', sender='send@qq.com', body='Test',
                  recipients=['recive@qq.com'])
    mail.send(msg)
