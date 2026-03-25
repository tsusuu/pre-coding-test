import sys
from collections import deque

n = int(sys.stdin.readline().strip())


counter = 0
stack = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().strip().split(" "))
    if not stack:
        stack.append(y)
        continue

    while stack and stack[-1] > y:
        stack.pop()
        counter += 1

    if not stack:
        stack.append(y)
    elif stack[-1] != y:
        stack.append(y)


try:
    stack.remove(0)
except:
    pass

counter += len(stack)

print(counter)
