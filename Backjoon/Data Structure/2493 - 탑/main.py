import sys
from collections import deque

lenArray = int(sys.stdin.readline())
getTower = list(map(int, sys.stdin.readline().strip().split()))

stack = deque()
ans = [0 for i in range(lenArray)]


for i in range(lenArray):
    while stack:
        if stack[len(stack) - 1][1] >= getTower[i]:
            ans[i] = stack[len(stack) - 1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, getTower[i]])

print(*ans)
