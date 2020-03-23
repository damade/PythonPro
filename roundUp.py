import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve():

    if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())

        tax_percent = int(input())
        totalCost = (meal_cost + ((meal_cost * tip_percent)/100) + ((meal_cost*tax_percent)/100))
        print(roundValues(totalCost))
        return
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