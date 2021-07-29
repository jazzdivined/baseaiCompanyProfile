from . import teams, projects, quiz, members


def api_teams():
    return teams.TeamResource


def api_members():
    return members.MemberResource


def api_projects():
    return projects.run()


def api_quiz():
    return quiz.QuizResource
