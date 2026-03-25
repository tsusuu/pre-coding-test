import sys


N = int(sys.stdin.readline().strip())
stack = list(map(int, sys.stdin.readline().strip().split()))
delete = int(sys.stdin.readline().strip())


def DFS(tree, delete):
    tree[delete] = -2
    for _ in range(len(tree)):
        if tree[_] == delete:
            DFS(tree, _)


counter = 0
DFS(stack, delete)
for _ in range(len(stack)):
    if stack[_] != -2 and _ not in stack:
        counter += 1

print(counter)
