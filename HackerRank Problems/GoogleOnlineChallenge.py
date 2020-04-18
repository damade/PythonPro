from time import time

from memory_profiler import profile

fruitObjects = {}


def timePerformance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"it took {t2-t1} ms")
        return result

    return wrapper


def average(List):
    count = 0
    for i in range(len(List)):
        count += List[i]
    averageOfIt = count / len(List)
    return averageOfIt


@timePerformance
@profile()
def giveMe(fruitObjects):
    sorted(fruitObjects)
    for fruits in sorted(fruitObjects.keys()):
        theNewList = fruitObjects[fruits]
        minPrice = min(theNewList)
        maxPrice = max(theNewList)
        averagePrice = average(theNewList)
        finalList = [minPrice, maxPrice, averagePrice]
        # newFruitObjects[fruits] = finalList
        print(f"{fruits} {minPrice} {maxPrice} {averagePrice}")
    return

n = int(input().strip())
for i in range(n):
    try:
        eachItems = input().split(" ")
        fruit = eachItems[0]
        price = int(eachItems[1])
        if fruit in fruitObjects.keys():
            fruitObjects[fruit] += [price]
        else:
            theList = []
            theList += [price]
            fruitObjects[fruit] = theList
    except:
        pass
sorted(fruitObjects)

giveMe(fruitObjects)
# for fruits in averageFruitObject.keys():

# pprint.pprint(fruitObjects)
#pprint.pprint(giveMe(fruitObjects))
