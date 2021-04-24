from time import time


def timePerformance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} ms")
        return result

    return wrapper

"""Given an unsorted array nums, write a function to find the start and end positions of a given number
val in an array after sorting it. Your function should return [-1,-1] if val isn't in the array.

Examples: nums = [0,8,-2,5,0] and val = 0 , your function return [1,2]"""

nums = [9, 29, 2, 4, 65, 64, 2, 6, 9, 0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 9763, 24, 25]

val = int(input("What is the number: "))

@timePerformance
def getThePositions(numberList):
    default = [-1, -1]
    defaultCounter = 0
    numberList.sort()
    for i in range(0, len(numberList)):
        if numberList[i] == val:
            if defaultCounter > 0:
                default[1] = i
            else:
                default[0] = i
                default[1] = i
                defaultCounter += 1

    return default

print(getThePositions(nums))