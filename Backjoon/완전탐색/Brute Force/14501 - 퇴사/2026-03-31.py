import sys

n = int(sys.stdin.readline().strip())
T, P = [], []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

max_income = 0


def dfs(day, income):
    global max_income

    if day > n:
        return
    if day == n:
        max_income = max(max_income, income)
        return

    dfs(day + T[day], income + P[day])
    dfs(day + 1, income)


dfs(0, 0)
print(max_income)
