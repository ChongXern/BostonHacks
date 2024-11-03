from computation_utils import *
#import computeIdealWaterIntake

currDay = 0
totalDays = 180

def main():
    age, weight, _, gender, exerciseTime = inputUserData()
    idealWaterIntake = computeIdealWaterIntake(age, weight, gender, exerciseTime)
    print("Ideal Water Intake:", idealWaterIntake, "ml")
    
    hourInterval = computeHourIntervalToDrink(idealVol=idealWaterIntake)
    totalPouches = computeTotalPouches(idealVol=idealWaterIntake)
    print(f"hourInterval is {hourInterval} for {totalPouches} pouches")
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
