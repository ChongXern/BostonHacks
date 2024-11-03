from __init__ import db
import datetime
import models

class Iss(db.Model):
    __tablename__ = 'iss'
    id = db.Column(db.Integer, primary_key=True)

    totalWaterAmt = db.Column(db.Integer, nullable=False)
    totalPissAmt = db.Column(db.Integer, nullable=False)
    totalAstronauts = db.Column(db.Integer, nullable=False)
    stationName = db.Column(db.String(100), nullable=False) #Adjust length as needed
    missionDuration = db.Column(db.Integer, nullable=False)

    pissLog = []
    
    def __repr__(self):
        return f'<ISS ID: {self.id}>'

    def __init__(self, totalWaterAmt=900000, totalAstronauts=5, stationName="Default Station", missionDuration=180):
        self.totalWaterAmt = totalWaterAmt
        self.totalAstronauts = totalAstronauts
        self.stationName = stationName
        self.missionDuration = missionDuration

    def recycle_piss(self):
        now = datetime.now()
        reclaimed_water = 0
        self.pissLog = [entry for entry in self.pissLog if (now - entry['timestamp']).days < 8 or (reclaimed_water := reclaimed_water + entry['amount'] * 0.98) == 0]
        self.totalWaterAmt += reclaimed_water
        db.session.commit()
