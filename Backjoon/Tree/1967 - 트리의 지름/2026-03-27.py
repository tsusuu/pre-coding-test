import sys

n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))


def dfs(tree, root):
    visited = [-1] * (n + 1)
    visited[root] = 0
    stack = [(root, 0)]

    while stack:
        node, dist = stack.pop()
        for child, d in tree[node]:
            if visited[child] == -1:
                visited[child] = dist + d
                stack.append((child, dist + d))

    max_dist = 0
    far_node = root
    for _ in range(1, n + 1):
        if visited[_] > max_dist:
            max_dist = visited[_]
            far_node = _
    return far_node, max_dist


far_node, _ = dfs(tree, 1)
_, dist = dfs(tree, far_node)
print(dist)
