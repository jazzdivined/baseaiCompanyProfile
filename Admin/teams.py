import requests
from flask import request

def run():
    team_obj = Teams('http://127.0.0.1:5000/admin/api/teams/')
    if request.method == "POST":
        data = request.form
        return team_obj.add_teams(dict(data)) 
    
    elif request.method == "GET":
        return team_obj.show_teams()

    elif request.method == "DELETE":
        data = request.form
        return team_obj.delete_teams(dict(data))

class Teams():
    """Implements a custom authentication scheme."""
    def __init__(self, link):
        self.api_link = link

    def show_teams(self):
        # Making a GET request
        r = requests.get(self.api_link)
        # success code - 200
        # print content of request
        return r.content
		
    def add_teams(self, dict_element):
        # Making a POST request
        r = requests.post(self.api_link, data = dict_element)
        return str(r.status_code)

    def delete_teams(self, team_id):
        # Making a DELETE request
        r = requests.delete(self.api_link, data = team_id)
        return str(r.status_code)

    def update_teams(self): 
        # Making a PUT request
        r = requests.put(self.api_link)
        print(r)