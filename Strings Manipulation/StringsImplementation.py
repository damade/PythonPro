"""The three quotation marks can be used to make comment on multiple lines"""

""" r before the beginning quotation mark of a string to make it a raw string.
 A raw string completely ignores all escape characters and prints any backslash that appears in the string."""
print(r"Damilola's cat is owned by Damilola")
print(r"Damilola\'s cat is owned by Damilola")

"""Multiline Strings with triple Quotes
While you can use the \n escape character to put a newline into a string, it
is often easier to use multiline strings.
 A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes,
tabs, or newlines in between the “triple quotes” are considered part of the
string."""

# Example with the code below
print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

theString = "Dear Alice,Eve's cat has been arrested for catnapping, cat burglary, and extortion."

"""The Spilt and Partiton function is alike but 
Partition only splits the string once
It keeps track of the delimeter
Always return same Data Structure"""
print(theString.split('cat'))
print(theString.partition('cat'))
