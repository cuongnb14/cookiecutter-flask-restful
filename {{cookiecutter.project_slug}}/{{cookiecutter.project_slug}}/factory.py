from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("{{cookiecutter.project_slug}}")
app.config.from_pyfile('configs/config.py')

# Init db
db = SQLAlchemy(app)
