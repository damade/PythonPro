"""Python is a type inference language;
It means Python can automatically detect the data type of an expression.
It is the characteristics of most functional PL.
Given the above, from Python 3.6 and PEP 526 standards, you can now declare the type of a variable."""

"""A variable is like a box in the computer’s memory where you can store a
single value, while A data type is a category for values, and every value belongs to exactly one data type.
 Common Data types include Integer, Byte, Character, String, Boolean, Float"""

# Type inference type.

anInteger = 78
aFloat = 34.5
aBoolean = True
aChar = chr(71)
aString = "This is a string and not a character"
aByte = b"Test"

print(f"\n{anInteger}\n{aFloat}\n{aBoolean}\n{aChar}\n{aString}\n{aByte}\n")

# Declaring datatype of a variable
declareInteger: int = 78
declareFloat: float = 34.5
declareBoolean: bool = True
declareChar: chr(71) = chr(71)
declareString: str = "This is a string and not a character"
declareByte: bytes = b"Test"

print(f"\n{declareInteger}\n{declareFloat}\n{declareBoolean}\n{declareChar}\n{declareString}\n{declareByte}\n")

# To check their Data type class or instance.

print(f"\nanInteger = {type(anInteger)} and declareInteger = {type(declareInteger)} ")
print(f"\naFloat = {type(aFloat)} and declareFloat = {type(declareFloat)} ")
print(f"\naBoolean = {type(aBoolean)} and declareBoolean = {type(declareBoolean)} ")
print(f"\naChar = {type(aChar)} and declareChar = {type(declareChar)} ")
print(f"\naString = {type(aString)} and declareString = {type(declareString)} ")
print(f"\naByte = {type(aByte)} and declareByte = {type(declareByte)} ")
