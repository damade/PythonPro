"""We have treated data types, we have treated operations and operators for numeric values.
Let us check operations that can be done in string"""

declareString: str = "This is a string and not a character"
nameJohn: str = "John"
nameDoe: str = "Doe"
theLongString: str = "There is basically nothing, i don\'t want to think about it " \
                     "because; there is absolutely nothing to think about"

# Concatenation: It is joining two or more strings with + operator.
print("\nString Concatenation: ")
firstResult = nameJohn + nameDoe;
print(f"{firstResult}\n")  # it gives JohnDoe
first_Result = nameJohn + " " + nameDoe;
print(f"{first_Result}\n")  # it gives JohnDoe

print("\nString Replication: ")
# Replication: It is a way of repeating a single string value  a number of times  with * operator.
firstResult = nameJohn * 4;
print(f"{firstResult}\n")  # it gives JohnJohnJohn
first_Result = nameDoe * 2;
print(f"{first_Result}\n")  # it gives DoeDoe

# Other basic functions

print("\nLength of a String: ")
# 1. length of a string using len()
firstResult = len(nameJohn)
first_Result = len(declareString)
print(f"{firstResult}\n")  # 4
print(f"{first_Result}\n")  # 36

print("\nEscape Characters: ")
# 1. Escape Characters
"""Escape character Prints as
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash"""
nextLine = "This is to show \n next line"
singleQuote = "This is to show a single qoute, I\'m done"
doubleQuote = "This is to show \"a double quote\""
tabResult = "This is to show a \t tab"
backLash = "This is to show a backlash\\ sign"
print(f"{nextLine}\n")  # 4
print(f"{singleQuote}\n")  # This is to show a single qoute, I'm done
print(f"{doubleQuote}\n")  # This is to show "a double quote"
print(f"{tabResult}\n")  # This is to show a 	 tab
print(f"{backLash}\n")  # This is to show a backlash\ sign

"""Check directory String Manipulation for continuation"""
