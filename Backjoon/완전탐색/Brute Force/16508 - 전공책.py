import sys
from itertools import combinations
from collections import Counter

Tw = list(sys.stdin.readline().strip())
Tc = Counter(Tw)

N = int(sys.stdin.readline().strip())
books = []

for _ in range(N):
    c, w = sys.stdin.readline().split()
    books.append((int(c), Counter(w)))

min_price = 1600001

for i in range(1, N + 1):
    for subset in combinations(books, i):
        total_price = 0
        total_alphas = Counter()

        for price, alpha in subset:
            total_price += price
            total_alphas += alpha

        usable = True
        for char, count in Tc.items():
            if total_alphas[char] < count:
                usable = False
                break
        if usable:
            min_price = min(min_price, total_price)

if min_price == 1600001:
    print(-1)
else:
    print(min_price)
