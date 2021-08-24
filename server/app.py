from flask import Flask, jsonify, request

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
  if request.method == "GET":
    return jsonify({ "people": people_data })
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
    return jsonify({ 'new_person': new_person })

@app.route('/people/<int:person_id>')
def person(person_id): 
  person = [person for person in people_data if person['id'] == person_id]
  return jsonify({ "person": person[0]})
