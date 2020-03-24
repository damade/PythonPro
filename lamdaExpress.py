from functools import reduce

myList = [1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10]  # creating list of numbers
stringList = ["Adeoye", "damilola", "SeunFunmi", "Heal the World!!!", "COVID-19"]  # creating list for Strings

""" Lambda expressions in Python are more than time
 anonymous functions that you don't need more than once.
 Functions you only use once.
"""
print(reduce(lambda acc, item: acc + item, myList, 10))
print("\n")

print(list(map(lambda item: item * 2, myList)))
print("\n")
print(list(map(lambda item: str(item).lower(), stringList)))
print("\n")
print(list(map(lambda item: str(item).upper(), stringList)))
print("\n")

print(list(filter(lambda item: item % 2 != 0, myList)))
print("\n")
print(list(filter(lambda item: str(item).isalpha(), stringList)))
print("\n")
