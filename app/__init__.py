import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


# extensions
db = SQLAlchemy()
migrate = Migrate()


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

    #register blueprints
    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.teachers import bp as teachers_bp
    app.register_blueprint(teachers_bp)

    @app.route('/')
    def index():
        return 'Hello World'

    return app

from app import models