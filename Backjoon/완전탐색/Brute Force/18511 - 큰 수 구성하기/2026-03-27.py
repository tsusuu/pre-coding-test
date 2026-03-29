import sys
from itertools import product

n, _ = map(int, sys.stdin.readline().split())
k = list(map(int, sys.stdin.readline().split()))

max_value = 0
lenth = len(str(n))
for i in range(2):
    if lenth - i == 0:
        break
    for pair in product(k, repeat=(lenth - i)):
        temp = str()
        for _ in pair:
            temp += str(_)
        if int(temp) <= n:
            max_value = max(max_value, int(temp))

print(max_value)
