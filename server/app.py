from flask import Flask, jsonify


app = Flask(__name__)

people_data = [
  {
    "id": 1,
    "name": "daniel",
    "cohort": "morris",
    "fave_colour": {
        "name": "mustard",
        "hex:": "#deb326",
        "rgb": "222, 179, 38"
    }
  },
  {
      "id": 2,
      "name": "jawwad",
      "cohort": "morris",
      "fave_colour": {
          "name": "grey",
          "hex:": "#808080",
          "rgb": "128,128,128"
      }
  },
  {
      "id": 3,
      "name": "max",
      "cohort": "morris",
      "fave_colour": {
          "name": "purple",
          "hex:": "#7F00FF",
          "rgb": "127, 0, 255"
      }
  }
]

next_id = 4

@app.route('/')
def root():
  return "Hello world!"

@app.route('/colours')
def colours(): 
  unique_colours = list({person['fave_colour']['name'] for person in people_data})
  colours = [{'number_of_favourites': 0, 'name': colour} for colour in unique_colours]
  for colour in colours:
    for person in people_data:
      if person['fave_colour']['name'] == colour['name']:
        colour["number_of_favourites"] += 1
  return jsonify({ "colours": colours })

@app.route('/people', methods=["POST", "GET"])
def people(): 
  return jsonify({ "people": people_data })

@app.route('/people/<int:person_id>')
def person(person_id): 
  return jsonify({ "person": f'Person id: {person_id}' })
