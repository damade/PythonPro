stringList = ["Adeoye", "damilola", "SeunFunmi", "Heal the World!!!", "COVID-19"]  # creating list for Strings
numericList = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # creating list for numbers


def convertToUpperStrings(item):  # creating a "pure function" that turns a string to upper case
    return str(item).upper()

def convertToLowerStrings(item):  # creating a "pure function" that turns a string to lower case
    return str(item).lower()

def multiplyByTwo(item):  # creating a "pure function" that multiply a number by 2
    return item * 2


# implementing Map Function
"""Basically Map Function is a shorter method of implementing functions
(that output remains constant relatively to input and one parameter) on data(list, tuple, dict or any iterable object)
without affecting the data but producing a new data. It is known to be useful in Space Complexity.
"""

print(list(map(convertToUpperStrings, stringList)))
print("\n")
print(list(map(convertToLowerStrings, stringList)))
print("\n")
print(list(map(multiplyByTwo, numericList)))
