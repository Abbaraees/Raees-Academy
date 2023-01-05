import sys

from flask import render_template, url_for, redirect, g, flash, request, abort

from app.models import db, Lesson

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

    # check if the student have completed all the lessons in the course
    completed_course = course.lessons.filter(
        Lesson.id.in_([x.id for x in g.user.lessons_completed])
    ).count() == course.lessons.count()

    return render_template(
        'students/view_course.html',
        course=course,
        enumerate=enumerate,
        form=EmptyForm(),
        completed_course=completed_course
    )


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

@bp.route('/learn/course/<int:id>/next_lesson')
def next_lesson(id):
    course = Course.query.filter_by(id=id).first_or_404()
    lesson = course.next_lesson([x.id for x in g.user.lessons_completed])

    return redirect(url_for('students.view_lesson', lesson_id=lesson.id, course_id=course.id))


@bp.route('/learn/course/<int:course_id>/lesson/<int:lesson_id>')
@require_role('student')
def view_lesson(course_id, lesson_id):
    course = Course.query.filter_by(id=course_id).first_or_404()
    lesson = course.lessons.filter_by(id=lesson_id).first_or_404()

    if course not in g.user.courses:
        abort(403)

    return render_template('students/view_lesson.html', lesson=lesson)

@bp.route('/learn/lesson/<int:id>/complete', methods=['POST'])
def complete(id):
    lesson = Lesson.query.filter_by(id=id).first_or_404()
    try:
        if lesson not in g.user.lessons_completed:
            g.user.lessons_completed.append(lesson)
            
        db.session.commit()
        return {'success': True}
    except:
        db.session.rollback()

    return {'success': False}