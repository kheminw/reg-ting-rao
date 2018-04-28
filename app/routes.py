from flask import render_template,flash, redirect, url_for, request, jsonify
from flask_login import current_user,login_user,login_required,logout_user
from app import app, login_manager, db
from app.models import *
from app.forms import LoginForm
from datetime import timedelta
from sqlalchemy import and_
from sqlalchemy.sql import text

# A kinda ugly query is needed to get the current semester/year as a global variable

CURRENT_SEMESTER_YEAR = db.engine.execute("SELECT MAX(semester_no) as current_semester, \
    `year` AS current_year FROM db_test1.Semester WHERE `year` IN \
    (SELECT max(`year`) FROM db_test1.Semester)").first()

@app.route("/",methods=['GET','POST'])
@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
       return redirect(url_for('schedule'))
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print("Form Validated: " + form.username.data + " " + form.password.data)
            User = user.query.filter_by(username=form.username.data).first()
            if User is None or not User.check_password(form.password.data):
                flash("Invalid username or password")
                return redirect(url_for('login'))
            login_user(User,duration=timedelta(hours=3))
            return redirect(url_for('schedule'))
    return render_template("login.html", title='login',form=form)

@app.route("/main")
def main():
    return render_template("main.html", title='Dashboard')

@app.route("/schedule",methods=['GET','POST'])
@login_required
def schedule():
    return render_template("schedule.html", title='schedule')

@app.route("/grade",methods=['GET','POST'])
@login_required
def grade():
    user_gpax = Student.query.filter_by(sid=current_user.username).first().gpax
    registered_course = Study.query.filter_by(sid=current_user.username).all()
    registered_course_name_credit = Course.query \
    .filter(Course.course_id.in_([c.course_id for c in registered_course])).all()
    registered_course_name_dict = {}

    re = [(c.course_name,c.course_year,c.course_semester_no) for c in registered_course_name_credit]

    for course in registered_course_name_credit:
        registered_course_name_dict[course.course_id] = [course.course_name,course.credit]

    year_semester = set()
    for course in registered_course:
        year_semester.add((course.course_year,course.course_semester_no))
    year_semester = sorted(list(year_semester))

    all_credit_semester = {}
    all_credit_semester[(0,0)] = 0

    for course in registered_course:
        if not (course.course_semester_no,course.course_year) in all_credit_semester:
            all_credit_semester[(course.course_semester_no,course.course_year)] = 0
        all_credit_semester[(course.course_semester_no,course.course_year)] +=  \
        registered_course_name_dict[course.course_id][1]
        all_credit_semester[(0,0)] += registered_course_name_dict[course.course_id][1]

    registered_course_dict = {}
    for i in year_semester:
        registered_course_dict[(i[0],i[1])] = Study.query \
        .filter_by(sid=current_user.username,course_semester_no=i[1],course_year=i[0]).all()

    return render_template("grade.html", title='grade',
    year_semester=year_semester,registered_course=registered_course,
    all_credit_semester=all_credit_semester,registered_course_name_credit=re,user_gpax=user_gpax,
    registered_course_name_dict=registered_course_name_dict,registered_course_dict=registered_course_dict)

@app.route("/transcript", methods=['GET', 'POST'])
@login_required
def transcript():
    user = {}
    current_user_info = Student.query.filter_by(sid=current_user.username).first()
    current_user_faculty = Faculty.query.filter_by(faculty_id=current_user_info.faculty_id).first()
    user["name"] = current_user_info.name
    user["sid"] = current_user_info.sid
    user["enroll_year"] = current_user_info.enroll_year
    user["degree"] = current_user_info.degree
    user["faculty_name"] = current_user_faculty.faculty_name

    registered_course = Study.query.filter_by(sid=current_user.username).all()
    registered_course_name_credit = Course.query \
    .filter(Course.course_id.in_([c.course_id for c in registered_course])).all()
    registered_course_name_dict = {}

    for course in registered_course_name_credit:
        registered_course_name_dict[course.course_id] = [course.course_name,course.credit]

    year_semester = set()
    for course in registered_course:
        year_semester.add((course.course_year,course.course_semester_no))
    year_semester = sorted(list(year_semester))

    all_credit_semester = {}
    all_credit_semester[(0,0)] = 0

    stack_credit_semester ={}

    for course in registered_course:
        if not (course.course_semester_no,course.course_year) in all_credit_semester:
            all_credit_semester[(course.course_semester_no,course.course_year)] = 0
        if not (course.course_semester_no,course.course_year) in stack_credit_semester:
            if course.course_semester_no == 1:
                if (3,course.course_year-1) in stack_credit_semester:
                    stack_credit_semester[(course.course_semester_no,course.course_year)] = \
                    stack_credit_semester[(3,course.course_year-1)]
                else:
                    stack_credit_semester[(course.course_semester_no,course.course_year)] = \
                    stack_credit_semester[(2,course.course_year-1)]
            else:
                stack_credit_semester[(course.course_semester_no,course.course_year)] = \
                stack_credit_semester[(course.course_semester_no-1,course.course_year)]

        stack_credit_semester[(course.course_semester_no,course.course_year)] += \
        registered_course_name_dict[course.course_id][1]

        all_credit_semester[(course.course_semester_no,course.course_year)] +=  \
        registered_course_name_dict[course.course_id][1]

        all_credit_semester[(0,0)] += registered_course_name_dict[course.course_id][1]

    return render_template("transcript.html", title='transcript')

