from flask import render_template, redirect, url_for, flash, g, session, abort

from app.auth import bp
from app.auth.forms import LoginForm, RegisterForm
from app.models import Admin, Teacher, Student, db


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    role = session.get('role')
    if user_id:
        roles = {
            'admin': Admin,
            'teacher': Teacher,
            'student': Student
        }

        g.user = roles[role].query.get(user_id)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Student.query.filter_by(username=username).first()

        if user is None or not user.check_password_hash(password):
            flash('Invalid username or password')
        else:
            session.clear()
            session['role'] = 'student'
            session['user_id'] = user.id

            return redirect(url_for('students.dashboard'))

    return render_template('auth/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("Valid")
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data

        user = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )
        user.generate_password_hash(password)

        try:
            db.session.add(user)
            db.session.commit()
            flash("Account created successfully")

            return redirect(url_for('auth.login'))
        except:
            db.session.rollback()
            abort(422)
    return render_template('auth/register.html', form=form)


@bp.route('/teachers/login', methods=['GET', 'POST'])
def teachers_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Teacher.query.filter_by(username=username).first()

        if user is None or not user.check_password_hash(password):
            flash('Invalid username or password')
        else:
            session.clear()
            session['role'] = 'teacher'
            session['user_id'] = user.id

            return redirect(url_for('teachers.index'))

    return render_template('auth/login.html', form=form)


@bp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Admin.query.filter_by(username=username).first()

        if user is None or not user.check_password_hash(password):
            flash('Invalid username or password')
        else:
            session.clear()
            session['role'] = 'admin'
            session['user_id'] = user.id

            return redirect(url_for('admin.index'))

    return render_template('auth/login.html', form=form)
