from app import app, db
from app.models import *
import random

############################ PART FIX YEAR ############################

# semester = Semester.query.filter_by(semester_no=2)
# for s in semester:
#         s.enroll_start_date=str(s.year)+'-01-01'
#         s.enroll_end_date=str(s.year)+'-01-15'
#         s.withdraw_start_date=str(s.year)+'-02-01'
#         s.withdraw_end_date=str(s.year)+'-03-01'
# db.session.commit()
# semester = Semester.query.filter_by(semester_no=1)
# for s in semester:
#         s.enroll_start_date=str(s.year)+'-08-01'
#         s.enroll_end_date=str(s.year)+'-08-15'
#         s.withdraw_start_date=str(s.year)+'-09-01'
#         s.withdraw_end_date=str(s.year)+'-010-01'
# db.session.commit()

# course = Course.query.filter_by()
# for c in course:
#         c.course_year=c.course_year if (c.course_year < 2500) else c.course_year-543
#         c.course_semester_no = 2
# db.session.commit()

# teaches = Teaches
# Study
# request

############################ PART TUITION ############################

degree_rate = {'Bachelor':21000, 'Master':23000, 'Doctoral':25000}

# tuiteach = [
#         Tuition(tuition_semester=semester,
#                     tuition_year=year,
#                     faculty_id=facID,
#                     tuition_degree=degree,
#                     tuition_amount=degree_rate[degree],
#                     tuition_start_date=str(year)+'-12-21',
#                     tuition_end_date=str(year)+'-12-29')
#                 for degree in degree_rate
#                 for year in range (2013, 2019)
#                 for semester in range (1, 3)
#                 for facID in range( 21, 27)
# ]
# db.session.add_all(tuiteach)
# db.session.commit()
# for tu in tuiteach:
#         print(tu.tuition_semester, tu.tuition_year, tu.faculty_id, tu.tuition_degree)

############################ PART PAY_TUITION ############################


# student = Student.query.filter_by(enroll_year=2018)
# for s in student:
#     s.enroll_year = 2017
# db.session.commit()

# student = Student.query.filter_by()
# for st in student :
#         print(st.name, st.sid, st.degree, st.faculty_id)
# tuition = Tuition.query.filter_by()
# for tui in tuition :
#         print(tui)

# payTpass = []
# time = {'Bachelor':4, 'Master':2, 'Doctoral':2}

# for s in student:
#     for sem in range (1, 3):
#         for year in range (2013, 2017):
#             if (s.enroll_year > year) : continue
#             elif (s.enroll_year + time[s.degree] < year) : continue
#             else :
#                 payTpass.append( Pay_Tuition(
#                     sid=s.sid,
#                     tuition_semester=sem,
#                     tuition_year=year,
#                     faculty_id=s.faculty_id,
#                     # tuition_degree=s.degree,
#                     tuition_late=random.randint(0,1),
#                     tuition_paid=1
#                 ))

# late = random.randint(0,1)

# payTpres = []
# current_year = 2017
# for s in student:
#     for sem in range(1, 3):
#         if (s.enroll_year > current_year) : continue
#         elif (s.graduated == 0) :
#             isPay =1 if (sem==1) else random.randint(0,1)
#             payTpres.append(  Pay_Tuition(
#                     sid=s.sid,
#                     tuition_semester=sem,
#                     tuition_year=current_year,
#                     faculty_id=s.faculty_id,
#                     # tuition_degree=s.degree,
#                     tuition_paid=isPay,
#                     tuition_late=late if (late==1 and sem==2 and isPay==0) else random.randint(0,1),
#             ))

# db.session.add_all(payTpass)
# db.session.add_all(payTpres)
# db.session.commit()

# for pay in payTpass:
#         print(pay.sid, pay.tuition_semester, pay.tuition_year, pay.tuition_late, pay.tuition_paid)
# for pay in payTpres:
#         print(pay.sid, pay.tuition_semester, pay.tuition_year, pay.tuition_late, pay.tuition_paid)

############################ PART DORM ############################

# out = Dorm_Room.query.filter_by()
# dorm = set()
# for o in out:
#         dorm.add((o.dorm_name, o.dorm_room_no))
# moreDorm = [
#         Dorm_Room(
#                 dorm_name=name,
#                 dorm_room_no=no
#                 for name in ['AA','BB','CC','DD','EE']
#                 for no in [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         )
# ]

############################ PART SEMESTER ############################

# semester = []
# for sem in range (1, 3):
#         for y in range (2016, 2018):
#                 if (sem==1 and y == 2017): continue
#                 elif (sem==2 and y==2015): continue
#                 elif (sem==2 and y==2017): continue
#                 else :
#                        semester.append(
#                                 Semester(
#                                         semester_no=sem,
#                                         year=y,
#                                         enroll_start_date=str(y) + '-08-01' if (sem==1) else str(y+1) + '-01-01',
#                                         enroll_end_date=str(y) + '-08-15' if (sem==1) else str(y+1) + '-01-15',
#                                         withdraw_start_date=str(y) + '-11-01' if (sem==1) else str(y+1) + '-03-01',
#                                         withdraw_end_date=str(y+1) + '-01-01' if (sem==1) else str(y+1) + '-05-01'
#                                 )  
#                        ) 
# db.session.add_all(semester)
# db.session.commit()

# for s in semester:
#         print(s.semester_no, s.year, s.enroll_start_date, s.enroll_end_date)


############################ PART STUDY ############################

