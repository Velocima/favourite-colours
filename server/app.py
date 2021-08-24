from flask import Flask, jsonify


app = Flask(__name__)

people_data = []

@app.route('/')
def root():
  return "Hello world!"

@app.route('/colours', methods=["POST", "GET"])
def colours(): 
  colours = []
  return jsonify({ "colours": colours })

@app.route('/people', methods=["POST", "GET"])
def people(): 
  return jsonify({ "people": people_data })

@app.route('/people/<int:person_id>')
def person(person_id): 
  return jsonify({ "person": f'Person id: {person_id}' })

