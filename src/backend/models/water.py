from __init__ import db
from backend.models.astronaut import Astronaut
import datetime
import models

class Water(db.Model):
    __tablename__ = 'water'
    id = db.Column(db.Integer, primary_key=True)
    personId = db.Column(db.Integer, models.ForeignKey(Astronaut), nullable=False)
    recyclingRate = db.Column(db.Float, nullable=False)
    currWaterAmt = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Water ID: {self.id}>'
    
    def __init__(self, personId=-1, currWaterAmt = 900000, recyclingRate=0.98):
        self.personId = personId
        self.recyclingRate = recyclingRate
        self.currWaterAmt = currWaterAmt