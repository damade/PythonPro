# Complete the solve function below.

def roundValues(value):
    newValue = int(value * 10)
    newValueString = str(newValue)
    lastValue = int(newValueString[(len(newValueString))-1])
    if (0 <= lastValue < 5):
        roundedFig = int(newValueString[0:(len(newValueString))-1])
        return roundedFig
    elif(5 <= lastValue <= 9):
        roundedFig = int(newValueString[0:(len(newValueString))-1]) + 1
        return roundedFig
    else:
        return
#solve()
print(roundValues(12.505))