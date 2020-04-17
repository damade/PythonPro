import pprint

fruitObjects = {}
n = int(input().strip())
for i in range(n):
    try:
        eachItems = input().split(" ")
        fruit = eachItems[0]
        price = eachItems[1]
        if fruit in fruitObjects.keys():
            fruitObjects[fruit] += [price]
        else:
            theList = []
            theList += [price]
            fruitObjects[fruit] = theList
    except:
        pass
pprint.pprint(fruitObjects)
