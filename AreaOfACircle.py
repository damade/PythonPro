import math

"""This creates a function of calculating Area of a circle,
 while passing radius as it parameter"""


def AreaOfACircle(radius):
    return ((math.pow(radius, 2)) * math.pi)


"""This accepts an input 'Radius' of datatype integer"""
radius = int(input("What is the radius: "))

"""Implementing the function created above and parsing it into the variable Area"""
Area = AreaOfACircle(radius)

"""This is a short snippets that can be used to superscript or subscript numbers in python"""
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

"""Superscripting the word Cm^2, metric SI unit of Areas"""
cm = "Cm2".translate(SUP)

"""Printing out the final result using the print format method"""
# Note that :.4f is use to format an integer with a specific rounded up decimal place
print(f"The Area of a Circle with radius {radius} is {Area:.4f}{cm}")
