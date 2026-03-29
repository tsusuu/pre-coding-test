import sys

n, m = map(int, sys.stdin.readline().split())
not_comb = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    not_comb[x][y] = 1
    not_comb[y][x] = 1

count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if not_comb[i][j]:
            continue
        for k in range(j + 1, n + 1):
            if not_comb[i][k] or not_comb[j][k]:
                continue
            count += 1

print(count)
