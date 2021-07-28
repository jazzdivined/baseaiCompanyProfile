from flask import Flask, render_template, url_for, abort, redirect, request
import mysql.connector
import json

"""
:http-method POST: Adds a Team with it's members
:http-method GET: Gets all the teams with their members
:http-method UPDATE: 
"""


class Team:

    def __init__(self, team_id=None, team_name=None):
        if team_id is None or team_name is None:
            pass
        else:
            self.id = team_id
            self.name = team_name

    def get_team(self):
        team_dict = {
            'team_id': self.id,
            'team_name': self.name
        }
        return team_dict


def run():
    id = None
    if id is not None:
        if request.method == "GET":
            teams = get_teams()
            for team in teams:
                if team['team_id'] == id:
                    teams_json = json.dumps(teams)
                    return str(teams_json)

            error = {
                        "title": "Not Found",
                        "status": 404,
                    }
            return json.dumps(error)

        elif request.method == "POST":
            abort(404)

    else:
        if request.method == "GET":
            teams = get_teams()
            teams_json = json.dumps(teams)
            return str(teams_json)

        elif request.method == "POST":
            team_input = request.get_json()
            team_id = int(team_input['team_id'])
            team_name = str(team_input['team_name'])
            post_teams(team_id, team_name)
            redirect('/admin/api/teams/')
            return team_input


def get_teams():
    teams = []
    db = mysql.connector.connect(
        host="base-ai.com",
        user="baseaico_jazz",
        passwd="Petraguy123",
        database="baseaico_teams_test"
    )
    teams_cursor = db.cursor(buffered=True)
    teams_cursor.execute("SELECT * FROM teams;")
    for key, value in teams_cursor.fetchall():
        teams.append(Team(key, value).get_team())
    db.close()
    return teams


def post_teams(id, name):
    db = mysql.connector.connect(
        host="base-ai.com",
        user="baseaico_jazz",
        passwd="Petraguy123",
        database="baseaico_teams_test"
    )
    teams_cursor = db.cursor(buffered=True)
    team_id = id
    team_name = name
    teams_cursor.execute(f"INSERT INTO teams (team_id, team_name) VALUES({team_id}, \'{team_name}\')")
    db.commit()
    db.close()
