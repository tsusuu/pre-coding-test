import sys

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)


def isRoot(tree, k):
    if len(tree[k]) == 1:
        print("no")
    else:
        print("yes")


q = int(sys.stdin.readline().strip())
for _ in range(q):
    t, k = map(int, sys.stdin.readline().strip().split())
    if t == 1:
        isRoot(tree, k)
    elif t == 2:
        print("yes")
