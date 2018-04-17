from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return "<User {}".format(self.username)

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
    tuition_degree = db.Column(db.String(60), )
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

