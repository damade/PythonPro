import random as rd

gameList = ["rock","paper","scissors"]
randomValue =  rd.randrange(0,3)
var = 1
while var == 1: #it is used to create an infinite loop in order to continue running the program
    userInput = input("What is your pick? ").lower()
    computer = gameList[randomValue].lower()
    computer_chose_ = "Computer chose "
    if (userInput == "scissors" and computer == "paper"):
        congratsModification = "You have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    elif (userInput == "paper" and computer == "scissors"):
        congratsModification = "Computer have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    elif(userInput == "paper" and computer == "rock"):
        congratsModification = "You have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    elif(userInput == "rock" and computer == "paper"):
        congratsModification = "Computer have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    elif(userInput == "rock" and computer == "scissors"):
        congratsModification = "You have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    elif(userInput == "scissors" and computer == "rock"):
        congratsModification = "Computer have won"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    else:
        congratsModification = "It is stalemate"
        whatComputerModification = computer_chose_ + computer
        printOut = congratsModification.center(40, "*") + "\n" + whatComputerModification.center(40, "-")
        print(printOut)
    print("\nThank you, can we start again? \n")
