"""This is a short snippets that can be used to superscript or subscript numbers in python"""
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

print("H2SO4".translate(SUB))
print("\n")
print("Cm3".translate(SUP))
print("\n")
print("A2 * B3".translate(SUP))
print("\n")
