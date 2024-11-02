from __init__ import db
import datetime
import models
from water import Water

class Astronaut(db.Model):
    __tablename__ = 'astronaut'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    # water_id = db.Column(db.Integer, models.ForeignKey("app.Model"))
    dob = db.Column(db.datetime, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
    water = db.relationship(Water, back_populates='author') #fix l8r
    
    def __repr__(self):
        return f'<Astronaut name: {self.name}>'
    
    def __init__(self, name="John Doe", dob=datetime.date.today, weight=70, height=160, age=40):
        self.name = name
        self.dob = dob
        self.weight = weight
        self.height = height
        self.age = age
