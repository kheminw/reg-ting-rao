from flask import render_template,flash, redirect, url_for, request
from flask_login import current_user,login_user,login_required
from app import app, login_manager
from app.models import user
from app.forms import LoginForm
from datetime import timedelta

@app.route("/index")
def index():
    return render_template("index.html", title='Home')

@app.route("/",methods=['GET','POST'])
@app.route("/login",methods=['GET','POST'])
def login():
    #if current_user.is_authenticated:
    #    return redirect(url_for('schedule'))
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
    return render_template("grade.html", title='grade')

@app.route("/register", methods=["GET","POST"])
def register():
    
    return render_template("register.html", title='Dashboard')

@app.route("/profile",methods=['GET','POST'])
@login_required
def profile():
    return render_template("profile.html", title='profile')

@app.route("/addcourse",methods=['GET','POST'])
@login_required
def addcourse():
    return render_template("add-eliminate.html", title='addcourse')

@app.route("/courses",methods=['GET','POST'])
@login_required
def courses():
    return render_template("courses.html", title='courses')

@app.route("/tuition",methods=['GET','POST'])
@login_required
def tuition():
    return render_template("tuition.html", title='tuition')
