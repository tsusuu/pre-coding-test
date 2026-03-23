import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())

garden = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 1, -1, 0, 0]  # 제자리, 동, 서, 남, 북
dy = [0, 0, 0, -1, 1]
possible = []
for x in range(1, n - 1):
    for y in range(1, n - 1):
        planted = set()
        cost = 0
        for i in range(5):
            nx, ny = x + dx[i], y + dy[i]
            cost += garden[nx][ny]
            planted.add((nx, ny))
        possible.append((planted, cost))

price = 3000
for f1, f2, f3 in combinations(possible, 3):
    if f1[0].isdisjoint(f2[0]) and f1[0].isdisjoint(f3[0]) and f2[0].isdisjoint(f3[0]):
        cost = f1[1] + f2[1] + f3[1]
        if cost < price:
            price = cost

print(price)