@app.route("/slip/<year>/<semester>", methods=["GET", "POST"])
@login_required
def slip(year, semester):
    user = {}
    current_user_info = Student.query.filter_by(sid=current_user.username).first()
    current_user_faculty = Faculty.query.filter_by(faculty_id=current_user_info.faculty_id).first()
    user["name"] = current_user_info.name
    user["sid"] = current_user_info.sid
    user["degree"] = current_user_info.degree
    user["faculty_name"] = current_user_faculty.faculty_name

    pay_tuition = Pay_Tuition.query.filter_by(sid=current_user.username,tuition_year=year,tuition_semester=semester).first()

    tuition = Tuition.query.filter_by(faculty_id=current_user_info.faculty_id,
    tuition_degree=current_user_info.degree,tuition_year=pay_tuition.tuition_year,
    tuition_semester=pay_tuition.tuition_semester).first()
    return render_template("slip.html", title='slip', user=user, tuition=tuition, pay_tuition=pay_tuition)

@app.route("/register", methods=["GET","POST"])
@login_required
def register():
    if(request.method == 'GET'):
        request_data = Request.query.filter_by(sid=current_user.username).all()
        if(len(request_data) != 0):
            requested_course_info = Course.query \
                .filter(Course.course_id.in_([x.course_id for x in request_data])) \
                .filter(Course.course_semester_no == CURRENT_SEMESTER_YEAR[0]) \
                .filter(Course.course_year == CURRENT_SEMESTER_YEAR[1]).all()
            return render_template("register.html", registered=True, registration_data=requested_course_info, title='Course Registration')
        else:
            return render_template("register.html", registered=False, title='Course Registration') 
    elif(request.method == 'POST'):
        subject_id = request.form.getlist('subject_id')
        subject_section = request.form.getlist('subject_section')
        print(subject_id, subject_section)
        for i in range(len(subject_id)):
            if(subject_id[i] == '' or subject_section[i] == ''):
                continue
            else:
                if(not register_course(subject_id[i], subject_section[i], CURRENT_SEMESTER_YEAR[0], \
                     CURRENT_SEMESTER_YEAR[1])):
                    print("Registration Error")
                    return redirect("/register")
        return redirect("/register")
        

@app.route("/profile",methods=['GET','POST'])
@login_required
def profile():
    user = {}
    current_user_info = Student.query.filter_by(sid=current_user.username).first()
    current_user_faculty = Faculty.query.filter_by(faculty_id=current_user_info.faculty_id).first()
    user["name"] = current_user_info.name
    user["sid"] = current_user_info.sid
    user["enroll_year"] = current_user_info.enroll_year
    user["degree"] = current_user_info.degree
    user["dorm_score"] = current_user_info.dorm_score
    user["faculty_name"] = current_user_faculty.faculty_name
    return render_template("profile.html", title='profile', user=user)

@app.route("/addcourse",methods=['GET','POST'])
@login_required
def addcourse():
    current_courses = Study.query.filter_by(sid=current_user.username,
     course_year=CURRENT_SEMESTER_YEAR[1], course_semester_no=CURRENT_SEMESTER_YEAR[0]).all()
    current_courses_name_credit = Course.query \
        .filter(Course.course_id.in_([x.course_id for x in current_courses])).all()
    name_credit_serialized = {}
    for course in current_courses_name_credit:
        name_credit_serialized[course.course_id] = [course.course_name, course.credit]
    return render_template("add-eliminate.html", title='addcourse',
        current_courses=current_courses, name_credit=name_credit_serialized)

@app.route("/courses",methods=['GET','POST'])
@login_required
def courses():
    if(request.method == "GET"):
        return render_template("courses.html", title='courses')
    elif(request.method == "POST"):
        current_courses = []
        if(request.form["course_name"] != ""):
            current_courses = Course.query.filter(Course.course_name.startswith(
                request.form["course_name"])).all()
        elif(request.form["course_id"] != ""):
            current_courses = Course.query.filter(Course.course_id.startswith(
                request.form["course_id"])).all()
        else:
            return redirect("/courses")
        return render_template("course_result.html", result=current_courses)


