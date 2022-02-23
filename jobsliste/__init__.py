from flask import Flask
from flask_sqlalchemy import SQLAlchemy

nomedatabase = 'sqlite:///'+"AllJobs.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = nomedatabase
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)
db1 = SQLAlchemy(app)

from jobsliste import routes

