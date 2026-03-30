import sys
from itertools import combinations

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline().strip())

stickers = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    stickers.append((r, c))

area = 0
for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]

        cases = [(r1, c1, r2, c2), (r1, c1, c2, r2), (c1, r1, r2, c2), (c1, r1, c2, r2)]

        for r1, c1, r2, c2 in cases:
            if (
                (r1 + r2) <= h
                and max(c1, c2) <= w
                or (r1 + r2) <= w
                and max(c1, c2) <= h
            ):
                area = max(area, r1 * c1 + r2 * c2)
                break


print(area)
