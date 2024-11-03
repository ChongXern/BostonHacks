from flask import Flask, jsonify, request, abort
from models import Iss
from __init__ import *
from flask_cors import CORS  # Import CORS

app = create_app()

# Enable CORS
CORS(app)  # Initialize CORS

'''
#POST - Create Station
@app.route('/iss', methods=['POST'])
def create_station():
    data = request.json
    new_station = Iss(
        totalWaterAmt=data['totalWaterAmt'],
        totalAstronauts=data['totalAstronauts'],
        stationName=data['stationName']
    )
    db.session.add(new_station)
    db.session.commit()
    
    return jsonify({'id': new_station.id, 'stationName': new_station.stationName}), 201

#GET - All Stations
@app.route('/iss', methods=['GET'])
def get_all_stations():
    stations = Iss.query.all()
    return jsonify([
        {
            'id': s.id,
            'stationName': s.stationName,
            'totalAstronauts': s.totalAstronauts,
            'totalWaterAmt': s.totalWaterAmt
        } for s in stations
    ])

#GET - Station by ID
@app.route('/iss/<int:station_id>', methods=['GET'])
def get_station(station_id):
    station = Iss.query.get_or_404(station_id)
    return jsonify({
        'id': station.id,
        'stationName': station.stationName,
        'totalAstronauts': station.totalAstronauts,
        'totalWaterAmt': station.totalWaterAmt
    })

#DELETE - Station by ID
@app.route('/iss/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    station = Iss.query.get_or_404(station_id)
    db.session.delete(station)
    db.session.commit()
    return jsonify({'message': 'ISS Station deleted successfully'}), 200

#PATCH - Update station by ID
@app.route('/iss/<int:station_id>', methods=['PATCH'])
def update_station(station_id):
    station = Iss.query.get_or_404(station_id)
    data = request.get_json()

    if 'totalWaterAmt' in data:
        station.totalWaterAmt = data['totalWaterAmt']
    if 'totalAstronauts' in data:
        station.totalAstronauts = data['totalAstronauts']
    if 'stationName' in data:
        station.stationName = data['stationName']

    db.session.commit()

    return jsonify({
        'id': station.id,
        'totalWaterAmt': station.totalWaterAmt,
        'totalAstronauts': station.totalAstronauts,
        'stationName': station.stationName
    }), 200
    
#PATCH - Consume water by astronaut
@app.route('/iss/<int:station_id>/consume_water', methods=['PATCH'])
def consume_water(station_id):
    station = Iss.query.get_or_404(station_id)
    data = request.get_json()
    
    if 'amount' not in data:
        return jsonify({'error': 'Amount of water to consume must be specified'}), 400
    
    amount = data['amount']
    if station.totalWaterAmt < amount:
        return jsonify({'error': 'Not enough water available'}), 400
    
    station.totalWaterAmt -= amount
    db.session.commit()

    return jsonify({
        'id': station.id,
        'totalWaterAmt': station.totalWaterAmt,
        'stationName': station.stationName
    }), 200
'''
