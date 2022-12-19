from flask import render_template, url_for, redirect


from app.auth.utils import require_role
from app.students import bp
from app.models import Course


@bp.route('/dashboard')
@require_role('student')
def dashboard():
    courses = Course.query.filter_by(published=True)
    return render_template('students/dashboard.html', courses=courses)


@bp.route('/learn/course/<int:id>')
@require_role('student')
def view_course(id):
    course = Course.query.filter_by(id=id, published=True).first_or_404()

    return render_template('students/view_course.html', course=course, enumerate=enumerate)

