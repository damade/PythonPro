# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneContacts = {}
nameList = []

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        cont = input()
        try:
            name = cont.split(" ")[0]
            phoneNumber = cont.split(" ")[1]
            if (len(phoneNumber) == 8):
                phoneContacts[name] = int(phoneNumber)
            else:
                continue
        except (IndexError, RuntimeError) as e:
            pass
    for j in range(n):
        request = input()
        nameList += [request]
    for k in range(0, n):
        try:
            namePost = nameList[k]
            if namePost in phoneContacts.keys():
                print(f"{namePost}={phoneContacts[namePost]}")
            else:
                print("Not found")
        except (IndexError, KeyError) as e:
            pass
