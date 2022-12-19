import sys

from flask import render_template, url_for, redirect, g, flash, request

from app.models import db


from app.auth.utils import require_role
from app.students import bp
from app.models import Course
from app.teachers.forms import EmptyForm


@bp.route('/dashboard')
@require_role('student')
def dashboard():
    courses = Course.query.filter_by(published=True)
    return render_template('students/dashboard.html', courses=courses)


@bp.route('/learn/course/<int:id>')
@require_role('student')
def view_course(id):
    course = Course.query.filter_by(id=id, published=True).first_or_404()

    return render_template('students/view_course.html', course=course, enumerate=enumerate, form=EmptyForm())


@bp.route('/learn/course/<int:id>/enroll', methods=['POST'])
@require_role('student')
def enroll(id):
    course = Course.query.filter_by(id=id, published=True).first_or_404()
    form = EmptyForm(request.form)
    if form.validate_on_submit():
        if course not in g.user.courses:
            g.user.courses.append(course)
            try:
                db.session.commit()
                flash("Congratulations, you have successfully enrolled in the course!")
                return redirect(url_for('students.view_course', id=id))
            except:
                flash("Unfortunately, your enrollment into the course failed, please try again later!")
                return redirect(url_for('students.view_course', id=id))

        flash("You are already enrolled in to the course")
        return redirect(url_for('students.view_course', id=id))

    flash("Something went wrong, please try again later!")
    return redirect(url_for('students.view_course', id=id))


@bp.route('/learn/course/<int:id>/unenroll', methods=['POST'])
@require_role('student')
def unenroll(id):
    course = Course.query.filter_by(id=id, published=True).first_or_404()
    form = EmptyForm(request.form)
    if form.validate_on_submit():
        if course in g.user.courses:
            try:
                g.user.courses.remove(course)
                db.session.commit()
                flash("You have successfully unenrolled from the course")
                return redirect(url_for('students.view_course', id=id))
            except:
                db.session.rollback()
                flash("Failed to unenroll from the course, please try agin later!")
                return redirect(url_for('students.view_course', id=id))

        flash("Sorry! You are not enrolled in the course")
        return redirect(url_for('students.view_course', id=id))

    flash("Something went wrong, please try again later!")
    return redirect(url_for('students.view_course', id=id))
