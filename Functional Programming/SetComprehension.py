"""
Set is a datatype that does not allow duplicated items, only unique items
Set Comprehension is one of the short one liner ways of creating set.
Instead of looping through and appending data to the set, rather use set comprehension
"""

# Old convension of creating the list
oldSet = []
for char in "hello":
    oldSet.append(char)

# The new convension using list comprehension is below
newSet = [char for char in "hello"]

'''print(oldSet)
print("\n")
print(newSet)'''

# By running it you'll find out it is the same output
# Other case scenarios

# A list containing range of numbers from 0 to 99
setRangeOfHundred = [num for num in range(0, 100)]

# A list containing square of range of numbers from 0 to 99
setSquareRangeOfHundred = [num ** 2 for num in range(0, 100)]

# A list containing esquare of even numbers ranging from 0 to 99
setEvenSquareRangeOfHundred = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(setRangeOfHundred)
print("\n")
print(setSquareRangeOfHundred)
print("\n")
print(setEvenSquareRangeOfHundred)
