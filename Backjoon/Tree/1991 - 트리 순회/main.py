import sys

tree = {}

N = int(sys.stdin.readline().strip())

for _ in range(N):
    parent, left, right = sys.stdin.readline().strip().split()
    tree[parent] = [left, right]


def preOrder(node):
    if node != ".":
        print(node, end="")
        preOrder(tree[node][0])
        preOrder(tree[node][1])


def inOrder(node):
    if node != ".":
        inOrder(tree[node][0])
        print(node, end="")
        inOrder(tree[node][1])


def postOrder(node):
    if node != ".":
        postOrder(tree[node][0])
        postOrder(tree[node][1])
        print(node, end="")


preOrder("A")
print()
inOrder("A")
print()
postOrder("A")
