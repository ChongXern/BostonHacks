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
        'currWaterAmt': astronaut.currWaterAmt,
        'currPissAmt': astronaut.currPissAmt
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
    if 'currPissAmt' in data:
        astronaut.currPissAmt = data['currPissAmt']

    db.session.commit()

    return jsonify({
        'id': astronaut.id,
        'name': astronaut.name,
        'weight': astronaut.weight,
        'height': astronaut.height,
        'age': astronaut.age,
        'gender': astronaut.gender,
        'currWaterAmt': astronaut.currWaterAmt,
        'currPissAmt': astronaut.currPissAmt
    }), 200

@app.route('/astronaut/<int:astronaut_id>/drink', methods=['POST'])
def drink_water(astronaut_id):
    data = request.get_json()
    amount_drunk = data.get('amount', 0)

    water_record = Astronaut.query.filter_by(id=astronaut_id).first()
    issStation = Iss.query.first() 

    if not water_record or not issStation:
        abort(404, "Astronaut or ISS station not found.")

    if water_record.currWaterAmt < amount_drunk:
        return jsonify({"message": "Not enough water available for this astronaut"}), 400

    if issStation.totalWaterAmt < amount_drunk:
        return jsonify({"message": "Not enough water available in ISS"}), 400

    water_record.currWaterAmt -= amount_drunk
    issStation.totalWaterAmt -= amount_drunk
    db.session.commit()
    
    return jsonify({
        "astronaut_id": astronaut_id,
        "new_currWaterAmt": water_record.currWaterAmt,
        "new_totalWaterAmt": issStation.totalWaterAmt,
    }), 200

@app.route('/astronaut/<int:astronaut_id>/piss', methods=['POST'])
def take_a_piss(astronaut_id):
    data = request.get_json()
    pissAmt = data.get('amount', 0)
    
    astronaut_record = Astronaut.query.filter_by(id=astronaut_id).first()
    issStation = Iss.query.first()
    
    if not astronaut_record or not issStation:
        abort(404, "Astronaut or ISS station not found.")
    
    astronaut_record.currPissAmt += pissAmt
    issStation.pee_log.append({"amount": pissAmt, "timestamp": datetime.now()})
    
    db.session.commit()

    return jsonify({
        "astronaut_id": astronaut_id,
        "new_currPissAmt": astronaut_record.currPissAmt,
        "pee_log": issStation.pee_log
    }), 200

@app.route('/astronaut/<int:astronaut_id>/next_pee_time', methods=['GET'])
def get_next_piss_time(astronaut_id):
    astronaut = Astronaut.query.get_or_404(astronaut_id)
    
    current_time = datetime.now()
    next_piss_time = current_time + timedelta(hours=2)
    
    return jsonify({
        "astronaut_id": astronaut_id,
        "next_piss_time": next_piss_time.isoformat()
    }), 200

