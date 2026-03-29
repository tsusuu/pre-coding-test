import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

n, r = map(int, sys.stdin.readline().split())

tree = defaultdict(dict)
for i in range(n - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a][b] = d
    tree[b][a] = d


giganode = r
root_to_giga = 0
while len(tree[giganode]) == 1:
    node, _ = list(tree[giganode].items())[0]
    del tree[node][giganode]
    giganode = node
    root_to_giga += _


def dfs(tree, giganode):
    branch = 0
    for node, d in tree[giganode].items():
        del tree[node][giganode]
        temp_lenth = d + dfs(tree, node)
        branch = max(branch, temp_lenth)
    return branch


print(root_to_giga, dfs(tree, giganode))
