import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')
config_path = os.environ.get("CONFIG_PATH", "project.config.DevelopmentConfig")
app.config.from_object(config_path)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from database import Base, engine
Base.metadata.create_all(engine)
