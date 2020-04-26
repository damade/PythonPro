import random


def easyMode():
    easyRandomValue = random.randrange(1, 10)
    count = 1
    totalNumber = 6
    while (count <= totalNumber):
        try:
            userInput = int(input("What is the number? "))
            if (userInput == easyRandomValue):
                print("\nYou guessed right")
                print(f"You got it after {count} trials\n")
                break
                # homeAnyOther()
            elif (userInput < easyRandomValue):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("Please enter a number")
            continue
    print("Game Over")
    homeAnyOther()


def mediumMode():
    mediumRandomValue = random.randrange(1, 20)
    count = 1
    totalNumber = 4
    while (count <= totalNumber):
        try:
            userInput = int(input("What is the number? "))
            if (userInput == mediumRandomValue):
                print("\nYou guessed right")
                print(f"You got it after {count} trials\n")
                # break
                homeAnyOther()
            elif (userInput < mediumRandomValue):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("Please enter a number")
            continue
    print("Game Over")
    homeAnyOther()


def hardMode():
    hardRandomValue = random.randrange(1, 50)
    count = 1
    totalNumber = 3
    while (count <= totalNumber):
        try:
            userInput = int(input("What is the number? "))
            if (userInput == hardRandomValue):
                print("\nYou guessed right")
                print(f"You got it after {count} trials\n")
                # break
                homeAnyOther()
            elif (userInput < hardRandomValue):
                print("\nThat was wrong\nYour guess is low")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
            else:
                print("\nThat was wrong\nYour guess is high")
                print(f"\nYou have {totalNumber-count} guesses left\n")
                count += 1
                continue
        except ValueError:
            print("Please enter a number")
            continue
    print("Game Over")
    homeAnyOther()


def homePage():
    print("\nWELCOME TO GUESS GAME\n")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< HOME PAGE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Do you want to exit?\n")
    print("Choose the level you want to play\n")

    promptQuestion = int(input("Reply: "))
    if (promptQuestion == 1):
        easyMode()
    elif (promptQuestion == 2):
        mediumMode()
    elif (promptQuestion == 3):
        hardMode()
    elif (promptQuestion == 4):
        exit()
    else:
        print("Enter a valid option")
        homeAnyOther()


def homeAnyOther():
    print("\nThank you, can we start again? \n")
    print("\n-------------------------- KINDLY CHOOSE WHAT NEXT --------------------------\n")
    print("1. Do you want to return to home page?")
    print("2. Do you want to exit\n")
    promptQuestion = input("Reply: ")
    if (promptQuestion == '1'):
        homePage()
    elif (promptQuestion == '2'):
        exit()
    else:
        exit()


var = 1
while var == 1:  # it is used to create an infinite loop in order to continue running the program
    homePage()
