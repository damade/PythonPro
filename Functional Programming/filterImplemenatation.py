stringList = ["ADEOYE", "damilola", "SeunFunmi", "Heal the World!!!", "COVID-19",
              "are you there"]  # creating list for Strings
numericList = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # creating list for numbers


def onlyUpperStrings(item):  # creating a "pure function" that checks for upper case string
    return str(item).isupper()


def onlyAlphanumericStrings(item):  # creating a "pure function" that checks for upper case string
    return str(item).isalnum()


def onlyAlphabetStrings(item):  # creating a "pure function" that checks for upper case string
    return str(item).isalpha()


def onlyLowerStrings(item):  # creating a "pure function" that checks for lower case string
    return str(item).islower()


def onlyOddNumber(item):  # creating a "pure function" that checks for odd numbers
    return item % 2 != 0


def onlyEvenNumber(item):  # creating a "pure function" that checks for even numbers
    return item % 2 == 0


# implementing Map Function
"""Basically Filter Function is when a function is implemented on a list, 
filter() only selects items in any of the iterables that suits the result 
of the function specified and for,s a new iterable. 
"""

print(list(filter(onlyUpperStrings, stringList)))
print("\n")
print(list(filter(onlyLowerStrings, stringList)))
print("\n")
print(list(filter(onlyAlphabetStrings, stringList)))
print("\n")
print(list(filter(onlyAlphanumericStrings, stringList)))
print("\n")
print(list(filter(onlyOddNumber, numericList)))
print("\n")
print(list(filter(onlyEvenNumber, numericList)))
