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


class AddStudentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add')


class UpdateStudentForm(AddStudentForm):
    id = StringField("Id", validators=[DataRequired()])
    password = PasswordField('Password')

    def __init__(self, *args, **kwargs):
        super(UpdateStudentForm, self).__init__(*args, **kwargs)


class DeleteUserForm(FlaskForm):
    id = StringField("id", validators=[DataRequired()])

    