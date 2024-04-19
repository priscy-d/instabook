from app.application import db


class User(db.document):
    email = db.StringField(default='')
    name = db.StringField(required=True)
    userName = db.StringField(unique=True, required=True)
