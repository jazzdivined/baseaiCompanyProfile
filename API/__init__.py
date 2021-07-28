from . import teams, projects, quiz


def api_teams():
    return teams.run()


def api_quiz():
    return projects.run()


def api_projects():
    return quiz.run()
