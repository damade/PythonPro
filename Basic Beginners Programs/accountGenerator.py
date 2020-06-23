import random
import string


def PasswordGenerator():
    accountPrefix = ["00", "01"]
    size = 8
    chars = string.digits  # specifies the type of chracter needed through ASCII
    randomString = ''.join(random.choice(chars) for _ in range(size))
    randomPrefixGen = random.randint(0, 1)
    finalAccount = accountPrefix[randomPrefixGen] + randomString
    return finalAccount  # releases the output of the input


print(PasswordGenerator())
