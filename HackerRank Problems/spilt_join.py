def split_and_join(line):
    line1 = line.split(" ")
    line2 = ("-").join(line1)
    return line2
    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
