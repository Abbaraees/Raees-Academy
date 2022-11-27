from flask import (
    g, render_template, flash, redirect, url_for, abort, request
)

from app.models import Admin, Student, Teacher, db
from app.admin import bp
from app.admin.forms import (
    AddNewTeacherForm, ResetTeacherPasswordForm, AddStudentForm, UpdateStudentForm,
    DeleteUserForm
)
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
    reset_password_form = ResetTeacherPasswordForm()
    teacher = Teacher.query.filter_by(id=id).first_or_404()
    return render_template(
        'admin/view_teacher.html',
        teacher=teacher,
        reset_password_form=reset_password_form
    )

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


@bp.route('/teachers/update', methods=['POST'])
@require_role('admin')
def update_teacher():
    json_data = request.get_json()
    teacher = Teacher.query.filter_by(id=json_data.get('id')).first_or_404()
    print(json_data)
    teacher.username = json_data.get('username')
    teacher.email = json_data.get('email')

    try:
        db.session.commit()
        return redirect(url_for('admin.view_teacher', id=teacher.id))
    except:
        db.session.rollback()
        abort(422)


@bp.route('/teachers/reset-password', methods=['POST'])
@require_role('admin')
def reset_teacher_password():
    form = ResetTeacherPasswordForm()
    if form.validate_on_submit():
        teacher = Teacher.query.filter_by(id=form.teacher_id.data).first_or_404()
        teacher.generate_password_hash('teacher123')
        try:
            db.session.commit()
            flash("Password changed successfully")
            return redirect(url_for('admin.view_teacher', id=teacher.id))
        except:
            db.session.rollback()
            abort(422)

        
    flash("Error!, failed to reset password")
    return redirect(url_for('admin.view_teacher', id=teacher.id))


@bp.route('/students')
@require_role('admin')
def students():
    students = Student.query.all()
    
    return render_template(
        'admin/students.html',
        students=students,
        add_student_form=AddStudentForm()
    )


@bp.route('/students/<int:id>')
@require_role('admin')
def view_student(id):
    student = Student.query.filter_by(id=id).first_or_404()

    return render_template(
        'admin/view_student.html',
        student=student,
        len=len,
        update_form=UpdateStudentForm(),
        delete_user_form=DeleteUserForm()
    )


@bp.route('/students', methods=['POST'])
@require_role('admin')
def add_student():
    form = AddStudentForm(request.form)
    if form.validate_on_submit():
        student = Student(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data
        )
        student.generate_password_hash(form.password.data)

        try:
            db.session.add(student)
            db.session.commit()
            flash('Student added successfully')
            return redirect(url_for('admin.students'))
        except:
            db.session.rollback()
            flash("Failed to add Student")

    return render_template(
        'admin/students.html', 
        students=Student.query.all(),
        add_student_form=form
    )


@bp.route('/students/update', methods=['POST'])
@require_role('admin')
def update_student():
    form = UpdateStudentForm(request.form)
    if form.validate_on_submit():
        student = Student.query.filter_by(id=form.id.data).first_or_404()
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.email = form.email.data
        student.username = form.username.data

        try:
            db.session.commit()
            flash('Student info updated successfully!')
            return redirect(url_for('admin.view_student', id=student.id))
        except:
            db.session.rollback()
            abort(422)

    flash("Failed to update student")
    return redirect(url_for('admin.view_student', id=form.id.data))


@bp.route('/students/delete', methods=['POST'])
@require_role('admin')
def delete_student():
    form = DeleteUserForm(request.form)
    if form.validate_on_submit():
        student = Student.query.filter_by(id=form.id.data).first_or_404()
        try:
            db.session.delete(student)
            db.session.commit()
            flash("Student Deleted Successfully")
            return redirect(url_for("admin.students"))
        except:
            db.session.rollback()
            abort(422)
    
    flash("Failed to Delete Student")
    return redirect(url_for('admin.view_student', id=form.id.data))
