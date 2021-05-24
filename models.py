"""Models for Users table"""
from os import name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User."""

    __tablename__ = "users"    

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    firstname = db.Column(db.String(30), nullable=False)
    middlename = db.Column(db.String(30), nullable=True)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    age =  db.Column(db.Integer, nullable=False)
    version_id = db.Column(db.Integer, nullable=False)

    def __init__(self,firstname,middlename,lastname,email,age,version_id):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
        self.age = age
        self.version_id = version_id


    def __repr__(self):
        """Show info about user"""
        u = self
        return f"<User {u.id} {u.firstname} {u.middlename} {u.lastname} {u.email} {u.age} {u.version_id}>"

    def serialize_user(self):

        return {
        "id": self.id,
        "firstname":self.firstname,
        "middlename": self.middlename,
        "lastname": self.lastname,
        "email": self.email,
        "age": self.age,
        "version_id": self.version_id
        }


class UserVersion(db.Model):
    """Copy User for versioning."""

    __tablename__ = "users_previous_version"    

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    middlename = db.Column(db.String(30), nullable=True)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.Text, nullable=False)
    age =  db.Column(db.Integer, nullable=False)
    version_id = db.Column(db.Integer, nullable=False)

    def __init__(self,user_id,firstname,middlename,lastname,email,age,version_id):
        self.user_id = user_id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.email = email
        self.age = age
        self.version_id = version_id

    def __repr__(self):
        """Show info about user"""
        u = self
        return f"<User {u.id} {u.user_id} {u.firstname} {u.middlename} {u.lastname} {u.email} {u.age} {u.version_id}>"

    def serialize_backup_user(self):

        return {
        "id": self.id,
        "user_id":self.user_id,
        "firstname":self.firstname,
        "middlename": self.middlename,
        "lastname": self.lastname,
        "email": self.email,
        "age": self.age,
        "version_id": self.version_id
        }




def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


