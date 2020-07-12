# os.getcwd()

searchfile = open(r'TextDocuments\theText.txt', "r")
for line in searchfile:
    if "damilola.adeoyecom" in line:
        theString = line
        username = theString.split(" ")[0]
        password = theString.split(" ")[1]
        email = theString.split(" ")[2]
        firstname = theString.split(" ")[3]
        lastname = theString.split(" ")[4]
        print(f"{username}\n{password}\n{email}\n{firstname}\n{lastname}")
        print(line)

searchfile.close()
