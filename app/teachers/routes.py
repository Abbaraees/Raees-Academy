from flask import (
    render_template, redirect, url_for, g, request, flash,jsonify
)
from werkzeug.datastructures import ImmutableMultiDict

from app.auth.utils import require_role
from app.teachers import bp
from app.teachers.forms import AddCourseForm
from app.models import Course, db



@bp.route('/')
@require_role('teacher')
def index():
    return render_template('teachers/index.html')


@bp.route('/courses')
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
                    'description': course.description
                }
            }
            
        except:
            db.session.rollback()


    return jsonify({
        'status': 'failed',
        'message': 'Failed to add course'
    }), 400

