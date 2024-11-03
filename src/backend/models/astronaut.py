from __init__ import db
import datetime
import models

class Astronaut(db.Model):
    __tablename__ = 'astronaut'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    # water_id = db.Column(db.Integer, models.ForeignKey("app.Model"))
    # dob = db.Column(db.datetime, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    exerciseTime = db.Column(db.Integer, nullable=False) #in minutes
    currWaterAmt = db.Column(db.Integer, nullable=False)
    currPissAmt = db.Column(db.Integer, nullable=False)
    
    #water = db.relationship(Water, back_populates='author') #fix l8r
    
    def __repr__(self):
        return f'<Astronaut name: {self.name}>'
    
    def __init__(self, name="John Doe", dob=datetime.date.today(), weight=70, height=160, age=40, gender="male", currWaterAmt=350, currPissAmt=0):
        self.name = name
        self.dob = dob
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.currWaterAmt = currWaterAmt
        self.currPissAmt = currPissAmt
