import sys
from itertools import combinations

stack = []
temp = []
answer = set()

n = list(map(str, sys.stdin.readline().strip()))

for index, letter in enumerate(n):
    if letter == "(":
        temp.append(index)
    elif letter == ")":
        stack.append((temp.pop(), index))

for _ in range(1, len(stack) + 1):
    combination = combinations(stack, _)

    for case in combination:
        copyOfn = list(n)

        for tries in case:
            copyOfn[tries[0]] = ""
            copyOfn[tries[1]] = ""

        answer.add("".join(copyOfn))

for result in sorted(answer):
    print(result)
