
from datetime import datetime, date
import email
from unicodedata import name
from click import password_option
from os import environ
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

db = SQLAlchemy()


class Users(db.Model, UserMixin):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)



def create_dummy_data():
    dummy1 = User(email="dummy1@gmail.com", password="pass123")
    dummy2 = User(email="dummy2@gmail.com", password="pass456")
    dummy3 = User(email="dummy3@gmail.com", password="pass789")

    db.session.add(dummy1)
    db.session.add(dummy2)
    db.session.add(dummy3)
    db.session.commit()




def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
