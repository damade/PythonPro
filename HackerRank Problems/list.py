listA = []
if __name__ == '__main__':
    try:
        N = int(input())
        for i in range(N):
            try:
                command = input("")
                if command == "print":
                    print(listA)
                    continue
                elif command == "sort":
                    listA.sort()
                    continue
                elif command == "reverse":
                    listA.reverse()
                    continue
                elif command == "pop":
                    listA.pop()
                    continue
                elif "insert" in command:
                    indexI = int(command.split(" ")[1])
                    value = int(command.split(" ")[2])
                    listA.insert(indexI, value)
                    continue
                elif "remove" in command:
                    value = int(command.split(" ")[1])
                    listA.remove(value)
                    continue
                elif "append" in command:
                    value = int(command.split(" ")[1])
                    listA.append(value)
                    continue
                else:
                    print("Input A Valid Command")
            except (ValueError, TypeError) as e:
                print("Input Valid Inputs")
    except (ValueError, TypeError) as e:
        print("Input Valid Inputs")
