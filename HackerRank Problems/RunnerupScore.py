n = int(input())
arr = map(int, input().split())
newList = list(arr)


def findRunnerUpScore(newArray):
    maxim = max(newArray)
    newList.remove(maxim)
    newMaxim = max(newArray)
    if maxim == newMaxim:
        return findRunnerUpScore(newArray)
    else:
        return newMaxim


print(findRunnerUpScore(newList))
# print(maxim)
