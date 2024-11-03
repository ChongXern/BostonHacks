from flask import Flask, jsonify, request, abort
from models.astronaut import Astronaut
from models.iss import Iss
#from models.water import Water
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
        'gender': astronaut.gender,
        'currWaterAmt': astronaut.currWaterAmt
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
    if 'currWaterAmt' in data:
        astronaut.currWaterAmt = data['currWaterAmt']

    db.session.commit()

    return jsonify({
        'id': astronaut.id,
        'name': astronaut.name,
        'weight': astronaut.weight,
        'height': astronaut.height,
        'age': astronaut.age,
        'gender': astronaut.gender,
        'currWaterAmt': astronaut.currWaterAmt
    }), 200

@app.route('/astronaut/<int:astronaut_id>/drink', methods=['POST'])
def drink_water(astronaut_id):
    data = request.get_json()
    amount_drunk = data.get('amount', 0)

    water_record = Water.query.filter_by(personId=astronaut_id).first()
    iss_station = Iss.query.first() 

    if not water_record or not iss_station:
        abort(404, "Water record or ISS station not found.")

    if water_record.currWaterAmt < amount_drunk or iss_station.totalWaterAmt < amount_drunk:
        return jsonify({"message": "Not enough water available"}), 400

    water_record.currWaterAmt -= amount_drunk
    iss_station.totalWaterAmt -= amount_drunk

    db.session.commit()

    return jsonify({
        "astronaut_id": astronaut_id,
        "new_currWaterAmt": water_record.currWaterAmt,
        "new_totalWaterAmt": iss_station.totalWaterAmt,
    }), 200
