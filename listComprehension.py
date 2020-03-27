"""
List Comprehension is one of the short one liner ways of creating list.
Instead of looping through and appending data to the list, rather use list comprehension
"""

# Old convension of creating the list
oldList = []
for char in "hello":
    oldList.append(char)

# The new convension using list comprehension is below
newList = [char for char in "hello"]

'''print(oldList)
print("\n")
print(newSet)'''

# By running it you'll find out it is the same output
# Other case scenarios

# A list containing range of numbers from 0 to 99
listRangeOfHundred = [num for num in range(0, 100)]

# A list containing square of range of numbers from 0 to 99
listSquareRangeOfHudred = [num ** 2 for num in range(0, 100)]

# A list containing esquare of even numbers ranging from 0 to 99
listEvenSquareRangeOfHundred = [num ** 2 for num in range(0, 100) if num % 2 == 0]

'''print(listRangeOfHundred)
print("\n")
print(listSquareRangeOfHudred)
print("\n")
print(listEvenSquareRangeOfHundred)'''
