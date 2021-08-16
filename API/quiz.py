import sys
from setup import db, current_path
sys.path.append('../'+current_path)

from Handlers.QuizHandler import QuizHandler
from flask_restful import Resource, fields, marshal_with, reqparse
from Models.Quiz import QuizModel
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

question_fields = {
    'question_id': fields.Integer,
    'question_path': fields.String,
}

question_post_args = reqparse.RequestParser()
question_post_args.add_argument("question_id", type=int, help="question id is required", required=True)
question_post_args.add_argument("question", type=str, help="question is required", required=True)
question_post_args.add_argument("option", type=str, action='append', help="if option is not required, write '[]' without the (').", required=False)

question_delete_args = reqparse.RequestParser()
question_delete_args.add_argument("question_id", type=int, help="question id is required", required=True)

class QuizResource(Resource):
    
    def __init__(self) -> None:
        self.handler = QuizHandler()

    def get(self):
        
        result = self.handler.load()
        return result, 200

    def post(self):

        args = question_post_args.parse_args()
        path = self.handler.make(args)
        question = QuizModel(question_id=args['question_id'], question_path=path)
        db.session.add(question)
        db.session.commit()
        return args

    def delete(self):
        
        args = question_delete_args.parse_args()
        id = args['question_id']
        
        get_dict = marshal_with(question_fields)(self.__get_dict_from_id)
        dict_from_id = get_dict(id)
        
        path = dict_from_id['question_path']
        db.session.delete(self.__get_dict_from_id(id))
        db.session.commit()

        return self.handler.erase(path)
        
    @staticmethod
    def __get_dict_from_id(id):
        return QuizModel.query.filter_by(question_id=id).first()
        


