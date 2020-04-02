import random
import string

"""Generating Password of length 9 with two inputs"""


def PasswordGenerator(first_name, last_name):
    size = 5
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(size))
    finalPassword = first_name[0:2] + last_name[-2:] + randomString
    print(finalPassword)  # releases the output of the input
    return


"""Generating Password of length 9 without no input"""


def PasswordGeneratorOnly():
    size = 9
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(size))
    print(randomString)  # releases the output of the input
    return


PasswordGeneratorOnly();
PasswordGenerator("Damilola", "Adeoye")
