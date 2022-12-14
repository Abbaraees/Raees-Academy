from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class AddCourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])


class AddLessonForm(FlaskForm):
    name = StringField('Lesson Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    