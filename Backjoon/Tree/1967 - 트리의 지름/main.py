# import sys
# import collections
# import copy

# sys.setrecursionlimit(10**9)


# n = int(sys.stdin.readline())

# tree = collections.defaultdict(dict)

# for _ in range(n - 1):
#     parent, child, dis = map(int, sys.stdin.readline().strip().split())
#     tree[parent][child] = dis
#     tree[child][parent] = dis


# def dfs(tree, root):
#     maxDis = 0
#     visited = []
#     for node, dis in tree[root].items():
#         visited.append(node)
#         del tree[node][root]
#         tempDis = dis + dfs(tree, node)
#         if maxDis < tempDis:
#             maxDis = tempDis
#     # print(visited)
#     return maxDis


# # 딕셔너리를 임시로 참조해서 트리의 일부분만 순회를 돌도록 하는 함수 작성
# # 생각중인것
# # for문을 이용해 나누기
# # 부모 노드에 있는 값을 하나만 저장하는 또다른 딕셔너리를
# # for문을 이용해 만들기
# # 나머지는 그대로 복사하되, 첫번째 자식의 경우 하나만


# # for _ in range(1, n + 1):
# #     for k in tree[_].keys():
# #         print(dfs(tree, k))


# # maxDis = 0
# # for _ in range(1, n + 1):
# #     tempDis = dfs(tree, _)
# #     if maxDis < tempDis:
# #         maxDis = tempDis
# #     print(maxDis)

# # print(tree)


# def copyTree(tree, node, key):
#     tempTree = copy.deepcopy(tree)
#     copiedTree = copy.deepcopy(tempTree)
#     del copiedTree[node]
#     k = tempTree[node][key]
#     # print(k)
#     copiedTree[node][key] = k
#     # sortedTree = sorted(copiedTree.items())
#     # return sortedTree
#     return copiedTree


# # for _ in range(1, n + 1):
# #     print(dfs(tree, _))

# getValue = []
# for _ in range(1, n + 1):
#     for key in tree[_]:
#         # dictTree = collections.defaultdict(copyTree)
#         dictTree = copyTree(tree, _, key)
#         # print(dictTree)
#         # print(dfs(dictTree, _))
#         # print()
#         getValue.append(dfs(dictTree, _))

# print(max(getValue))

###################################################
# 위의 시도는 루트노드를 기준으로 가지를 전부 순회한 뒤
# 최대 2개의 겹치지 않는 값을 더한 방식
# 모든 루트를 여러번 탐험하기 때문에 메모리, 시간초과하였음

# 아래에 만드려는 것은 노드 to 노드의 길이가 최대일 경우
# 항상 끝에서 끝까지 가야한다는 생각이 나서 만들어본 코드
# 먼저 끝단인 노드를 구한 뒤, 해당 노드를 root로 하여
# 최대길이를 찾아 출력하도록 구성
###################################################

# import sys
# import collections
# import copy

# sys.setrecursionlimit(10**4)

# n = int(sys.stdin.readline())

# tree = collections.defaultdict(dict)
# for _ in range(n - 1):
#     parent, child, dis = map(int, sys.stdin.readline().strip().split())
#     tree[parent][child] = dis
#     tree[child][parent] = dis

# # def dfs(tree,root):
# #     lastNode = []
# #     visited =[]
# #     for node, dis in tree[root].items():
# #         visited.append(node)
# #         del tree[node][root]
# #         dfs()
# #         if len():
# #             _


# def getLastNode(tree, n):
#     lastNode = []
#     for _ in range(n):
#         # print(tree[_])
#         if len(tree[_]) == 1:
#             lastNode.append(_)
#     return lastNode
#     # print(lastNode)


# def dfs(tree, root):
#     copyTree = copy.deepcopy(tree)
#     visited = []
#     maxDist = 0
#     for node, dis in copyTree[root].items():
#         visited.append(node)
#         del copyTree[node][root]
#         tempDist = dis + dfs(copyTree, node)
#         if maxDist < tempDist:
#             maxDist = tempDist
#     return maxDist


# lastNode = getLastNode(tree, n + 1)
# distance = []
# for _ in lastNode:
#     # print(_)
#     distance.append(dfs(tree, _))

# print(max(distance))
# # print(distance)
# # print(tree)
# # print()
# # getLastNode(tree, n + 1)
# # print(getLastNode(tree, n))


###################################################
# 위 알고리즘은 반례없이 깔끔하게 작동했으나
# 일부 함수로 인해 시간초과가 발생했음
#
# 함수목록
# del, copy.deepcopy(O(N^2)의 시간복잡도)
# 딕셔너리를 계속 쓰게 된다면 깊은참조를 하지 않을 경우
# 메모리 주소값에서의 변수 변경으로 인해 값이 변하기 때문에
# 여러번 순회가 불가능
# 따라서 리스트 형식으로 교체하기로 함
#
#
# 1. 처음 주어진 root노드로부터 가장 멀리 떨어진 점을 탐색
# 2.이후 해당 노드로부터 가장 멀리 떨어진 노드를 탐색
#
#
# 해당 알고리즘으로는 단 두번의 dfs탐색으로 가장 멀리 떨어진
# 노드를 찾는게 가능해보임
#
# 아래는 정답본
###################################################

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
