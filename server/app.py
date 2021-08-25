from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from werkzeug.exceptions import NotFound
import os


app = Flask(__name__)

if (os.getenv('FLASK_ENV') == 'development'):
    cors = CORS(app, resources={r'/*': {"origins": "*"}, r"/api/*": {"origins": "http://127.0.0.1:5000/"}})
else:
    cors = CORS(app, resources={r'/*': {"origins": "*"}, r"/api/*": {"origins": "https://cohort-colours.herokuapp.com/"}})

people_data = [

    {
        "id": 1,
        "name": "daniel",
        "cohort": "morris",
        "fave_colour": {
            "name": "mustard",
            "hex": "#deb326",
            "rgb": {
                "r": 222,
                "g": 179,
                "b": 38
            }
        }
    },
    {
        "id": 2,
        "name": "jawwad",
        "cohort": "morris",
        "fave_colour": {
            "name": "grey",
            "hex": "#808080",
            "rgb": {
                "r": 128,
                "g": 128,
                "b": 128
            }
        }
    },
    {
        "id": 3,
        "name": "max",
        "cohort": "morris",
        "fave_colour": {
            "name": "purple",
            "hex": "#7F00FF",
            "rgb": {
                "r": 127,
                "g": 0,
                "b": 255
            }
        }
    }
]


@app.route('/')
def root():
    if (os.getenv('FLASK_ENV') == 'development'):
        url = 'http://127.0.0.1:5000/people'
    return render_template('index.html', title="Home", content="Cohort Colours", url=url)


@app.route('/people')
def show_colours():
  return render_template('people.html', cohort="morris")


@app.route('/api/colours')
def colours():
    unique_colours = list({person['fave_colour']['name']
                          for person in people_data})
    colours = [{'number_of_favourites': 0, 'name': colour}
               for colour in unique_colours]
    for colour in colours:
        for person in people_data:
            if person['fave_colour']['name'] == colour['name']:
                colour["number_of_favourites"] += 1
    return jsonify({"colours": colours})


@app.route('/api/people', methods=["POST", "GET"])
def people():
    if request.method == "GET":
        return jsonify({"people": people_data})
    elif request.method == "POST":
        new_person_data = request.json
        new_person = {
            "id": people_data[-1]['id'] + 1,
            "name": new_person_data['name'],
            "cohort": new_person_data['cohort'],
            "fave_colour":
            new_person_data["fave_colour"]
        }
        people_data.append(new_person)
        return jsonify({'new_person': new_person})


@app.route('/api/people/<int:person_id>')
def person(person_id):
    if person_id > len(people_data):
        raise NotFound('Person not found - index out of range')
    person = [person for person in people_data if person['id'] == person_id]
    return jsonify({"person": person[0]})


@app.errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({'error': f'{err}'})