@app.route("/tuition",methods=['GET','POST'])
@login_required
def tuition():
    user = {}
    current_user_info = Student.query.filter_by(sid=current_user.username).first()
    current_user_faculty = Faculty.query.filter_by(faculty_id=current_user_info.faculty_id).first()
    pay_tuition = Pay_Tuition.query.filter_by(sid=current_user.username).all()
    pay_tuition = sorted(pay_tuition,key=lambda p :p.tuition_year)

    tuition = Tuition.query.filter_by(faculty_id=current_user_info.faculty_id,
    tuition_degree=current_user_info.degree,tuition_year=pay_tuition[-1].tuition_year,
    tuition_semester=pay_tuition[-1].tuition_semester).all()

    tuition_amount_dict = {}
    for p in pay_tuition:
        tuition_amount_dict[(p.tuition_year,p.tuition_semester)]=Tuition.query \
        .filter_by(faculty_id=current_user_info.faculty_id,tuition_degree=current_user_info.degree,
        tuition_year=p.tuition_year,tuition_semester=p.tuition_semester).first().tuition_amount

    user["name"] = current_user_info.name
    user["degree"] = current_user_info.degree
    user["faculty_name"] = current_user_faculty.faculty_name


    return render_template("tuition.html", title='tuition',
    user=user,tuition=tuition,pay_tuition=pay_tuition,tuition_amount_dict=tuition_amount_dict)

@app.route("/recommend", methods=['GET','POST'])
@login_required
def recommend():
    if(request.method == "GET"):
        return render_template("recommend.html", title='recommend')
    elif(request.method == "POST"):
        results = []
        LAST_SEMESTER_YEAR = CURRENT_SEMESTER_YEAR

        if(CURRENT_SEMESTER_YEAR[0] > 1):
            LAST_SEMESTER_YEAR = (CURRENT_SEMESTER_YEAR[0] - 1, CURRENT_SEMESTER_YEAR[1])
        else:
            LAST_SEMESTER_YEAR = (2, CURRENT_SEMESTER_YEAR[1] - 1)

        gened_course = [(course.course_id,course.course_name,course.credit) for course in Course.query.filter_by(course_Type=request.form["course_Type"]) \
                        if course.course_semester_no == LAST_SEMESTER_YEAR[0] and course.course_year == LAST_SEMESTER_YEAR[1] ]
        

        for course in gened_course:

            query_statement = "SELECT AVG(S.grade) from db_test1.Study S WHERE S.course_id = " + str(course[0])
            average_grade = db.engine.execute(query_statement).first()[0]

            results.append({"course_id" : course[0], "course_name" : course[1], "credit" : course[2], "average" : average_grade})

        return render_template("recommend.html", grade_results=results)

    return render_template("recommend.html", title='recommend')



@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/login")

def register_course(course_id, section, course_semester_no, course_year):
    successful = False
    new_request = Request(sid=current_user.username,
                      course_id=course_id,
                      section=section,
                      course_semester_no=course_semester_no,
                      course_year=course_year)
    try:
        db.session.add(new_request)
        db.session.commit()
        successful = True
    except:
        db.session.rollback()
    return successful

@app.route("/api/add_remove_course", methods=["POST", "DELETE"])
@login_required
def add_remove_course():
    successful = False
    res = {}
    if(request.method == "POST"):
        print(current_user.username)
        new_course_entry = Study(sid=current_user.username,
                               course_id=request.form["course_id"],
                               section=request.form["section"],
                               course_semester_no=request.form["course_semester_no"],
                               course_year=request.form["course_year"])
        try:
            db.session.add(new_course_entry)
            db.session.commit()
            successful = True
        except:
            db.session.rollback()
    elif(request.method == "DELETE"):
        print(current_user.username, request.form["course_id"])
        delete_entry = Study.query.filter_by(sid=current_user.username, \
         course_id=request.form["course_id"]).first()
        print(delete_entry.course_id)
        try:
            db.session.delete(delete_entry)
            db.session.commit()
            successful = True
        except:
            db.session.rollback()
    if(successful):
        res["result"] = "success"
    else:
        res["result"] = "adding data to the table failed"
    return jsonify(res)

@app.route("/api/get_current_courses/", methods=["GET"])
@login_required
def get_current_courses():
    current_courses = Study.query.filter_by(sid=current_user.username, course_year=2560).all()
    current_courses_parsed = {"sid":current_user.username, "courses":[]}
    for course in current_courses:
        current_courses_parsed["courses"].append(course.course_id)
    return jsonify(current_courses_parsed)

@app.route("/api/get_all_courses/", methods=["GET"])
@login_required
def get_all_courses():
    all_courses = Study.query.filter_by(sid=current_user.username).all()
    all_courses_parsed = {"sid":current_user.username, "courses":[]}
    for course in all_courses:
        all_courses_parsed["courses"].append(course.course_id)
    return jsonify(all_courses_parsed)

@app.route('/test', methods=["GET"])
def get_student():
    student = Student.query.filter_by(sid=1).first()
    print(student)
    return str(student)
