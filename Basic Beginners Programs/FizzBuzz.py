def FizzBuzzCheck(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif (number % 3 == 0 and number % 5 != 0):
        return "Fizz"
    elif (number % 5 == 0 and number % 3 != 0):
        return "Buzz"
    else:
        return number


if __name__ == "__main__":
    try:
        theInput = int(input("What is the number? "));
        for i in range(1, theInput + 1):
            print(FizzBuzzCheck(i))
    except:
        raise
