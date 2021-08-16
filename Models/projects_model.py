import sys

sys.path.append('../baseaiCompanyProfile')
from flask_sqlalchemy import SQLAlchemy
from setup import app

db = SQLAlchemy(app)


class Project(db.Model):
    __bind_key__ = 'projects_db'
    
    # table column name
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(255), nullable=False, unique=True)
    show    = db.Column(db.Boolean, nullable=False)
    path    = db.Column(db.String(1000), nullable=False, unique=True)
     
    def __repr__(self):
        return f"Project : {self.name}"
    