from flask import render_template, url_for, redirect


from app.auth.utils import require_role
from app.students import bp


@bp.route('/dashboard')
@require_role('student')
def dashboard():
    return render_template('students/dashboard.html')