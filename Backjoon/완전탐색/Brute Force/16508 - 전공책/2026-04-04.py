import sys
from itertools import combinations
from collections import Counter

t = sys.stdin.readline().strip()
t = Counter(t)
n = int(sys.stdin.readline().strip())


books = []
for _ in range(n):
    c, w = sys.stdin.readline().split()
    books.append((int(c), Counter(w)))

min_price = 16 * 100000 + 1

for i in range(1, n + 1):
    for subset in combinations(books, i):
        total_price = 0
        total_alpha = Counter()

        for price, alpha in subset:
            total_price += price
            total_alpha += alpha

        usable = True
        for char, count in t.items():
            if total_alpha[char] < count:
                usable = False
                break
        if usable:
            min_price = min(min_price, total_price)

if min_price == 16 * 100000 + 1:
    print(-1)
else:
    print(min_price)
