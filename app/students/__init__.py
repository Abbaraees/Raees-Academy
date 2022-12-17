from flask import Blueprint


bp = Blueprint('students', __name__, url_prefix='/')


from app.students import routes