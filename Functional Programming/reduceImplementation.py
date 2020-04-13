from functools import reduce

myList = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]  # creating list of numbers


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, myList, 10))
