import sys

N = int(sys.stdin.readline())


for _ in range(N):
    temp = [_]
    M = []
    x = _
    while x >= 1:
        temp.append(x % 10)
        x = int(x / 10)

    if sum(temp) == N:
        M.append(temp[0])
        break

if len(M) != 0:
    print(min(M))
else:
    print(0)
