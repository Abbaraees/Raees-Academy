import os
from flask import Flask, url_for, send_from_directory, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor, upload_fail, upload_success

from config import Config


# extensions
db = SQLAlchemy()
migrate = Migrate()
ckeditor = CKEditor()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_object(Config)

    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)


    #register blueprints
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.teachers import bp as teachers_bp
    app.register_blueprint(teachers_bp)

    from app.students import bp as students_bp
    app.register_blueprint(students_bp)

    @app.route('/')
    def index():
        return 'Hello World'


    @app.route('/uploaded/<path:filename>')
    def uploaded(filename):
        return send_from_directory('static/uploads', filename)


    @app.route('/upload', methods=['POST'])
    def upload():
        f = request.files.get('upload')
        ext = f.filename.split('.')[-1]
        if ext not in ['jpg', 'jpeg', 'gif', 'png']:
            return upload_fail(message='Image only!')

        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        url = url_for('uploaded', filename=f.filename)
        
        return upload_success(url, filename=f.filename)

    return app

from app import models