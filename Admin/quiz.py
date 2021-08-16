import requests
from flask import request

def run():
    question_obj = Question('http://127.0.0.1:5000/admin/api/quiz/')
    if request.method == "POST":
        data = request.form
        return question_obj.add_question(dict(data)) 
    
    elif request.method == "GET":
        return question_obj.show_question()

    elif request.method == "DELETE":
        data = request.form
        return question_obj.delete_question(data)

class Question():
    """Implements a custom authentication scheme."""
    def __init__(self, link):
        self.api_link = link

    def show_question(self) :
        # Making a GET request
        r = requests.get(self.api_link)
        # success code - 200
        # print content of request
        return r.content
		
    def add_question(self, dict_element):
        # Making a POST request
        r = requests.post(self.api_link, data=dict_element)
        return str(r.status_code)

    def delete_question(self, question_id):
        # Making a DELETE request
        r = requests.delete(self.api_link, data = question_id)
        return str(r.status_code)

    def update_question(self): #For future updates
        # Making a PUT request
        r = requests.put(self.api_link)
        print(r)
        return r.status_code