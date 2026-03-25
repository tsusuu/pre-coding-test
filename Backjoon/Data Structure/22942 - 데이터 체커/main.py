import sys

N = int(sys.stdin.readline().strip())
x = list(0 for _ in range(N))
r = list(0 for _ in range(N))
d = 0
result = list()

for _ in range(N):
    x[_], r[_] = map(int, sys.stdin.readline().strip().split(" "))

for i in range(N - 1):
    for j in range(i + 1, N):
        d = abs(x[i] - x[j])
        if d > r[i] + r[j]:
            continue
        elif d < abs(r[i] - r[j]):
            continue
        elif not d:
            continue
        else:
            result.append("fail")
            break

if "fail" in result:
    print("NO")
else:
    print("YES")
