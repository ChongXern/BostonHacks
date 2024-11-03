from flask import Flask, jsonify, request, abort
from models import Astronaut
from __init__ import *

app = create_app()


#POST - Create Astronaut
@app.route('/astronauts', methods=['POST'])
def create_astronaut():
    data = request.json
    new_astronaut = Astronaut(
        name=data['name'],
        weight=data['weight'],
        height=data['height'],
        age=data['age'],
        gender=data['gender']
    )
    db.session.add(new_astronaut)
    db.session.commit()
    
    return jsonify({
        'id': new_astronaut.id,
        'name': new_astronaut.name,
        'weight': new_astronaut.weight,
        'height': new_astronaut.height,
        'age': new_astronaut.age,
        'gender': new_astronaut.gender
    }), 201
    #return jsonify({'id': new_astronaut.id, 'name': new_astronaut.name}), 201

#GET - Astonaut by ID
@app.route('/astronauts/<int:astronaut_id>', methods=['GET'])
def get_astronaut(astronaut_id):
    astronaut = Astronaut.query.get_or_404(astronaut_id)
    return jsonify({
        'id': astronaut.id,
        'name': astronaut.name,
        'weight': astronaut.weight,
        'height': astronaut.height,
        'age': astronaut.age,
        'gender': astronaut.gender
    })
    #return jsonify({'id': astronaut.id, 'name': astronaut.name, 'weight': astronaut.weight})

#PATCH - Update astronaut by ID
@app.route('/astronauts/<int:astronaut_id>', methods=['PATCH'])
def update_astronaut(astronaut_id):
    astronaut = Astronaut.query.get_or_404(astronaut_id)
    data = request.get_json()

    if 'name' in data:
        astronaut.name = data['name']
    if 'weight' in data:
        astronaut.weight = data['weight']
    if 'height' in data:
        astronaut.height = data['height']
    if 'age' in data:
        astronaut.age = data['age']
    if 'gender' in data:
        astronaut.gender = data['gender']

    db.session.commit()

    return jsonify({
        'id': astronaut.id,
        'name': astronaut.name,
        'weight': astronaut.weight,
        'height': astronaut.height,
        'age': astronaut.age,
        'gender': astronaut.gender
    }), 200
