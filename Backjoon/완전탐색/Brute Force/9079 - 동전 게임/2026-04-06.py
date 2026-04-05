import sys
from collections import deque

n = int(sys.stdin.readline().strip())

flips = [
    0b111000000,
    0b000111000,
    0b000000111,
    0b100100100,
    0b010010010,
    0b001001001,
    0b100010001,
    0b001010100,
]


def bfs():
    temp = ""
    for _ in range(3):
        temp += "".join(sys.stdin.readline().split())
    coin = int(temp.replace("H", "0").replace("T", "1"), 2)

    queue = deque([(coin, 0)])
    visited = {coin}

    while queue:
        curr, dist = queue.popleft()

        if curr == 0 or curr == 0b111111111:
            return dist

        for flip in flips:
            next_curr = curr ^ flip
            if next_curr not in visited:
                visited.add(next_curr)
                queue.append((next_curr, dist + 1))
    return -1


for _ in range(n):
    print(bfs())
