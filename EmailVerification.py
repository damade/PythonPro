import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

yourEmail = input("What is your email: ").lower()
if (re.search(regex, yourEmail)):
    domain = yourEmail.split('@')[1]
    if domain == "hngtech.com":
        print("verified email")
    else:
        print("Wrong Email domain")
else:
    print("Wrong Email")
