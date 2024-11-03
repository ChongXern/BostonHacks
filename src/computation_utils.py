# Import db and User model
from backend import db, User, create_app
from backend import Astronaut, Iss
import math

recyclingRate = 0.98  # 98% of pee becomes water
currentWaterAvailable = 900000  # ml
totalPeeGenerated = 0
PissOutputRate = 0.6
totalWaterConsumed = 0
isHydrated = 1
totalDays = 180
totalAstronauts = 5

app = create_app()

# for terminal use
def inputUserData():
    name = input("Name: ")
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    age = int(input("Age: "))
    gender = input("Gender: ")
    activityTime = int(input("Activity time: "))  # minutes
    
    with app.app_context():
        new_astronaut = Astronaut(name=name, age=age, weight=weight, height=height, gender=gender, exerciseTime=activityTime)
        db.session.add(new_astronaut)
        db.session.commit()
    
    print("User data saved to the database.")
    return age, weight, height, gender, activityTime


def computeIdealWaterIntake(astronaut: Astronaut):
    baseIntake = astronaut.weight
    if astronaut.gender.lower() == "male":
        baseIntake *= 35
    else:
        baseIntake *= 31
    if astronaut.age > 50:
        baseIntake *= 0.95
    
    #exercising
    baseIntake += (astronaut.exerciseTime / 30) * 300

    return baseIntake

def getPissOutputPercentage(activityTime):
    if activityTime < 30:
        return 0.7
    if activityTime < 120:
        return 0.7 - (0.2 / 90) * (activityTime - 30)
    else: 
        return 0.5

def logWaterInput(iss: Iss, astronaut: Astronaut, volume):
    #global totalWaterConsumed, currentWaterAvailable
    astronaut.currWaterAmt += volume
    iss.totalWaterAmt += volume
    # totalWaterConsumed += volume
    # currentWaterAvailable -= volume

def logPissOutput(activityTime, recyclingRate=0.8):
    #global totalPeeGenerated, currentWaterAvailable
    PissOutput = totalWaterConsumed * getPissOutputPercentage(activityTime)
    totalPeeGenerated += PissOutput
    currentWaterAvailable += PissOutput * recyclingRate
    
def computeTotalPouches(idealVol, pouchSize=300):
    global isHydrated
    isHydrated ^= 1
    return (idealVol + (pouchSize - 1) * isHydrated) // pouchSize

def computeHourIntervalToDrink(idealVol, sleepHours=6, pouchSize=300):
    totalPouches = idealVol // pouchSize
    return max(1, (24 - sleepHours + totalPouches - 1) // totalPouches)

def computeWaterIntakeTopDown(currentWaterAvailable, totalAstronauts, totalDays):
    

def computeChangesAfterDay():
    global totalDays
    totalDays += 1
    # re-ration water supply