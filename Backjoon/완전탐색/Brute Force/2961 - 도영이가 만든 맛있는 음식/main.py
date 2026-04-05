import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())
foods = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

min_balance = float("inf")

for i in range(1, n + 1):
    for dishes in combinations(foods, i):
        temp_s = 1
        temp_b = 0

        for dish in dishes:
            s, b = dish
            temp_s *= s
            temp_b += b
        temp_balance = abs(temp_b - temp_s)
        min_balance = min(min_balance, temp_balance)

print(min_balance)
