from __init__ import db
import datetime
import models

from astronaut import Astronaut

class HistoryItem(db.Model):
    __tablename__ = 'history_item'
    id = db.Column(db.Integer, primary_key=True)
    astronautId = db.Column(db.Integer, models.ForeignKey(Astronaut), nullable=False)
    timestamp = db.Column(db.datetime, nullable=False)
    isDrink = db.Column(db.Boolean, nullable=False)
    isPiss = db.Column(db.Boolean, nullable=False)
    astronaut = db.relationship('Astronaut', back_populates='history_items')
    
    def __repr__(self):
        return f'<ISS ID: {self.id}>'
    
    def __init__(self, totalWaterAmt=900000, totalAstronauts=5):
        self.totalWaterAmt = totalWaterAmt
        self.totalAstronauts = totalAstronauts
