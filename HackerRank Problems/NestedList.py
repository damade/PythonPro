myArr = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    myArr[name] = score


def findSecondLowest(newDict):
    sorted(newDict.values())
    newArr = []
    for v in sorted(newDict.values()):
        newArr += [v]
    secondHighestMark = newArr[1]
    listOfKeys = [key for (key, value) in newDict.items() if value == secondHighestMark]
    return listOfKeys


thatList = findSecondLowest(myArr)
for items in sorted(thatList):
    print(items)
