from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    '''
        基于wtforms，我们应该思考怎么样去写我们的代码，这是我们可以努力的方向
    '''

    # validators列表中对象定义的时候都可以传入message，实现对错误消息的定制
    # validators列表中中传入的为对象，不是类，记得加上()
    # q此处如果不要求最大的长度可以去掉Length，只传入DataRequired即可
    q = StringField(validators=[DataRequired(), Length(min=1, max=64)])
    page = IntegerField(validators=[NumberRange(1)], default=1)


class DriftForm(Form):
    recipient_name = StringField(
        validators=[
            DataRequired(),
            Length(min=2, max=20, message='收件人姓名长度必须在2到20个字符之间')])

    mobile = StringField(
        validators=[DataRequired(), Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])

    message = StringField()

    address = StringField(
        validators=[
            DataRequired(),
            Length(min=10, max=70, message='地址还不到10个字吗？尽量写详细一些吧')])
