import random

randomValue = random.randrange(0, 20)
var = 1
while var == 1:  # it is used to create an infinite loop in order to continue running the program
    while True:
        try:
            userInput = int(input("What is the number? "))
            if (userInput == randomValue):
                print("You guessed right")
                break
            elif (userInput < randomValue):
                print("Your guess is low")
                continue
            else:
                print("Your guess is high")
                continue
        except ValueError:
            print("Please enter a number")
            continue
    print("\nThank you, can we start again? \n")
