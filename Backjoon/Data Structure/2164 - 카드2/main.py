import sys
from collections import deque

N = int(sys.stdin.readline())
card2 = deque()

for i in range(1, N + 1, 1):
    card2.append(i)

while len(card2) - 1:
    card2.popleft()
    card2.rotate(-1)


print(card2[0])
