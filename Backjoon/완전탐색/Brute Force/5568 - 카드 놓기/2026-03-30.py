import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
card = []

for _ in range(n):
    card.append(int(sys.stdin.readline().strip()))

cards = []
for i in permutations(card, k):
    temp = ""
    for j in i:
        temp += str(j)
    cards.append(temp)

print(len(set(cards)))
