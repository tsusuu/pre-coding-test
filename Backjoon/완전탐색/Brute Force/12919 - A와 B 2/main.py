import sys

s = str(sys.stdin.readline().strip())
t = str(sys.stdin.readline().strip())


def del_a(char):
    char = char[0 : len(char) - 1]
    return char


def del_b(char):
    char = char[::-1]
    char = char[0 : len(char) - 1]
    return char


def dfs(curr):
    if len(curr) == len(s):
        if curr == s:
            return 1
        else:
            return 0
    if len(curr) < len(s):
        return 0

    if curr[0] == "A" and curr[-1] == "B":
        return 0

    result1 = 0
    result2 = 0
    if curr[-1] == "A":
        next1 = del_a(curr)
        result1 = dfs(next1)

    if curr[0] == "B":
        next2 = del_b(curr)
        result2 = dfs(next2)

    if result1 or result2:
        return 1
    else:
        return 0


print(dfs(t))
