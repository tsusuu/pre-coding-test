import sys

sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline().strip())

tree = [[] for _ in range(N + 1)]
parent = [None for _ in range(N + 1)]

for _ in range(N - 1):
    key, value = map(int, sys.stdin.readline().strip().split())
    tree[key].append(value)
    tree[value].append(key)


def DFS(graph, start, visited):
    for i in graph[start]:
        if not visited[i]:
            visited[i] = start
            DFS(graph, i, visited)


DFS(tree, 1, parent)


for i in range(2, N + 1):
    print(parent[i])
