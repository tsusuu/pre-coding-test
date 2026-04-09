import sys

n = int(sys.stdin.readline().strip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))


def dfs(tree, root):
    visited = [-1] * (n + 1)
    visited[root] = 0
    stack = [(root, 0)]

    while stack:
        node, dist = stack.pop()
        for child, temp_dist in tree[node]:
            if visited[child] == -1:
                visited[child] = dist + temp_dist
                stack.append((child, dist + temp_dist))
    max_dist = 0
    far_node = root
    for _ in range(1, n + 1):
        if visited[_] > max_dist:
            max_dist = visited[_]
            far_node = _

    return far_node, max_dist


root = 1
root, _ = dfs(tree, root)
_, dist = dfs(tree, root)
print(dist)
