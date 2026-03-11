import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

maxCard = 0
for _ in combinations(card, 3):
    blackJack = sum(_)
    if blackJack > M:
        continue
    if blackJack > maxCard:
        maxCard = blackJack

print(maxCard)
