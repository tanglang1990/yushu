from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    '''
        基于wtforms，我们应该思考怎么样去写我们的代码，这是我们可以努力的方向
    '''

    # validators列表中对象定义的时候都可以传入message，实现对错误消息的定制
    # validators列表中中传入的为对象，不是类，记得加上()
    # q此处如果不要求最大的长度可以去掉Length，只传入DataRequired即可
    q = StringField(validators=[DataRequired(), Length(min=1, max=64)])
    page = IntegerField(validators=[NumberRange(1)], default=1)
