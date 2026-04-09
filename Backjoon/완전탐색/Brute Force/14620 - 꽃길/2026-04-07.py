import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())
garden = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]
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


price = float("inf")
for c1, c2, c3 in combinations(possible, 3):
    if c1[0].isdisjoint(c2[0]) and c1[0].isdisjoint(c3[0]) and c2[0].isdisjoint(c3[0]):
        cost = c1[1] + c2[1] + c3[1]
        price = min(price, cost)


print(price)
