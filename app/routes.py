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
def dashboard():
    return render_template("main.html", title='Dashboard')
