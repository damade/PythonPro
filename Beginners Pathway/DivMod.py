"""
Divmod is a quick and easy way to perform Euclidean division with a single operation.
Divmod is an operation in form of modulo, but you get both th module and the floor division.
In Maths. Divmod(13,5) gives (2,3) where 2 => floor division of 13 and 5 and 3 => 13 is 13 modulo 5
So let's see it in practice in Python.
"""
euclideanDivisor = divmod(13, 5)
print(euclideanDivisor)  # (2,3), which is a tuple.

"""We can destructure the tuple so we can get it independently"""
quotient, remainder = divmod(13, 5)
print(f"\nThe quotient of divmod(13,5) is {quotient}, while the remainder is {remainder}\n")

"""You can also use it with floating points numbers"""
print(divmod(6.5, 2))  # gives (3.0, 0.5)
print(divmod(9.0, 1.5))  # gives (6.0, 0.0)

"""Let's Use it to build a time converter"""
# Let's start with minutes and second converter
print("\n\t\t\t\tSecond to Minutes converter")
rawTime = 9575  # it is in seconds
minutes, seconds = divmod(rawTime, 60)  # gives(159,35)
print(f"{rawTime} seconds is {minutes} minutes and {seconds} seconds\n")

# Let's go to Hour and Minute converter
print("\n\t\t\t\tSecond to Minutes and Hours converter")
hours, minutes = divmod(minutes, 60)  # gives(2,39)
print(f"{rawTime} seconds is {hours} hour(s), {minutes} minute(s) and {seconds} second(s)\n")
