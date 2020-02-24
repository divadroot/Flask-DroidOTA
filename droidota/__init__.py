from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

from droidota import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from droidota.models import User, Device, Build, Channel
db.create_all()
db.session.commit()
