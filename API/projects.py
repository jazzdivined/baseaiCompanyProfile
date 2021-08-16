
from flask_restful import Resource, reqparse, fields, marshal_with
from Models.projects_model import *
from Handlers.ProjectHandler import ProjectHandler

postParser = reqparse.RequestParser()
postParser.add_argument("name", type=str, help="The name of the Project", required=True)
postParser.add_argument("description", type=str, help="The description of the Project", required=True)
postParser.add_argument("show", type=bool, help="Want to show it in the website", required=True)
postParser.add_argument("images", type=list, help="image for the project", required=True)
postParser.add_argument("technology", type=list, help="technology the project", required=True)

putParser = reqparse.RequestParser()

deleteParser = reqparse.RequestParser()
deleteParser.add_argument("id", type=int, help="question id is required", required=True)

delete_field = {
    'id': fields.Integer,
    'name': fields.String,
    'show': fields.Boolean,
    'path': fields.String
}

class ProjectResource(Resource):    
    def __init__(self) -> None:
        self.handler = ProjectHandler()

    def get(self):
        result = self.handler.load()
        return result
    
    def post(self):
        args = postParser.parse_args()
        path = self.handler.make(args, 'project')
        project = Project(  name=args['name'], 
                                show=args["show"], 
                                path=path
                                )
        db.session.add(project)
        db.session.commit()

    def put(self):
        args = putParser.parse_args()
        #new_project = Project(  name=args['name'], 
        #                        show=args["show"], 
        #                        path=args['path']
        #                        )
        #db.session.add(new_project)
        #db.session.commit()
        print(args)
        return args

    def delete(self):
        
        args = deleteParser.parse_args()
        id = args['id']
        
        get_dict = marshal_with(delete_field)(self.__get_dict_from_id)
        dict_from_id = get_dict(id)
        
        path = dict_from_id['path']
        db.session.delete(self.__get_dict_from_id(id))
        db.session.commit()

        return self.handler.erase(path)

    @staticmethod
    def __get_dict_from_id(id):
        return Project.query.filter_by(id=id).first()
        

        
        
        
