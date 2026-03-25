import sys

n = int(sys.stdin.readline().strip())
T = []
P = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

maxIncome = 0


def dfs(day, income):
    global maxIncome

    if day > n:
        return

    if day == n:
        maxIncome = max(maxIncome, income)
        return

    dfs(day + T[day], income + P[day])
    dfs(day + 1, income)


dfs(0, 0)
print(maxIncome)
