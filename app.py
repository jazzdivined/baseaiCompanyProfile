from flask import Flask, render_template, url_for, abort, redirect
import dotenv
from View.index import index
from View.projects import projects
from View.register import register
import Admin
import API

dotenv.load_dotenv()

app = Flask(__name__)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/register', view_func=register)
app.add_url_rule('/projects', view_func=projects)

app.add_url_rule('/admin/api/projects/', view_func=API.projects, methods=["GET", "POST"])
app.add_url_rule('/admin/api/teams/', view_func=API.teams, methods=["GET", "POST"])
app.add_url_rule('/admin/api/quiz/', view_func=API.quiz, methods=["GET", "POST"])

app.add_url_rule('/admin/projects/', view_func=Admin.projects)
app.add_url_rule('/admin/teams/', view_func=Admin.teams)
app.add_url_rule('/admin/quiz/', view_func=Admin.quiz)


if __name__ == '__main__':
    app.run(debug=True)
