import sys

K = int(sys.stdin.readline().strip())
inOrdered = list(map(int, sys.stdin.readline().strip().split()))
tree = [[] for _ in range(K)]


def DFS(inOrdered, level):
    mid = len(inOrdered) // 2
    tree[level].append(inOrdered[mid])

    if len(inOrdered) > 1:
        DFS(inOrdered[:mid], level + 1)
        DFS(inOrdered[mid + 1 :], level + 1)
    else:
        return


DFS(inOrdered, 0)

for _ in tree:
    print(*_)
