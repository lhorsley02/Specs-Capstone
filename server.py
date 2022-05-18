
from flask import Flask, redirect, render_template, flash, request, session, url_for
from flask_login import login_user, LoginManager
from jinja2 import StrictUndefined
from models import connect_to_db, db, User
from werkzeug.security import generate_password_hash, check_password_hash
from webforms import LoginForm, SignupForm

app = Flask(__name__)

app.secret_key="ASDF"

app.jinja_env.undefined = StrictUndefined
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Password Incorrect")
                return redirect(url_for("login"))
        else:
            flash("Email Not Found")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    form.validate()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        username = form.username.data
        password_hash = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
        if User.query.filter_by(username=username).first():
            flash("This username is taken")
            return redirect(url_for("signup"))
        new_user = User(fname=fname, 
                        lname=lname,
                        email=email,
                        username=username,
                        password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("signup.html", form = form)


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