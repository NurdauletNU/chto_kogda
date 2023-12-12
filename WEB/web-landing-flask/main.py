from flask import Flask, render_template

app=Flask(__name__)


@app.route("/")
def home():
    name="Nurdaulet"
    return render_template("home.html", name=name)


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route("/about us")
def about_us():
    return render_template("about_us.html")

@app.route("/new")
def new():
    return render_template("new.html")