import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


n, r = map(int, sys.stdin.readline().split())
tree = defaultdict(dict)
for _ in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a][b] = d
    tree[b][a] = d

giga_node = r
dist = 0
while len(tree[giga_node]) == 1:
    node, temp = list(tree[giga_node].items())[0]
    del tree[node][giga_node]
    dist += temp
    giga_node = node


def dfs(tree, root):
    branch_dist = 0
    for node, dis in tree[root].items():
        del tree[node][root]
        temp = dis + dfs(tree, node)
        branch_dist = max(branch_dist, temp)

    return branch_dist


print(dist, dfs(tree, giga_node))
