from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def root():
  return "Hello world!"

@app.route('/colours', methods=["POST", "GET"])
def colours(): 
  return "colours"

@app.route('/people', methods=["POST", "GET"])
def people(): 
  return "people"

@app.route('/people/<int:person_id>')
def person(person_id): 
  return f'Person id: {person_id}'
