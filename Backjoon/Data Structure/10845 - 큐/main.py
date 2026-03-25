import sys
from collections import deque

que = deque()
N = int(sys.stdin.readline())
result = []


def push(x):
    que.append(x)


def pop():
    if len(que) == 0:
        result.append(-1)
    else:
        result.append(que.popleft())


def size():
    result.append(len(que))


def empty():
    if len(que) == 0:
        result.append(1)
    else:
        result.append(0)


def front():
    if len(que) == 0:
        result.append(-1)
    else:
        result.append(que[0])


def back():
    if len(que) == 0:
        result.append(-1)
    else:
        result.append(que[-1])


for i in range(N):
    command = sys.stdin.readline().strip().split(" ")
    if command[0] == "push":
        push(command[1])
    elif command[0] == "pop":
        pop()
    elif command[0] == "size":
        size()
    elif command[0] == "empty":
        empty()
    elif command[0] == "front":
        front()
    elif command[0] == "back":
        back()

for _ in result:
    print(_)
