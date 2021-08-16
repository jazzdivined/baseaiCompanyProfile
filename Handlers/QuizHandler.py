import sys
from setup import current_path
sys.path.append('../'+current_path)

from Models.Quiz import QuizModel
from flask_restful import Resource, fields, marshal_with, reqparse
import json, os, os.path, errno

question_fields = {
        'question_id': fields.Integer,
        'question_path': fields.String,
        }


class QuizHandler:
	__question_dict = []

	def __init__(self):
		question_dict = []
		# This constructor is to query all the questions
		for questions in self.__query_all():
			question_dict.append(dict(questions))
		self.__question_dict = question_dict

	@marshal_with(question_fields)
	def __query_all(self):
		return QuizModel.query.all()
			
	def __create(self, json_input, path):
		parent_path = os.path.dirname(path)
		try:
			os.makedirs(parent_path)
		except OSError as exc: # Python >2.5
			if exc.errno == errno.EEXIST and os.path.isdir(parent_path):
				pass
			else: raise

		# This is a private method to save a question to a file
		with open(path, 'w') as json_file:
			json.dump(json_input, json_file)

	def make(self, json_input: dict, relative_path=''):
		filename = f"{relative_path}/{json_input['question_id']}.json"
		path = f"{current_path}/static/questions/{filename}"
		self.__create(json_input, path)
		return filename

	def load(self):
		questions = []
		for question in self.__question_dict:
			relative_path = question['question_path']
			try:
				json_file = open(f"{current_path}/static/questions/{relative_path}", 'r') 
				q = json.load(json_file)
				json_file.close()
				    
			except FileNotFoundError:
				q = {
				'question_id': int(question['question_id']),
				'question': '<Empty>',
				'option': []
				}
				json_file = f"{current_path}/static/questions/{relative_path}"
				self.__create(q, json_file)

			finally:
				questions.append(q)

		return questions
		
	def erase(self, path):
		destination = f"{current_path}/static/questions/{path}"
		if os.path.exists(destination):
			os.remove(destination)
		return "Removed successfully!"

