from enum import unique
from flask import Flask
from os import environ
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)

# app.config['POSTGRES_URI']
app.config['SECRET_KEY'] = 'thisisasecret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index(): 
    user = User.query.filter_by(username='Dummy1').first()
    login_user(user)
    return 'User is now logged in!'

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'User logged out'

@app.route('/user')
@login_required
def user_info():
    return 'The current user is' + current_user.username


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    app.run(debug=True)