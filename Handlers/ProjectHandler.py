import sys
from setup import current_path
sys.path.append('../'+current_path)

import json, os, os.path, errno
from flask_restful import fields, marshal_with
from Models.projects_model import Project

project_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'show': fields.Boolean,
    'path': fields.String
}

class ProjectHandler:
    __project_dict = []

    def __init__(self):
        project_dict = []
        for projects in self.__query_all():
            project_dict.append(dict(projects))
        self.__project_dict = project_dict
        
    @marshal_with(project_fields)
    def __query_all(self):
        return Project.query.all()

    def __create(self, json_input, path):
        parent_path = os.path.dirname(path)
        try:
            os.makedirs(parent_path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(parent_path):
                pass
            else: raise

        with open(path, 'w') as json_file:
            json.dump(json_input, json_file)

    def load(self):
        projects = []
        for project in self.__project_dict:
            relative_path = project['path']
            try:
                json_file = open(f"{current_path}/DATAS/{relative_path}")
                print(f"{current_path}/DATAS/{relative_path}")
                p = json.load(json_file)
                json_file.close()
            except FileNotFoundError:
                p = {
                    "name": "<Empty>",
                    "description": "<Empty>",
                    "show": True,
                    "images": [
                        {
                            "name": "<Empty>",
                            "path": "images/404.jpg"
                        }
                    ],
                    "technology": []
                }
                json_file = f"{current_path}/DATAS/{relative_path}"
                self.__create(p, json_file)
            finally:
                projects.append(p)
            
        return projects


    def make(self, json_input: dict, relative_path=''):
        filename = f"{relative_path}/{json_input['name']}.json"
        path = f"{current_path}/DATAS/{filename}"
        self.__create(json_input, path)
        return filename
    
    def erase(self, path):
        destination = f"{current_path}/static/questions/{path}"
        if os.path.exists(destination):
            os.remove(destination)
        return "Removed successfully!"

    def __repr__(self):
        return f"Project : {self.project['name']}"