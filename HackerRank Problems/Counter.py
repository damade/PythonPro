def counter(start, stop):
    if start < stop:
        print("Counting up:", end=" ")
        while (start < stop):
            print(f"{start},", end=" ")
            start += 1
        print(f"{stop}\n")
    elif start == stop:
        print(f"Counting up: {start}", end="")
        print("\n")
    else:
        print("Counting down:", end=" ")
        while (start > stop):
            print(f"{start},", end=" ")
            start -= 1
        print(f"{stop}\n")
    return


counter(1, 30)
counter(9, 3)
counter(15, 15)
