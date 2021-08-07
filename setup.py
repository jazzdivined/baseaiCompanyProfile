from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
<<<<<<< HEAD
import os
=======
>>>>>>> 4600a921d86e07c996b0f5bd9e4171510c2b825a

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://baseaico_jazz:Petraguy123@base-ai.com:3306/'
app.config['SQLALCHEMY_BINDS'] = {
    'teams' : 'mysql://baseaico_jazz:Petraguy123@base-ai.com:3306/baseaico_teams_test',
    'quiz'  : 'mysql://baseaico_jazz:Petraguy123@base-ai.com:3306/baseaico_quiz_test'
}
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
db = SQLAlchemy(app)
current_path = os.getcwd()

