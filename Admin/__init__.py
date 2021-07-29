from . import projects, quiz, teams


def admin_teams():
    return teams.run()


def admin_quiz():
    return quiz.run()


def admin_projects():
    return projects.run()
