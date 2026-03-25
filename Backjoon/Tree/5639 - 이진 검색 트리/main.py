import sys

sys.setrecursionlimit(10**6)

stack = []
while True:
    try:
        stack.append(int(sys.stdin.readline().strip()))
    except:
        break


def DFS(start, end):
    if start > end:
        return
    mid = end + 1
    for _ in range(start + 1, end + 1):
        if stack[_] > stack[start]:
            mid = _
            break
    DFS(start + 1, mid - 1)
    DFS(mid, end)
    print(stack[start])


DFS(0, len(stack) - 1)
