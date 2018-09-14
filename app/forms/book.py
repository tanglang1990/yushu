from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=64)])
    page = IntegerField(validators=[NumberRange(1)], default=1)
