import enum
from droidota import db

class UserRole(enum.Enum):
    ADMIN = 1
    MAINTAINER = 2


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Enum(UserRole))


class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    brand = db.Column(db.String, nullable=False)
    codename = db.Column(db.String, unique=True, nullable=False)
    maintainer = db.Column(db.Integer)