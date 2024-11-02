from __init__ import db
import datetime
import models

class Iss(db.Model):
    __tablename__ = 'iss'
    id = db.Column(db.Integer, primary_key=True)

    totalWaterAmt = db.Column(db.Integer, nullable=False)
    totalAstronauts = db.Column(db.Integer, nullable=False)
    stationName = db.Column(db.String(100), nullable=False)  # Adjust length as needed

    def __repr__(self):
        return f'<ISS ID: {self.id}>'
    
    def __init__(self, totalWaterAmt=900000, totalAstronauts=5, stationName="Default Station"):
        self.totalWaterAmt = totalWaterAmt
        self.totalAstronauts = totalAstronauts
        self.stationName = stationName
