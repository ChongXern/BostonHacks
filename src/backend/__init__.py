import os
import json
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
from extensions import db  # Import db from extensions
from models.astronaut import Astronaut  # Ensure that Astronaut is defined in models.py

from models.astronaut import Astronaut
from models.iss import Iss
from models.water import Water

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    activity_time = db.Column(db.Integer, nullable=False)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Enable CORS
    CORS(app)  # Initialize CORS

    with app.app_context():
        db.create_all()  # Creates the tables

    # Define the main route
    @app.route('/')
    def home():
        return "Welcome to the User API!"

    # Define astronaut-related routes directly in create_app

    # POST - Create Astronaut
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
        
    # GET - All astronauts
    @app.route('/astronauts', methods=['GET'])
    def get_astronauts():
        astronauts = Astronaut.query.all()  # Fetch all astronauts from the database
        return jsonify([{
            'id': astronaut.id,
            'name': astronaut.name,
            'weight': astronaut.weight,
            'height': astronaut.height,
            'age': astronaut.age,
            'gender': astronaut.gender
        } for astronaut in astronauts]), 200


    # GET - Astronaut by ID
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

    # PATCH - Update astronaut by ID
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

    # POST - Create Station
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

    # GET - Station by ID
    @app.route('/iss/<int:station_id>', methods=['GET'])
    def get_station(station_id):
        station = Iss.query.get_or_404(station_id)
        return jsonify({'id': station.id, 'stationName': station.stationName, 'totalAstronauts': station.totalAstronauts})

    # DELETE - Station by ID
    @app.route('/iss/<int:station_id>', methods=['DELETE'])
    def delete_station(station_id):
        station = Iss.query.get_or_404(station_id)
        db.session.delete(station)
        db.session.commit()
        return jsonify({'message': 'ISS Station deleted successfully'}), 200

    return app
