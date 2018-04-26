from app import app, db
from app.models import *
import random
import string


degree_rate = {'Bachelor':21000, 'Master':23000, 'Doctoral':25000}
degree_time = {'Bachelor':4, 'Master':2, 'Doctoral':2}


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

# for s in student:
#     for sem in range (1, 3):
#         for year in range (2013, 2017):
#             if (s.enroll_year > year) : continue
#             elif (s.enroll_year + degree_time[s.degree] -1 < year) : continue
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

# student = Student.query.filter_by()
# current_year = 2017
# data = []

# for s in student:
#     course = Course.query.filter_by(faculty_id=s.faculty_id)
#     # for year in range (s.enroll_year, 2018):
#     #     if (s.enroll_year + degree_time[s.degree]-1 < year) : continue
#     #     else :
#     for c in course:
#         data.append((s.sid,s.enroll_year,s.degree,s.faculty_id, c.course_id, c.course_year, c.section, c.course_semester_no))

# # for d in data:
# #     print(d)

# study = [
#     Study(
#         sid=10000,
#         course_id=2110101,
#         section=1,
#         course_semester_no=2,
#         course_year=2017,
#         grade=''
#     ),
#     Study(
#         sid=10000,
#         course_id=2110422,
#         section=2,
#         course_semester_no=2,
#         course_year=2017,
#         grade=''
#     ),
#     Study(
#         sid=10001,
#         course_id=2313213,
#         section=1,
#         course_semester_no=2,
#         course_year=2017,
#         grade=''
#     ),
# ]

# db.session.add_all(study)
# db.session.commit()


############################ PART STUDENT ############################



############################ PART COURSE ############################   

# course = [Course(
#     course_id=2110471,
#     section=2,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Computer Network I",
#     credit=3,
#     midterm_exam_date='2018-03-08',
#     final_exam_date='2018-05-17',
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="CP Juniors Only",
#     course_gpax=None,
#     major_id=10,
#     faculty_id=21,
#     room_no=405,
#     building_name="Engineering 3",
#     course_day="Monday",
#     course_start_time='11:00',
#     course_end_time='13:00'),
    
#     Course(
#     course_id=2110511,
#     section=21,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Game Programming",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="CP Approve Only",
#     course_gpax=None,
#     major_id=10,
#     faculty_id=21,
#     room_no=113,
#     building_name="Engineering 1",
#     course_day="Monday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2110332,
#     section=33,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="System Analysis Design",
#     credit=3,
#     midterm_exam_date='2018-03-07',
#     final_exam_date='2018-05-15',
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="CP Junior Only",
#     course_gpax=None,
#     major_id=10,
#     faculty_id=21,
#     room_no=321,
#     building_name="Engineering 3",
#     course_day="Tuesday",
#     course_start_time='08:30',
#     course_end_time='11:30'),

#     Course(
#     course_id=2110432,
#     section=21,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Automatic Speech Recognition",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="CP Approve Only",
#     course_gpax=None,
#     major_id=10,
#     faculty_id=21,
#     room_no=420,
#     building_name="Engineering 3",
#     course_day="Thursday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2110318,
#     section=1,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="System Analysis Design",
#     credit=3,
#     midterm_exam_date='2018-03-06',
#     final_exam_date='2018-05-16',
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="CP Junior Only",
#     course_gpax=None,
#     major_id=10,
#     faculty_id=21,
#     room_no=315,
#     building_name="Engineering 3",
#     course_day="Friday",
#     course_start_time='08:30',
#     course_end_time='11:30'),

#     ############# GENED #####################3

#     Course(
#     course_id=2313221,
#     section=1,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Photographic Science",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=60,
#     registered_amount=0,
#     course_Type="GENED-SC",
#     course_gpax=None,
#     major_id=13,
#     faculty_id=23,
#     room_no=501,
#     building_name="Mahamakut",
#     course_day="Thursday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2207103,
#     section=1,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Philosophy and Logic",
#     credit=3,
#     midterm_exam_date='2018-03-06',
#     final_exam_date='2018-05-16',
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-HU",
#     course_gpax=None,
#     major_id=7,
#     faculty_id=22,
#     room_no=402,
#     building_name="Borom",
#     course_day="Friday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2502390,
#     section=1,
#     course_semester_no=2,
#     course_year=2017,
#     course_name="Intro Pack Design",
#     credit=3,
#     midterm_exam_date='2018-03-09',
#     final_exam_date='2018-05-18',
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-IN",
#     course_gpax=None,
#     major_id=2,
#     faculty_id=25,
#     room_no=3201,
#     building_name="Vodhyakorn",
#     course_day="Wednesday",
#     course_start_time='08:30',
#     course_end_time='11:30'),   
    
#     ################### before 2017 ####################
    
#      Course(
#     course_id=2313221,
#     section=1,
#     course_semester_no=2,
#     course_year=2016,
#     course_name="Photographic Science",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=60,
#     registered_amount=0,
#     course_Type="GENED-SC",
#     course_gpax=3.98,
#     major_id=13,
#     faculty_id=23,
#     room_no=501,
#     building_name="Mahamakut",
#     course_day="Thursday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2207103,
#     section=1,
#     course_semester_no=1,
#     course_year=2016,
#     course_name="Philosophy and Logic",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-HU",
#     course_gpax=2.89,
#     major_id=7,
#     faculty_id=22,
#     room_no=402,
#     building_name="Borom",
#     course_day="Friday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2502390,
#     section=1,
#     course_semester_no=2,
#     course_year=2016,
#     course_name="Intro Pack Design",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-IN",
#     course_gpax=3.5,
#     major_id=2,
#     faculty_id=25,
#     room_no=3201,
#     building_name="Vodhyakorn",
#     course_day="Wednesday",
#     course_start_time='08:30',
#     course_end_time='11:30'),

#     ##################### before 2016 #################

#     Course(
#     course_id=2313221,
#     section=1,
#     course_semester_no=2,
#     course_year=2015,
#     course_name="Photographic Science",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=60,
#     registered_amount=0,
#     course_Type="GENED-SC",
#     course_gpax=3.87,
#     major_id=13,
#     faculty_id=23,
#     room_no=501,
#     building_name="Mahamakut",
#     course_day="Thursday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2207103,
#     section=1,
#     course_semester_no=1,
#     course_year=2015,
#     course_name="Philosophy and Logic",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-HU",
#     course_gpax=3.12,
#     major_id=7,
#     faculty_id=22,
#     room_no=402,
#     building_name="Borom",
#     course_day="Friday",
#     course_start_time='13:00',
#     course_end_time='16:00'),

#     Course(
#     course_id=2502390,
#     section=1,
#     course_semester_no=2,
#     course_year=2015,
#     course_name="Intro Pack Design",
#     credit=3,
#     midterm_exam_date=None,
#     final_exam_date=None,
#     course_capacity=30,
#     registered_amount=0,
#     course_Type="GENED-IN",
#     course_gpax=3.34,
#     major_id=2,
#     faculty_id=25,
#     room_no=3201,
#     building_name="Vodhyakorn",
#     course_day="Wednesday",
#     course_start_time='08:30',
#     course_end_time='11:30')
# ]

c = Course.query.filter_by(course_id=2110422)
for cc in c:
    cc.course_day = "Thursday"
    cc.course_start_time = '8:30'
    cc.course_end_time = '11:30'

# db.session.add_all(course)
db.session.commit()

