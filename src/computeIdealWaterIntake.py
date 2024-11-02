recyclingRate = 0.98 # 98% of piss becomes water
currentWaterAvailable = 900000 # ml
totalPeeGenerated = 0
peeOutputRate = 0.6
totalWaterConsumed = 0

#for terminal use
def inputUserData():
    age = int(input("Age: "))
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    gender = input("Gender: ")
    #activity = input("Activity: ")
    activityTime = int(input("Activity time: ")) # minutes
    
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

def logPeeOutput():
    global totalPeeGenerated, currentWaterAvailable
    peeOutputPercentage = getPeeOutputPercentage()
    peeOutput = totalWaterConsumed * peeOutputPercentage
    totalPeeGenerated += peeOutput
    currentWaterAvailable += peeOutput * recyclingRate

def main():
    age, weight, _, gender, exerciseTime = inputUserData()
    idealWaterIntake = computeIdealWaterIntake(age, weight, gender, exerciseTime)
    print(idealWaterIntake)
    while (currentWaterAvailable > 0):
        logWaterInput(10)
        logPeeOutput()

if __name__ == '__main__':
    main()