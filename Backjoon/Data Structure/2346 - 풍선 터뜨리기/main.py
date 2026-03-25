import sys
from collections import deque

n = int(sys.stdin.readline())

Balloon = deque(enumerate(map(int, sys.stdin.readline().split())))

result = list()
for i in range(n):
    index, pop = Balloon.popleft()
    result.append(index + 1)
    if pop > 0:
        Balloon.rotate(-(pop - 1))
    elif pop < 0:
        Balloon.rotate(-pop)

print(*result)
