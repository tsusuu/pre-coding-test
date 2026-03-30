import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
prefer = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_prefer = 0
for combi in combinations(range(m), 3):
    temp_total = 0
    for row in range(n):
        temp_total += max(
            prefer[row][combi[0]], prefer[row][combi[1]], prefer[row][combi[2]]
        )
    max_prefer = max(max_prefer, temp_total)

print(max_prefer)
