class Difference:

    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        arr = self.__elements
        newArr = sorted(arr)
        a = newArr[0]
        b = newArr[(len(arr)) - 1]
        maxDiff = b - a
        self.maximumDifference = maxDiff
        return self.maximumDifference

    # Add your code here


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
