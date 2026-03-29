import sys
import collections

sys.setrecursionlimit(10**9)

N, R = map(int, sys.stdin.readline().strip().split())

tree = collections.defaultdict(dict)
for _ in range(N - 1):
    a, b, d = map(int, sys.stdin.readline().strip().split())
    tree[a][b] = d
    tree[b][a] = d


gigaNode = R
rootToGiga = 0
while len(tree[gigaNode]) == 1:
    node, temp = list(tree[gigaNode].items())[0]
    del tree[node][gigaNode]
    rootToGiga += temp
    gigaNode = node


def dfs(tree, gigaNode):
    branchLenth = 0
    for node, d in tree[gigaNode].items():
        del tree[node][gigaNode]
        tempLenth = d + dfs(tree, node)
        if branchLenth < tempLenth:
            branchLenth = tempLenth
    return branchLenth


print(rootToGiga, dfs(tree, gigaNode))
