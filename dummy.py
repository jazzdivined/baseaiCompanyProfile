from page_card.card import Card, Deck
from flask import Flask, request, abort

app = Flask(__name__)

this_dict = {}

@app.route("/<int:id>/<string:name>", methods=['GET', 'POST', 'PUT'])
def index(id, name):
    if request.method == 'GET':
        if id is None:
            return this_dict
        else:
            return this_dict[id]
    elif request.method == 'POST':
        if id is None or name is None:
            abort(404)
        else:
            this_dict[id] = name
            return {id: name}


if __name__ == '__main__':
    app.run()
