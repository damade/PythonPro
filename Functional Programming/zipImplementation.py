stringList = ["ADEOYE", "damilola", "SeunFunmi", "Heal the World!!!", "COVID-19",
              "are you there"]  # creating list for Strings
numericList = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # creating list for numbers
string = ["Surname", "First name", "Babe's name", "Best song", "Pandemic", "Question", "Answer", "Feedback"]
number = [1, 2, 3, 4, 5, 6]

# implementing Map Function
"""Basically Zip Function, zip() only connects two or more iterables.
It selects the item each from the iterables to form a new list or iterable 
In order to avoid loss of memory, ensure the length of the iterable are the same.
"""

print(list(zip(number, stringList)))
print("\n")
print(list(zip(numericList, stringList)))
print("\n")
print(list(zip(string, stringList)))
print("\n")
