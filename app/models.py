from werkzeug.security import generate_password_hash, check_password_hash

from app import  db


students_courses = db.Table('student_courses',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
)

students_lessons_completed = db.Table('students_lessons_completed', 
    db.Column('lesson_id', db.Integer, db.ForeignKey('lesson.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)

    def __repr__(self) -> str:
        return f"Admin: '{self.username}'"
    
    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    courses = db.relationship('Course', backref='teacher', lazy='dynamic')

    def __repr__(self) -> str:
        return f"Teacher(name: '{self.username}')"

    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(512), nullable=False)
    courses = db.relationship('Course', secondary=students_courses,
                                backref=db.backref('students', lazy='dynamic'))
    lessons_completed = db.relationship('Lesson', secondary=students_lessons_completed,
                                            backref=db.backref('students_completed', lazy='dynamic')
    )

    def __repr__(self) -> str:
        return f"Student(name: '{self.username}')"

    def generate_password_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'))
    lessons = db.relationship('Lesson', backref='course', lazy='dynamic')
    published = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return f"Course(name: '{self.name}')"

    def next_lesson(self, completed_courses):
        return self.lessons.filter(Lesson.id.not_in(completed_courses))[0]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    content = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return f"Lesson(name: '{self.name}')"
