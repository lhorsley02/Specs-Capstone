
from flask import Flask, render_template, flash, session
from jinja2 import StrictUndefined
from model import connect_to_db, db

app = Flask(__name__)

app.secret_key="ASDF"

app.jinja_env.undefined = StrictUndefined


@app.route("/", methods=["GET"])
def show_home():
    return render_template("home.html")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def run_login():
   return render_template("home.html")


@app.route("/signup", methods=["GET"])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def run_signup():
   return render_template("home.html")

@app.route("/account", methods=["GET"])
def show_account():
    return render_template("account.html")

@app.route("/academia", methods=["GET"])
def show_academia():
    return render_template("academia.html")

@app.route("/cottagecore", methods=["GET"])
def show_cottagecore():
    return render_template("cottagecore.html")

@app.route("/cyberpunk", methods=["GET"])
def show_cyberpunk():
    return render_template("cyberpunk.html")

@app.route("/forest", methods=["GET"])
def show_forest():
    return render_template("forest.html")

@app.route("/rainy", methods=["GET"])
def show_rainy():
    return render_template("rainy.html")

@app.route("/summer", methods=["GET"])
def show_summer():
    return render_template("summer.html")





if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    app.env="development"
    app.run(port=5000, debug=True)