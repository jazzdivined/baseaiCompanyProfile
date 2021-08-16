import dotenv
from View.index import index
from View.projects import projects
from View.register import register
from Admin import admin_teams, admin_projects, admin_quiz
from API import api_teams, api_projects, api_quiz, api_members
#from Models import Member, Team
from flask_restful import Api


dotenv.load_dotenv()

from setup import app

api = Api(app)

app.add_url_rule('/', view_func=index)
app.add_url_rule('/register', view_func=register)
app.add_url_rule('/projects', view_func=projects)

api.add_resource(api_projects(), '/admin/api/projects/')
api.add_resource(api_quiz(), '/admin/api/quiz/')
api.add_resource(api_teams(), '/admin/api/teams/')
api.add_resource(api_members(), '/admin/api/teams/<int:id>')

app.add_url_rule('/admin/projects/', view_func=admin_projects)
app.add_url_rule('/admin/teams/', view_func=admin_teams, methods=["GET", "POST", "DELETE"])
app.add_url_rule('/admin/quiz/', view_func=admin_quiz, methods=["GET", "POST", "DELETE"])

if __name__ == '__main__':
    app.run(debug=True)
