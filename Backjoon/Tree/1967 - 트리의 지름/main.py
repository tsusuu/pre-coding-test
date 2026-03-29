import sys

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, dis = map(int, sys.stdin.readline().strip().split())
    tree[parent].append((child, dis))
    tree[child].append((parent, dis))


def dfs(tree, root):
    visited = [-1] * (n + 1)
    visited[root] = 0
    stack = [(root, 0)]

    while stack:
        node, dist = stack.pop()
        for child, tempDist in tree[node]:
            if visited[child] == -1:
                visited[child] = dist + tempDist
                stack.append((child, dist + tempDist))

    maxDist = 0
    farNode = root
    for _ in range(1, n + 1):
        if visited[_] > maxDist:
            maxDist = visited[_]
            farNode = _

    return farNode, maxDist


farNode, _ = dfs(tree, 1)
_, maxDist = dfs(tree, farNode)
print(maxDist)
