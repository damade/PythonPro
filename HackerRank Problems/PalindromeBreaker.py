def solve(palindrome):
    if len(palindrome) == 1:
        return "IMPOSSIBLE"
    elif (palindrome == (len(palindrome) * palindrome[0])):
        return "IMPOSSIBLE"
    else:
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
    return palindrome[:-1] + 'b'


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
