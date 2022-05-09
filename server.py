
from flask import Flask, render_template, redirect, flash, session
import jinja2

app = Flask(__name__)

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login_run():
   