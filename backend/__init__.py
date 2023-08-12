from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/forms'
db = SQLAlchemy(app)

from backend import models, routes
