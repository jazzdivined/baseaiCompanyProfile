from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://baseaico_jazz:Petraguy123@base-ai.com:3306/'
app.config['SQLALCHEMY_BINDS'] = {
    'teams' : 'mysql://baseaico_jazz:Petraguy123@base-ai.com:3306/baseaico_teams_test'
}
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)