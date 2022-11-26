from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class AddNewTeacherForm(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')


class ResetTeacherPasswordForm(FlaskForm):
    teacher_id = StringField('teacher_id', validators=[DataRequired()])

