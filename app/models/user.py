from datetime import datetime

from app.application import db


class User(db.document):
    email = db.StringField(default='')
    firstName = db.StringField(required=True)
    lastName = db.StringField(required=True)
    userName = db.StringField(unique=True, required=True)
    password = db.StringField(required=True)
    location = db.StringField(required=True)
    country = db.StringField(required=True)
    createdOn = db.DateTimeField(default=datetime.utcnow)
    modifiedOn = db.DateTimeField(default=None, null=True)
