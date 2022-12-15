import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY='supersecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///raees_academy.sqlite'
    CKEDITOR_FILE_UPLOADER = 'upload'
    CKEDITOR_ENABLE_CSRF = True
    UPLOADED_PATH = os.path.join(basedir, 'app/static/uploads')