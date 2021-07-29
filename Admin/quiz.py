import json
import uuid
import collections
from flask import Flask, render_template, url_for, abort, redirect


def teams():
    raise NotImplementedError()

class Question:

	def path_to_file_question(self):
		with open('config.json', 'r') as file:
			file = json.load(file)
		return file["simple_question_path"]
	
	def read_question_file(self):
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'r') as json_file:
			questions_json_file = json.load(json_file)
		return questions_json_file

	def write_questions_json_file(self, questions_json_file):
		path_to_file = self.path_to_file_question()
		with open(path_to_file, 'w') as file_question:
			json.dump(questions_json_file, file_question)

	def show_question(self, question_id):
		#open and read json file
		question_file = self.read_question_file()

		#find question in the json file
		for dic_quest in question_file:
			if dic_quest['id'] == question_id:
				return {
					'status': '200',
					'question': dic_quest['question'],
					'answer': dic_quest['answer'],
					'category':dic_quest['category'],
					'level': dic_quest['level']
				}

		#if the id is not in the json it returns 404
		return {
			'status': '404'
		}

	def show_categories(self):
		#open and read json file
		json_file = self.read_question_file()
		categories = {}
		categories_num = {}
		i = 0

		#find categories in the json file and insert them in a dictionary with seperate keys
		for category in json_file:
			cat = category['category']
			if not(cat is None):
				if not(cat in categories.values()): #check for duplicate categories
					key = "category " + str(i + 1)
					categories[key] = cat
					i = i + 1
					categories_num[cat] = 1
				else:
					if (cat in categories_num):
						categories_num[cat] = categories_num[cat] + 1

		#create a dictionary with nested values
		data = {}
		for item in categories:
			category = categories[item]
			data[category] = {}
			data[category]['number of questions'] =  categories_num[category]

		if categories:
			return{
			"categories" : 	data
			}
		else:
			#in case all the categories are null it returns special message
			return{
			"status" : "No categories have been created"
			}

	def show_all_question(self):
		return self.read_question_file()
	
	def add_question(self, dict_element):
		"rewrite file with the added question and args"
		#generate id
		dict_element['id'] = int(uuid.uuid4())
		
		#check if required args are in dict_element
		for key in ["question", "answer"]:
			if key not in dict_element:
				return {
					'status': f"{key} is required"
				}

		#check if args and exists and if not add None
		for key in ["level", "category"]:
			if key not in dict_element:
				dict_element[key] = None

		#check if level is between 1 and 3
		if dict_element["level"] != None and dict_element["level"] > 3 or dict_element["level"] < 1:
			return {
				"status":"Error level must be between 1 and 3"
			}
		#open, read and write the new question in json file
		questions_json_file = self.read_question_file()
		questions_json_file.append(dict_element)
		self.write_questions_json_file(questions_json_file)

		return {
			'status' : '200 question added'
		}

	def delete_question(self, question_id):
        #read json file
		questions_json_file = self.read_question_file()
		delete_bool = False