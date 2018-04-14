from flask import render_template
from app import app, login_manager


@app.route("/index")
def index():
    return render_template("index.html", title='Home')

@app.route("/")
@app.route("/login")
def login():
    return render_template("login.html", title='Login')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title='Dashboard')
