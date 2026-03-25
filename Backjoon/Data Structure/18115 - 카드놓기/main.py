# 18115 - 카드놓기
import sys
from collections import deque


N = int(sys.stdin.readline())
technic = list(map(int, sys.stdin.readline().strip().split(" ")))
technic.reverse()
card = deque()


for i in range(N):
    if technic[i] == 1:
        card.appendleft(i + 1)
    elif technic[i] == 2:
        card.insert(1, i + 1)
    elif technic[i] == 3:
        card.append(i + 1)

print(*card)
