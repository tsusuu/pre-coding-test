import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
cases = set(permutations(range(1, 10), 3))


for _ in range(n):
    number, s, b = map(int, sys.stdin.readline().split())
    number = tuple(map(int, list(str(number))))
    temp = set()

    for case in cases:
        xs, xb = 0, 0

        for i in range(3):
            if case[i] == number[i]:
                xs += 1
            elif case[i] in number:
                xb += 1
        if (xs == s) and (xb == b):
            temp.add(case)
    cases = temp
print(len(cases))
