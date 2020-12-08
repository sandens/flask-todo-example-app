from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], render_kw={"placeholder": "add something..."})