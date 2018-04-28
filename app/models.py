from app import db,login_manager
from flask_login import UserMixin

class user(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64), nullable=False)
    def __repr__(self):
        return "<User {}".format(self.username)

    def check_password(self,password):
        return self.password == password

@login_manager.user_loader
def load_user(id):
    return user.query.get(int(id))

class Faculty(db.Model):
    __tablename__ = 'Faculty'

    faculty_id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(60), nullable=False)

class Dorm_Room(db.Model):
    __tablename__ = 'Dorm_Room'

    dorm_name = db.Column(db.String(60), primary_key=True)
    dorm_room_no = db.Column(db.Integer, primary_key=True)

class Student(db.Model):
    __tablename__ = 'Student'

    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    enroll_year = db.Column(db.Integer, )
    graduated = db.Column(db.Boolean(), )
    degree = db.Column(db.String(60), )
    gpax = db.Column(db.Float(), )
    dorm_score = db.Column(db.Integer, )
    dorm_name = db.Column(db.String(60), db.ForeignKey('Dorm_Room.dorm_name'), )
    dorm_room_no = db.Column(db.Integer, db.ForeignKey('Dorm_Room.dorm_room_no'), )
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.faculty_id'), )

class Tuition(db.Model):
    __tablename__ = 'Tuition'

    tuition_semester = db.Column(db.Integer, primary_key=True)
    tuition_year = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.faculty_id'), primary_key=True)
    tuition_degree = db.Column(db.String(60), primary_key=True)
    tuition_amount = db.Column(db.Integer, )
    tuition_start_date = db.Column(db.Date, )
    tuition_end_date = db.Column(db.Date, )

class Pay_Tuition(db.Model):
    __tablename__ = 'Pay_Tuition'

    sid = db.Column(db.Integer, db.ForeignKey('Student.sid'), primary_key=True)
    tuition_semester = db.Column(db.Integer, db.ForeignKey('Tuition.tuition_semester'), primary_key=True)
    tuition_year = db.Column(db.Integer, db.ForeignKey('Tuition.tuition_year'), primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Tuition.faculty_id'), primary_key=True)
    tuition_late = db.Column(db.Boolean(), nullable=False)
    tuition_paid = db.Column(db.Boolean(), nullable=False)

class Building(db.Model):
    __tablename__ = 'Building'

    name = db.Column(db.String(60), primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.faculty_id'))

class Building_Room(db.Model):
    __tablename__ = 'Building_Room'

    room_no = db.Column(db.Integer, primary_key=True)
    building_name = db.Column(db.String(60), db.ForeignKey('Building.name'), primary_key=True)
    capacity = db.Column(db.Integer, nullable=False)

class Major(db.Model):
    __tablename__ = 'Major'

    major_id = db.Column(db.Integer, primary_key=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('Faculty.faculty_id'), primary_key=True)
    major_name = db.Column(db.String(60))

class Professor(db.Model):
    __tablename__ = 'Professor'
    
    professor_id = db.Column(db.Integer, primary_key=True)
    major_id = db.Column(db.Integer, db.ForeignKey('Major.major_id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('Major.faculty_id'))
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)

class Semester(db.Model):
    __tablename__ = 'Semester'

    semester_no = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    enroll_start_date = db.Column(db.Date)
    enroll_end_date = db.Column(db.Date)
    withdraw_start_date = db.Column(db.Date)
    withdraw_end_date = db.Column(db.Date)

class Course(db.Model):
    __tablename__ = 'Course'

    course_id = db.Column(db.Integer, primary_key=True)
    section = db.Column(db.Integer, primary_key=True)
    course_semester_no = db.Column(db.Integer, db.ForeignKey('Semester.semester_no'), primary_key=True)
    course_year = db.Column(db.Integer, db.ForeignKey('Semester.year'), primary_key=True)
    course_name = db.Column(db.String(60), nullable=False)
    course_day = db.Column(db.String(60))
    course_start_time = db.Column(db.Time)
    course_end_time = db.Column(db.Time)
    credit = db.Column(db.Integer, nullable=False)
    midterm_exam_date = db.Column(db.Date)
    final_exam_date = db.Column(db.Date)
    course_capacity = db.Column(db.Integer)
    registered_amount = db.Column(db.Integer)
    course_Type = db.Column(db.String(60), nullable=False)
    course_gpax = db.Column(db.Float)
    major_id = db.Column(db.Integer, db.ForeignKey('Major.major_id'))
    faculty_id = db.Column(db.Integer, db.ForeignKey('Major.faculty_id'))
    room_no = db.Column(db.Integer, db.ForeignKey('Building_Room.room_no'))
    building_name = db.Column(db.String(60), db.ForeignKey('Building_Room.building_name'))

class Teaches(db.Model):
    __tablename__ = 'Teaches'

    professor_id = db.Column(db.Integer, db.ForeignKey('Professor.professor_id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('Course.course_id'), primary_key=True)
    section = db.Column(db.Integer, db.ForeignKey('Course.section'), primary_key=True)
    course_semester_no = db.Column(db.Integer, db.ForeignKey('Course.course_semester_no'), primary_key=True)
    course_year = db.Column(db.Integer, db.ForeignKey('Course.course_year'), primary_key=True)

class Study(db.Model):
    __tablename__ = 'Study'

    sid = db.Column(db.Integer, db.ForeignKey('Student.sid'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('Course.course_id'), primary_key=True)
    section = db.Column(db.Integer, db.ForeignKey('Course.section'), primary_key=True)
    course_semester_no = db.Column(db.Integer, db.ForeignKey('Course.course_semester_no'), primary_key=True)
    course_year = db.Column(db.Integer, db.ForeignKey('Course.course_year'), primary_key=True)
    grade = db.Column(db.Float)

class Request(db.Model):
    __tablename__ = 'Request'

    sid = db.Column(db.Integer, db.ForeignKey('Student.sid'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('Course.course_id'), primary_key=True)
    section = db.Column(db.Integer, db.ForeignKey('Course.section'), primary_key=True)
    course_semester_no = db.Column(db.Integer, db.ForeignKey('Course.course_semester_no'), primary_key=True)
    course_year = db.Column(db.Integer, db.ForeignKey('Course.course_year'), primary_key=True)
    random_priority = db.Column(db.Integer)
    result = db.Column(db.String(60))

