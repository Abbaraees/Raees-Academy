from flask import (
    g, render_template, flash, redirect, url_for, abort, request
)

from app.models import Admin, Student, Teacher, db
from app.admin import bp
from app.admin.forms import AddNewTeacherForm
from app.auth.utils import require_role


@bp.route('/')
@require_role('admin')
def index():
    return render_template('admin/index.html')

@bp.route('/teachers')
@require_role('admin')
def teachers():
    form = AddNewTeacherForm()
    teachers = Teacher.query.all()
    return render_template('admin/teachers.html', teachers=teachers, form=form)


@bp.route('/teachers/<int:id>')
@require_role('admin')
def view_teacher(id):
    teacher = Teacher.query.filter_by(id=id).first_or_404()
    return render_template('admin/view_teacher.html', teacher=teacher)

@bp.route('/teachers', methods=['POST'])
@require_role('admin')
def add_teacher():
    form = AddNewTeacherForm(request.form)
    if form.validate_on_submit():
        new_teacher = Teacher(
            username=form.username.data,
            email=form.email.data
        )
        new_teacher.generate_password_hash(form.password.data)

        try:
            db.session.add(new_teacher)
            db.session.commit()
            flash("New Teacher Added")
            return redirect(url_for('admin.teachers'))
        except:
            db.session.rollback()
            abort(404)

    abort(404)


@bp.route('/teachers/delete', methods=['POST'])
@require_role('admin')
def delete_teacher():
    json_data = request.get_json()
    teacher_id = json_data.get('id')    

    teacher = Teacher.query.filter_by(id=teacher_id).first_or_404()

    try:
        db.session.delete(teacher)
        db.session.commit()

        return redirect(url_for('admin.teachers'))
    except:
        db.session.rollback()
        abort(422)


@bp.route('/test')
def test():
    return f"<h1>Admin Test Page {g.get('user')}</h1>"