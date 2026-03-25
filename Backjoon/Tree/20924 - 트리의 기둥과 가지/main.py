import sys
import collections

sys.setrecursionlimit(10**9)


# N, R = map(int, sys.stdin.readline().strip().split())

# tree = [[] for _ in range(N + 1)]
# distance = [[] for _ in range(N + 1)]

# for _ in range(N - 1):
#     a, b, d = map(int, sys.stdin.readline().strip().split())
#     tree[a].append(b)
#     distance[a].append(d)
#     tree[b].append(a)

# branchPointer = 0
# for _ in range(1, N + 1):
#     if _ == 1:
#         if len(tree[_]) > 1:
#             branchPointer = _
#             break
#     else:
#         if len(tree[_]) > 2:
#             branchPointer = _
#             break
#     branchPointer = _

# rootDislist = []
# for _ in range(1, branchPointer):
#     rootDislist += distance[_]
# rootDis = sum(rootDislist)

# print(tree)
# print(distance)
# print(branchPointer)
# print(rootDis)

# # branchDis = []

# lastNode = 0
# for _ in range(1, N + 1):
#     if _ > 1:
#         if len(tree[_]) == 1:
#             lastNode += 1

# orderList = [[] for _ in range(lastNode)]
# print(orderList)


# def order(node, pointer):
#     orderList.append(node[pointer][0])

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

# print(rootToGiga, gigaNode)
# print(tree)
# print(list(tree[4].items())[0])


# def gradle(tree, gigaNode):
#     lenth = 0
#     while len(tree[gigaNode]) != 1:
#         node, temp = list(tree[gigaNode].items())[0]
#         print(node, temp)
#     lenth += temp
#     del tree[node][gigaNode]
#     return lenth


def dfs(tree, gigaNode):
    branchLenth = 0
    for node, d in tree[gigaNode].items():
        del tree[node][gigaNode]
        tempLenth = d + dfs(tree, node)
        if branchLenth < tempLenth:
            branchLenth = tempLenth
    return branchLenth


print(rootToGiga, dfs(tree, gigaNode))
# print(gradle(tree, gigaNode))
# print(len(tree[gigaNode]))
# node, temp = list(tree[gigaNode].items())[0]
# print(node, temp)

# print(len(tree[node]))
# node, temp = list(tree[node].items())[1]
# print(node, temp)
