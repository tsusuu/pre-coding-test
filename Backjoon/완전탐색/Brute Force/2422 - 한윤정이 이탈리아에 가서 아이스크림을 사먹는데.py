import sys

n, m = map(int, sys.stdin.readline().split())

bad = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    bad[a][b] = 1
    bad[b][a] = 1


count = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if bad[i][j]:
            continue
        for k in range(j + 1, n + 1):
            if bad[i][k] or bad[j][k]:
                continue

            count += 1
print(count)
