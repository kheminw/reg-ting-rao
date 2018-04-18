from flask import render_template
from app import app, login_manager


@app.route("/index")
def index():
    return render_template("index.html", title='Home')

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html", title='Login')

@app.route("/main")
def main():
    return render_template("main.html", title='Dashboard')

@app.route("/schedule")
def schedule():
    return render_template("schedule.html", title='Dashboard')

@app.route("/grade")
def grade():
    return render_template("grade.html", title='Dashboard')

@app.route("/register",methods=["GET","POST"])
def register():

    return render_template("register.html", title='Dashboard')

@app.route("/profile")
def profile():
    return render_template("profile.html", title='Dashboard')

@app.route("/addcourse")
def addcourse():
    return render_template("add-eliminate.html", title='Dashboard')

@app.route("/courses")
def courses():
    return render_template("courses.html", title='Dashboard')

@app.route("/tuition")
def tuition():
    return render_template("tuition.html", title='Dashboard')
