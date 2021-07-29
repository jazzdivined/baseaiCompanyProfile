import sys

sys.path.append('../baseaiCompanyProfile')

from flask_restful import Resource, fields, marshal_with, reqparse
from Models.Member import MemberModel
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
:var <List of members>: {
            'member_id': <id>,
            'member_name': <name>,
            'major': <major>,
            'motto': <motto>,
            'img_path': <img_path>,
        }

:http-method GET: Gets all the teams with their members
:http-method UPDATE: TBA
"""

member_put_args = reqparse.RequestParser()
member_put_args.add_argument("member_id", type=int, help="Member id is required", required=True)
member_put_args.add_argument("member_name", type=str, help="Member name is required", required=True)
member_put_args.add_argument("major", type=str, help="Major is required", required=True)
member_put_args.add_argument("motto", type=str, help="Motto is required", required=False)
member_put_args.add_argument("img_path", type=str, help="Image Path is required", required=False)
#member_put_args.add_argument("team_id", type=int, help="Team id is required", required=True)

member_fields = {
            'member_id': fields.Integer,
            'member_name': fields.String,
            'major': fields.String,
            'motto': fields.String,
            'img_path': fields.String,
            }


class MemberResource(Resource):
    @marshal_with(member_fields)
    def get(self, id):
        result = MemberModel.query.filter_by(team_id=id).all()
        return result, 200

    @marshal_with(member_fields)
    def put(self, id):
        args = member_put_args.parse_args()
        test_id = args['member_id']
        print(test_id)
        member = MemberModel(member_id= test_id,member_name=args['member_name'],major=args['major'],motto=args['motto'],img_path=args['img_path'],team_id=id)
        db.session.add(member)
        db.session.commit()
        return member, 201
