import sys
from itertools import product


N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
products = list()
lenth = len(str(N))
for _ in range(lenth):
    for pair in product(numbers, repeat=lenth - _):
        temp = str()
        for _ in pair:
            temp += str(_)
        products.append(int(temp))
    for _ in numbers:
        products.append(_)
products.sort(reverse=True)
for _ in products:
    if _ > N:
        continue
    else:
        maxValue = _
        break
print(maxValue)
