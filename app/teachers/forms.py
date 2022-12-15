from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField



class AddCourseForm(FlaskForm):
    name = StringField('Course Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])


class AddLessonForm(FlaskForm):
    name = StringField('Lesson Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])
    

class EmptyForm(FlaskForm):
    submit = SubmitField()
