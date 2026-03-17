import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
chart = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


maxTotal = 0
for combi in combinations(range(m), 3):
    total = 0
    for _ in range(n):
        total += max(chart[_][combi[0]], chart[_][combi[1]], chart[_][combi[2]])
    maxTotal = max(total, maxTotal)

print(maxTotal)
