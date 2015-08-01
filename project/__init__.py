import os

from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
config_path = os.environ.get("CONFIG_PATH", "project.config.DevelopmentConfig")
app.config.from_object(config_path)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)


from database import Base, engine
Base.metadata.create_all(engine)
