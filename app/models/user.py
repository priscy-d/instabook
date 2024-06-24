from datetime import datetime

from app.application import db

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


class User(FlaskForm):
    submit = SubmitField("Add todo")
    email = StringField('email', validators=[DataRequired()])
    firstName = StringField('firstName', validators=[DataRequired()])
    lastName = StringField('lastName', validators=[DataRequired()])
    userName = StringField('userName', validators=[DataRequired()])
    password = StringField('passwprd', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
