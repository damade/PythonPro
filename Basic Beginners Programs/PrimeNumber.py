def checkprime(n):
    k = 0
    j = 2
    while (j <= (n / j)):
        if not (n % j):
            break
        j = j + 1
    if (j > (n / j)):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")


n = int(input("What is your input: "))
checkprime(n)
