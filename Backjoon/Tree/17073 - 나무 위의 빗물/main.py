import sys

N, W = map(int, sys.stdin.readline().strip().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    tree[a].append(b)
    tree[b].append(a)

counter = 0
for _ in range(len(tree)):
    if _ > 1 and len(tree[_]) == 1:
        counter += 1
    elif _ == 1 and len(tree) == 2:
        counter += 1

result = W / counter

print(result)
