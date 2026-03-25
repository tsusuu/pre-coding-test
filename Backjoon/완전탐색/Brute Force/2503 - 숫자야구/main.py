import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
target = set(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for _ in range(n):
    number, s, b = map(int, sys.stdin.readline().split())
    number = tuple(map(int, list(str(number))))
    temp = set()

    for num in target:
        xs, xb = 0, 0

        for i in range(3):
            if num[i] == number[i]:
                xs += 1
            elif num[i] in number:
                xb += 1

        if (xs == s) and (xb == b):
            temp.add(num)
    target = temp

print(len(target))
