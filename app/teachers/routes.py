from app.auth.utils import require_role
from app.teachers import bp



@bp.route('/')
@require_role('teacher')
def index():
    return '<h1>Welcome Teacher</h1>'
