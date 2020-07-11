def print_formatted(number):
    width = int(bin(number)[2:])
    print(width)
    for i in range(1, number + 1):
        numberToBaseEight = oct(i)
        numberToBaseSixteen = hex(i)
        numberToBaseTwo = bin(i)
        print(
            f"{str(i).rjust(width)} {str(numberToBaseEight[2:]).rjust(number)} {str(numberToBaseSixteen[2:]).rjust(number)} {str(numberToBaseTwo[2:]).rjust(number)}")  # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
