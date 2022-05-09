
from flask import Flask, render_template, flash, session
from jinja2 import StrictUndefined
from model import connect_to_db, db

app = Flask(__name__)

app.secret_key="ASDF"

app.jinja_env.undefined = StrictUndefined



@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def run_login():
   return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.env="development"
    app.run(port=5000, debug=True)