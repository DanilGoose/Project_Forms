from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='html')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forms.db'
