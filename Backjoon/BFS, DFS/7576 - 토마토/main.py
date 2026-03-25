import sys
from collections import deque

# * BFS 구현 함수
def bfs(graph, root):
    visited = list()
    queue = list()

    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[root])

    return visited


# * 데이터 수와 행렬을 받는 구문
m, n = map(int, sys.stdin.readline().strip().split(" "))

matrix = [[0 for _ in range(m)] for _ in range(n)]

for i in range(0, n, 1):
    matrix[i] = list(map(int, sys.stdin.readline().strip().split(" ")))


countDays = 0
moveX = [-1, 1, 0, 0]
moveY = [0, 0, -1, 1]


queue = list()

for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1:
            queue.append((x, y))


for i in range(0, n, 1):
    print(matrix[i])
