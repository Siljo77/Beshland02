from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, Length
from wtforms import StringField, SubmitField, PasswordField


class UserForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired(Length(min=2, max=100))])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password_hash = PasswordField("Password", validators=[DataRequired(), EqualTo('password_hash2', message= 'Passwords Must Match!')]) 
    password_hash2 = PasswordField("Confirm Password", validators=[DataRequired()])                              
    submit = SubmitField("Create Account")    
    
         
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class UpdateForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])