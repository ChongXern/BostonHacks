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
        totalWaterAmt = data['totalWaterAmt'],
        totalAstronauts = data['totalAstronauts'],
        stationName = data['stationName']
    )
    db.session.add(new_station)
    db.session.commit()
    
    return jsonify({'id': new_station.id, 'stationName': new_station.stationName}), 201

#GET - All Stations
@app.route('/iss', methods=['GET'])
def get_all_stations():
    stations = Iss.query.all()
    return jsonify({'id': s.id, 'stationName': s.stationName, 'totalAstronauts': s.totalAstronauts} for s in stations)

#GET - Station by ID
@app.route('/iss/<int:station_id>', methods=['GET'])
def get_station(station_id):
    station = Iss.query.get_or_404(station_id)
    return jsonify({'id': station.id, 'stationName': station.stationName, 'totalAstronauts': station.totalAstronauts})

#DELEET - Station by ID
@app.route('/iss/<int:station_id>', methods=['DELETE'])
def delete_station(station_id):
    station = Iss.query.get_or_404(station_id)
    db.session.delete(station)
    db.session.commit()
    return jsonify({'message': 'ISS Station deleted successfully'}), 200
'''
