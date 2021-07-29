import sys

sys.path.append('../baseaiCompanyProfile')

from flask_restful import Resource, fields, marshal_with, reqparse
from Models.Team import TeamModel
from setup import db

"""
:http-method POST: Adds a Team
:format:
    {
        'team_id': <team_id>,
        'team_name': <team_name>,
        'members':
            [<List of members>]
    }

:http-method GET: Gets all the teams with their members
"""

team_post_args = reqparse.RequestParser()
team_post_args.add_argument("team_id", type=int, help="Team id is required", required=True)
team_post_args.add_argument("team_name", type=str, help="Team name is required", required=True)

team_fields = {
        'team_id': fields.Integer,
        'team_name': fields.String,
        }


class TeamResource(Resource):
    @marshal_with(team_fields)
    def get(self):
        result = TeamModel.query.all()
        return result, 200

    @marshal_with(team_fields)
    def post(self):
        args = team_post_args.parse_args()
        team = TeamModel(team_id=args['team_id'], team_name=args['team_name'])
        db.session.add(team)
        db.session.commit()
        return team, 201
