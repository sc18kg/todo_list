
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class AddTask(FlaskForm):
    title = StringField("Task Title")
    description = StringField("What is the Task?")
    submit = SubmitField("Submit Task")