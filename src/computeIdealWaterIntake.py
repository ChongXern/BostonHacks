import math

recyclingRate = 0.98  # 98% of pee becomes water
currentWaterAvailable = 900000  # ml
totalPeeGenerated = 0
peeOutputRate = 0.6
totalWaterConsumed = 0
isHydrated = 1

# for terminal use
def inputUserData():
    age = int(input("Age: "))
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    gender = input("Gender: ")
    activityTime = int(input("Activity time: "))  # minutes
    
    return age, weight, height, gender, activityTime

def computeIdealWaterIntake(age, weight_kg, gender, activityTime):
    baseIntake = weight_kg
    if gender == "male": 
        baseIntake *= 35
    else: 
        baseIntake *= 31

    if age > 50: 
        baseIntake *= 0.95
    
    if activityTime >= 30: 
        baseIntake += (activityTime / 30) * 350

    return baseIntake

def getPeeOutputPercentage(activityTime):
    if activityTime < 30:
        return 0.7
    if activityTime < 120:
        return 0.7 - (0.2 / 90) * (activityTime - 30)
    else: 
        return 0.5

def logWaterInput(volume):
    global totalWaterConsumed, currentWaterAvailable
    totalWaterConsumed += volume
    currentWaterAvailable -= volume

def logPeeOutput(activityTime):
    global totalPeeGenerated, currentWaterAvailable
    peeOutputPercentage = getPeeOutputPercentage(activityTime)
    peeOutput = totalWaterConsumed * peeOutputPercentage
    totalPeeGenerated += peeOutput
    currentWaterAvailable += peeOutput * recyclingRate
    
def computeTotalPouches(idealVol, pouchSize=300):
    global isHydrated
    isHydrated ^= 1
    return (idealVol + (pouchSize - 1) * isHydrated) // pouchSize

def computeHourIntervalToDrink(idealVol, sleepHours=6, pouchSize=300):
    totalPouches = idealVol // pouchSize
    return max(1, (24 - sleepHours + totalPouches - 1) // totalPouches)

def main():
    age, weight, _, gender, exerciseTime = inputUserData()
    idealWaterIntake = computeIdealWaterIntake(age, weight, gender, exerciseTime)
    print("Ideal Water Intake:", idealWaterIntake, "ml")
    
    hourInterval = computeHourIntervalToDrink(idealVol=idealWaterIntake)
    totalPouches = computeTotalPouches(idealVol=idealWaterIntake)
    print(f"hourInterval is {hourInterval} for {totalPouches}")
    print(totalPouches * 300 - idealWaterIntake)
    
    '''while currentWaterAvailable > 0 and totalWaterConsumed < idealWaterIntake:
        logWaterInput(10)
        logPeeOutput(exerciseTime)

        if totalWaterConsumed >= idealWaterIntake:
            break

    print("Total Water Consumed:", totalWaterConsumed, "ml")
    print("Total Pee Generated:", totalPeeGenerated, "ml")
    print("Current Water Available:", currentWaterAvailable, "ml")'''

if __name__ == '__main__':
    main()
