import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline().strip()))

setList = set(list(permutations(card, k)))
setList = list(setList)
cardList = []

for i in range(len(setList)):
    temp = ""
    for _ in setList[i]:
        temp += str(_)
    cardList.append(temp)

print(len(set(cardList)))
