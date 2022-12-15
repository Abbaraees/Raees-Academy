from flask import (
    render_template, redirect, url_for, g, request, flash,jsonify, abort
)
from werkzeug.datastructures import ImmutableMultiDict

from app.auth.utils import require_role
from app.teachers import bp
from app.teachers.forms import AddCourseForm, AddLessonForm, EmptyForm
from app.models import Course, db, Lesson



@bp.route('/')
@require_role('teacher')
def index():
    return render_template('teachers/index.html')


@bp.route('/courses/')
@require_role('teacher')
def courses():
    courses = g.user.courses
    form=AddCourseForm()

    return render_template('teachers/courses.html', courses=courses, form=form)


@bp.route('/add_course', methods=['POST'])
@require_role('teacher')
def add_course():
    formdata = ImmutableMultiDict(request.get_json())
    form = AddCourseForm(formdata)
    if form.validate_on_submit():
        course = Course(
            name=form.name.data,
            description=form.description.data
        )
        course.teacher = g.user
        try:
            db.session.add(course)
            db.session.commit()

            return {
                'status': 'success',
                'message': 'course added successfully',
                'course': {
                    'name': course.name,
                    'description': course.description,
                    'id': course.id
                }
            }
            
        except:
            db.session.rollback()


    return jsonify({
        'status': 'failed',
        'message': 'Failed to add course'
    }), 400


@bp.route('/courses/<int:id>')
@require_role('teacher')
def view_course(id):
    course = Course.query.filter_by(id=id).first_or_404()
    update_form = AddCourseForm()
    delete_form = EmptyForm()
    update_form.name.data = course.name
    update_form.description.data = course.description

    return render_template(
        'teachers/view_course.html',
        course=course, update_form=update_form,
        delete_form=delete_form
    )


@bp.route('/courses/<int:id>/update', methods=['POST'])
@require_role('teacher')
def update_course(id):
    course = Course.query.filter_by(id=id).first_or_404()
    form = AddCourseForm(request.form)
    if form.validate_on_submit():
        course.name = form.name.data
        course.description = form.description.data
        db.session.commit()
        flash("Course updated successfully")
        return redirect(url_for('teachers.view_course', id=id))

    flash("Failed to update course")
    return redirect(url_for('teachers.view_course', id=id))


@bp.route('/courses/<int:id>/delete', methods=['POST'])
@require_role('teacher')
def delete_course(id):
    course = Course.query.filter_by(id=id).first_or_404()
    form = EmptyForm(request.form)

    if form.validate_on_submit():
        db.session.delete(course)
        db.session.commit()
        flash("Course Deleted Successfully!")
        return redirect(url_for('teachers.courses'))
    
    flash("Failed to delete course!")
    return redirect(url_for('teachers.view_course', id=course.id))


@bp.route('/courses/<int:id>/add_lesson', methods=['GET', 'POST'])
@require_role('teacher')
def add_lesson(id):
    form = AddLessonForm()
    if form.validate_on_submit():
        course = Course.query.filter_by(id=id).first_or_404()
        lesson = Lesson(
            name=form.name.data,
            description=form.description.data,
            content=form.content.data
        )
        try:
            course.lessons.append(lesson)
            db.session.commit()
            flash("Lesson added successfully!")
            return redirect(url_for('teachers.view_course', id=id))
            
        except:
            db.session.rollback()
            flash("Failed to add Lesson.\nPlease try again")
            return redirect(url_for('teachers.view_course', id=id))


    return render_template('teachers/add_lesson.html', form=form)


@bp.route('/courses/<int:course_id>/lessons/<int:lesson_id>')
@require_role('teacher')
def view_lesson(course_id, lesson_id):
    course = Course.query.filter_by(id=course_id).first_or_404()
    lesson = course.lessons.filter_by(id=lesson_id).first_or_404()

    return render_template('teachers/view_lesson.html', lesson=lesson)
