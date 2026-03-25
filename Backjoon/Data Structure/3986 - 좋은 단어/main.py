import sys

N = int(sys.stdin.readline().strip())

count = 0


def isValid(getList):
    global count
    stack = []
    for i in getList:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        count += 1


for i in range(N):
    getString = sys.stdin.readline().strip()
    isValid(getString)

print(count)
