from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")



class SignupForm(FlaskForm):
	fname = StringField("First Name", render_kw={'placeholder':'First Name'}, validators=[DataRequired()])
	lname = StringField("Last Name", render_kw={'placeholder':'Last Name'}, validators=[DataRequired()])
	email = StringField("Email", render_kw={'placeholder':'Email'}, validators=[DataRequired()])
	username = StringField("Username", render_kw={'placeholder':'Username'}, validators=[DataRequired()])
	password = PasswordField('Password', render_kw={'placeholder':'Password'}, validators=[DataRequired()])
	submit = SubmitField("Submit")
